"""Merge NHANES files, engineer features, harmonize cycles for trend analysis."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from config import DATA, LOGS, RESULTS
from data_collection import read_nhanes_xpt


def _log(msg: str) -> None:
    with open(LOGS / "preprocessing.log", "a", encoding="utf-8") as f:
        f.write(msg + "\n")


def _safe_select(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    present = [c for c in cols if c in df.columns]
    return df[present].copy()


def _find_xpt(cycle_dir: Path, prefix: str) -> Path | None:
    for pat in ("*.xpt", "*.XPT"):
        for p in sorted(cycle_dir.glob(pat)):
            if p.name.upper().startswith(prefix.upper()):
                return p
    return None


def load_cycle(cycle_dir: Path, label: str) -> pd.DataFrame | None:
    if not cycle_dir.exists():
        _log(f"Missing dir {cycle_dir}")
        return None
    try:
        p_dr = _find_xpt(cycle_dir, "DR1TOT")
        p_demo = _find_xpt(cycle_dir, "DEMO")
        if p_dr is None or p_demo is None:
            _log(f"Missing DR1TOT or DEMO in {cycle_dir}")
            return None
        dr = read_nhanes_xpt(p_dr)
        demo = read_nhanes_xpt(p_demo)
        p_bmx = _find_xpt(cycle_dir, "BMX")
        p_bpx = _find_xpt(cycle_dir, "BPX")
        bmx = read_nhanes_xpt(p_bmx) if p_bmx else None
        bpx = read_nhanes_xpt(p_bpx) if p_bpx else None
    except Exception as e:
        _log(f"Read fail {cycle_dir}: {e}")
        return None

    m = dr.merge(demo, on="SEQN", how="inner", suffixes=("", "_d"))
    m = m.drop_duplicates(subset=["SEQN"])
    if bmx is not None:
        m = m.merge(_safe_select(bmx, ["SEQN", "BMXBMI"]), on="SEQN", how="left")
    if bpx is not None:
        m = m.merge(_safe_select(bpx, ["SEQN", "BPXSY1", "BPXDI1"]), on="SEQN", how="left")

    nutrient_cols = [
        "DR1TKCAL",
        "DR1TPROT",
        "DR1TCARB",
        "DR1TSFAT",
        "DR1TMFAT",
        "DR1TPFAT",
        "DR1TCHOL",
        "DR1TFIBE",
        "DR1TSUGR",
        "DR1TCALC",
        "DR1TVARA",
        "DR1TVB12",
        "DR1TVC",
        "DR1TVD",
        "DR1TVK",
        "DR1TMAGN",
        "DR1TPOTA",
        "DR1TSODI",
        "DR1TIRON",
        "DR1TZINC",
    ]
    demo_cols = ["RIAGENDR", "RIDAGEYR", "INDFMPIR"]
    keep = ["SEQN"] + [c for c in nutrient_cols + demo_cols + ["BMXBMI", "BPXSY1", "BPXDI1"] if c in m.columns]
    out = m[keep].copy()
    out["cycle"] = label
    return out


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    d = df.copy()
    if "DR1TKCAL" in d.columns:
        kcal = d["DR1TKCAL"].replace(0, np.nan)
        for c in ["DR1TPROT", "DR1TCARB", "DR1TSFAT", "DR1TFIBE", "DR1TSUGR"]:
            if c in d.columns:
                d[f"pct_{c}"] = d[c] / kcal * 100.0
    if "DR1TFIBE" in d.columns and "DR1TMFAT" in d.columns and "DR1TPFAT" in d.columns:
        d["plant_fat_ratio"] = (d["DR1TMFAT"] + d["DR1TPFAT"]) / (d["DR1TSFAT"] + d["DR1TMFAT"] + d["DR1TPFAT"] + 1e-6)
    if all(x in d.columns for x in ["DR1TFIBE", "DR1TCARB", "DR1TSUGR"]):
        d["fiber_diversity_proxy"] = np.log1p(d["DR1TFIBE"]) * (1 - (d["DR1TSUGR"] / (d["DR1TCARB"] + 1e-6)).clip(0, 1))
    if "BMXBMI" in d.columns:
        d["obese"] = (d["BMXBMI"] >= 30).astype(float)
    if "BPXSY1" in d.columns:
        d["elevated_bp"] = (d["BPXSY1"] >= 130).astype(float)
    return d


def preprocess() -> dict[str, str]:
    base = DATA / "nhanes"
    frames = []
    for sub, lab in [("2017_2018", "2017-2018"), ("2011_2012", "2011-2012")]:
        p = base / sub
        if p.exists():
            f = load_cycle(p, lab)
            if f is not None:
                frames.append(engineer_features(f))
    if not frames:
        _log("No NHANES merged; writing empty placeholder.")
        empty = pd.DataFrame()
        empty.to_csv(RESULTS / "master_nhanes.csv", index=False)
        return {"master": str(RESULTS / "master_nhanes.csv"), "n": 0}

    master = pd.concat(frames, ignore_index=True)
    num_cols = master.select_dtypes(include=[np.number]).columns
    master[num_cols] = master[num_cols].replace([np.inf, -np.inf], np.nan)
    master = master.dropna(subset=[c for c in ["DR1TKCAL", "RIDAGEYR"] if c in master.columns], how="any")
    master.to_csv(RESULTS / "master_nhanes.csv", index=False)
    meta = {"master": str(RESULTS / "master_nhanes.csv"), "n": int(len(master))}
    with open(RESULTS / "preprocessing_meta.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)
    return meta


if __name__ == "__main__":
    print(preprocess())
