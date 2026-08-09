# When Human Writing Moves: AI-Text Detection, Style Editing, Controlled Corruption, and the Problem of a Historical Baseline

**Author:** [Author name]
**Affiliation:** Tennessee Labs, Tennessee, USA
**Correspondence:** hello@tennesseelabs.com

## Abstract

AI-text detectors are commonly evaluated against a stable binary: archived human writing versus newly generated machine text. That design may become less informative as people repeatedly read, edit, and converse with large language models (LLMs). We report a paired pilot evaluation of Pangram 3.3.2 on 20 pre-2020 open-access biomedical introductions and 80 matched LLM-derived passages. For each source topic, a pinned OpenAI model produced an introduction that was left unchanged, copyedited, revised with a rule-based “deslopping” prompt, or substantially paraphrased without detector feedback. Pangram classified all 20 historical passages as human and all 80 LLM-derived passages as AI (document-level AI fractions 0.0 and 1.0, respectively). Deslopping shortened passages but did not alter any classification; neither did the stronger paraphrase. We then generated 220 additional variants along nested punctuation- and word-corruption dose curves. Every variant remained classified as AI, including passages with an average of 29 word-level errors or approximately 57 punctuation edits. Continuous segment scores changed only slightly. These results do not contradict prior demonstrations that paraphrasing can defeat other detectors. They show that removal of familiar AI commonisms is not necessarily equivalent to crossing a contemporary detector’s decision boundary. In a complementary longitudinal analysis of 11,465 arXiv titles and abstracts, a prespecified set of LLM-associated style terms rose from 209 occurrences per million words in 2010 to 1,835 in 2025, before falling to 737 in 2026. We argue that the larger measurement problem is temporal. Human linguistic distributions respond to exposure and coordination, while LLM-associated vocabulary is already changing scientific writing. A detector validated mainly against pre-LLM prose may therefore estimate distance from a historical human distribution rather than machine authorship. Future evaluations should use time-indexed controls, longitudinal within-author samples, disclosed AI-assisted writing, and unaided contemporary writing.

**Keywords:** AI-text detection; scientific writing; paraphrasing; stylometry; lexical entrainment; human–LLM coevolution

## 1. Introduction

AI-text detection is often posed as classification between two natural classes: human-written and machine-generated text. The labels appear simple, but the distributions underneath them are not fixed. Generators change, editing practices change, and human language changes in response to the language people encounter.

Robustness studies have shown that transformations can expose detector brittleness. Krishna et al. [1] used the DIPPER paraphraser to reduce DetectGPT accuracy from 70.3% to 4.6% at a fixed 1% false-positive rate, while also reducing the performance of GPTZero, watermarking, and OpenAI’s former classifier. Wang et al. [2] examined editing, paraphrasing, co-generation, and prompting attacks; averaged across detectors, performance declined by 35%. An apparently strong detector on untouched model output may therefore fail after meaning-preserving transformation.

The popular response to recognizable “AI style” has produced editing checklists that remove recurrent lexical, syntactic, and formatting patterns. We call this process *deslopping*: revising formulaic prose for directness, specificity, varied rhythm, and appropriate disciplinary register. Deslopping differs from detector-guided evasion. It need not query a detector, optimize a score, introduce errors, or obscure provenance. It represents an editorial intervention that a writer might apply because the original prose is repetitive or generic.

We ask whether ordinary copyediting, deslopping, or general paraphrasing changes the classification of matched scientific prose under a current commercial detector. We then consider what a historical human comparison means if human writing is itself moving toward patterns associated with LLMs.

Repeated exposure can support lexical acquisition [3], and interlocutors coordinate lexical choices through conceptual pacts and lexical entrainment [4]. LLMs now participate directly and indirectly in that linguistic environment. Kobak et al. [5] found abrupt increases in LLM-associated style words across more than 15 million biomedical abstracts and estimated that at least 13.5% of 2024 abstracts had been processed with LLMs. Geng and Trotta [6] documented subsequent changes in conspicuous LLM-favored terms and described the process as human–LLM coevolution. These observations do not show that every lexical shift reflects unconscious adoption; direct AI editing, changing publication norms, and strategic removal of known markers are competing explanations. They do establish that contemporary scientific prose is not sampled from the same distribution as pre-LLM prose. A 2026 study of 149,452 civil and environmental engineering abstracts similarly reported departures from historical vocabulary trends after 2022 [8].

## 2. Methods

