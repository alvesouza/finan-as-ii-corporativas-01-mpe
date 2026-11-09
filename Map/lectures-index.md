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
| [[Aula/Topic1.pdf\|Topic 1]] — Accounting review | 63 | 1 | [[rules/01_introducao_fatos\|Topic 1]] | PS1 Ex. 1 | [[Simulados/quiz-topic1-accounting-2026-10-24\|quiz]] | `NotebookLM/audio/topic1-audio-part1…3.md` |
| [[Aula/Topic2A.pdf\|Topic 2A]] — Valuation, NPV, MM | 105 | 2 → 3 | [[rules/02_valuation\|Topic 2]] · [[rules/03_benchmark_mm\|Topic 3]] | PS1 Ex. 2–3; PS2 Ex. 1, 3(a–b), 4 | [[Simulados/quiz-topic2a-valuation-mm-2026-10-24\|quiz]] | `NotebookLM/audio/topic2a-audio-part1…3.md` |
| [[Aula/Topic2B.pdf\|Topic 2B]] — Taxes, distress, trade-off | 63 | 3 | [[rules/03_benchmark_mm\|Topic 3]] | PS2 Ex. 2, 3(c) | [[Simulados/quiz-topic2b-taxes-tradeoff-2026-10-24\|quiz]] | `NotebookLM/audio/topic2b-audio-part1…3.md` |
| [[Aula/Topic_3.pdf\|Topic 3]] — Asymmetric information (adverse selection) | 91 | 5 | [[rules/06_assimetria_informacao\|Topic 6]] | — | — | `NotebookLM/audio/topic3-audio-part1…3.md` |
| [[Aula/Topic4_A.pdf\|Topic 4A]] — Moral hazard, credit rationing, debt vs. equity | 69 | 4 | [[rules/04_agencia_estrutura_governanca\|Topic 4]] | — | — | `NotebookLM/audio/topic4a-audio-part1…3.md` |
| [[Aula/Topic4_B.pdf\|Topic 4B]] — Asset substitution, debt overhang, renegotiation | 62 | 4 | [[rules/04_agencia_estrutura_governanca\|Topic 4]] | — | — | `NotebookLM/audio/topic4b-audio-part1…3.md` |
| [[Aula/Topic_5.pdf\|Topic 5]] — Nonverifiable income, termination, sovereign debt | 30 | — (beyond item 4) | [[rules/04_agencia_estrutura_governanca\|Topic 4]] | — | — | `NotebookLM/audio/topic5-audio-part1…3.md` |

> **Lecture numbering ≠ syllabus numbering (2026-11-08).** The lecture files run Topic 1, 2A, 2B
> (syllabus items 1–3), then **Topic 3 = syllabus item 5** (asymmetric information, Tirole Ch. 6),
> **Topic 4A/4B = item 4** (moral hazard, Tirole Ch. 3), and **Topic 5** = nonverifiable income and
> sovereign debt (Tirole §3.8; not a syllabus item of its own). Lists: R4 and R5 were built from the
> syllabus before these slides existed; **R7** ([[Listas/lista-r7-lectures-3-5|lista-r7]]) is built from
> the slides and repeats none of R1–R6.

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

## Topic 3 — Asymmetric information: adverse selection, signalling, IPO underpricing
#aula/topic3 #topic/asymmetric-information

