#!/usr/bin/env python3
"""Harvest arXiv abstracts and measure diachronic lexical shifts.

The harvester uses arXiv's public Atom API, caches every response, and sleeps
between requests. Paper year is defined by the Atom ``published`` field (v1),
not the record's most recent update date.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import random
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path

API = "https://export.arxiv.org/api/query"
ATOM = "{http://www.w3.org/2005/Atom}"
OPEN = "{http://a9.com/-/spec/opensearch/1.1/}"
TOKEN = re.compile(r"[A-Za-z]+(?:['’-][A-Za-z]+)?")
YEARS = (2010, 2015, 2020, 2022, 2023, 2024, 2025, 2026)
CATEGORIES = ("cs.CL", "hep-ph", "math.PR")
MONTHS = tuple(range(1, 8))  # complete, seasonally matched January--July

# Confirmatory vocabulary selected before inspecting this arXiv corpus. These
# terms are drawn from the excess-vocabulary literature and our deslop rules.
TARGETS = (
    "aligns", "boasts", "commendable", "comprehensively", "crucial",
    "delve", "delves", "delving", "emphasizing", "enhance", "enhances",
    "enhancing", "fostering", "groundbreaking", "intricate", "intricacies",
    "meticulously", "notably", "nuanced", "pivotal", "realm", "showcasing",
    "tapestry", "underscore", "underscores", "underscoring", "valuable",
)


def month_end(year: int, month: int) -> int:
    import calendar
    return calendar.monthrange(year, month)[1]


def fetch(url: str, cache_dir: Path, delay: float) -> bytes:
    key = hashlib.sha256(url.encode()).hexdigest()
    path = cache_dir / f"{key}.xml"
    if path.exists():
        return path.read_bytes()
    request = urllib.request.Request(url, headers={"User-Agent": "ai-writing-detection-study/0.1 (research)"})
    with urllib.request.urlopen(request, timeout=90) as response:
        payload = response.read()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)
    time.sleep(delay)
    return payload


def harvest_cell(year: int, category: str, cache_dir: Path, delay: float) -> list[dict]:
    papers: dict[str, dict] = {}
    for month in MONTHS:
        start = f"{year}{month:02d}010000"
        end = f"{year}{month:02d}{month_end(year, month):02d}2359"
        query = f"cat:{category} AND submittedDate:[{start} TO {end}]"
        offset = 0
        while True:
            params = {
                "search_query": query, "start": offset, "max_results": 1000,
                "sortBy": "submittedDate", "sortOrder": "ascending",
            }
            url = API + "?" + urllib.parse.urlencode(params)
            root = ET.fromstring(fetch(url, cache_dir, delay))
            total = int(root.findtext(f"{OPEN}totalResults", "0"))
            entries = root.findall(f"{ATOM}entry")
            for entry in entries:
                paper_id = entry.findtext(f"{ATOM}id", "").rsplit("/", 1)[-1].split("v", 1)[0]
                published = entry.findtext(f"{ATOM}published", "")
                if not published.startswith(str(year)):
                    continue
                papers[paper_id] = {
                    "id": paper_id,
                    "year": year,
                    "month": month,
                    "category": category,
                    "published": published,
                    "title": " ".join(entry.findtext(f"{ATOM}title", "").split()),
                    "abstract": " ".join(entry.findtext(f"{ATOM}summary", "").split()),
                }
            offset += len(entries)
            if not entries or offset >= total:
                break
    return sorted(papers.values(), key=lambda p: (p["published"], p["id"]))


def tokenize(text: str) -> list[str]:
    return [match.group(0).lower().replace("’", "'") for match in TOKEN.finditer(text)]


def stratified_sample(papers: list[dict], n: int, seed: int) -> list[dict]:
    if len(papers) <= n:
        return papers
    rng = random.Random(seed)
    groups: dict[int, list[dict]] = defaultdict(list)
    for paper in papers:
        groups[paper["month"]].append(paper)
    allocation = {m: n * len(v) / len(papers) for m, v in groups.items()}
    counts = {m: int(v) for m, v in allocation.items()}
    for month, _ in sorted(allocation.items(), key=lambda x: x[1] - counts[x[0]], reverse=True)[: n - sum(counts.values())]:
        counts[month] += 1
    selected = []
    for month, group in groups.items():
        selected.extend(rng.sample(group, counts[month]))
    return selected


def log_odds(a: int, na: int, b: int, nb: int, prior: float = 0.5) -> float:
    return math.log((a + prior) / (na - a + prior)) - math.log((b + prior) / (nb - b + prior))


def analyse(papers: list[dict], out_dir: Path, per_cell: int) -> None:
    sampled = []
    by_cell: dict[tuple[int, str], list[dict]] = defaultdict(list)
    for paper in papers:
        by_cell[(paper["year"], paper["category"])].append(paper)
    for (year, category), cell in sorted(by_cell.items()):
        seed = int(hashlib.sha256(f"{year}:{category}".encode()).hexdigest()[:8], 16)
        sampled.extend(stratified_sample(cell, per_cell, seed))

    stats = {}
    corpus_counts: dict[int, Counter] = defaultdict(Counter)
    doc_counts: dict[int, Counter] = defaultdict(Counter)
    tokens_by_year = Counter()
    docs_by_year = Counter()
    for paper in sampled:
        words = tokenize(paper["title"] + " " + paper["abstract"])
        year = paper["year"]
        corpus_counts[year].update(words)
        doc_counts[year].update(set(words))
        tokens_by_year[year] += len(words)
        docs_by_year[year] += 1
    for year in sorted(docs_by_year):
        target_documents = sum(
            1 for paper in sampled if paper["year"] == year
            and set(tokenize(paper["title"] + " " + paper["abstract"])).intersection(TARGETS)
        )
        stats[year] = {
            "documents": docs_by_year[year], "tokens": tokens_by_year[year],
            "target_tokens_per_million": 1e6 * sum(corpus_counts[year][w] for w in TARGETS) / tokens_by_year[year],
            "target_document_prevalence": target_documents / docs_by_year[year],
        }

    rows = []
    for word in TARGETS:
        a, na = corpus_counts[2026][word], tokens_by_year[2026]
        b, nb = corpus_counts[2010][word], tokens_by_year[2010]
        rows.append({
            "word": word, "count_2010": b, "count_2026": a,
            "per_million_2010": 1e6 * b / nb, "per_million_2026": 1e6 * a / na,
            "log_odds_2026_vs_2010": log_odds(a, na, b, nb),
            "documents_2010": doc_counts[2010][word], "documents_2026": doc_counts[2026][word],
        })
    rows.sort(key=lambda row: row["log_odds_2026_vs_2010"], reverse=True)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "summary.json").write_text(json.dumps({"years": stats, "cells": {f"{y}:{c}": len(v) for (y, c), v in by_cell.items()}, "sample_per_cell": per_cell}, indent=2))
    with (out_dir / "target-word-shifts.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader(); writer.writerows(rows)
    with (out_dir / "sampled-papers.jsonl").open("w") as handle:
        for paper in sampled:
            handle.write(json.dumps(paper, ensure_ascii=False) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("ai-writing-detection-study/data/arxiv-diachrony"))
    parser.add_argument("--delay", type=float, default=3.1)
    parser.add_argument("--per-cell", type=int, default=500)
    args = parser.parse_args()
    all_papers = []
    for year in YEARS:
        for category in CATEGORIES:
            cell = harvest_cell(year, category, args.root / "raw", args.delay)
            print(year, category, len(cell), flush=True)
            all_papers.extend(cell)
    analyse(all_papers, args.root / "results", args.per_cell)


if __name__ == "__main__":
    main()