### 2.1 Human source texts

We queried Europe PMC for English-language, open-access articles published from 2015 through 2018 with abstracts and full text. From results sorted by citation count, we retained the first 20 records whose XML contained an Introduction or Background section of at least 550 words. Each passage was truncated at a sentence boundary near 800 words. Inline numeric citation markers were removed during whitespace normalization. The resulting passages contained a mean of 709.0 words (SD 93.1).

Publication before widespread public access to modern generative LLMs makes these passages useful historical controls. It does not prove that every token was produced without computational assistance, nor does it make the sample representative of contemporary human writing.

### 2.2 Matched generation

For each article, the pinned model gpt-5-mini-2025-08-07 received the title, abstract, and target word count. It was instructed to write a scientific-paper introduction using only supplied information, without copying abstract phrases or inventing citations, numerical findings, authors, or unsupported facts. Requests used minimal reasoning effort, disabled server-side storage, and archived the complete API response.

### 2.3 Transformations

Each raw generation independently entered three transformations:

1. **Copyedit:** grammar and local clarity edits while preserving claims and qualifications.
2. **Deslop:** revision under a fixed rule set targeting formulaic contrasts, canned transitions, punctuation templates, false agency, repetitive paragraph structures, vague significance claims, and uniform rhythm. The instructions protected terminology, uncertainty, citation scope, and legitimate scientific passive voice.
3. **Paraphrase:** substantial changes to syntax, sentence boundaries, transitions, and wording while preserving meaning and uncertainty.

No transformation received detector output. No passage was resampled or iteratively revised to lower a detector score. Natural length changes were retained as part of the interventions. This produced five conditions per source and 100 passages: 20 historical human and 80 LLM-derived.

### 2.4 Controlled corruption

We conducted two nested dose-response experiments on each raw AI passage. Punctuation corruption changed commas, colons, and semicolons through deterministic insertion, deletion, and substitution at 0.25, 0.5, 1, 2, 4, and 8 edits per 100 words. A validation step confirmed that the words and their order remained identical. Word noise combined internal-letter transposition, single-character deletion, article deletion, and duplication of function words at 0.25, 0.5, 1, 2, and 4 edits per 100 words. Every variant retained an exact edit log and was generated without detector feedback. The doses were nested, so each higher dose included the edits at lower doses.

The punctuation experiment produced 120 additional passages and the word-noise experiment produced 100. These interventions were designed to preserve topic and broad intelligibility, but semantic fidelity and readability at the highest word-noise doses await blinded human assessment.

### 2.5 Detection and reproducibility

We submitted each passage once to Pangram’s V3 API with public dashboard links disabled. The detector identified itself as version 3.3.2. We archived complete responses, including document-level fractions and segment windows. AI-derived text was the positive class. Pangram was selected because it offered a current programmatic interface within budget. Its developers describe a transformer classifier trained with hard-negative mining and synthetic mirrors [7]. Originality.ai was excluded before data collection because API access required an enterprise subscription beyond the project budget.

Every source, prompt response, transformation, detector response, model identifier, and SHA-256 text hash was retained. A deterministic shuffle assigned all 100 passages anonymous IDs for planned human evaluation. Reviewers will provide a human/AI judgment, confidence, perceived quality, and comments. The private condition key is stored separately. Human ratings were not complete for this report.

### 2.6 Longitudinal arXiv analysis

We harvested public arXiv metadata for papers first submitted from January through July in 2010, 2015, 2020, and 2022 through 2026. We selected three long-running categories with different subject matter: computational linguistics (cs.CL), high-energy phenomenology (hep-ph), and probability (math.PR). Within each category-year, a deterministic month-stratified sample retained at most 500 papers. The 2010 cs.CL and 2015 cs.CL strata contained only 54 and 411 eligible papers; all were retained. The final corpus comprised 11,465 titles and abstracts.

A confirmatory lexicon of 27 LLM-associated style terms was fixed before examining the corpus, drawing on published excess-vocabulary work [5] and the study editing rules. We measured token frequency per million words and the proportion of documents containing one or more target terms. Approximate rate-ratio intervals treated target-token counts as Poisson; field-specific results and a sensitivity analysis excluding the small 2010 cs.CL stratum addressed compositional change. The analysis defines year by first submission rather than arXiv record-update date, caches every raw Atom response, and uses only complete matched months. It tests for a temporal distribution shift, not authorship or undisclosed AI use.

