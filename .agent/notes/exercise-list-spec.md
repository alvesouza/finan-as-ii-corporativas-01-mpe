# Spec — Ricca topic exercise lists (`Listas/lista-r*.md`)

User request (2026-10-24): one list per Ricca syllabus topic, **15 real book exercises**, ordered
**easy → really hard**, each exercise **copied in full** with its reference at the start.
Plan: `.agent/plans/remap-books-ricca-exercise-lists.md`.

## Candidate pool
- `Map/exercises-index.md`: read the "Ricca syllabus crosswalk" first, then filter rows by the
  topic's tag(s). Use only `Verified = yes` rows (or rows you verify yourself in the MD).
- Allowed books: Tirole, Amaro de Matos, Higgins (Koski–Higgins–Mitton 13e), Ross *Fundamentos*
  9e, Berk–DeMarzo–Harford *Fundamentals* 2e, Grinblatt & Titman 2e. Not PS1/PS2.
- Page offsets (PDF = printed + n): Tirole 13 · Amaro de Matos 18 · Higgins 21 · Ross 24 ·
  Berk 31 · Grinblatt–Titman 14 (Ch. 1–3) / 13 (Ch. 4+). Book MDs are in `Livros/` with
  `<!-- page N -->` = PDF page.
- Pick exercises that test what the topic actually covers (see `Map/lectures-index.md` for
  Topics 1–3 and `rules/` for the topic). Draw from at least 3 books when the pool allows;
  Tirole is the floor for R4, R5, R6. Avoid near-duplicates. An exercise that says "Repeat
  Problem 6" or relies on an earlier one: copy the earlier one in the same block (as part 0),
  or pick another.

## Difficulty
15 exercises in strict increasing difficulty: **Tier 1 Easy (1–5)** · **Tier 2 Exam level
(6–11)** · **Tier 3 Really hard (12–15)**. Tier 3 = index `advanced` rows, Berk starred (`*`)
problems, Ross DESAFIO, Tirole continuous/variable-investment/multi-period variants and Review
Problems, Amaro de Matos proofs. Judge by what the exercise demands, not only the index label.

## File format (Markdown, English frame; statements stay in the book's language)
```
---
tags: [exercise-list, ricca-<rN>, <slug>]
date: 2026-10-24
---

# Exercise list <RN> — <topic title>

<2–3 lines: what the topic covers, 15 exercises easy → really hard, copied verbatim from the
course books for personal study; pages printed (PDF in brackets).> Links: [[Map/exercises-index|exercise index]] · [[rules/<file>|rules]].

## References
| # | Tier | Book | Ch. | Exercise | Printed p. | Answer in book | Trains |
|---|---|---|---|---|---|---|---|
(15 rows; "Trains" = one line)

## Tier 1 — Easy

### 1. <short title>
**Source:** <Book short name>, Ch. <c>, Exercise <id>, p. <printed> (PDF <pdf>) · Answer in book: <yes, p. X | no>

<verbatim statement, all parts (a), (b)…, all data tables as Markdown tables>

---
(…same for 2–15, Tier 2 — Exam level, Tier 3 — Really hard headings…)
```
- The `**Source:**` line must contain one of: `Tirole`, `Amaro de Matos`, `Higgins`, `Ross`,
  `Berk`, `Grinblatt`, and `(PDF <n>)` = PDF page where the statement **starts**.
  The statement must start on the line after a blank line following `**Source:**`.
- **Verbatim**: same words, same order, every part. Allowed edits only: re-typeset math in LaTeX
  (`$...$`, `$$...$$`), rebuild tables as Markdown tables, undo hyphenation/line breaks, drop
  interleaved sidebars/glossary/"MyFinanceLab" margin text that is not part of the problem.
  Currency: write `\$` (escaped), never a bare `$` for money.
- **Self-contained (rule `exercise-lists#2`, 2026-10-31; replaces the old one-line `*Context:*`
  pointer).** Every block must be solvable without opening the book. After the verbatim
  statement, add a `#### Context needed to solve it` sub-block with everything the statement
  points to, each piece headed by its own source (`*From Tirole §3.2, pp. 113–115 (PDF 126–128):*`):
  - a model the statement invokes ("the fixed-investment model of Section 3.2", "properties
    described in section 1.1"): copy verbatim the book passage that sets it up — assumptions,
    timing, notation, and the result equations the question uses (e.g. the threshold $\bar A$,
    pledgeable income). Copy the setup, not the whole section; stop once every symbol and
    assumption in the statement is defined;
  - a table, figure or example the statement reads from ("Table 2.3", "Figure 6.5"): copy the
    table as a Markdown table; transcribe a figure with every value, label and timing step;
  - an earlier problem ("Given your answer to Problem 17", "the firm in exercise 14.2", "the
    preceding problem"): copy it in full, with its own Source line, as **Part 0** inside this
    sub-block.
  Keep the statement itself first (right after the Source line) so `tools/check_lists.py` still
  anchors on it.
- **Garbled math or tables in the MD** (Grinblatt–Titman always: =, +, −, Greek letters and tables
  are stripped; Tirole/Amaro sometimes): read the PDF page itself with the Read tool
  (`pages: "<pdf page>"`) and typeset from the image. Never guess a symbol.

## Gate (must pass before you report)
`python -I tools/check_lists.py Listas/<your file>` → `15 exercises checked, 0 failures`.
It matches the first 60 letters of each statement against the source MD near the cited PDF page
(math stripped). If a G&T statement fails only because the MD lost words, re-check it against
the PDF image and report it as such; do not reword to make the check pass.
