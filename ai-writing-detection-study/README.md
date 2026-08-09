# AI Writing Detection Robustness Study

This directory contains a reproducible study of AI-writing detectors on human,
AI-generated, and edited scientific prose. The initial phase is a 20-document
pilot. The full study is planned only after the pilot establishes detector input
limits, score mappings, costs, and failure modes.

## Experimental conditions

Each source topic produces matched passages in these conditions:

1. `human`: a licensed, pre-2020 passage with documented provenance.
2. `ai_raw`: output from a pinned model snapshot and archived prompt.
3. `ai_copyedit`: correction of grammar and local clarity only.
4. `ai_deslop_upstream`: revision with the unmodified upstream `deslop` skill.
5. `ai_deslop_enhanced`: revision with the local intervention in
   `interventions/deslop-enhanced/`.
6. `ai_paraphrase`: an OpenAI-prompted, meaning-preserving paraphrase (not DIPPER).

The upstream and enhanced deslop conditions must be generated independently
from `ai_raw`, not serially. This isolates the effect of each intervention.

## Study controls

- Archive exact text, prompts, model identifiers, timestamps, detector versions,
  detector settings, and raw detector responses.
- Fix passage boundaries before any detector is queried.
- Do not use detector feedback to revise a passage.
- Blind semantic-quality raters to condition and detector scores.
- Treat the source document as the resampling and clustering unit.
- Report sensitivity, specificity, false-positive and false-negative rates,
  balanced accuracy, and AUROC when continuous scores permit it.
- Report detector failures and indeterminate results rather than dropping them.
- Measure semantic preservation and factual/citation changes alongside evasion.

## Local intervention provenance

`interventions/deslop-enhanced/` is an experimental derivative inspired by
Stephen Turner's `skill-deslop`, retrieved from
https://github.com/stephenturner/skill-deslop on 2026-08-08. The upstream
repository was MIT-licensed. The local variant intentionally has a different
name so study artifacts cannot be confused with upstream output.

## Longitudinal arXiv analysis

Run `python3 analysis/arxiv_diachronic.py` from the repository root to harvest
and cache January--July metadata. Then run
`python3 analysis/derive_arxiv_contrasts.py` to reproduce the field summaries
and rate-ratio intervals. The harvester observes arXiv API pacing and defines
year by first submission.

The existing `ai_paraphrase` condition is an OpenAI-prompted paraphrase, not
DIPPER. A genuine DIPPER replication remains pending because the official 11B
checkpoint recommends at least 40 GB of GPU memory; this host has no compatible
