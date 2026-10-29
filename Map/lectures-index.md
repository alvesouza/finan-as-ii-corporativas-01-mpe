---
tags: [map, cross-reference, lectures]
date: 2026-10-24
---

# Lectures Index

Lecture-centred view of the real slides by Prof. Bernardo Ricca (`Aula/Topic*.pdf`; text
extracts in `Aula/markitdown/`). Each block lists its slide range, the worked examples, the key
results, the problem-set questions that practise it, and the book sections that back it (pages
from [[Map/books-index|books-index]], printed pages).

> **Syllabus note.** The real syllabus (`syllabus(1).pdf`, extract `Aula/markitdown/syllabus.txt`)
> differs from the ementário that the rest of `Map/` was built on: main text **Berk & DeMarzo
> (2011)** + Tirole; topics 1 Intro/accounting/capital structure · 2 Valuation · 3 Frictionless
> benchmark, taxes, distress, trade-off · 4 Moral hazard and financing capacity (Tirole Ch. 3) ·
> 5 Asymmetric information (Tirole Ch. 6) · 5′ Trade credit and working capital · 6 Liquidity and
> risk management (Tirole Ch. 5). Grading: problem sets 10%, paper presentation 10%, midterm 20%,
> final 60%. Berk & DeMarzo is **not** in `Livros/`; book links below use the local books.

| Lecture | Slides | Syllabus item | Rules | Problem set | Quiz | Audio prompt |
|---|---|---|---|---|---|---|
| [[Aula/Topic1.pdf\|Topic 1]] — Accounting review | 63 | 1 | [[rules/01_introducao_fatos\|Topic 1]] | PS1 Ex. 1 | [[Simulados/quiz-topic1-accounting-2026-10-24\|quiz]] | `NotebookLM/audio/topic1-audio.md` |
| [[Aula/Topic2A.pdf\|Topic 2A]] — Valuation, NPV, MM | 105 | 2 → 3 | [[rules/02_valuation\|Topic 2]] · [[rules/03_benchmark_mm\|Topic 3]] | PS1 Ex. 2–3; PS2 Ex. 1, 3(a–b), 4 | [[Simulados/quiz-topic2a-valuation-mm-2026-10-24\|quiz]] | `NotebookLM/audio/topic2a-audio.md` |
| [[Aula/Topic2B.pdf\|Topic 2B]] — Taxes, distress, trade-off | 63 | 3 | [[rules/03_benchmark_mm\|Topic 3]] | PS2 Ex. 2, 3(c) | [[Simulados/quiz-topic2b-taxes-tradeoff-2026-10-24\|quiz]] | `NotebookLM/audio/topic2b-audio.md` |

---

## Topic 1 — Introduction and accounting review
#aula/topic1 #topic/introduction