| Block | Slides | Content | Examples / data |
|---|---|---|---|
| 3.1 Hidden information | 2–3 | Used cars, insurance, labour, credit, IPOs; adverse selection, cross-subsidisation, overinvestment, market breakdown, credit rationing (underinvestment) | — |
| 3.2 Lemons model of credit | 4–19 | Penniless borrower, cost $I$, pays $R$ or 0; risk neutrality, $r_f = 0$; good type $p$, bad type $q$, share $\alpha$ of good types, prior $m = \alpha p + (1-\alpha)q$; limited liability, $R_u + R_f = R$. **Symmetric info**: $R_u^G = I/p < I/q = R_u^B$, each type gets its NPV, efficient. **Asymmetric info**: pooling contract $mR_u = I$; **breakdown** if $mR < I$, i.e. $\alpha < \alpha^* = (I/R - q)/(p - q)$; **cross-subsidy** $R_u^G < R_u < R_u^B$; **overinvestment** when $mR \ge I > qR$ | — |
| 3.3 Cost to the good type | 20–27 | $pR_f = p(R - I/m) = (pR - I) - \chi I$ with $\chi = p/m - 1 = (1-\alpha)(p-q)/m$ (discount due to asymmetry; the slide prints the denominator as $p$, but its own example needs $m$: $10 - 30\chi = 8$) | $R = 50$, $I = 30$, $p = 0.8$, $q = 0.7$, $\alpha = 0.5$: $m = 0.75$, $R_u = 40$, $U_G = 8 < 10$, $U_B = 7 > 5$; $q = 0.5$: $R_u = 46.15$, overinvestment, value 32.5 < 35; $\alpha = 0.2$: breakdown; threshold $\alpha^* = 1/3$ |
| 3.4 Credit bureau | 28–37 | Public signal $x_G/x_B$ with $P(x_G\mid G) = P(x_B\mid B) = 0.9$; Bayes: $m_{x_G} = 0.79$, $m_{x_B} = 0.71$; rates 26.6% / 40.8% vs. 33.3%; less cross-subsidy ($U_G$ 9.27 > 8); efficiency gain only when the signal stops funding negative-NPV types (34.5 > 32.5 with $q = 0.5$) | Interest-rate tables (slides 34, 36) |
| 3.5 Pecking order | 38–46 | Internal funds first; debt before equity because debt is less information-sensitive (Holmström 2015, pawn example); $R_S$/$R_F$ project: good type's utility $= \text{NPV} + (m - p)(R_u^S - R_u^F)$, minimised spread ⇒ pledge all of $R_F$ (riskless debt $R_F$ + rest), $R_u^S = R_F + (I - R_F)/m$ | — |
| 3.6 Stiglitz–Weiss (1981) | 47–55 | Mean-preserving spreads, $p_L R_L = p_H R_H = \bar R$; borrower payoff $\bar R - p_i(1+r)I$; $\hat r = \bar R/(p_L I) - 1$ (safe types leave), $r_{max} = \bar R/(p_H I) - 1$; bank return non-monotonic in $r$ ⇒ backward-bending supply, equilibrium rationing | $p_L = 0.9$, $X_L = 100$, $p_H = 0.6$, $X_H = 150$, $\alpha = 0.5$, $I = 85$: $r_{max} = 76.5\%$, $\hat r = 17.6\%$ |
| 3.7 Signalling with costly collateral | 56–68 | Collateral worth $C$ to borrower, $\beta C$ to lender; symmetric info ⇒ $C = 0$; separating equilibrium: bad type $C_B = 0$, $R_u^B = I/q$; good type maximises $p(R - \tilde R) - (1-p)\tilde C$ s.t. no-mimicking and break-even (both bind); signalling pays when adverse selection is severe; other signals: payout, short maturity, underdiversification | — |
| 3.8 Empirics | 69–70 | Kawai et al. (2022): adverse selection destroys up to 34% of surplus, signalling restores up to 78%, backward-bending supply; Michaely et al. (2021): payout signals cash-flow volatility, not level | — |
| 3.9 Self-financing as a signal (optional) | 71–82 | CARA utility (coefficient $\rho$), $\tilde r(\theta) \sim N(\theta, \sigma^2)$; symmetric info ⇒ sell everything (retained share $\alpha = 0$); unobservable $\theta$ ⇒ only $\theta < \hat\theta = P + \rho\sigma^2/2$ sell (lemons); **Leland–Pyle (1977)** PBE: $\alpha^*(\theta_1) = 0$, $\alpha^*(\theta_2) = \tilde\alpha$ with $\tilde\alpha^2/(1-\tilde\alpha) = 2(\theta_2 - \theta_1)/(\rho\sigma^2)$ (Pareto-dominant), informational cost $\rho\tilde\alpha^2\sigma^2/2$ | Two types $\theta_1 < \theta_2$ |
| 3.10 IPO underpricing (Rock) | 83–90 | $V \in \{V_B, V_G\}$, uninformed value $\hat V$; informed investors hold share $\lambda$ of capital $A$, pro-rata rationing ⇒ winner's curse; uninformed break-even gives $P_0 = (\hat V - \lambda\alpha V_G)/(1 - \lambda\alpha) < \hat V = E[P_1]$; underpricing vanishes without informed investors, rises with their share and with $V_G - V_B$ | — |

