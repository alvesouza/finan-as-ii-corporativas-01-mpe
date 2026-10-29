# Plan — remap books (incl. 2 new ones) to the Ricca syllabus, then one exercise list per topic

Date: 2026-10-24. User choices: Ricca syllabus topics (7), 15 exercises each, easy → really hard,
**full exercise statement copied verbatim with the reference at the top**, sources = Tirole,
Ross *Fundamentos*, Higgins, Amaro de Matos + the new books.

## Ricca topic ↔ index-topic crosswalk
| Ricca | Theme | Index topic tag(s) |
|---|---|---|
| R1 | Intro, accounting revision, capital structure | Introduction & stylized facts |
| R2 | Valuation: FCF, discount rates, NPV | Valuation |
| R3 | Frictionless benchmark, taxes, distress, static trade-off (+ payout) | MM benchmark |
| R4 | Moral hazard, financing capacity, inv.–CF sensitivity, debt vs equity | Agency & capital structure |
| R5 | Asymmetric information and capital structure | Asymmetric information |
| R5b | Trade credit and working capital | **new** Working capital & trade credit (Ross Cap. 18–20 move here from Liquidity) |
| R6 | Liquidity and risk management | Liquidity |
Out of Ricca scope (kept in index, not used): Activism, M&A, Macro implications.

## Steps
1. Convert new PDFs → `Livros/*.md` with `<!-- page N -->` (PDF page). Done (pymupdf, scratchpad `pdf2md.py`).
   - Berk, DeMarzo & Harford, *Fundamentals of Corporate Finance* 2e (2011), 773 pp, printed = PDF − 31.
     NOT the syllabus's Berk & DeMarzo *Corporate Finance* (different chapter numbers).
   - Grinblatt & Titman, *Financial Markets and Corporate Strategy* 2e (© 2002) = syllabus edition.
   - Duplicate `... libgen.li (1).pdf` is byte-identical to the Berk PDF — ask before deleting.
2. Index new books into `Map/exercises-index.md` (same 8 columns), in-scope chapters only;
   index Ross Cap. 20; add the crosswalk + retag note. (parallel subagents, one per book)
3. Update `Livros/BOOKS.md`, `Map/books-index.md` (chapter → topic rows for the new books),
   `rules/10_curso_programa.md` bibliography line if it lists books.
4. Write `Listas/lista-r<N>-<slug>.md` × 7: 15 exercises, ordered by difficulty in 3 tiers
   (Easy 5 · Exam 6 · Really hard 4), each = header `Source, Ch., Ex., printed p.` + verbatim
   statement (math in LaTeX, tables kept). Only `Verified = yes` rows or re-verified in the MD.
5. Gate: every quoted statement grep-matches its source MD on the cited page; no invented numbers.
6. Report; ask about study-pack PDF and solutions PDF (style §9).

## Status (2026-10-24)
Steps 1–5 done. Index: +471 Berk, +235 G&T, +40 Ross Cap. 20, 84 rows retagged to
`Working capital & trade credit`. Lists: 7 × 15 = 105 exercises; `tools/check_lists.py` →
`105 exercises checked, 0 failures`. Step 6 (study-pack / solutions PDFs) asked at hand-over.
