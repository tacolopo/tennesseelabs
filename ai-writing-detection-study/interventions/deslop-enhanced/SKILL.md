---
name: deslop-enhanced
description: Revise substantial prose to reduce repetitive language-model writing patterns while preserving meaning, evidence, citations, technical terminology, and authorial register. Use for controlled de-AI editing experiments, scientific prose revision, or requests to remove formulaic AI commonisms, including overused colons, em dashes, rhetorical pivots, symmetric lists, canned transitions, false agency, and uniform sentence rhythm. Do not use detector scores as revision feedback.
---

# Deslop Enhanced

Revise prose for specificity and natural variation. Preserve the author's
claims and voice. Never promise that edited text is human-written or that it
will evade a detector.

## Workflow

1. Record the source text without altering it.
2. Identify repeated patterns across the whole passage. Do not flag an isolated
   construction merely because it appears in a catalog.
3. Protect quotations, citations, equations, terminology, numerical values,
   headings required by a template, and field-specific conventions.
4. Revise the smallest span that fixes each material pattern.
5. Compare source and revision sentence by sentence. Restore any claim,
   qualification, causal direction, citation scope, or uncertainty that moved.
6. Return the revision. When an audit is requested, also list changes by pattern
   category without claiming authorship or detector success.

For a controlled study, start every intervention from the same raw generation.
Never feed detector results back into this workflow.

## Editing priorities

### Preserve content before style

Do not add facts, examples, citations, limitations, or interpretations. Keep
negation, modality, effect direction, units, confidence intervals, and the
distinction between association and causation intact. A less polished faithful
sentence is better than a fluent distortion.

### Replace announcements with claims

Cut throat-clearing such as "It is important to note," "This section explores,"
and "The key takeaway is." State the supported claim. Remove conclusions that
merely restate a preceding sentence.

### Remove mechanical contrast

Rewrite repeated `not X but Y`, `while X, Y`, `whether X or Y`, and
question-answer pivots. Preserve genuine scientific contrasts. Prefer a direct
claim when the rejected alternative contributes no information.

### Correct false agency and abstraction

Name the actor when the evidence identifies one. Do not invent an actor to force
active voice; passive voice remains appropriate when the procedure or result
matters and the actor is unknown or irrelevant.

### Vary rhythm without manufacturing quirks

Combine needless fragments and split overloaded sentences. Vary sentence and
paragraph length in response to the argument, not by random synonym replacement.
Avoid conspicuous slang, typos, rare-word substitutions, and personal anecdotes
that were absent from the source.

### Audit punctuation as a pattern

Colons are allowed for definitions, ratios, quotations, and a genuine expansion
of a complete clause. Revise them when several sentences use the same
`announcement: explanation` template, a colon introduces a single ordinary
clause, or paragraph endings repeatedly use a colon for suspense.

Avoid em dashes as a default connective. Use commas, parentheses, or separate
sentences according to the grammatical relationship. Do not replace every em
dash with the same mark. Limit semicolons when they create repeated balanced
couplets. Keep punctuation required by citations, code, mathematics, and data.

### Reduce templated symmetry

Break up serial three-item lists, parallel headings, bold-label bullets, repeated
sentence openings, and paragraphs that all follow claim-explanation-summary.
Retain symmetry when it represents the actual experimental design or taxonomy.

### Prefer precise verbs and nouns

Replace vague significance language, inflated stakes, generic praise, and
business metaphors with the supported observation. Keep established technical
terms even when they are uncommon in general prose.

Read [references/commonisms.md](references/commonisms.md) when diagnosing or
auditing a substantial passage.

## Final checks

- Did any fact, number, citation scope, or degree of certainty change?
- Does punctuation follow syntax rather than a house-wide ban?
- Do two or more paragraphs share the same rhetorical skeleton?
- Are lists determined by content rather than a preference for three items?
- Did editing introduce vocabulary the putative author would not use?
- Can any sentence be cut without losing evidence or reasoning?
- Was detector feedback kept out of the editing loop?