**Practise:** [[Listas/lista-r7-lectures-3-5|R7]] ex. 1 and 6 (Rock, block 3.10), 5 (undervalued equity issue, 3.5), 11 (pooling and breakdown, 3.2–3.3), 19 (information sharing among lenders, 3.4), 20 (Leland–Pyle, 3.9); [[Listas/lista-r5-asymmetric-information|R5]] ex. 2–4, 6–15 (lemons and breakdown, Myers–Majluf, ratings, maturity signal, pecking order with variable investment).
**Books:** Tirole Ch. 6 §6.2 (lemons, cross-subsidisation, breakdown, p. 241), §6.3 (dissipative signals: collateral, short maturity, underpricing, payout, p. 249), appendixes §6.5–6.9 (pp. 269–272); Amaro de Matos Ch. 3 §3.2.2 (Leland–Pyle, p. 82), §3.2.3 (Myers–Majluf, p. 85), Ch. 6 §6.2.2 (Rock, p. 163); Berk Ch. 14 §14.3 (IPO puzzles, p. 425), Ch. 16 §16.6 (p. 482); Ross Cap. 15 §15.5 (subprecificação, p. 504), Cap. 16 §16.8 (ordem hierárquica, p. 564); Grinblatt–Titman Ch. 19.
**Not in the books:** Stiglitz–Weiss numbers, Kawai et al. (2022), Michaely et al. (2021), Holmström (2015) — slides only.

---

## Topic 4A — Moral hazard, credit rationing, and debt vs. equity
#aula/topic4a #topic/agency #topic/moral-hazard

| Block | Slides | Content | Examples / data |
|---|---|---|---|
| 4A.1 Credit rationing | 2–7 | Hidden action (Holmström–Tirole 1997): capital structure matters through the asset side; markets clear through quantities as well as prices; definitions (Bester–Hellwig 1987; Baltensperger 1978 — refusal for lack of collateral is not rationing) | De Mel et al. (2008): returns to capital of 4.6–5.3% a month in Sri Lankan microenterprises |
| 4A.2 Fixed-investment model | 8–24 | Wealth $A < I$, competitive risk-neutral investors, $r = 0$; $R$ or 0; $a_H$/$a_L$ with $p_H > p_L$; private benefit $B$ from $a_L$ (effort vs. project-choice readings, Jensen–Meckling quote); limited liability ⇒ contract $R_u$, $R_f = R - R_u$; loan reading $i = R_u/(I-A) - 1$; (A1) $p_H R > I$, (A2) $p_L R - I + B < 0$ ⇒ contract must induce $a_H$ | Payoff table (slide 18), timeline (slides 12, 16) |
| 4A.3 IC, pledgeable income, IR | 25–30 | IC $\Delta p R_f \ge B$ ⇒ $R_f \ge B/\Delta p$ ("skin in the game"); pledgeable income $R - B/\Delta p$, independent of $A$; IR $p_H R_u \ge I - A$; financed iff $p_H(R - B/\Delta p) \ge I - A \iff A \ge \bar A = p_H B/\Delta p - (p_H R - I)$; (A3) $\bar A > 0$ | — |
| 4A.4 Equilibrium and rationing | 31–37 | $R_u = (I-A)/p_H$, $i = 1/p_H - 1$, borrower gets the full NPV; $A < \bar A$ rationed even at higher rates (commitment problem); $\bar A$ ↑ in $B$, ↓ in $\Delta p/p_H$ (informativeness); first best has no rationing; $A$ as zero-cost collateral gives the same cutoff | — |
| 4A.5 Investment–cash-flow sensitivity | 38–39 | Fazzari–Petersen (1988); in the model only firms just below $\bar A$ respond; marginal value of cash > 1 | — |
| 4A.6 Debt vs. equity | 40–46 | Liabilities senior and specific, equity junior and residual; standard debt contract; payoffs $\min(A, D)$ and $\max(A - D, 0)$; with outcomes $\{0, R\}$ debt and equity ($\alpha = R_u/R$) coincide | Payoff diagrams |
| 4A.7 Two positive outcomes $R_S > R_F > 0$ | 47–65 | First best: MM irrelevance, $D = R_F + (I - A - R_F)/p_H$ or $\alpha = (I-A)/[p_H R_S + (1-p_H)R_F]$; moral hazard IC $R_f^S - R_f^F \ge B/\Delta p$; pledgeable income $p_H(R_S - R_F) + R_F - p_H B/\Delta p - R_f^F$ ⇒ set $R_f^F = 0$; all-equity sub-optimal ($1 - \alpha \ge B/[\Delta p(R_S - R_F)]$, $\bar A_{equity} > \bar A_{debt}$); **debt dominates equity** (any $D \ge R_F$; riskless debt $R_F$ + equity also works) | Threshold line (slide 63), investor-payoff diagrams (slide 65) |
| 4A.8 Limits of debt optimality | 66–67 | Relies on risk neutrality (no risk-sharing need); distress costs, direct and indirect (debt overhang, asset substitution → Topic 4B) | — |

