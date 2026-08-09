#!/usr/bin/env python3
"""Derive field summaries and Poisson rate-ratio intervals from the sample."""

import json
import math
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path("ai-writing-detection-study/data/arxiv-diachrony/results")
TARGETS = set("aligns boasts commendable comprehensively crucial delve delves delving emphasizing enhance enhances enhancing fostering groundbreaking intricate intricacies meticulously notably nuanced pivotal realm showcasing tapestry underscore underscores underscoring valuable".split())
TOKEN = re.compile(r"[A-Za-z]+(?:['’-][A-Za-z]+)?")


def interval(a, exposure_a, b, exposure_b):
    ratio = (a / exposure_a) / (b / exposure_b)
    error = math.sqrt(1 / a + 1 / b)
    return {"rate_ratio": ratio,
            "ci95_low": math.exp(math.log(ratio) - 1.96 * error),
            "ci95_high": math.exp(math.log(ratio) + 1.96 * error)}


cells = defaultdict(lambda: {"documents": 0, "tokens": 0,
                             "target_tokens": 0, "target_documents": 0})
for line in (ROOT / "sampled-papers.jsonl").open():
    paper = json.loads(line)
    words = [m.group(0).lower().replace("’", "'") for m in
             TOKEN.finditer(paper["title"] + " " + paper["abstract"])]
    cell = cells[(paper["year"], paper["category"])]
    cell["documents"] += 1
    cell["tokens"] += len(words)
    cell["target_tokens"] += sum(word in TARGETS for word in words)
    cell["target_documents"] += bool(set(words).intersection(TARGETS))

years = defaultdict(lambda: {"documents": 0, "tokens": 0,
                             "target_tokens": 0, "target_documents": 0})
for (year, _), cell in cells.items():
    for key in years[year]:
        years[year][key] += cell[key]

contrasts = {}
for later, earlier in ((2026, 2010), (2026, 2022), (2025, 2022), (2026, 2025)):
    a, b = years[later], years[earlier]
    contrasts[f"{later}_vs_{earlier}"] = interval(
        a["target_tokens"], a["tokens"], b["target_tokens"], b["tokens"])
a = {key: sum(cells[(2026, category)][key] for category in ("hep-ph", "math.PR")) for key in years[2026]}
b = {key: sum(cells[(2010, category)][key] for category in ("hep-ph", "math.PR")) for key in years[2010]}
contrasts["2026_vs_2010_excluding_cs.CL"] = interval(
    a["target_tokens"], a["tokens"], b["target_tokens"], b["tokens"])

output = {"years": years, "fields": {f"{y}:{c}": v for (y, c), v in cells.items()},
          "contrasts": contrasts}
(ROOT / "contrasts.json").write_text(json.dumps(output, indent=2))
print(json.dumps(contrasts, indent=2))
