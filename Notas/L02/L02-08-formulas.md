---
tags: [notes, lecture-02, formulas, reference]
date: 2026-10-24
status: taught
source: "Topic 2A slides 2–105; block list in Map/lectures-index.md (Topic 2A, blocks 2A.1–2A.10); book results cited in the notes that derive them."
---

# L02 · Formulas — the exam specification, every equation, every number

> Prev: [[L02-07-mm2-wacc-cost-of-debt]] · Next: [[L02-09-pitfalls]] · Map: [[L02-00-map]]

---

## 0 · The specification, mapped

The slides state no learning goals; the specification is the lecture's block list
([[../../Map/lectures-index|Map/lectures-index]], Topic 2A), item by item.

| Block | Slides | What must be done with it | Note |
|---|---|---|---|
| 2A.1 Present value | 2–7 | write $P_A$ as an expected PV; distinguish expected and realized return; price a coupon bond with spot rates | [[L02-01-present-value-capm-betas]] §1 |
| 2A.2 Discount rates and betas | 8–23 | apply the CAPM; explain why a levered comparable's $\beta_E$ overstates $\beta_A$; **derive** $r_A$ and $\beta_A$ as value-weighted averages; unlever comparables and compute the project rate | [[L02-01-present-value-capm-betas]] §2–6 |
| 2A.3 Which cash flows | 24–27 | build unlevered FCF; incremental basis; opportunity in, sunk out; consistent inflation; terminal and after-tax salvage value; NWC recovery | [[L02-02-cash-flows-npv-irr]] §1–2 |
| 2A.4 NPV rule | 28–38 | state the rule and its "arbitrage across the boundary" reading; show NPV = shareholders' gain under three financings; list and exhibit the IRR pitfalls | [[L02-02-cash-flows-npv-irr]] §3–5 |
| 2A.5 Debt vs. equity | 39–45 | the four differences; covenants, technical default, limited liability; payoffs $\min$ / $\max$; equity as a call | [[L02-03-debt-vs-equity-claims]] |
| 2A.6 Benchmark, complete markets | 46–54 | the assumptions; contingent claims, completeness, law of one price, the two arbitrages; compute state prices by replication | [[L02-04-complete-markets-state-prices]] |
| 2A.7 Entrepreneur example | 55–81 | state prices; $A$, $D$, $E$, $\alpha$ under each financing; returns tables; $r_E$ as a function of $D$; spot the "1.77" fallacy | [[L02-05-entrepreneur-example]] |
| 2A.8 MM I | 82–96 | prove MM I by arbitrage both ways (homemade leverage); risky debt = bond − put, equity = call; parity ⇒ $V(K)$ constant | [[L02-06-mm1-arbitrage-put-call]] |
| 2A.9 MM II and WACC | 97–102 | derive MM II; linear vs. flat region; $r_A=r_{WACC}=r_U$; conservation of value | [[L02-07-mm2-wacc-cost-of-debt]] §1–3 |
| 2A.10 $r_D$ vs. coupon and yield | 103–105 | define $y$ and $r_D$; prove $y>r_D$ for risky debt | [[L02-07-mm2-wacc-cost-of-debt]] §4 |

---

## 1 · Every numbered equation