**Practise:** [[Listas/lista-r7-lectures-3-5|R7]] ex. 12 (random private benefits), 16 (loan size and collateral, block 4A.4 collateral reading); [[Listas/lista-r4-moral-hazard-financing-capacity|R4]] ex. 5–15 (fixed- and variable-investment model, equity multiplier, lender market power, maximal incentives principle = 4A.7, retained earnings = 4A.5).
**Books:** Tirole Ch. 3 §3.2 (fixed-investment model, credit rationing, p. 115), §3.4 (variable investment, equity multiplier, p. 127), §3.5 (inside equity and outside debt, p. 130), §3.6 (verifiable income, debt optimality, p. 132); Ch. 4 §4.3 (collateral, p. 164); Amaro de Matos Ch. 3 §3.1.1–3.1.2 (Jensen–Meckling, principal–agent, pp. 64–66).

---

## Topic 4B — Asset substitution, debt overhang, renegotiation
#aula/topic4b #topic/agency #topic/moral-hazard

| Block | Slides | Content | Examples / data |
|---|---|---|---|
| 4B.1 Asset substitution | 2–3 | Equity = call on $X$ with strike $K$ (prefers risk), debt = bond − put (prefers safety); equity has control ⇒ risk-shifting at high leverage | — |
| 4B.2 Three-project example | 4–13 | $r_f = 20\%$, cash 100, debt face 120, states 20/60/20%; P1 110/130/150 (NPV 8.3), P2 60/90/240 (NPV −5.0), P3 120/122/125 (NPV 1.8); equity picks P2 (E = 20), debt prefers P3 (D = 100); balance sheet A = 95, D = 75, E = 20; new debt finance: breakdown (P2 negative NPV); with P2 = 80/100/240 (NPV 3.3) lenders demand face 220 (rate 120%); outside equity ⇒ P1, $\alpha = 100/108.3$ | Payoff tables for firm, equity, debt |
| 4B.3 Implications, mitigation, evidence | 14–18 | More discretion over risk ⇒ less debt; gambling for resurrection, delayed filing; reputation (Jensen–Meckling), short-term debt, covenants, convertibles; Gilje (2016) oil and gas firms reduce risk near distress; friction = no commitment to project choice | — |
| 4B.4 Debt overhang | 19–31 | Debt as a tax on new investment (Myers 1977); households: Melzer (2017), Dobbie–Song (2020), Di Maggio et al. (2020); example: assets 500/200, $F = 300$ ⇒ D = 250, E = 100; project costs 60, adds 100 in both states (NPV 40) but raises E only to 150 (+50 < 60) and D to 300; renegotiating to $F = 280$ ⇒ E = 170, D = 280, both gain; unconditional renegotiation still works here (110 either way); fixes: senior new claims, DIP financing, bank debt, few creditors | Market-value tables (slides 23–29) |
| 4B.5 Benefits of renegotiation | 32–36 | Ex post efficient, insurance against bad luck, keeps access to credit (Bos et al., 2018), avoids foreclosure externalities (Campbell et al., 2011); out-of-court restructuring dominates (Dawsey et al., 2013; BCB: 4.6 m over-indebted in 2019, ≈252 k restructurings a month); policy: CARES, HAMP, student debt | — |
| 4B.6 Costs of renegotiation | 37–40 | Anticipated renegotiation softens debt and weakens incentives at the moral-hazard stage; strategic default (Mayer et al., 2014) vs. liquidity default; ex ante inefficient, like too-big-to-fail | Timelines (slides 37–38) |
| 4B.7 Default as insurance (Indarte 2023) | 41–44 | Debt $D$, unseizable liquid assets $A$, income $Y \sim F$; default keeps $A + E$ at non-pecuniary cost $\sigma$; default iff $Y < Y^*$ with $u(A + Y^* - D) = u(A+E) - \sigma$; $\partial p/\partial E = F'(Y^*)\,u'(A+E)/u'(A + Y^* - D) > 0$ — more insurance, more default | — |
| 4B.8 Separating adverse selection from moral hazard | 45–58 | Karlan–Zinman (2009): randomised offer rate $r_o$, contract rate $r_c$, future rate $r_f$; model with risk type $\theta$ and effort $e$; effort ↓ in $r_c$, ↑ in default cost $C_b(r_f)$; take-up threshold $\underline\theta(r_o)$ ↑ in $r_o$ (riskier pool); regression $\beta_o > 0$ (selection), $\beta_c > 0$, $\beta_b < 0$ (hidden action) | Experimental design (slide 56) |

