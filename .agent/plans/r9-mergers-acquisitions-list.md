# Plan — list R9 Mergers and acquisitions (+ solutions)

Parent: `.agent/plans/lists-audit-deeper-solutions-new-topics.md` (item L2).

Files: `Listas/lista-r9-mergers-acquisitions.md`, `-solutions.tex/.pdf`, `-solutions-short.tex/.pdf`,
`-solutions_check.py`. Specs: `rules/exercise-lists.md`, `.agent/notes/exercise-list-spec.md`,
`.agent/notes/solutions-and-roadmap-spec.md` §B+§C. Label prefix `r9e<n>-`.

Exercises (none used in other lists; Amaro 8.1.5 #5, 8.2.6 #10, Tirole 14.1, 14.4 excluded):

| # | Tier | Source | Trains |
|---|---|---|---|
| 1 | Easy | Higgins 9.1 | M&A facts: target returns, discount rate, control premium, liquidation floor, MBO |
| 2 | Easy | G&T 20.5 + 20.8 | Where LBOs fit; MBO incentives without manager change |
| 3 | Easy | Higgins 5.10 (Figure 5.3 transcribed) | Announcement returns, efficiency, price above bid |
| 4 | Easy | Amaro 7.2.4 #3 | Sources of LBO premiums |
| 5 | Easy | Amaro 8.1.5 #1 | Grossman–Hart free riding; toehold makes p >= v profitable |
| 6 | Exam | Higgins 9.3 | Acquisition cost (equity + debt) and value of control |
| 7 | Exam | Higgins 9.9 | EPS-dilution criterion, maximum premium |
| 8 | Exam | Amaro 8.2.6 #3 | Hansen: lemons kill cash, stock works if x < 150 |
| 9 | Exam | Amaro 8.2.6 #1 | Fishman (1988) preemptive bid: partial revelation |
| 10 | Exam | Amaro 8.1.5 #8 | Jegadeesh–Chowdhry: no pooling, toehold as signal |
| 11 | Exam | Tirole 11.1 | Poison pill (flip-over) when new shares vote |
| 12 | Hard | Amaro 8.2.6 #4 | Hansen: stock offer dominates every cash offer |
| 13 | Hard | Amaro 8.2.6 #8 | Fishman (1989): cash signals at a lower face value than debt |
| 14 | Hard | Tirole 14.2 | Shleifer–Vishny with arbitrary resale price P |
| 15 | Hard | Tirole 14.3 | Financial muscle, random retooling cost, P + rho* = 1 |

Steps: list MD -> gate `check_lists.py` -> check script -> detailed tex -> short tex ->
pdflatex x2 each, pdffonts, clean aux files.
