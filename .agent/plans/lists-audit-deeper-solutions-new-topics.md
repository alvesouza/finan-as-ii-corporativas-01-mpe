# Lists audit, deeper solutions, new lists for the uncovered topics

Date: 2026-11-12. Request: analyse the real-exercise lists; make the solutions more detailed and
better explained; check every statement is replicated in full with the tables and figures it
uses (standalone); find missing topics and build lists for them. Push to origin at the end.

## Audit findings (main loop, done)
- `tools/check_lists.py`: 11 lists, 168 blocks, 0 failures (head probe only).
- Every block that names an outside problem, figure, table or section either copies it inline
  (Figures 6.5, 6.6, 5.13 transcribed in the statement) or has `#### Context needed to solve it`.
  Figures/tables named only once in a block: 2, both are headings of the transcription. No gap.
- Tail probe (last 40 letters of the final paragraph): 168/168 match the book. It cannot detect a
  dropped trailing part (any prefix of the book text matches), so it was **not** added to the tool;
  each agent below re-reads its statements against the PDF page instead.
- Solutions exist for R1–R3 and Topic 3–5 (detailed + short for topics). Format is rigorous but
  compressed: no "what is asked / approach", algebra steps skipped ("Dividing by 1+μ…"), no
  pitfalls. Rendering bug: R1 Ex. 3, `(t = 1,2,3,4)` split across align rows (lines 194, 207).
- No solutions for R4 (8 of 15 not solved elsewhere), R5 (6), R5b (15), R6 (13), R7 (4) = 46;
  the other 34 R-list exercises are solved in the Topic 3–5 files (matched by Source line).
- Topics with no list (ementário scope, `CLAUDE.md`): governance/control rights + activism
  (Tirole Ch. 8–10), M&A (Tirole Ch. 11, 14; Amaro de Matos Ch. 7–8; Higgins Ch. 9), macro
  implications (Tirole Ch. 13–16). Tirole Ch. 1 has no exercises; governance goes with Ch. 10.

## Work (background agents; format spec `.agent/notes/solutions-and-roadmap-spec.md` §B + §C)
| Agent | Output |
|---|---|
| D1–D6 | Deepen `lista-r1/r2/r3`, `lista-topic3/4/5` `-solutions.tex` to §C; re-verify the list's statements against the PDF; extend check script; recompile |
| N1 | `lista-r5b-…-solutions.tex/.pdf/_check.py`, all 15 |
| N2 | R6: the 13 new exercises (fragment) |
| N3 | R4 (1,3,7,8,12,13,14,15), R5 (2,4,8,11,12,15), R7 (3,9,10,12) (fragments) |
| L1 | `lista-r8-governance-activism.md` + solutions (detailed, short, check) |
| L2 | `lista-r9-mergers-acquisitions.md` + solutions |
| L3 | `lista-r10-macro-implications.md` + solutions |

Main loop afterwards: assemble R4, R5, R6, R7 solution files (new fragments + sections copied
from the deepened Topic 3–5 files, renumbered); list PDFs for R8–R10 (pandoc + LuaLaTeX, as the
topic lists); update `Map/exercises-index.md` crosswalk, `Map/lectures-index.md` list note,
`rules/10_curso_programa.md` if needed; commit; push to origin.

## Gates
`check_lists.py` 0 failures per list · each `_check.py` prints PASS · pdflatex twice, no errors or
undefined refs · `pdffonts` Type 1 + uni=yes only.

## Outcome (2026-11-12)
- All gates pass: check_lists 0 failures on 14 lists; 16 check scripts PASS; every new/changed
  PDF Type 1 (pdflatex) or CID with uni=yes (LuaLaTeX lists).
- Statement gaps found and fixed: Tirole 5.7 (setup of §3.4.1), Tirole 6.10 (§6.3 App. 6 +
  Fig. 6.1), Amaro 3.2.1 footnotes 12–13 (R5 #8); page ranges R5b #10, R5 #11, #15, R7 #12.
- Book slips flagged in solutions (not "fixed" in statements): Tirole 3.8 objective, answers to
  3.3(iii), 3.20(iii), 3.21, 5.1(ii),(iv), 10.3, 10.8, 14.4; inconsistent assumptions in 6.3.
- Re-sync after editing a Topic 3–5 solutions file: `python -I tools/splice_solutions.py
  Listas/lista-r{4,5,6,7}-*-solutions.tex`, then recompile those four.
