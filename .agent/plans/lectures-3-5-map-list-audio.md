# Lectures 3, 4A, 4B, 5 — map, exercise list R7, NotebookLM audio

Date: 2026-11-08. New slides (Prof. Ricca): `Aula/Topic_3.pdf` (91), `Topic4_A.pdf` (69),
`Topic4_B.pdf` (62), `Topic_5.pdf` (30). Text extracts: `Aula/markitdown/*.txt` (pdftotext -layout, UTF-8).

## Lecture → syllabus
| Lecture | Content | Syllabus item | Existing list |
|---|---|---|---|
| Topic 3 | Adverse selection: lemons, credit bureau, pecking order, Stiglitz–Weiss, collateral signalling, Leland–Pyle, IPO underpricing (Rock) | 5 (Tirole Ch. 6) | R5 |
| Topic 4A | Holmström–Tirole fixed investment, IC/IR, pledgeable income, credit rationing, debt vs. equity | 4 (Tirole Ch. 3) | R4 |
| Topic 4B | Asset substitution, debt overhang, renegotiation (benefits/costs), default as insurance (Indarte), Karlan–Zinman | 4 | R4 (partly) |
| Topic 5 | Nonverifiable income, threat of termination, sovereign debt (Eaton–Gersovitz, Arellano) | none (new) | none |

## Part A — map (main loop)
- `Map/lectures-index.md`: 4 table rows, 4 lecture blocks (block / slides / content / examples),
  Practise / Books / Bridges lines, syllabus note on the numbering, new synthesis points.

## Part B — list R7 (3 background agents, fragments assembled in main loop)
`Listas/lista-r7-lectures-3-5.md`, 20 real exercises, easy → really hard, no repeats of R1–R6,
format of `.agent/notes/exercise-list-spec.md` + `rules/exercise-lists.md` (source first, full
statement verbatim, `#### Context needed to solve it`).

| # | Tier | Exercise | Lecture |
|---|---|---|---|
| 1 | Easy | Ross Cap. 15, 15.3 (Subpreço de IPO) | 3 IPO |
| 2 | Easy | Grinblatt–Titman 16.14 (DIP financing) | 4B overhang |
| 3 | Easy | Amaro de Matos 3.1.5 #7 (convertibles, warrants, call provisions) | 4B mitigation |
| 4 | Easy | Grinblatt–Titman 16.1 (project A or B) | 4B asset substitution |
| 5 | Easy | Grinblatt–Titman 19.6 (ABC undervalued equity issue) | 3 pecking order |
| 6 | Exam | Amaro de Matos 6.2.7 #4 + #6 (Rock) | 3 IPO |
| 7 | Exam | Berk *16.26 (Zymase) | 4B asset substitution |
| 8 | Exam | Grinblatt–Titman 16.12 + 16.13 (Ajax) | 4B overhang |
| 9 | Exam | Grinblatt–Titman 16.3 (senior bond, subordinated loan) | 4B |
| 10 | Exam | Amaro de Matos 3.1.5 #9 (Myers 1977) | 4B overhang |
| 11 | Exam | Tirole 6.2 (more on pooling) | 3 lemons |
| 12 | Exam | Tirole 3.3 (random private benefits) | 4A |
| 13 | Exam | Amaro de Matos 5.2.5 #1 (β° decreasing in q) | 5 termination |
| 14 | Exam | Tirole 3.6 (renegotiation and debt forgiveness) | 4B renegotiation |
| 15 | Hard | Amaro de Matos 5.2.5 #2 (strategic vs liquidity default) | 5 |
| 16 | Hard | Tirole 4.17 (loan size and collateral) | 4A collateral |
| 17 | Hard | Tirole 7.3 (dealing with asset substitution) | 4B |
| 18 | Hard | Tirole 4.9 (borrower-friendly bankruptcy court) | 4B/5 |
| 19 | Hard | Tirole 6.7 (endogenous communication among lenders) | 3 credit bureau |
| 20 | Hard | Amaro de Matos 3.2.6 #2 (Leland–Pyle, mean-variance) | 3 signalling |

No book exercise covers the Eaton–Gersovitz sovereign model or Karlan–Zinman; stated in the list.
Gate: `python -I tools/check_lists.py Listas/lista-r7-lectures-3-5.md` → 0 failures.

## Part C — audio (main loop)
`NotebookLM/audio/topic3|topic4a|topic4b|topic5-audio-part1..3.md` (concepts / derivations /
exercises). < 5,000 chars each, no language line, sources by `NotebookLM/sources/` names.
Copy slides to `sources/Aula_Topic3…5 - <title>.pdf`, lists R4, R5, R7 to `sources/Lista_R*.md`.
Update `NotebookLM/README.md` table.

## Verify
check_lists gate; `wc -m` per prompt (< 5,000); grep prompts for "language"; git status.