**Practise:** [[Listas/lista-r7-lectures-3-5|R7]] ex. 2 (DIP, 4B.4), 3 (convertibles and covenants, 4B.3), 4 and 7 (asset substitution, 4B.1–4B.2), 8–10 (debt overhang, 4B.4), 14 (renegotiation and debt forgiveness, 4B.5–4B.6), 17 (dealing with asset substitution), 18 (borrower-friendly bankruptcy court, 4B.6–4B.7); [[Listas/lista-r4-moral-hazard-financing-capacity|R4]] ex. 2–4 (short-term debt, asset substitution, debt overhang).
**Books:** Tirole Ch. 3 §3.3 (debt overhang, p. 125), Ch. 4 §4.3 (collateral), Ch. 7 (exercise 7.3); Amaro de Matos Ch. 3 §3.1.3 (equity as a call, asset substitution, Myers underinvestment, p. 71), §3.1.4 (evidence, p. 75); Berk Ch. 16 §16.6 (agency costs, p. 482); Grinblatt–Titman Ch. 16 (debt holder–equity holder conflicts, DIP financing); Higgins 13e Ch. 6 §6.2.3 (distress costs, debt overhang, p. 208).
**Not in the books:** Indarte (2023) and Karlan–Zinman (2009) — slides and papers only.

---

## Topic 5 — Nonverifiable income, threat of termination, sovereign debt
#aula/topic5 #topic/agency #topic/default

