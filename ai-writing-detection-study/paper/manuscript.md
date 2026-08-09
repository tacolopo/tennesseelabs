# When Human Writing Moves: AI-Text Detection, Style Editing, and the Problem of a Historical Baseline

**Author:** [Author name]
**Affiliation:** Tennessee Labs, Tennessee, USA
**Correspondence:** hello@tennesseelabs.com

## Abstract

AI-text detectors are commonly evaluated against a stable binary: archived human writing versus newly generated machine text. That design may become less informative as people repeatedly read, edit, and converse with large language models (LLMs). We report a paired pilot evaluation of Pangram 3.3.2 on 20 pre-2020 open-access biomedical introductions and 80 matched LLM-derived passages. For each source topic, a pinned OpenAI model produced an introduction that was left unchanged, copyedited, revised with a rule-based “deslopping” prompt, or substantially paraphrased without detector feedback. Pangram classified all 20 historical passages as human and all 80 LLM-derived passages as AI (document-level AI fractions 0.0 and 1.0, respectively). Deslopping shortened passages but did not alter any classification; neither did the stronger paraphrase. These results do not contradict prior demonstrations that paraphrasing can defeat other detectors. They show that removal of familiar AI commonisms is not necessarily equivalent to crossing a contemporary detector’s decision boundary. We argue that the larger measurement problem is temporal. Human linguistic distributions respond to exposure and coordination, while LLM-associated vocabulary is already changing scientific writing. A detector validated mainly against pre-LLM prose may therefore estimate distance from a historical human distribution rather than machine authorship. Future evaluations should use time-indexed controls, longitudinal within-author samples, disclosed AI-assisted writing, and unaided contemporary writing.

**Keywords:** AI-text detection; scientific writing; paraphrasing; stylometry; lexical entrainment; human–LLM coevolution

## 1. Introduction

AI-text detection is often posed as classification between two natural classes: human-written and machine-generated text. The labels appear simple, but the distributions underneath them are not fixed. Generators change, editing practices change, and human language changes in response to the language people encounter.

Robustness studies have shown that transformations can expose detector brittleness. Krishna et al. [1] used the DIPPER paraphraser to reduce DetectGPT accuracy from 70.3% to 4.6% at a fixed 1% false-positive rate, while also reducing the performance of GPTZero, watermarking, and OpenAI’s former classifier. Wang et al. [2] examined editing, paraphrasing, co-generation, and prompting attacks; averaged across detectors, performance declined by 35%. An apparently strong detector on untouched model output may therefore fail after meaning-preserving transformation.

The popular response to recognizable “AI style” has produced editing checklists that remove recurrent lexical, syntactic, and formatting patterns. We call this process *deslopping*: revising formulaic prose for directness, specificity, varied rhythm, and appropriate disciplinary register. Deslopping differs from detector-guided evasion. It need not query a detector, optimize a score, introduce errors, or obscure provenance. It represents an editorial intervention that a writer might apply because the original prose is repetitive or generic.

We ask whether ordinary copyediting, deslopping, or general paraphrasing changes the classification of matched scientific prose under a current commercial detector. We then consider what a historical human comparison means if human writing is itself moving toward patterns associated with LLMs.

Repeated exposure can support lexical acquisition [3], and interlocutors coordinate lexical choices through conceptual pacts and lexical entrainment [4]. LLMs now participate directly and indirectly in that linguistic environment. Kobak et al. [5] found abrupt increases in LLM-associated style words across more than 15 million biomedical abstracts and estimated that at least 13.5% of 2024 abstracts had been processed with LLMs. Geng and Trotta [6] documented subsequent changes in conspicuous LLM-favored terms and described the process as human–LLM coevolution. These observations do not show that every lexical shift reflects unconscious adoption; direct AI editing, changing publication norms, and strategic removal of known markers are competing explanations. They do establish that contemporary scientific prose is not sampled from the same distribution as pre-LLM prose.

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

### 2.4 Detection and reproducibility

