"""Download and cache public datasets (NHANES, USDA FDC, PubMed, WHO GHO, open nutrition CSV)."""
from __future__ import annotations

import json
import time
from pathlib import Path
from urllib.parse import urlencode

import pandas as pd
import requests

from config import (
    DATA,
    KAGGLE_PROXY_NUTRITION,
    LOGS,
    NHANES_2011,
    NHANES_2017,
    NHANES_BASE,
    PUBMED_EUTILS,
    USDA_FDC_API,
    USDA_API_KEY,
    WHO_GHO_API,
)


def _log(msg: str) -> None:
    p = LOGS / "data_collection.log"
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "a", encoding="utf-8") as f:
        f.write(msg + "\n")


def _download(url: str, dest: Path, timeout: int = 120) -> bool:
    try:
        r = requests.get(url, timeout=timeout, headers={"User-Agent": "research-portfolio/1.0"})
        r.raise_for_status()
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(r.content)
        return True
    except Exception as e:
        _log(f"FAIL {url} -> {dest}: {e}")
        return False


def download_nhanes_cycle(name: str, urls: dict[str, str]) -> dict[str, Path]:
    out: dict[str, Path] = {}
    for key, url in urls.items():
        dest = DATA / "nhanes" / name / f"{key}.xpt"
        ok = _download(url, dest)
        if not ok:
            _log(f"NHANES alternative: retry or skip {key}")
        out[key] = dest
    return out


def read_nhanes_xpt(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size < 100:
        raise FileNotFoundError(path)
    return pd.read_sas(str(path), format="xport", encoding="utf-8")


def fetch_usda_fdc_foods_sample(max_items: int = 50) -> pd.DataFrame:
    """List foods from USDA FoodData Central API (public)."""
    url = f"{USDA_FDC_API}foods/list?api_key={USDA_API_KEY}"
    payload = {"pageSize": max_items, "pageNumber": 1, "dataType": ["Foundation", "SR Legacy"]}
    try:
        r = requests.post(url, json=payload, timeout=60)
        r.raise_for_status()
        js = r.json()
        foods = js.get("foods", [])
        rows = []
        for f in foods:
            desc = f.get("description", "")
            nutrients = f.get("foodNutrients", []) or []
            row = {"fdc_id": f.get("fdcId"), "description": desc}
            for n in nutrients:
                nn = n.get("nutrient", {}) or {}
                name = (nn.get("name") or "").lower().replace(" ", "_")
                if name:
                    row[name] = n.get("amount")
            rows.append(row)
        df = pd.DataFrame(rows)
        df.to_csv(DATA / "usda_fdc_sample.csv", index=False)
        return df
    except Exception as e:
        _log(f"USDA FDC API failed: {e}; using synthetic fallback from open nutrition.")
        return pd.DataFrame()


def fetch_pubmed_counts(queries: list[str], years: tuple[int, int] | None = None) -> pd.DataFrame:
    rows = []
    for q in queries:
        term = q
        if years:
            term += f" AND {years[0]}:{years[1]}[pdat]"
        params = urlencode(
            {
                "db": "pubmed",
                "term": term,
                "retmode": "json",
                "retmax": 0,
            }
        )
        url = f"{PUBMED_EUTILS}esearch.fcgi?{params}"
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            js = r.json()
            cnt = int(js["esearchresult"]["count"])
            rows.append({"query": q, "count": cnt})
            time.sleep(0.35)
        except Exception as e:
            _log(f"PubMed query fail {q}: {e}")
            rows.append({"query": q, "count": 0})
    df = pd.DataFrame(rows)
    df.to_csv(DATA / "pubmed_counts.csv", index=False)
    return df


def fetch_who_indicator(indicator_code: str) -> pd.DataFrame:
    """WHO GHO OData-style API."""
    url = f"{WHO_GHO_API}{indicator_code}"
    try:
        r = requests.get(url, timeout=90)
        r.raise_for_status()
        js = r.json()
        df = pd.json_normalize(js.get("value", []))
        df.to_csv(DATA / f"who_{indicator_code}.csv", index=False)
        return df
    except Exception as e:
        _log(f"WHO fetch fail {indicator_code}: {e}")
        return pd.DataFrame()


def download_open_nutrition_table() -> pd.DataFrame:
    dest = DATA / "open_nutrition.csv"
    ok = _download(KAGGLE_PROXY_NUTRITION, dest)
    if not ok:
        _log("Open nutrition CSV failed; generating minimal synthetic public-style table.")
        df = pd.DataFrame(
            {
                "food": ["apple", "broccoli", "salmon", "oats", "yogurt"],
                "calories": [52, 34, 208, 389, 59],
                "protein": [0.3, 2.8, 20, 17, 10],
                "fat": [0.2, 0.4, 13, 7, 0.4],
                "carbs": [14, 7, 0, 66, 3.6],
                "fiber": [2.4, 2.6, 0, 11, 0],
            }
        )
        df.to_csv(dest, index=False)
    return pd.read_csv(dest)


def collect_all() -> dict:
    """Run all collectors; return manifest with paths and source URLs."""
    manifest: dict = {
        "nhanes_portal": NHANES_BASE,
        "cycles": {},
    }
    manifest["cycles"]["2017_2018"] = download_nhanes_cycle("2017_2018", NHANES_2017)
    manifest["cycles"]["2011_2012"] = download_nhanes_cycle("2011_2012", NHANES_2011)
    manifest["usda"] = str(DATA / "usda_fdc_sample.csv")
    fetch_usda_fdc_foods_sample(40)
    manifest["pubmed"] = str(DATA / "pubmed_counts.csv")
    fetch_pubmed_counts(
        [
            "functional food",
            "bioactive compound",
            "polyphenol",
            "omega-3",
            "dietary fiber microbiome",
        ]
    )
    manifest["who"] = {}
    for ind in ("NUTRITION_HA_1", "NUTRITION_HA_2"):
        dfw = fetch_who_indicator(ind)
        manifest["who"][ind] = len(dfw)
    manifest["kaggle_proxy_url"] = KAGGLE_PROXY_NUTRITION
    download_open_nutrition_table()
    def _jsonify(obj):
        if isinstance(obj, Path):
            return str(obj)
        if isinstance(obj, dict):
            return {k: _jsonify(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [_jsonify(x) for x in obj]
        return obj

    with open(DATA / "manifest.json", "w", encoding="utf-8") as f:
        json.dump(_jsonify(manifest), f, indent=2)
    return manifest


if __name__ == "__main__":
    collect_all()
