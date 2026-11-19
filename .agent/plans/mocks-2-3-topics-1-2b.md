# Plan: mock midterms 2 and 3 (Topics 1–2B) with true/false sections, solutions, push

## Deliverables (per mock k = 2, 3), in `Simulados/`
1. `mock{k}-midterm-topics-1-2b-statements.tex` — every statement once as a macro, source line first,
   verbatim (rules/exercise-lists.md); `\input` by the two documents below.
2. `mock{k}-midterm-topics-1-2b.tex/.pdf` — exam paper, format of mock 1 / `Prova/q2.pdf`.
3. `mock{k}-midterm-topics-1-2b-solutions.tex/.pdf` — statement, then worked solution, boxed answer.
4. `mock{k}-midterm-topics-1-2b-solutions_check.py` — recomputes every printed number; PASS/FAIL.

## Composition — all real exercises; none used in Listas R1–R3, PS1–PS2 or mock 1 unless noted
True/false items are the books' own "Answer true or false" sets (all parts kept); 2 marks each.

### Mock 2 (100)
- Q1 (26) T/F: Higgins Ch. 1 Ex. 3 (a–g, accounting) + Higgins Ch. 8 Ex. 1 (a–f, cost of capital).
- Q2 (34) Topics 1/2A: Berk 13.1 + 13.3 (market vs. book weights) · 13.18–13.19 (project-specific
  discount rate) · 13.15 (full WACC: DDM, preferred, market values) · 16.3 (MM, levered equity
  returns). (13.4 and 13.20 were dropped: Lista R2 already uses them.)
- Q3 (40) Topic 2B: Berk 16.10 (riskless firm, value of leverage) · 16.16–16.17 (fixed debt; constant
  D/V WACC) · 16.23 (CAPM, distress) · 17.9 (dividend tax vs. repurchase).

### Mock 3 (100)
- Q1 (28) T/F: Higgins Ch. 2 Ex. 3 (a–g, ratios; also in Lista R1) + Higgins Ch. 4 Ex. 3 (a–f,
  growth and buybacks) + Berk Ch. 16 Critical Thinking 2 ("what is wrong with this argument").
- Q2 (32) Topics 1/2A/MM: Berk 16.2 (biotech, MM fractions) · 16.4* (homemade leverage) · 13.21
  (division WACC) · 16.6 (cost of equity with leverage).
- Q3 (40) Topic 2B: Berk 16.7–16.8 (ITS, NI vs. FCF) · 16.9 + 16.12 (PV of permanent shields) ·
  16.13–16.15 (pre-/after-tax WACC) · 17.3–17.5 (repurchase vs. dividend, perfect markets).

No topic gap: every topic in 1–2B has real exercises, so no original exercises.

## Checks
- Statements: first 60 letters found at the cited PDF page (functions of `tools/check_lists.py`).
- `python -I Simulados/mock{k}-...-solutions_check.py` → PASS.
- pdflatex with lmodern + cmap; `pdffonts`: Type 1 only, uni = yes; render pages and look.

## Publishing
Commit the mocks, this plan, and the two cheatsheets from this session (long + two-page); push to
origin/main with the session's Co-Authored-By line.
