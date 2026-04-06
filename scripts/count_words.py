import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from config import PAPERS

for md in sorted(PAPERS.glob("paper_*.md")):
    t = md.read_text(encoding="utf-8")
    n = len(re.findall(r"\b[\w'-]+\b", t))
    print(md.name, n)
