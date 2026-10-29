---
tags: [notes, lecture-02, pitfalls, true-false, review]
date: 2026-10-24
status: taught
source: "Topic 2A slides 2–105; the confusions are those the slides' own examples expose (slides 14, 23, 38, 55, 79, 100, 102, 105). True/False items are original, in the macro-1 V/F style (rules/00_estilo_avaliacao.md)."
---

# L02 · Pitfalls and a True/False self-test

> Prev: [[L02-08-formulas]] · Next: [[L02-10-python]] · Map: [[L02-00-map]]

---

## Part I — the confusions this lecture produces

### 1 · Book value vs. market value of the assets
The entrepreneur invests 1 and expects 2.1: "$r_A=110\%$". **Wrong denominator.** The market
value is $A=1.75$, so $r_A=2.1/1.75-1=20\%$ (slide 55). The 0.75 gap is the NPV. Returns, betas
and leverage ratios in this lecture are always on **market** values. → [[L02-05-entrepreneur-example]] §1.

### 2 · Equity beta vs. asset beta
Plugging a levered comparable's $\beta_E$ into the CAPM charges the project for leverage it does
not have. Minimal counterexample: the house has $\beta_A=1$; financed 50/50 its equity has
$\beta_E=2$ (slide 15). Averaging the comparables' **equity** betas gives 11.92% instead of 10.56%.
→ [[L02-01-present-value-capm-betas]] §4–6.

### 3 · "Debt is cheaper, so borrowing lowers the cost of capital"
Holding $r_E$ at 24.4% while raising $D$ from 0.4 to 0.5 makes $A$ jump to 1.77 (slide 79). The
correct $r_E$ is 26% and $A$ stays 1.75. **Every unit of cheap debt makes the remaining equity
dearer by exactly enough** (MM II). → [[L02-05-entrepreneur-example]] §7.

### 4 · "Equity gets riskier only because of default"
In the entrepreneur example debt is **riskless** for every $D\le1$, yet $r_E$ rises from 20% to
40% (slides 75–77, 97). Leverage concentrates the assets' **systematic** risk on a smaller
equity base; default risk is a second, separate effect. → [[L02-07-mm2-wacc-cost-of-debt]] §1.

### 5 · "MM II says $r_E$ is linear in $D/E$"
Only while $r_D$ is constant. With risky debt (7.3) holds and, with finitely many states, $r_E$
can go **flat** (40% for every face above 1.05 in the entrepreneur economy) while $r_D$ rises.
And it is linear in $D/E$, **not** in $D$: $r_E=20\%+15\%\,D/(1.75-D)$ is convex in $D$
(slide 76). → [[L02-07-mm2-wacc-cost-of-debt]] §2.

### 6 · The yield as the cost of debt
With $F=2.1$, the yield is 52.73% and $r_D$ is 14.55%: the yield discounts the **promised** payment,
$r_D$ the **expected** one (slides 104–105). Putting $y$ in a WACC overstates it. Nor is $r_D$ the
coupon contracted years ago (slide 103). → [[L02-07-mm2-wacc-cost-of-debt]] §4.

### 7 · State prices vs. probabilities
Both states have probability ½, yet $p_1=0.357\ne p_2=0.595$ (slides 65–67). State prices embed
time **and** risk aversion; the risk-neutral weights $\pi$ are not beliefs either
(0.4 / 0.6 in the stock–bond example). → [[L02-04-complete-markets-state-prices]] §4.

