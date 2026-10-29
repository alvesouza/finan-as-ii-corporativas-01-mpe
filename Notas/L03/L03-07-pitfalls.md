---
tags: [notes, lecture-03, pitfalls, true-false, review]
date: 2026-10-24
status: taught
source: "Aula/Topic2B.pdf slides 2–63; original True/False items in the macro-1 V/F style (rules/00_estilo_avaliacao.md)"
---

# L03 · Pitfalls and an original True/False self-test

> Prev: [[L03-06-formulas]] · Next: [[L03-08-python]] · Map: [[L03-00-map]]

---

## Part I — the confusions this lecture produces

### 1 · Counting the shield twice

Unlevered FCF already excludes the shield ([[L03-01-tax-shield-mm-taxes]] §2). **Either** discount
it at the after-tax WACC **or** discount it at $r_U$ and add $V_{ITS}$ — never both. *Minimal
counterexample:* slide-28 project at 11.5% plus 6,250 gives 106,250, not 100,000.

### 2 · Using the levered FCF in the WACC

Discounting $FCF+\tau r_DD$ at the after-tax WACC is the same double count from the other side:
the appendix's (16) uses $r_L$, (18) uses $r_{WACC}$, and the shield moves from the numerator to the
denominator — it is not in both ([[L03-02-after-tax-wacc-apv]] §7).

### 3 · Mixing the two MM II formulas

$r_E=r_U+\frac{D}{E}(1-\tau)(r_U-r_D)$ is for a **fixed debt level**; $r_E=r_U+\frac{D}{E}(r_U-r_D)$ for
a **target ratio**. Unlevering comparables with Hamada and relevering into a WACC built on a target
ratio mixes two incompatible policies. *Counterexample:* at $D/E=1/3$, $r_U=12\%$, $r_D=5\%$,
$\tau=40\%$ the two give 13.40% and 14.33%.

### 4 · Applying $(1-\tau D/V)r_U$ to a growing firm

That WACC is exact only for constant debt **and** $g=0$ ([[L03-02-after-tax-wacc-apv]] (7)–(8)). With
$g>0$ a constant debt level means a falling $D/V$: use APV.

### 5 · "Default is what makes debt costly"

The transfer of control is free in MM ([[L03-03-debt-puzzle-bankruptcy-costs]] §3); with $C=0$ the
trade-off model gives $V=V_U+\tau D(K)$, rising all the way to $K=\bar X$
([[L03-04-static-trade-off]] (9)). **The cost is the deadweight $C$, not the default.**

### 6 · Reading $\tau[1-H(K)]$ as "the tax shield"

It is the **marginal** benefit of one more unit of promised repayment. The **level** of the shield
is $\tau E[\min(X,K)]$, which includes $\tau X$ in default states. The marginal benefit declines
because in default states the extra unit shields nothing — all tax is already avoided.

### 7 · "More volatile firms always choose less debt"

Slide 45 signs $K^*$ in $\tau$ and $C$ only. In the uniform case $K^*=\bar X-C/\tau$ **rises** with a
mean-preserving spread in the interior regime and falls in the corner regime; what falls with
volatility there is the **gain** from debt ([[L03-04-static-trade-off]] §6). Ross's advice is about
debt capacity in practice, not a theorem of this model.

### 8 · Using $r_D$ for a distressed bond's shield

The deduction follows the coupon paid, $\bar r_D=E[C_{t+1}]/D_t$; the expected return $r_D$ includes
compensation for default losses that are not interest (slides 62–63:
$525\times33.33\%=175\neq$ the interest).

### 9 · "A lower ROE hurts shareholders" / "equity is expensive"

ROE and $r_E$ fall with leverage **because risk falls**; the WACC is unchanged without taxes
([[L03-05-bank-capital-dividend-irrelevance]] §1). Only the tax subsidy makes equity privately
costlier, and that is a transfer.