We submitted each passage once to Pangram’s V3 API with public dashboard links disabled. The detector identified itself as version 3.3.2. We archived complete responses, including document-level fractions and segment windows. AI-derived text was the positive class. Pangram was selected because it offered a current programmatic interface within budget. Its developers describe a transformer classifier trained with hard-negative mining and synthetic mirrors [7]. Originality.ai was excluded before data collection because API access required an enterprise subscription beyond the project budget.

Every source, prompt response, transformation, detector response, model identifier, and SHA-256 text hash was retained. A deterministic shuffle assigned all 100 passages anonymous IDs for planned human evaluation. Reviewers will provide a human/AI judgment, confidence, perceived quality, and comments. The private condition key is stored separately. Human ratings were not complete for this report.

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

## 4. Discussion

### 4.1 Deslopping was not detector evasion

The direct result is negative: removing recognizable AI commonisms did not make generated introductions appear human to Pangram. The detector remained maximally confident after copyediting, deslopping, and substantial paraphrasing.

This should not be generalized to all detectors, generators, domains, or attacks. Prior studies evaluated different architectures and stronger or detector-targeted transformations [1,2]. DIPPER explicitly controls lexical diversity and content reordering, and adversarial studies may search over candidates or exploit model-specific weaknesses. Our transformations were single-pass, meaning-preserving edits without detector feedback. The contrast is informative. “Sounds less like stereotypical AI prose” and “crosses a detector boundary” are different hypotheses.

The saturated response also limits interpretation. We can conclude that these 80 passages remained on Pangram’s AI side of the boundary. We cannot infer their distance from that boundary from aggregate fractions alone. Segment-level analysis and additional detectors are needed.

### 4.2 The historical-control problem

The stronger implication concerns the negative class. Pre-2020 prose provides relatively uncontaminated historical controls, but the deployment population for an AI detector is contemporary writing. Those are not interchangeable.

Language users adapt to exposure. Repeated encounters increase the likelihood that unfamiliar forms become learned and available [3]. Conversational partners reuse one another’s referring expressions [4]. LLMs now supply language across email, education, journalism, software interfaces, and scholarly editing. A person can encounter model-shaped language without directly asking a model to write.

At least three processes may move contemporary human prose toward an LLM-associated distribution:

1. **Direct assistance:** a person accepts or edits generated wording.
2. **Strategic adaptation:** writers remove conspicuous AI markers or adopt conventions rewarded by institutions.
3. **Incidental accommodation:** recurrent exposure changes which words and constructions feel available, ordinary, or authoritative.

Our experiment does not distinguish these mechanisms. Corpus evidence nevertheless shows the aggregate distribution moving. Biomedical abstracts contain abrupt increases in LLM-associated vocabulary [5], while later changes suggest authors and tools react to public knowledge of those markers [6]. The categories are coupled: LLMs learn from human text; people learn from environments populated by LLM text; newer models may train on the resulting mixture.

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

The transformations came from the same model family that produced the raw passages, and semantic preservation has not yet been independently rated. The paraphrase was not DIPPER and was not optimized against Pangram. “Deslopping” operationalizes one fixed instruction set, not a standardized intervention. Pangram is proprietary and its version may change. Finally, the moving-baseline account is a hypothesis supported by linguistic theory and corpus trends, not a causal finding from this detector experiment.

## 6. Conclusion

In this paired biomedical pilot, Pangram distinguished 20 historical human introductions from 80 matched LLM-derived passages without error. Copyediting, removal of common AI stylistic patterns, and single-pass paraphrasing did not change any classification. Editing away visible “AI style” did not remove the evidence used by this detector.

The more durable challenge may be the reference class. As LLM-associated language circulates through the environments in which people read, think, and write, human prose may move toward model-associated distributions. Historical controls then become simultaneously attractive and outdated: attractive because provenance is clearer, outdated because they may not represent the humans on whom detectors are used. AI-text detection should be evaluated as a temporally shifting measurement problem, not a permanent binary classification task.

## Data and code availability

The study directory contains source provenance, exact generated and transformed passages, raw API responses, hashes, document-level results, and a blinded human-rating packet. Public release should retain source licenses and exclude API credentials and the private condition key until human evaluation is complete.

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