## 3. Results

Pangram labeled every historical passage Human and every LLM-derived passage AI. Document-level scores were saturated: an AI fraction of 0.0 for every human passage and 1.0 for every AI-derived passage.

| Condition | n | Mean words (SD) | Labeled AI | Mean AI fraction |
|---|---:|---:|---:|---:|
| Human | 20 | 709.0 (93.1) | 0 | 0.00 |
| Raw AI | 20 | 720.6 (90.2) | 20 | 1.00 |
| Copyedited AI | 20 | 717.9 (90.1) | 20 | 1.00 |
| Deslopped AI | 20 | 640.9 (80.3) | 20 | 1.00 |
| Paraphrased AI | 20 | 665.0 (77.2) | 20 | 1.00 |

The observed false-positive rate was 0/20 (0%; two-sided 95% Clopper–Pearson upper bound 16.8%). Sensitivity was 80/80 (100%; lower bound 95.5%), and specificity was 20/20 (100%; lower bound 83.2%). Point-estimate balanced accuracy was 100%.

Deslopping removed about 11% of the raw generation’s words on average; paraphrasing removed about 8%. We do not treat these changes as protocol violations. Editing changes a passage’s realized distribution, including length and redundancy. Neither intervention changed a Pangram classification despite those changes.

Controlled corruption also produced no label changes. All 120 punctuation-corrupted and 100 word-corrupted passages were labeled AI with an AI fraction of 1.0. Pangram’s document-level fractions are proportions of labeled windows and were saturated in this sample, but each window also carried a continuous AI-assistance score. Table 2 reports the dose-response results.

| Corruption | Maximum dose | Mean edits at maximum | AI labels at maximum | Mean window score at maximum |
|---|---:|---:|---:|---:|
| None (raw AI) | 0 | 0 | 20/20 | 0.99294 |
| Mixed punctuation | 8 per 100 words | approximately 57 | 20/20 | 0.99272 |
| Mixed word noise | 4 per 100 words | 28.95 | 20/20 | 0.99254 |

At intermediate doses, every passage was also labeled AI. The highest punctuation dose changed the mean score by about 0.00021 relative to raw AI; the highest word-noise dose changed it by about 0.00040. These shifts were small relative to the separation from historical human windows, whose mean score was 0.00389 and maximum was 0.03337. No corruption threshold was observed within the tested range.

### 3.1 Diachronic vocabulary shift

The prespecified target terms occurred 209 times per million title-and-abstract tokens in 2010, 294 in 2015, 389 in 2020, and 416 in 2022. The rate then increased to 802 in 2023, 1,656 in 2024, and 1,835 in 2025, before falling to 737 in 2026. Document prevalence followed the same trajectory: 2.7% in 2010, 3.7% in 2015, 5.5% in 2020, 6.1% in 2022, 10.7% in 2023, 18.9% in 2024, 21.1% in 2025, and 11.3% in 2026.

The 2026 rate was 3.53 times the 2010 rate (approximate 95% CI 2.37--5.25) and 1.77 times the 2022 rate (1.39--2.26). Excluding cs.CL, which had only 54 eligible papers in 2010 and underwent exceptional growth, the 2010-to-2026 rate ratio remained 2.29 (1.46--3.61). The increase appeared in each field, although its magnitude differed. The 2025-to-2026 decline was also large: the rate ratio was 0.40 (0.34--0.48). Thus the data show an abrupt post-2022 rise and a subsequent reversal, not monotonic convergence toward one fixed LLM vocabulary.

| Year | Papers | Target terms per million words | Papers with at least one target term |
|---:|---:|---:|---:|
| 2010 | 1,054 | 208.8 | 2.7% |
| 2015 | 1,411 | 293.6 | 3.7% |
| 2020 | 1,500 | 389.0 | 5.5% |
| 2022 | 1,500 | 415.9 | 6.1% |
| 2023 | 1,500 | 802.2 | 10.7% |
| 2024 | 1,500 | 1,655.6 | 18.9% |
| 2025 | 1,500 | 1,834.7 | 21.1% |
| 2026 | 1,500 | 737.1 | 11.3% |

## 4. Discussion

### 4.1 Deslopping was not detector evasion

The direct result is negative: removing recognizable AI commonisms did not make generated introductions appear human to Pangram. The detector remained maximally confident after copyediting, deslopping, and substantial paraphrasing.

