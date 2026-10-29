# Plan — study notes L01–L03 (Topic 1, 2A, 2B)

Date: 2026-10-24. Command: `/notes` (`.claude/commands/notes.md` is binding). Reference unit:
`../Finanças 01 - MPE/Notas/S04/` (format only). Block map: `Map/lectures-index.md`.

User choices (Step 0): **Full** depth (U/C/G, all support notes) · **Equation-led** (derive every
equation, then read which assumption drives it) · **Model curves** (4–8 figures/unit, exact
expressions) · **Companions: every unit** (one per unit, contract below).

| Unit | Lecture | Status | Source |
|---|---|---|---|
| L01 | `Aula/Topic1.pdf` (63 slides) — accounting review | taught | slides + Higgins 13e Ch. 1–2, Ross *Fundamentos* Cap. 2–3, Berk *Fundamentals* Ch. 2 |
| L02 | `Aula/Topic2A.pdf` (105) — valuation, NPV, frictionless benchmark | taught | slides + Ross Cap. 9–10, 13–14, 16 §16.2–16.3; Higgins Ch. 7–8; Amaro de Matos Ch. 1–2; Berk Ch. 8–9, 12–13, 16 §16.2 |
| L03 | `Aula/Topic2B.pdf` (63) — taxes, distress, trade-off | taught | slides + Ross Cap. 16 §16.4–16.6, 17 §17.2; Higgins Ch. 6, 8 App.; Amaro de Matos Ch. 2, 4 §4.1; Berk Ch. 16 §16.3–16.5, 17 |

Slide text: `Aula/markitdown/Topic*.txt` (or `pdftotext -layout`); figures/tables on slides: read
the PDF page image. Book pages: printed; PDF = printed + offset + 1 (`Livros/book-registry.json`).

## Notes (slides blocks → note)
**L01** 01 `balance-sheet-view` (1.1–1.2, sl. 4–14) · 02 `balance-sheet-items` (1.3, 15–21) ·
03 `book-vs-market-leverage` (1.4–1.5, 22–31) · 04 `income-statement` (1.6, 32–39) ·
05 `ratios-dupont-roic` (1.7, 40–51) · 06 `cash-flows-fcf` (1.8, 52–62) · 07 formulas · 08 pitfalls · 09 python.
**L02** 01 `present-value-capm-betas` (2A.1–2A.2, sl. 2–23) · 02 `cash-flows-npv-irr` (2A.3–2A.4, 24–38) ·
03 `debt-vs-equity-claims` (2A.5, 39–45) · 04 `complete-markets-state-prices` (2A.6, 46–54) ·
05 `entrepreneur-example` (2A.7, 55–81) · 06 `mm1-arbitrage-put-call` (2A.8, 82–96) ·
07 `mm2-wacc-cost-of-debt` (2A.9–2A.10, 97–105) · 08 formulas · 09 pitfalls · 10 python.
**L03** 01 `tax-shield-mm-taxes` (2B.1–2B.2, sl. 2–15) · 02 `after-tax-wacc-apv` (2B.3–2B.4 + appendix 2B.10, 16–32, 54–63) ·
03 `debt-puzzle-bankruptcy-costs` (2B.5–2B.6, 33–40) · 04 `static-trade-off` (2B.7, 41–45) ·
05 `bank-capital-dividend-irrelevance` (2B.8–2B.9, 46–51) · 06 formulas · 07 pitfalls · 08 python.