### 10 · $D_t$ in slides 49–51 is a dividend per share

Not debt. And the dividend-irrelevance result needs the **investment plan fixed**: a dividend
financed by cutting a positive-NPV project does lower value.

---

## Part II — True/False self-test (24 items, original)

Score as in `rules/00_estilo_avaliacao.md`: $\max\{0,\ \text{right}-\text{wrong}/2\}$ × item value.

**1.** *With corporate taxes, a levered firm pays less tax than an identical unlevered firm, but its
net income is lower.* — **T.** Interest reduces taxable income (taxes 525 vs 647.5 on slide 2), and
net income falls by interest minus the tax saved ($1202.5-975=227.5=350\times0.65$). Total payments to
investors rise by $350\times0.35=122.5$; equity alone does not.

**2.** *The interest tax shield arises because corporate taxes reduce every claim on the firm
proportionally.* — **F.** A proportional tax on all claims would leave MM intact. The shield exists
because interest is deducted and dividends and retained earnings are not (slide 5): the friction is
the **differential** treatment.

**3.** *Unlevered free cash flow already includes the interest tax shield, so it must be discounted
at $r_U$ to value the levered firm.* — **F.** FCF uses $EBIT(1-\tau)$, as if there were no interest
(slide 4); discounting it at $r_U$ gives $V_U$, and the shield must be added (APV) or put into the
rate (after-tax WACC).

**4.** *With perpetual safe debt, $V_{ITS}=\tau D$ regardless of the interest rate.* — **T.** The
shield $\tau r_fD$ is a riskless perpetuity at $r_f$; the rate cancels: $\tau r_fD/r_f=\tau D$.

**5.** *Under MM I with taxes, the gain from a debt-financed repurchase is shared between the
shareholders who sell and the creditors.* — **F.** Creditors pay a fair price for a fair claim. The
whole $V_{ITS}$ goes to the original shareholders — sellers included, since they sell at the
post-announcement price (0.8 on slide 15; gain 200 = $V_{ITS}$).

**6.** *In the slide-14 repurchase the share price rises when the shares are bought back.* — **F.**
It rises at the announcement, when the market values the shield; the buyback then happens at 0.8 and
leaves the price unchanged ($300/375=0.8$).

**7.** *Investors can replicate the tax advantage of corporate debt by borrowing on personal account.*
— **F.** Personal interest is not deductible at the corporate rate (Higgins Table 6A.1: 80% on the
homemade replica vs. 96% on Bold). That is why investors pay a premium for levered firms (slide 8).

**8.** *If a firm keeps a constant debt-to-equity ratio, the tax shields are as risky as the firm's
assets.* — **T.** Debt moves with asset value, so do the shields: $\beta_{ITS}=\beta_U$,
$r_{ITS}=r_U$ (slide 12).

**9.** *Under a target $D/E$, the cost of equity is $r_U+\frac{D}{E}(1-\tau)(r_U-r_D)$.* — **F.** That
is the constant-debt formula. With $r_{ITS}=r_U$ the balance sheet gives $\frac{D}{V}r_D+\frac{E}{V}r_E=r_U$,
hence $r_E=r_U+\frac{D}{E}(r_U-r_D)$ — the no-tax formula.

**10.** *For a growing firm, a shield worth $\tau r_DD/(r_U-g)$ is always worth less than $\tau D$.* —
**F.** It is less when $r_U-g>r_D$ and more when growth is high enough that $r_U-g<r_D$ (crossing at
$g=7\%$ with $r_U=12\%$, $r_D=5\%$; figure in [[L03-01-tax-shield-mm-taxes]] §8). Note that the two
compare different policies.

**11.** *With annual rebalancing the shield is worth more than with continuous rebalancing.* —
**T.** The next shield is known one period ahead and discounted at $r_D<r_U$ for that period:
factor $(1+r_U)/(1+r_D)>1$.