| Eq. | Statement | Derived in |
|---|---|---|
| (1.1) | $P_A=\sum_t E[\tilde d_t]/(1+r_t)^t$ | [[L02-01-present-value-capm-betas]] §1 |
| (1.2) | coupon bond with spot rates | §1 |
| (1.3) | constant rate: $P_A=\sum_t E[\tilde d_t]/(1+r)^t$ | §1 |
| (1.4) | CAPM $r=r_f+\beta(E[\tilde r_m]-r_f)$ | §2 |
| (1.5) | $\beta=\operatorname{Cov}(\tilde r,\tilde r_m)/\operatorname{Var}(\tilde r_m)$ | §2 |
| (1.6) | project rate from a comparable, $\beta=\beta_A$ | §3 |
| (1.7)–(1.8) | house: $E[\tilde r_m]=7\%$, $\operatorname{Var}=0.0036$ | §4 |
| (1.9) | $D=E[\tilde C_D]/(1+r_D)$, etc. | §5 |
| (1.10) | $r_A=\frac{E}{D+E}r_E+\frac{D}{D+E}r_D$ (also realized returns) | §5 |
| (1.11) | $\beta_A=\frac{E}{D+E}\beta_E+\frac{D}{D+E}\beta_D$ | §5 |
| (1.12) | $r_E=r_A+\frac{D}{E}(r_A-r_D)$; $\beta_E=\beta_A+\frac{D}{E}(\beta_A-\beta_D)$ | §5 |
| (2.1) | $\mathrm{FCF}=\mathrm{EBIT}(1-\tau)+\mathrm{Dep}-\mathrm{CAPEX}-\Delta\mathrm{NWC}$ | [[L02-02-cash-flows-npv-irr]] §1 |
| (2.2) | after-tax salvage $SV-\tau(SV-\mathrm{PPE})$ | §2 |
| (2.3) | $\mathrm{TV}_T=\mathrm{FCF}_{T+1}/(r-g)$, $g<r$ | §2 |
| (2.4) | $NPV_A=PV_A-c_A$ | §3 |
| (2.5) | slides' project: $-15+22/1.1=5$ | §4 |
| (2.6) | IRR: $0=-c_A+\sum_t E[\tilde d_t]/(1+\mathrm{IRR})^t$ | §5 |
| (3.1)–(3.2) | $\tilde C_D=\min(\tilde A,F)$, $\tilde C_E=\max(\tilde A-F,0)$ | [[L02-03-debt-vs-equity-claims]] §2 |
| (3.3) | $\tilde C_D+\tilde C_E=\tilde A$ | §2 |
| (3.4) | $\min(\tilde A,F)=F-\max(F-\tilde A,0)$ | §2 |
| (4.1)–(4.4) | replication of $cc_1$, $cc_2$; $p_1=0.381$, $p_2=0.571$ | [[L02-04-complete-markets-state-prices]] §3 |
| (4.5) | price $=0.381y+0.571x$ (linear pricing) | §3 |
| (4.6) | $\pi_s=p_s/\sum p$; price $=\frac{1}{1+r_f}\sum\pi_s\,\text{payoff}_s$ | §4 |
| (5.1)–(5.4) | entrepreneur: $p_1=1/2.8=0.357$, $p_2=1/1.05-1/2.8=0.595$ | [[L02-05-entrepreneur-example]] §2 |
| (5.5)–(5.6) | entrepreneur under debt $2.1p_1=0.75$; $A=3.15p_1+1.05p_2=1.75$ | §3 |
| (5.7)–(5.9) | $1=\alpha(3.15p_1+1.05p_2)$, $\alpha=4/7$; entrepreneur $\tfrac37(1.75)=0.75$ | §4 |
| (5.10)–(5.12) | $r_E=\frac{E+D}{E}r_A-\frac{D}{E}r_D=20\%+\frac{D}{E}15\%=20\%+\frac{D}{1.75-D}15\%$ | §7 |
| (6.1)–(6.2) | Step 1 ($V_2>V_1$): cost 0, payoff $\alpha X(V_2/V_1-1)>0$ | [[L02-06-mm1-arbitrage-put-call]] §2 |
| (6.3)–(6.4) | Step 2 ($V_1>V_2$): cost 0, payoff $\alpha X(V_1/V_2-1)>0$ | §2 |
| (6.5)–(6.6) | $\min\{K,X\}=K-\max\{K-X,0\}$; $D=K/(1+r_f)-P(K)$ | §3 |
| (6.7)–(6.8) | $E=C(K)$; $V(K)=C(K)+K/(1+r_f)-P(K)$, independent of $K$ | §4 |
| (7.1)–(7.2) | MM II: $r_E=r_A+\frac{D}{E}(r_A-r_D)$ | [[L02-07-mm2-wacc-cost-of-debt]] §1 |
| (7.3) | $\partial r_E/\partial(D/E)=(r_A-r_D)-\frac{D}{E}\,\partial r_D/\partial(D/E)$ | §2 |
| (7.4)–(7.6) | risky face $F\in(1.05,3.15)$: $D=F/2.8+0.625$, $E=(3.15-F)/2.8$, $r_E=40\%$ | §2 |
| (7.7)–(7.9) | $V_L=V_U$; $r_A=r_{WACC}=r_U$; $r_E=r_U+\frac{D}{E}(r_U-r_D)$ | §3 |
| (7.10)–(7.12) | $D=F/(1+y)$; $D=[F(1-p)+Cp]/(1+r_D)$; $y>r_D$ if risky | §4 |

### 1.1 · Named results

