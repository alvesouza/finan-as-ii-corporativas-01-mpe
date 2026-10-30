# PS1 solutions (Listas/PS1.pdf)

Goal: a detailed worked solution and a short answer key for Problem Set 1 (3 exercises).

Outputs (next to the other list solutions in `Listas/`):
1. `Listas/PS1-solutions.tex` / `.pdf`: detailed, same macros as `lista-r2-valuation-solutions.tex`
   (notation, numbered steps, numbered equations, intuition, refs to Berk 2e Ch. 2 and Ch. 9).
2. `Listas/PS1-solutions-short.tex` / `.pdf`: direct answers only, 1-2 pages.
3. `Listas/PS1-solutions_check.py`: asserts every printed number (same pattern as the R2 check).

Key choices:
- Ex. 2: tax rate implied by the report, 2,625/7,500 = 35%; consulting fee is sunk; only 1,000
  of overhead is incremental; equipment has zero salvage; NWC out at t=0, back at t=10.
- Ex. 3: incremental (replace minus keep) FCF; old machine's book value 100,000 sold at 50,000
  gives a tax credit on the loss; both machines run 10 more years, zero salvage.

Verify: `python -I Listas/PS1-solutions_check.py` -> PASS; pdflatex twice; `pdffonts` Type 1 only.
