"""End-to-end execution: collect → preprocess → analyze → figures → papers (MD+PDF)."""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from analysis import run_all_analyses  # noqa: E402
from data_collection import collect_all  # noqa: E402
from paper_generator import generate_all  # noqa: E402
from preprocessing import preprocess  # noqa: E402
from visualization import make_all_figures  # noqa: E402


def main() -> None:
    collect_all()
    preprocess()
    run_all_analyses()
    make_all_figures()
    generate_all()


if __name__ == "__main__":
    main()