### 8 · IRR as a ranking device
Same IRR (50%), opposite NPVs (±363.6) for lending vs. borrowing; higher IRR (43% vs. 21%) for the
project that creates 3 instead of 100 (slide 38); two IRRs above the cost of capital with a
negative NPV (Ross' mine). → [[L02-02-cash-flows-npv-irr]] §5.

### 9 · Putting the tax shield in the cash flow
(2.1) taxes EBIT as if unlevered on purpose: financing subsidies are counted **in the discount
rate** (slide 25). Adding interest tax savings to FCF *and* using an after-tax WACC counts them
twice. → [[L02-02-cash-flows-npv-irr]] §1.

### 10 · Two slide displays to read with care
Slide 100 prints $\partial r_E/\partial(D/E)=r_A-\partial r_D/\partial(D/E)$; differentiating MM II
gives $(r_A-r_D)-\frac{D}{E}\partial r_D/\partial(D/E)$. Slide 102's first display swaps the WACC
weights ($\frac{D}{D+E}$ on $r_E$). The slide 14 table rounds $r_E$ to 8% (exact 8.25%), and slide
23 rounds $\bar\beta_A$ to 0.78 while computing 10.56% from 0.7811.

---

## Part II — True/False self-test (original items)

Scoring as in the exams: $\max\{0,\ \text{right}-\text{wrong}/2\}$; blanks do not count.
**[E]** easy · **[M]** medium · **[H]** hard.

| # | Claim | Verdict |
|---|---|---|
| 1 | If a project's cash flows have $\beta=0$, its discount rate is $r_f$ even if they are very volatile. **[E]** | **T** |
| 2 | A firm whose equity beta is 1.5 and whose debt is riskless has an asset beta above 1.5. **[E]** | **F** |
| 3 | $r_A=\frac{E}{D+E}r_E+\frac{D}{D+E}r_D$ requires the CAPM to hold. **[M]** | **F** |
| 4 | Averaging comparables' equity betas and then unlevering at the average leverage gives the same answer as averaging their asset betas. **[H]** | **F** |
| 5 | Unlevered free cash flow includes the interest tax shield, since it is cash the firm keeps. **[E]** | **F** |
| 6 | A consultancy fee paid last month for a project study belongs in the project's NPV. **[E]** | **F** |
| 7 | A positive-NPV project is an arbitrage that competition should eliminate, so in equilibrium no firm has one. **[M]** | **F** |
| 8 | In a frictionless all-equity firm, the shareholders' gain from a positive-NPV project is the same whether it is funded by insiders, new shares or safe debt. **[E]** | **T** |
| 9 | Two projects with the same IRR have the same NPV at any given discount rate. **[E]** | **F** |
| 10 | A project whose NPV profile never crosses zero has no IRR, and the NPV rule still decides it. **[M]** | **T** |
| 11 | Equity's payoff $\max(\tilde A-F,0)$ is convex in $\tilde A$, so shareholders can gain from a mean-preserving increase in asset risk. **[M]** | **T** |
| 12 | Risky debt is worth a riskless bond of the same face value plus a put on the firm's assets. **[M]** | **F** |
| 13 | With two states and two securities with linearly independent payoffs, the market is complete. **[E]** | **T** |
| 14 | Equally likely states must have equal state prices in an arbitrage-free market. **[E]** | **F** |
| 15 | The sum of the state prices equals $1/(1+r_f)$. **[E]** | **T** |
| 16 | In the entrepreneur example, the entrepreneur keeps more NPV under equity financing because she does not have to repay anything. **[E]** | **F** |
| 17 | In the entrepreneur example, $r_A$ is 110% because the project turns an investment of 1 into an expected 2.1. **[E]** | **F** |
| 18 | MM I's arbitrage proof needs individuals to borrow at the same rate as firms. **[M]** | **T** |
| 19 | If a levered firm traded **above** its unlevered twin, an investor could profit by buying the levered firm's debt and equity in proportion and shorting the twin. **[M]** | **F** |
| 20 | Put–call parity implies that the value of a firm with risky debt does not depend on the face value of that debt. **[M]** | **T** |
| 21 | Under MM, borrowing to repurchase shares raises the expected return on equity and leaves the WACC unchanged. **[E]** | **T** |
| 22 | MM II implies $r_E$ rises without bound as $D/E$ grows, even when debt becomes risky. **[H]** | **F** |
| 23 | Riskless debt cannot raise the equity beta, because it carries no risk. **[E]** | **F** |
| 24 | For risky one-period debt, the promised yield exceeds the expected return on the debt. **[M]** | **T** |
| 25 | $r_D$ can be read off the coupon rate written in the firm's existing loan contracts. **[E]** | **F** |

### Justifications

1. **T.** The CAPM prices only covariance with the market: $\beta=0$ in (1.4) gives $r=r_f$.
   Idiosyncratic volatility is diversifiable and unpriced (slide 31's alternative assumption).
2. **F.** With $\beta_D=0$, $\beta_A=\frac{E}{D+E}\beta_E\le\beta_E$ by (1.11): unlevering lowers
   the beta. It equals 1.5 only if $D=0$.
3. **F.** (1.10) follows from $A=D+E$ in market value and $\tilde C_A=\tilde C_D+\tilde C_E$ alone
   (slides 17–19); the CAPM only enters when one maps $r$'s into $\beta$'s.
4. **F.** Unlevering is nonlinear in leverage across firms. Slide-23 data: the mean $\beta_E$ is
   0.943 and the mean $E/(D+E)$ is $(0.96+0.77+0.79)/3=0.84$, giving $0.943\times0.84=0.792$, not
   the 0.781 average of asset betas. Close here, but not the same object.
5. **F.** (2.1) taxes EBIT as if the firm were unlevered; financing subsidies go into the discount
   rate (slide 25). Including them in the cash flow double counts with an after-tax WACC.
6. **F.** It is sunk: paid whether or not the project goes ahead (slide 26; Ross p. 320). Only
   cash flows that differ *with* vs. *without* the project count.
7. **F.** Slide 29: unlike financial arbitrages, positive-NPV projects are **not scalable**, so
   they can exist in equilibrium; they are rents to a specific capability or position.
8. **T.** Slides 33–36: gain 5 in each case. Competitive investors take zero NPV, so the whole
   NPV stays with the old shareholders. Fails with risky debt or asymmetric information (slide 31).
9. **F.** Slide 38: A and B both have IRR 50% and NPVs +363.6 and −363.6 at 10%. The IRR ignores
   whether the flows are lending or borrowing, and their scale.
10. **T.** Example $+100,-300,+250$ ([[L02-02-cash-flows-npv-irr]] §5): the discriminant is
    negative, NPV $>0$ at every rate; the NPV rule says accept.
11. **T.** A convex payoff's expectation rises with a mean-preserving spread (Jensen): with
    $F=1.05$, spreading (1.05, 3.15) to (0, 4.2) raises equity's mean from 1.05 to 1.575 and lowers
    debt's from 1.05 to 0.525 ([[L02-03-debt-vs-equity-claims]] §3; Tirole p. 77).
12. **F.** Minus a put: $\min(K,X)=K-\max(K-X,0)$ (6.5), so $D=K/(1+r_f)-P(K)$ (slide 92). The
    put is the creditors' loss from limited liability.
13. **T.** Completeness ⇔ number of linearly independent payoff vectors = number of states
    (Amaro p. 21); the stock (0, 2.8) and bond (1.05, 1.05) are an example (slides 64–66).
14. **F.** $p_1=0.357$ and $p_2=0.595$ with probabilities ½ each (slide 67): risk aversion makes
    a unit in the bad state dearer. No-arbitrage only requires $p_s>0$.
15. **T.** A riskless unit is one of each contingent claim: $\sum_sp_s=1/(1+r_f)$;
    $0.357+0.595=0.952=1/1.05$.
16. **F.** She keeps 0.75 under debt (5.5), under equity (5.9) and under any mix (slide 70).
    Selling 4/7 of the firm for 1 is a fair trade, not a free one.
17. **F.** 1 is the cost (book value). $r_A$ is on the market value: $2.1/1.75-1=20\%$ (slides
    55, 71).
18. **T.** Step 2 (slide 89) levers up the unlevered twin with a **personal** loan at $R_f$
    (assumption 2). With a higher personal rate, the arbitrage closes only within a band.
19. **F.** Wrong direction. Buying the levered firm's debt and equity in proportion and
    shorting the twin is Step 1 (slide 87), profitable when the **twin** is dearer, $V_2>V_1$.
    If the levered firm is dearer, $V_1>V_2$, the trade is Step 2 (slide 89): short its equity,
    buy the twin and borrow personally — homemade leverage.
20. **T.** $V(K)=C(K)+K/(1+r_f)-P(K)$ replicates $X$ for every $K$ (slides 94–96), so it equals
    the asset's price whatever $K$.
21. **T.** MM II raises $r_E$ by $\frac{D}{E}(r_A-r_D)$; MM I fixes $r_A=r_{WACC}$ (slides 99–101).
22. **F.** Once debt is risky, $r_D$ rises and (7.3) can turn zero: in the two-state economy $r_E$
    is flat at 40% for every face above 1.05 (slide 100).
23. **F.** Slide 97: even risk-free debt makes equity riskier. The house: riskless debt of 50 takes
    $\beta_E$ from 1 to 2 (slide 15).
24. **T.** (7.12): with $p>0$ and $C<F$ the expected payment is below the promised one, so the
    rate that discounts the promise to $D$ is higher (slide 105).
25. **F.** $r_D$ is today's required expected return; macro conditions and default risk change
    after the contract is signed (slide 103).