**12.** *The after-tax WACC $\frac{E}{V}r_E+\frac{D}{V}r_D(1-\tau)$ is exact for any debt policy.* —
**F.** It is exact under a continuously maintained target ratio (note 02 (5)); with a fixed debt
schedule $D/V$ changes and no single WACC exists (slide 32).

**13.** *When $D/E$ is constant, APV and WACC give the same value.* — **T.** Slides 25–27: substituting
$\frac{E}{V}r_E+\frac{D}{V}r_D=r_U$ into the WACC value yields $V_U+\frac{Dr_D\tau}{r_U-g}$.

**14.** *A fixed 60,000 loan repaid in five years adds more value than a perpetual 25% target ratio,
because its annual shield is larger.* — **F.** The loan's shields are 1,200 a year but stop after
five years: 5,195 vs. 6,250 for the smaller, growing, perpetual stream.

**15.** *In APV, the shield of a fixed repayment schedule should be discounted at $r_D$.* — **T.**
Its size is fixed in currency, so its risk is the debt's (slide 21: "use the appropriate $r_{ITS}$").

**16.** *For a risky bond, the tax deduction equals the bond's expected return times its market
value.* — **F.** The deduction is the coupon actually paid; the slides' example has $r_D=33.33\%$ on
525 (175) while the interest is the coupon. Use $\bar r_D=E[C]/D_t$.

**17.** *Bankruptcy is an MM violation because ownership passes from shareholders to creditors.* —
**F.** The transfer itself is costless in MM (slide 36); the violation is the deadweight cost of the
process.

**18.** *Indirect distress costs can arise before any bankruptcy filing.* — **T.** Slide 38: lost
customers, suppliers' and banks' credit, workers, and investment distortions occur as the
probability of distress rises (e.g. Hortaçsu et al.'s car prices and CDS).

**19.** *Debt overhang leads shareholders to take negative-NPV gambles.* — **F.** That is
risk-shifting. Debt overhang is underinvestment: shareholders reject positive-NPV projects whose
payoff partly goes to creditors (slide 40).

**20.** *In the slides' model, if the bankruptcy cost is zero, the firm-value-maximizing $K$ is the
highest cash flow $\bar X$.* — **T.** With $C=0$, $(1+r_f)V'=\tau[1-H(K)]>0$ for $K<\bar X$; at
$K=\bar X$ the whole tax bill is shielded.

**21.** *In the slides' model, with no taxes any level of debt leaves firm value unchanged.* — **F.**
With $\tau=0$, $V=V_U-CH(K)/(1+r_f)$: safe debt ($K\le\underline X$) leaves value unchanged, risky debt
destroys $CH(K)/(1+r_f)$.

**22.** *At the optimum, the probability of default equals $C/\tau$ times the density at $K^*$.* —
**F.** The FOC is $\tau[1-H(K^*)]=Ch(K^*)$: the **survival** probability is $(C/\tau)h(K^*)$.

**23.** *Higher capital requirements raise banks' funding costs because equity has a higher required
return than debt.* — **F.** Under MM the required return on equity falls as leverage falls and the
WACC is unchanged (12% at $E/V$ 25% and 50% in note 05). Only the lost tax subsidy raises the bank's
private cost.

**24.** *If the investment plan is fixed, paying a larger dividend this year financed by a share
issue leaves the firm's total value unchanged.* — **T.** Sources = uses forces the issue; substituting
it into the pricing equation removes the dividend: $V_t=\delta E[X_{t+1}-I_{t+1}+V_{t+1}]$ (slide 51).

---

## Links

Map: [[L03-00-map]] · Formulas: [[L03-06-formulas]] · Code: [[L03-08-python]] · Grading
conventions: [[../../rules/00_estilo_avaliacao|rules/00]] · Quiz:
[[../../Simulados/quiz-topic2b-taxes-tradeoff-2026-10-24|quiz Topic 2B]].