## Figures (exact expressions, slide/book numbers)
- **L01:** `L01-roe-leverage` (ROE vs D/E at fixed ROIC: ROE = ROIC + (D/E)(ROIC − r_D(1−τ)); Higgins two-firm example) ·
  `L01-dupont` (margin × turnover × leverage, the slide's 2013 DuPont firms) · `L01-fcf-bridge` (EBIT → FCF → FCFE
  waterfall with the slide's/GM 2020 numbers) · `L01-book-vs-market` (Starbucks 2020 book −7.9 bn vs market cap 122.6 bn; EV build).
- **L02:** `L02-npv-profile` (NPV(r) incl. a multiple-IRR cash flow from the slides) · `L02-sml-comparables` (SML, the three
  comparables, unlevered β_A = 0.78, r = 10.56%) · `L02-payoffs` (min(A,F), max(A−F,0) vs A) · `L02-mm2` (r_E, r_D, r_A vs D/E
  in the entrepreneur example, safe vs risky debt region) · `L02-state-prices` (boom/slump replication, p = 0.357 / 0.595).
- **L03:** `L03-mm-taxes` (V_L = V_U + τD, slide example 600 / 500 / 40%) · `L03-trade-off` (V(K), marginal tax benefit vs
  marginal expected distress cost, K*; comparative statics in τ and C) · `L03-wacc-taxes` (r_E, r_D(1−τ), WACC vs D/V) ·
  `L03-apv-vs-wacc` (slide project: constant D/V → 100,000 both ways; fixed loan → 98,945).

## Companions (one per unit; `/companion` Steps 2–6; check with node + Python at 3 vectors)
**L01 `companion-leverage-roe.html`** — ROE = ROIC + (D/E)(ROIC − r_D(1−τ)), ROIC = EBIT(1−τ)/(D+E).
| Control | Symbol | What it is | Range | Step | Default | Unit | Source | What visibly moves |
|---|---|---|---|---|---|---|---|---|
| Operating profit | EBIT | earnings before interest and taxes | 0 – 400 | 10 | slide (Higgins ex.) | currency | Topic 1 ROIC slide | ROIC level, ROE curve level |
| Invested capital | D+E | interest-bearing debt + equity | 500 – 2000 | 50 | slide | currency | same | ROIC |
| Debt share | D/(D+E) | leverage | 0 – 0.9 | 0.05 | 0.9 (900 of 1000) | — | same | point on the ROE curve |
| Interest rate | r_D | cost of debt | 0 – 20 | 0.5 | slide | % | same | slope sign of ROE in D/E |
| Tax rate | τ | corporate tax | 0 – 50 | 1 | slide | % | same | ROIC and spread |
Landmarks: D = 0 → ROE = ROIC; r_D(1−τ) = ROIC → ROE flat in leverage.

**L02 `companion-mm-state-prices.html`** — two-state firm (slides 55–81): A = p_b X_b + p_s X_s; D(F) = p_b min(X_b,F) + p_s min(X_s,F); E = A − D; r_A, r_D, r_E.
| Control | Symbol | Range | Step | Default | Source |
|---|---|---|---|---|---|
| Boom payoff | X_b | 0 – 5 | 0.05 | 3.15 | slides 55+ |
| Slump payoff | X_s | 0 – 3 | 0.05 | 1.05 | same |
| Boom state price | p_b | 0.05 – 0.9 | 0.001 | 0.357 | same |
| Slump state price | p_s | 0.05 – 0.9 | 0.001 | 0.595 | same |
| Face value of debt | F | 0 – 5 | 0.05 | 1.05 | same |
Read-outs: A, NPV (cost 1), D, E, r_D, r_E, r_A, r_f = 1/(p_b+p_s) − 1. Landmarks: F ≤ X_s → r_D = r_f (safe); A independent of F (MM I).

**L03 `companion-static-trade-off.html`** — slides 41–45 model exactly (cash flow X ~ h on [X_lo, X_hi], debt K, tax τ when solvent,
fixed default cost C): V(K) = V_U + PV tax saving − C·H(K)/(1+r_f). Controls: τ (0–50 %), C, X_lo, X_hi, r_f, with K as the
plotted axis and K* marked. Defaults: the slides give no numbers → declare a page calibration in the footer. Landmarks:
C = 0 → corner (all-debt); τ = 0 → K* at the lowest debt (MM).

## Wiring
`Notas/00-index.md` (3 rows), `Map/lectures-index.md` + `Map/study-guide.md` "Notes:" lines, links to
`Listas/lista-r1..r3` (+ solutions, study packs), `Simulados/quiz-topic*`, PS1/PS2 by number, `NotebookLM/audio/topic*`,
`rules/01..03`, `Aula/aula-01-notes.md` (older ementário notes on Tirole Ch. 1–2; related, not this lecture).
No exercise statement reproduced in notes (number + page only).

## PDF (Step 0 Q5, asked after the fact this run): yes, one per unit
After each unit passes Step 4: `python -I ~/.claude/commands/templates/notes_pdf.py Notas/LNN` → `Notas/LNN/LNN-notes.pdf`; no `Missing character`, no Type 3; link from the map and `Notas/00-index.md`.

## Status (2026-10-25)
Done. L01 10 notes / 5 figures, L02 11 / 5, L03 9 / 6; companions pass node-vs-Python at 3 vectors
(+ landmarks); link check ALL RESOLVE in all units; PDFs L01 63 pp, L02 59 pp, L03 57 pp (no missing
glyphs, no Type 3). Contract changes made by the unit writers:
- L02 companion: F step 0.005 (reaches slide cases F = 0.42, 0.525); default state prices exact 1/2.8, 1/1.05 − 1/2.8.
- L03 companion: calibration uniform X on [50, 150], τ 35%, C 20, r_f 5% (declared in footer); adds an
  inspected-K control and promised-yield read-out; C ≤ 49 and X_lo ≥ 50 so C < X_lo always holds.
Slide errata found: 2A sl. 100 (∂r_E/∂(D/E)), sl. 102 (WACC weights swapped); 2B sl. 13/18 (1+r_g → 1+r_D),
sl. 43 (label), sl. 51 (X_{t+i}).