| Block | Slides | Content | Examples / data |
|---|---|---|---|
| 1.1 Fields of financial economics | 4–5 | Asset pricing (prices of claims, risk premia → discount rates), corporate finance (governance, financing choices, effect on value), banking | — |
| 1.2 Balance-sheet view of the firm | 6–14 | $A = L + E$ in book **and** market value; recognition of tangible vs. intangible assets; historical cost vs. market value; firms sell goods/services **and promises**; liabilities senior, equity junior and residual; $FCF_A = FCF_L + FCF_E \Rightarrow A = L + E$; cash-flow–production cycle | Silicon Valley Bank (held-to-maturity vs. available-for-sale); intangibles ≈ 90% of S&P 500 EV; Higgins cycle diagram |
| 1.3 Balance-sheet items | 15–21 | Current vs. non-current assets and liabilities; goodwill; depreciation is not a cash expense; book value = cost − accumulated depreciation; net working capital | Rise in corporate cash (Faulkender et al., 2019); GPA 2020 (trade payables as short-term finance) |
| 1.4 Book vs. market equity | 22–27 | Market cap = price × shares; market values forward-looking, book values backward-looking; off-balance-sheet assets and liabilities; market-to-book (growth vs. value) | Starbucks 2020: book equity −7.9 bn USD vs. market cap 122.6 bn USD |
| 1.5 Leverage and liquidity ratios | 28–31 | Debt-equity (book vs. market), net debt (cash as negative debt), enterprise value $= E^{mkt} + D - \text{cash}$, current ratio, quick ratio, covenants | — |
| 1.6 Income statement | 32–39 | Accrual and matching principles; depreciation spreads capex; gross profit; COGS ≈ variable, other opex ≈ fixed → operating leverage; EBIT; net income; statement of equity | Accrual table (cash vs. revenue); GM 2020 income statement |
| 1.7 Income-statement analysis | 40–51 | EPS and diluted EPS; gross/operating/net margins (efficiency vs. market power vs. capital structure); economic earnings vs. hurdle rate; receivable/payable days; EBITDA; interest coverage; ROE, ROA, asset turnover; **DuPont** ROE = margin × turnover × leverage; ROE pitfalls (timing, risk, book value); **ROIC** $= EBIT(1-\tau)/(\text{interest-bearing debt} + E)$; P/E | DuPont 2013: Google, JPMorgan, Hyundai, Chevron; Higgins ROIC example (two firms, same EBIT, 0 vs. 900 debt) |
| 1.8 Cash-flow statement and FCF | 52–62 | Profits ≠ cash; operating (add back non-cash items, −ΔAR, +ΔAP, −Δinventory), investing (−capex), financing; net cash flow; CFO; **FCF** $= EBIT(1-\tau) + \text{Dep} - \text{Capex} - \Delta NWC$; **FCFE** = FCF − after-tax interest + net borrowing; FCF → EV, FCFE → equity value; uses of FCF | GM 2020 cash-flow statement |

**Notes:** [[Notas/L01/L01-00-map|L01 map]] (full study notes, figures, companion).
**Practise:** PS1 Ex. 1(a) net income vs. FCF (blocks 1.6, 1.8); PS1 Ex. 1(b) deferred taxes in the FCF formula (block 1.8, slide 54 lists deferred taxes as a non-cash add-back).
**Books:** Higgins 13e Ch. 1 (pp. 3–36: cash-flow cycle §1.1, balance sheet §1.3, income statement §1.4, cash-flow statement §1.6, market vs. book §1.7.1, imputed costs §1.7.3); Ch. 2 (pp. 37–76: DuPont §2.2.1, ROE problems §2.3, ROIC §2.3.2, P/E and market-to-book §2.3.3); Ross *Fundamentos* Cap. 2 (pp. 24–51: §2.1 balance sheet, §2.2 income statement, §2.4 cash flow from assets), Cap. 3 (pp. 52–92, ratio analysis).
**Feeds:** block 1.2 ($A = D + E$ in market value) and block 1.8 (FCF) are the inputs of Topic 2A.

---

## Topic 2A — Valuation, the NPV rule and the frictionless benchmark
#aula/topic2a #topic/valuation #topic/mm-benchmark