This should not be generalized to all detectors, generators, domains, or attacks. Prior studies evaluated different architectures and stronger or detector-targeted transformations [1,2]. DIPPER explicitly controls lexical diversity and content reordering, and adversarial studies may search over candidates or exploit model-specific weaknesses. Our transformations were single-pass, meaning-preserving edits without detector feedback. The contrast is informative. “Sounds less like stereotypical AI prose” and “crosses a detector boundary” are different hypotheses.

The saturated document response initially obscured a continuous output. Pangram supplies an AI-assistance score for each window, while its document fractions summarize the proportions of windows assigned categorical labels. Window scores showed that the texts occupied opposite extremes: historical human windows averaged 0.00389 and raw AI windows averaged 0.99294.

Punctuation noise barely moved the continuous score, even though the highest dose inserted or altered punctuation often enough to make the prose visibly irregular. Word-level errors produced a somewhat larger but still negligible change. This suggests that Pangram 3.3.2 did not rely primarily on punctuation cleanliness, spelling regularity, function-word perfection, or the rhetorical templates targeted by deslopping in this corpus. It also cautions against equating a detector with a grammar checker.

No threshold was found before the interventions approached a level at which readability could become a competing explanation. More severe corruption could eventually cross a boundary, but a threshold obtained only after destroying communicative quality would have little relevance to ordinary editing. The blinded human evaluation should therefore measure both perceived authorship and intelligibility.

### 4.2 The historical-control problem

The stronger implication concerns the negative class. Pre-2020 prose provides relatively uncontaminated historical controls, but the deployment population for an AI detector is contemporary writing. Those are not interchangeable.

Language users adapt to exposure. Repeated encounters increase the likelihood that unfamiliar forms become learned and available [3]. Conversational partners reuse one another’s referring expressions [4]. LLMs now supply language across email, education, journalism, software interfaces, and scholarly editing. A person can encounter model-shaped language without directly asking a model to write.

At least three processes may move contemporary human prose toward an LLM-associated distribution:

1. **Direct assistance:** a person accepts or edits generated wording.
2. **Strategic adaptation:** writers remove conspicuous AI markers or adopt conventions rewarded by institutions.
3. **Incidental accommodation:** recurrent exposure changes which words and constructions feel available, ordinary, or authoritative.

Our experiment does not distinguish these mechanisms. Corpus evidence nevertheless shows the aggregate distribution moving. Biomedical abstracts contain abrupt increases in LLM-associated vocabulary [5], while later changes suggest authors and tools react to public knowledge of those markers [6]. The categories are coupled: LLMs learn from human text; people learn from environments populated by LLM text; newer models may train on the resulting mixture.

Our arXiv analysis independently recovers the timing of that shift across computational linguistics, high-energy physics, and probability. Its reversal in 2026 is important. A static list of notorious AI words is not a permanent fingerprint. Model updates may alter preferred vocabulary, writers and editors may avoid publicized markers, and the scientific topics represented within a field may change. The result therefore supports temporal drift in scientific-language distributions, but it cannot attribute individual documents or partition direct AI assistance from social diffusion and unrelated stylistic change.

A detector evaluated against historical controls can remain internally accurate while becoming externally miscalibrated. It may learn the contrast

> historical human prose versus current model prose

when users interpret its output as

> unaided current human prose versus model-authored prose.

That substitution matters in academic-integrity settings. A contemporary writer who has absorbed common phrasing, uses an AI editor without delegating authorship, or follows standardized scientific templates may differ from a historical baseline for reasons that do not match the alleged behavior.

### 4.3 Evaluation should become temporal

Future benchmarks should treat calendar time and exposure as design variables. They should include pre-LLM historical writing, contemporary unaided writing, disclosed AI-edited human drafts, human-edited AI drafts, and longitudinal samples from the same writers before and after sustained LLM exposure. Multiple generators, detector versions, domains, and language backgrounds are required.

Within-author samples reduce confounding by education, first language, discipline, and stable personal style. Prospective studies could randomize exposure to LLM-generated versus human-generated reading material and measure later lexical and syntactic uptake without direct writing assistance. Such designs could test the moving-baseline hypothesis rather than infer cognition from corpus shifts.

Detector reports should distinguish authorship, assistance, and distributional similarity. A stylistic resemblance score cannot by itself establish the process that produced a document.

## 5. Limitations

This pilot used one commercial detector, one pinned generator, one scientific domain, and 20 source topics selected from highly cited open-access biomedical literature. Confidence intervals remain wide despite perfect point estimates. Historical passages may differ from generated passages in structure, factual density, citation history, and editorial review.

