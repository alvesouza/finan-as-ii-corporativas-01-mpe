# Plan: quant-focus analysis PDF + mock midterm (Topics 1–2B) with solutions

## Deliverables
1. `Artigos/quant-focus-ranking.tex/.pdf` — which of the six ARFE surveys is most quant-focused
   (model/asset-pricing sense vs. empirical-returns sense), ranking table, section/page cites.
2. `Simulados/mock-midterm-topics-1-2b-statements.tex` — every statement once, as macros,
   `\input` by both documents below (no duplicated text).
3. `Simulados/mock-midterm-topics-1-2b.tex/.pdf` — exam paper in the format of `Prova/q2.pdf`
   (Question N (marks), parts (a)… with marks).
4. `Simulados/mock-midterm-topics-1-2b-solutions.tex/.pdf` — full statement, then worked solution.
5. `Simulados/mock-midterm-topics-1-2b-solutions_check.py` — recomputes every printed number.

## Mock composition (100 marks, all real questions, verbatim, source line first)
- Q1 (40): 1.1 Berk 2.24 (EV vs. market cap multiples; Topic 1) · 1.2 Berk 9.13 (incremental
  earnings vs. FCF; Topics 1/2A) · 1.3 Berk 16.19–16.21 (equity vs. debt vs. distress; 2B) ·
  1.4 Berk 17.11–17.13 (payout with corporate and dividend taxes; 2B; 17.11 is part 0).
  None of these is used in Listas R1–R3 or PS1–PS2.
- Q2 (60): previous-year midterm Question 2 (`Prova/q2.pdf`), verbatim — the only real past exam
  question; constant D/E, CAPM, MM with taxes, WACC vs. APV, debt schedule and PV(ITS).

## Checks
- Berk statements: first 60 letters found in `Livros/Fundamentals…md` at the cited PDF page
  (functions from `tools/check_lists.py`).
- `python -I Simulados/mock-midterm-topics-1-2b-solutions_check.py` → PASS.
- pdflatex with lmodern + cmap; `pdffonts` Type 1 only, uni = yes.

## Publishing
Commit only files written here (+ the NotebookLM `artigos-audio-*` prompts and README row).
Repo is PUBLIC: third-party PDFs (`Artigos/*.pdf`, `NotebookLM/sources/Artigo_*.pdf`,
`Prova/q2.pdf`) stay uncommitted; tell the user.