| Block | Slides | Content | Examples / data |
|---|---|---|---|
| 2A.1 Present value | 2–7 | $P_A = \sum_t E[\tilde d_t]/(1+r_t)^t$; expected vs. realised return; spot rates; discount rate = risk-free + risk premium | Treasury coupon bond priced with spot rates |
| 2A.2 Discount rates and betas | 8–23 | CAPM $r = r_f + \beta(E[r_m]-r_f)$; estimating $r_f$, MRP, $\beta$; **comparables**; equity beta rises with leverage; **unlevering**: $r_A = \frac{E}{D+E}r_E + \frac{D}{D+E}r_D$ holds for expected and realised returns, hence $\beta_A = \frac{E}{D+E}\beta_E + \frac{D}{D+E}\beta_D$ | House bought with 20% / 50% debt ($\beta_E$ = 1.25 / 2); three comparables with risk-free debt, average $\beta_A$ = 0.78, $r$ = 10.56% |
| 2A.3 Which cash flows | 24–27 | Unlevered FCF (financing subsidies go into the discount rate); incremental basis; opportunity costs in, sunk costs out; nominal with nominal, real with real; terminal value; salvage value taxed on $SV - $ book value; NWC recouped at the end | — |
| 2A.4 NPV rule | 28–38 | $NPV = PV_A - c_A$; positive NPV = "arbitrage across the firm's boundary", not scalable so it survives in equilibrium; acquisition as an NPV problem (synergies, market power); in an all-equity firm with symmetric information, equity value rises by the NPV whether the project is funded by insiders, new equity, or safe debt; **IRR pitfalls**: multiple roots, non-existence, lending vs. borrowing, scale in mutually exclusive projects | Assets in place 100/10, safe project costs 15 and pays 22, $r_f$ = 10%, NPV = 5 under all three financing routes |
| 2A.5 Debt vs. equity | 39–45 | Payoff (fixed vs. residual), seniority, maturity, control rights; covenants and technical default; limited liability; credit bureaus; payoffs $\min(\tilde A, F)$ and $\max(\tilde A - F, 0)$ → **equity is a call** on the assets | Payoff diagram |
| 2A.6 Frictionless benchmark and complete markets | 46–54 | Assumptions (competitive and complete markets, same borrowing terms, no taxes/bankruptcy costs, financing doesn't affect cash flows or convey information, fixed investment, symmetric information); states, **contingent claims**, completeness via replication, law of one price, arbitrage ("free lunch", "money machine") | Stock 2 / (1.9, 2.4), bond 1 / 1.05 → state prices 0.381 (boom), 0.571 (slump) |
| 2A.7 Entrepreneur example | 55–81 | Penniless entrepreneur, project pays 1.05 / 3.15; stock 0 / 2.8, bond 1.05 / 1.05; state prices $p_1$ = 0.357 (boom), $p_2$ = 0.595 (slump) — slump claim costlier because of risk aversion; $A$ = 1.75 and NPV = 0.75 under debt, under equity ($\alpha = 4/7$), and any mix; $r_A$ = 20% fixed, $r_E = r_A + \frac{D}{E}(r_A - r_D)$; the "borrow more, value rises to 1.77" fallacy | Tables at D = 1, 0, 0.4, 0.5 |
| 2A.8 MM I | 82–96 | Proof by arbitrage with safe debt (sell overpriced, buy underpriced; **homemade leverage** / undoing leverage); risky debt = safe bond − put, equity = call; $V(K) = C(K) + K/(1+r_f) - P(K)$ independent of $K$ (**put–call parity**) | Two-firm arbitrage tables |
| 2A.9 MM II and WACC | 97–102 | $r_E = r_A + \frac{D}{E}(r_A - r_D)$, linear while debt is safe, flatter once $r_D$ rises; $r_A = r_{WACC} = r_U$ independent of financing; **conservation of value**: financial transactions repackage risk | — |
| 2A.10 $r_D$ is not the coupon or the yield | 103–105 | $D = F/(1+y)$ vs. $D = [F(1-p) + Cp]/(1+r_D)$; with default risk $y > r_D$ — yield overstates the cost of debt | — |

**Notes:** [[Notas/L02/L02-00-map|L02 map]] (full study notes, figures, companion).
**Practise:** PS1 Ex. 2 (incremental FCF: sunk consultancy fee, allocated vs. incremental overhead, NWC recovered; block 2A.3–2A.4); PS1 Ex. 3 (replacement decision: opportunity value of the old machine, tax on sale vs. book value; block 2A.3); PS2 Ex. 1(a–e) (state prices, calls/puts on project assets, put–call parity, $r_D, r_E, r_A$ across $D$; blocks 2A.6–2A.9); PS2 Ex. 1(f) (debt-financed dividend — Topic 2B block 2B.7); PS2 Ex. 3(a–b) (all-equity value, face value of debt, equity value; blocks 2A.7–2A.9); PS2 Ex. 4 (Yerba: beta and expected return after a debt-financed repurchase, EPS and P/E after the change; blocks 2A.9 + Topic 1 block 1.7).
**Books:** Ross *Fundamentos* Cap. 9 (pp. 281–317: NPV §9.1, IRR §9.5), Cap. 10 (pp. 318–359: incremental cash flows §10.2), Cap. 13 (pp. 424–458: beta §13.6, SML/CAPM §13.7), Cap. 14 (pp. 459–490: WACC §14.4, pure-play §14.5), Cap. 16 §16.2–16.3 (pp. 542–551: homemade leverage, M&M I and II); Higgins 13e Ch. 7 (pp. 237–284: NPV §7.2.2, IRR §7.2.4, relevant cash flows §7.3), Ch. 8 (WACC §8.4, asset beta App. 8.A.1–8.A.2, pp. 318–321), Ch. 6 §6.2.1 and App. 6.A.1 (pp. 206, 224); Amaro de Matos Ch. 1 §1.1.6 (NPV rule, p. 14), §1.2.1–1.2.4 (states, no-arbitrage, martingale measure, pp. 18–24), Ch. 2 §2.1.1–2.1.2 (MM1 Prop. 2.1.1 p. 42, MM2 Prop. 2.1.2 p. 43); Tirole Ch. 2 §2.2 (p. 77).

---

## Topic 2B — Taxes, bankruptcy costs and the static trade-off
#aula/topic2b #topic/mm-benchmark

| Block | Slides | Content | Examples / data |
|---|---|---|---|
| 2B.1 Interest tax shield | 2–5 | Levered firm pays less tax; $ITS = \tau r_D D$; unlevered FCF ignores it (enters via WACC or APV); the issue is the differential treatment of interest vs. dividends/retained earnings | Levered vs. unlevered firm, EBIT 1,850, interest 350, τ = 35%, ITS = 122.5 |
| 2B.2 MM I with taxes | 6–15 | Perpetual safe debt: $V_{ITS} = \tau D$; $V_L = V_U + V_{ITS}$; tax benefits accrue to shareholders; market-value balance sheet with $V_U$ and $V_{ITS}$; $r_{ITS} = r_D$ (constant debt) vs. $r_{ITS} = r_U$ (constant $D/E$, the usual assumption); three closed forms for $V_{ITS}$ with growth $g$ | Unlevered firm 600, borrows 500 to repurchase, τ = 40% → $V_L$ = 800, price 0.6 → 0.8, gain 200 = $V_{ITS}$ |
| 2B.3 After-tax WACC | 16–18 | $r_{WACC} = \frac{E}{D+E}r_E + \frac{D}{D+E}r_D(1-\tau)$ under a constant target $D/E$; WACC formulas for constant debt, annually and continuously adjusted $D/E$ | Berk–DeMarzo figure |
| 2B.4 APV vs. WACC | 19–32 | APV steps (unlevered FCF at $r_U$ + $V_{ITS}$ at $r_{ITS}$, marginal tax rate, annuity if debt is temporary); WACC steps (unlever comparables, relever at target $D/E$, after-tax WACC); equivalence when $D/E$ is constant; APV's flexibility when it is not | Project 60,000, FCF 7,500, g = 4%, τ = 40%, D/V = 25%: WACC 11.5% → $V_L$ = 100,000; $r_U$ = 12%, $V_U$ = 93,750, $V_{ITS}$ = 6,250; fixed 60,000 loan repaid in 5 years → $V_L$ = 98,945 |
| 2B.5 The 100%-debt puzzle | 33–35 | $V_L/V_U = 1 + \tau D/V_U$ suggests all-debt firms; evidence on cost of capital and leverage | Jagannathan et al. (2017); Graham et al. (2015) |
| 2B.6 Bankruptcy costs | 36–40 | Transfer of control is not an MM violation; **direct** (legal, managerial time, fire sales) vs. **indirect** costs (customers, suppliers/credit, workers, agency conflicts: debt overhang, risk-shifting, cashing out) | Hortaçsu et al. (2013) car auction prices and CDS; Brown & Matsa (2016); Baghai et al. (2021); Van Doornik et al. (2022) |
| 2B.7 Static trade-off model | 41–45 | Cash flow $X \sim h$ on $[\underline X, \bar X]$, debt $K$, tax $\tau$ when solvent, fixed cost $C$ in default; $V(K) = V_U$ + PV of tax saving − $C\,H(K)/(1+r_f)$; $K^*$ equates marginal tax benefit and marginal expected distress cost; $K^*$ rises with τ, falls with $C$; $V_L = V_U + V_{ITS} - PV(\text{distress})$ | — |
| 2B.8 Bank capital debate | 46–47 | Admati et al. (2013): "bank equity is not socially expensive"; three statements to judge (ROE falls; equity costlier; lost tax shield) + failure externality | — |
| 2B.9 Dividend irrelevance | 48–51 | With fixed investment, payout changes must be financed; sources = uses; $V_t = E\sum_i \beta^i (X_{t+i} - I_{t+i})$ → value independent of payout; extends to debt and risk aversion | — |
| 2B.10 Appendix | 54–63 | Derivation of the WACC formula from $V_{L,t} = (FCF_{t+1} + \tau r_D D_t + V_{L,t+1})/(1+r_L)$; ITS uses the coupon yield $\bar r_D = E[C_{t+1}]/D_t$, not the expected return $r_D$, when debt is risky | Bond, coupon 50, market value 525 |

**Notes:** [[Notas/L03/L03-00-map|L03 map]] (full study notes, figures, companion).
**Practise:** PS2 Ex. 2 (Company A: $r_E$ before/after, WACC, tax shield under continuously adjusted $D/E$, interest = 20% of FCF, fixed 100 m perpetual debt, share price and repurchase; blocks 2B.2–2B.4); PS2 Ex. 3(c) (direct bankruptcy cost of 7% of cash flow: who bears it; block 2B.6–2B.7); PS2 Ex. 1(f) (debt-financed dividend; block 2B.9 logic in a no-tax world).
**Books:** Ross *Fundamentos* Cap. 16 §16.4–16.6 (pp. 551–562: M&M with taxes, bankruptcy costs, static theory), §16.10 (p. 567, bankruptcy process), Cap. 17 §17.2 (p. 587, dividend irrelevance, homemade dividends); Higgins 13e Ch. 6 §6.2.2–6.2.3 (pp. 208–213: tax benefits, distress costs, debt overhang), App. 6.A.2 (p. 226), Ch. 8 App. 8.A.3 (p. 321, APV); Amaro de Matos Ch. 2 §2.1.3 (MM with taxes, Prop. 2.1.3 p. 45), §2.2 (Miller 1977, DeAngelo–Masulis, pp. 48–57), Ch. 4 §4.1 (dividend irrelevance, p. 100).
**Bridges forward:** debt overhang and risk-shifting (block 2B.6) are the agency frictions of syllabus item 4 (Tirole Ch. 3).

---

## Cross-lecture synthesis points
- **$A = D + E$ in market value** (Topic 1, slides 8, 13) → unlevering betas (2A, slides 17–21) → $V_L = V_U + V_{ITS}$ balance sheet (2B, slides 9–12).
- **FCF formula** (Topic 1, slide 60) → valuation input (2A, slides 24–27) → why unlevered FCF ignores the tax shield (2B, slide 4). PS1 Ex. 1 links the three.
- **ROE and P/E move with leverage** (Topic 1, slides 43, 47–51) ↔ MM II: higher $r_E$ offsets the higher ROE/EPS (2A, slides 97–102) ↔ PS2 Ex. 4 (Yerba P/E) ↔ Admati et al. statement 1 (2B, slide 47).
- **Equity as a call** (2A, slide 45) → MM I with risky debt (2A, slides 90–96) → risk-shifting as an indirect distress cost (2B, slide 40).