| Result | Statement | Note |
|---|---|---|
| **NPV rule** | undertake iff $NPV>0$; frictionless + all-equity ⇒ shareholder gain = NPV | [[L02-02-cash-flows-npv-irr]] §3–4 |
| **Law of one price / no arbitrage** | same payoff ⇒ same price; no free lunch, no money machine | [[L02-04-complete-markets-state-prices]] §2 |
| **MM I** (slide 83) | in a frictionless economy, total firm value is independent of capital structure | [[L02-06-mm1-arbitrage-put-call]] |
| **MM II** (slide 97) | cost of equity rises with market $D/E$; linear while debt is safe | [[L02-07-mm2-wacc-cost-of-debt]] |
| **Conservation of value** (slide 102) | financial transactions repackage risk; they neither add nor destroy value | [[L02-07-mm2-wacc-cost-of-debt]] §3 |
| Fisher separation (Amaro Prop. 1.1.1, p. 12) — G | investment decided by the market rate, independent of preferences | [[L02-02-cash-flows-npv-irr]] §6 |
| Amaro Prop. 1.2.1 (p. 22) — G | no arbitrage ⇔ strictly positive state prices | [[L02-04-complete-markets-state-prices]] §5 |
| Amaro Prop. 2.1.1 MM1 (p. 42), Prop. 2.1.2 MM2 (p. 43) — G | $V_l=V_u$; $R_s=R^u_s+(R^u_s-R_b)B/S$ | notes 06, 07 |

---

## 2 · Every number in the lecture

| Case | Inputs | Results | Note |
|---|---|---|---|
| House (slides 12–15) | 100; market +10% (0.8) / −5% (0.2); $r_f$ 2% | $E[\tilde r_m]$ 7%, Var 0.36%; 20% debt: $r_E$ **8.25%** (slide: 8%), $\beta_E$ 1.25; 50% debt: 12%, 2 | 01 §4 |
| Comparables (22–23) | $r_f$ 4%, $E[\tilde r_m]$ 12.4%; $\beta_E$ 0.75 / 1 / 1.08 | $\beta_A$ 0.72 / 0.77 / 0.85; mean 0.78 (0.7811); $r$ **10.56%** | 01 §6 |
| Polaris (Higgins pp. 303, 319) | $\beta_E$ 2.05; $E/V$ 5,898/7,334 | $K_E$ 14.8%; $\beta_A$ 1.65 | 01 §2, §6 |
| NPV and shareholders (32–36) | assets 100/10; project −15 → 22; $r_f$ 10% | NPV 5; equity 50 → 70; $\alpha=15/70$, old holders 55; debt face 16.5; gain 5 three ways | 02 §4 |
| IRR (38) | A −1000/+1500, B +1000/−1500; A −10/14.3, B −1000/1210 | IRR 50%/50%, NPV ±363.6; IRR 43%/21%, NPV 3/100 | 02 §5 |
| Mine (Ross pp. 297–298) | −60, +155, −100 | IRR 25% and 33⅓%; NPV(10%) −1.74 | 02 §5 |
| Stock/bond (52–54) | stock 2 → (1.9, 2.4); bond 1 → 1.05 | $p_{\text{boom}}$ 0.381, $p_{\text{slump}}$ 0.571; $\pi$ = 0.4 / 0.6 | 04 §3–4 |
| Entrepreneur (55–80) | project 1 → (1.05, 3.15); stock 1 → (0, 2.8); bond 1 → 1.05 | $p_1$ 0.357, $p_2$ 0.595; $A$ **1.75**; NPV **0.75**; $\alpha$ 4/7; $r_A$ **20%** | 05 |
| — debt 1 | $F$ 1.05 | $D$ 1, $E$ 0.75; $r_D$ 5%, $r_E$ 40% | 05 §3, §6 |
| — debt 0.4 | $F$ 0.42 | $E$ 1.35, $r_E$ 24.4% | 05 §7 |
| — debt 0.5 | $F$ 0.525 | $E$ 1.25, $r_E$ 26% (fallacy: 1.27, $A$ 1.77) | 05 §7 |
| — risky debt (built here) | $F$ 2.1 | $D$ 1.375, $E$ 0.375, $r_D$ 14.55%, $y$ 52.73%, $r_E$ 40% | 07 §2, §4 |
| Coffee shop (Berk pp. 465–471) | 24,000 → 34,500; 15% | $V^U$ 30,000; NPV 6,000; $r_E$ 25% (D 15,000), 17.5% (D 6,000), 75% (D 27,000) | 05 §8, 07 §3 |
| Ricardo S/A (Ross p. 549) | $R_A$ 12%, $R_D$ 8% | $R_E$ 13% at $D/E$ 0.25; 16% at 1 | 07 §3 |

**To know cold:** $A=1.75$, NPV $=0.75$, $r_A=20\%$, $p_1=0.357$, $p_2=0.595$, $r=10.56\%$.