| Block | Slides | Content | Examples / data |
|---|---|---|---|
| 5.1 Nonverifiable income | 2–3 | Borrower can always report failure (unrecorded sales, perks, sovereign debt); strategic vs. liquidity default; deterrents: direct bankruptcy costs (collateral, penalties) or termination in a repeated relationship | — |
| 5.2 Threat of termination | 4–12 | One period: always report 0 ⇒ no financing; two periods: contract $\{D, \gamma_0, \gamma_1\}$ (repayment, continuation probabilities after default/repayment), liquidation value $L$; (A1) $L < E(\tilde R_2)$, (A2) $L < I - A$; truth-telling IC $(\gamma_1 - \gamma_0)E(\tilde R_2) \ge D$; claims: lender IR binds, $\gamma_1 = 1$, IC binds ⇒ $1 - \gamma_0 = (I-A)/[pE(\tilde R_2) + (1-p)L]$; liquidation less likely with higher $E(\tilde R_2)$, $L$, $p$, $A$; collateral reading; renegotiation (bribe just above $L$) undermines incentives | — |
| 5.3 Sovereign debt: setup | 13–18 | Eaton–Gersovitz (1981), Arellano (2008): Markov endowment, one-period non-contingent bonds, no enforcement; default ⇒ autarky (re-entry probability $\theta$) and output $h(y) \le y$; $q(B', y) = [1 - \delta(B', y)]/(1+r)$ | — |
| 5.4 Recursive equilibrium | 19–22 | $V^o = \max\{V^d, V^c\}$; $V^d(y) = u(h(y)) + \beta\int[\theta V^o(0, y') + (1-\theta)V^d(y')]f(y', y)dy'$; $V^c(B, y) = \max_{B'} u(y + B - q(B', y)B') + \beta\int V^o(B', y')f(y', y)dy'$; default set $D(B)$, $\delta(B', y) = \int_{D(B')} f(y', y)dy'$ | — |
| 5.5 Properties | 23–29 | $V^c$ ↑ in $B$; default sets shrink as assets rise ⇒ $q$ ↑ in $B'$; i.i.d., $\theta = 0$, $h(y) = y$: no capital inflows when default is possible; default more likely at low $y$ (concavity) ⇒ threshold $y^*(B)$, $q(B') = [1 - F(y^*(B'))]/(1+r)$; endogenous borrowing limit $B^*$; risk-free region $B' > \bar B$ | — |

**Practise:** [[Listas/lista-r7-lectures-3-5|R7]] ex. 13 (continuation probability falls with the success probability, 5.2), 15 (one vs. two creditors: strategic and liquidity default, 5.1–5.2), 18 (bankruptcy court and continuation); [[Listas/lista-r6-liquidity-risk-management|R6]] ex. 10–11 (maturity and free cash flow). No course-book exercise covers the sovereign model (blocks 5.3–5.5).
**Books:** Tirole Ch. 3 §3.8 (nonverifiable income, strategic default, p. 141), Ch. 7 §7.1 (Bolton–Scharfstein termination threat, p. 283); Amaro de Matos Ch. 5 §5.2.1–5.2.2 (Hart–Moore, Bolton–Scharfstein: continuation probability, one vs. many creditors, pp. 134–139).
**Not in the books:** Eaton–Gersovitz (1981) and Arellano (2008) — slides and papers only.

---

## Cross-lecture synthesis points
- **$A = D + E$ in market value** (Topic 1, slides 8, 13) → unlevering betas (2A, slides 17–21) → $V_L = V_U + V_{ITS}$ balance sheet (2B, slides 9–12).
- **FCF formula** (Topic 1, slide 60) → valuation input (2A, slides 24–27) → why unlevered FCF ignores the tax shield (2B, slide 4). PS1 Ex. 1 links the three.
- **ROE and P/E move with leverage** (Topic 1, slides 43, 47–51) ↔ MM II: higher $r_E$ offsets the higher ROE/EPS (2A, slides 97–102) ↔ PS2 Ex. 4 (Yerba P/E) ↔ Admati et al. statement 1 (2B, slide 47).
- **Equity as a call** (2A, slide 45) → MM I with risky debt (2A, slides 90–96) → risk-shifting as an indirect distress cost (2B, slide 40) → asset-substitution example and its fixes (4B, slides 2–18).
- **Debt overhang** named as an indirect distress cost (2B, slide 40) → worked example and renegotiation (4B, slides 19–31).
- **Debt is optimal for two different reasons**: it is least information-sensitive under adverse selection (3, slides 38–46: pledge all of $R_F$) and it gives the strongest incentives under moral hazard (4A, slides 53–65: $R_f^F = 0$). Same contract, different friction.
- **Cross-subsidy vs. rationing**: in Topic 3 good types are hurt by bad types' presence (breakdown below $\alpha^*$); in Topic 4A poor borrowers are rationed below $\bar A$. Both are underinvestment with positive-NPV projects; the first is hidden information, the second hidden action. Karlan–Zinman (4B, slides 45–58) is the empirical design that separates the two.
- **Renegotiation cuts both ways**: ex post it fixes debt overhang (4B, slides 27–31); ex ante it softens incentives (4B, slides 37–40) and, in Topic 5, a bribe just above $L$ undermines the termination threat (slide 12). Sovereign default (Topic 5) is the extreme case: no seizure at all, only exclusion and output loss.