The transformations came from the same model family that produced the raw passages, and semantic preservation has not yet been independently rated. Punctuation-only variants preserved the exact word sequence, but the intelligibility and perceived quality of high-dose punctuation and word-noise variants require human validation. The paraphrase was not DIPPER and was not optimized against Pangram. “Deslopping” operationalizes one fixed instruction set, not a standardized intervention. Pangram is proprietary and its version may change. Finally, the moving-baseline account is a hypothesis supported by linguistic theory and corpus trends, not a causal finding from this detector experiment. The arXiv analysis used titles and abstracts rather than full text, only three categories, a hand-selected external lexicon, and unequal historical cell sizes. Field labels do not eliminate changes in topics, authorship, language background, submission practices, or abstract conventions. Revisions after first submission may also alter the metadata text exposed by the API. The corpus shift is compatible with direct LLM generation, AI editing, imitation, model-aware avoidance, and non-AI historical change; it cannot estimate undisclosed use by itself.

## 6. Conclusion

In this paired biomedical pilot, Pangram distinguished 20 historical human introductions from 80 matched LLM-derived passages without error. Copyediting, removal of common AI stylistic patterns, single-pass paraphrasing, 120 punctuation-corrupted variants, and 100 word-corrupted variants did not change any classification. Editing away visible “AI style” and adding substantial low-level noise did not remove the evidence used by this detector. No practical corruption threshold was observed within the tested range. Separately, arXiv titles and abstracts showed an abrupt rise in prespecified LLM-associated vocabulary after 2022 and a marked reversal in 2026, demonstrating that the relevant linguistic baseline is changing rather than moving monotonically toward a fixed model signature.

The more durable challenge may be the reference class. As LLM-associated language circulates through the environments in which people read, think, and write, human prose may move toward model-associated distributions. Historical controls then become simultaneously attractive and outdated: attractive because provenance is clearer, outdated because they may not represent the humans on whom detectors are used. AI-text detection should be evaluated as a temporally shifting measurement problem, not a permanent binary classification task.

## Data and code availability

The study directory contains source provenance, exact generated and transformed passages, raw API responses, hashes, document-level results, and a blinded human-rating packet. It also contains the arXiv harvesting and analysis script, deterministic sampling code, cached metadata, and derived lexical tables. Thank you to arXiv for use of its open access interoperability. Public release should retain source licenses and exclude API credentials and the private condition key until human evaluation is complete.

## Ethics statement

No detector feedback was used to optimize text for evasion. The study evaluates robustness and does not provide a service for concealing authorship. Detector outputs should not be treated as sole evidence of misconduct.

## References

1. Krishna K, Song Y, Karpinska M, Wieting J, Iyyer M. Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense. *Advances in Neural Information Processing Systems*. 2023;36. arXiv:2303.13408.
2. Wang Y, Feng S, Hou A, et al. Stumbling Blocks: Stress Testing the Robustness of Machine-Generated Text Detectors Under Attacks. *Proceedings of ACL*. 2024:2894–2925. doi:10.18653/v1/2024.acl-long.160.
3. Gaskell MG, Dumay N. Lexical competition and the acquisition of novel words. *Cognition*. 2003;89(2):105–132. doi:10.1016/S0010-0277(03)00070-2.
4. Brennan SE, Clark HH. Conceptual pacts and lexical choice in conversation. *Journal of Experimental Psychology: Learning, Memory, and Cognition*. 1996;22(6):1482–1493. doi:10.1037/0278-7393.22.6.1482.
5. Kobak D, González-Márquez R, Horvát E-Á, Lause J. Delving into LLM-assisted writing in biomedical publications through excess vocabulary. *Science Advances*. 2025;11(27). doi:10.1126/sciadv.adt3813.
6. Geng M, Trotta R. Human–LLM Coevolution: Evidence from Academic Writing. *Findings of ACL*. 2025:12689–12696. doi:10.18653/v1/2025.findings-acl.657.
7. Emi B, Spero M. Technical Report on the Pangram AI-Generated Text Classifier. arXiv:2402.14873. 2024.
8. Sanger MD, Maurer BW. Have Large Language Models Enhanced the Way Civil & Environmental Engineers Write? A Quantitative Analysis of Scholarly Communication over 25 Years. arXiv:2602.03864. 2026.
