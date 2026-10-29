---
tags: [notes, lecture-03, wacc, apv, valuation, tax-shield]
date: 2026-10-24
status: taught
source: "Aula/Topic2B.pdf slides 16–32 (blocks 2B.3–2B.4) and appendix slides 54–63 (block 2B.10); Berk Fundamentals 2e §16.3 pp. 476–478 (Example 16.4, Eqs. 16.8–16.9, Figure 16.7); Higgins 13e Ch. 8 App. 'Asset Beta and Adjusted Present Value' pp. 321–322; Ross Fundamentos 9e §16.4 p. 553"
---

# 2B.3–2B.4, 2B.10 · After-tax WACC, APV, and why they agree only under a target ratio

> **Claim.** There are two ways to put the shield back into a value built on unlevered FCF:
> **discount the FCF at a lower rate** (the after-tax WACC, $r_D$ replaced by $r_D(1-\tau)$), or
> **value the shield separately** (APV: $V_U$ at $r_U$ plus $V_{ITS}$ at $r_{ITS}$). They give the
> **same number exactly when $D/V$ is held constant** — the slide project is worth 100,000 both
> ways — and **APV alone survives a debt schedule that is fixed in currency** (the 60,000 loan:
> 98,945). The WACC formula is not an assumption: the appendix **derives** it from $V_L=V_U+V_{ITS}$.

Prev: [[L03-01-tax-shield-mm-taxes]] · Next: [[L03-03-debt-puzzle-bankruptcy-costs]] · Map: [[L03-00-map]]

**Notation.** As in [[L03-01-tax-shield-mm-taxes]], plus: $FCF_t$ unlevered free cash flow of
period $t$; $r_{WACC}$ after-tax WACC; $r_L$ expected return on the levered firm's assets
($V_U+V_{ITS}$); $C_{L,t+1}$ cash flow to all investors; $\bar r_D$ the coupon (interest) rate that
sets the tax deduction; $C_{t+1}$ the bond's coupon; $D_t,E_t,V_{L,t}$ values at $t$.

---

## 1 · C — the after-tax WACC (slide 16)

Interest is deductible, so a unit of interest costs the firm only $1-\tau$ after tax: the
**effective** cost of debt is $r_D(1-\tau)$. If the firm keeps a constant target $D/E$
(continuously adjusted),

$$\boxed{\;r_{WACC}=\frac{E}{E+D}r_E+\frac{D}{E+D}r_D(1-\tau)\;} \tag{1}$$

and **discounting the unlevered FCF at (1) gives the value of the levered firm** — Berk Eq. (16.8),
p. 477. Berk rewrites it (Eq. 16.9) as the pre-tax WACC minus the shield:

$$r_{WACC}=\underbrace{\frac{E}{E+D}r_E+\frac{D}{E+D}r_D}_{\text{pre-tax WACC}}-\underbrace{\frac{D}{E+D}\,\tau r_D}_{\text{reduction due to the ITS}} \tag{2}$$

## 2 · C — three WACC formulas (slide 18), derived

For an FCF growing at $g$ forever, $V_L=FCF_1/(r_{WACC}-g)$, and also $V_U=FCF_1/(r_U-g)$. Divide:

$$r_{WACC}-g=\frac{FCF_1}{V_L}=(r_U-g)\frac{V_U}{V_L}=(r_U-g)\Big(1-\frac{V_{ITS}}{V_L}\Big) \tag{3}$$

so **every WACC formula is (3) with one of slide 13's $V_{ITS}$** ([[L03-01-tax-shield-mm-taxes]] (14)–(16)).

**Continuous target ratio.** Substitute $V_{ITS}=\tau r_DD/(r_U-g)$ into (3):

$$r_{WACC}-g=(r_U-g)-\frac{\tau r_DD}{V_L}$$

$$r_{WACC}=r_U-\tau r_D\frac{D}{D+E} \tag{4}$$

and with (12) of note 01, $r_U=\frac{E}{V}r_E+\frac{D}{V}r_D$, substituted into (4):

$$r_{WACC}=\Big(\frac{E}{V}r_E+\frac{D}{V}r_D\Big)-\tau r_D\frac{D}{V}=\frac{E}{E+D}r_E+\frac{D}{E+D}r_D(1-\tau) \tag{5}$$

— formula (1) recovered: **(1) is exact under a continuously rebalanced target ratio.**

**Annual target ratio.** Substitute (16) of note 01 into (3):

$$r_{WACC}=r_U-\tau r_D\frac{D}{D+E}\cdot\frac{1+r_U}{1+r_D} \tag{6}$$

(slide 18 prints $1+r_g$ again; it is $1+r_D$, as derived in note 01 §8).

**Constant debt level.** Substitute $V_{ITS}=\tau D$ into (3):

$$r_{WACC}=g+(r_U-g)\Big(1-\tau\frac{D}{D+E}\Big) \tag{7}$$

and with $g=0$ — the only case in which a constant debt is also a constant $D/V$ —

$$r_{WACC}=\Big(1-\tau\frac{D}{D+E}\Big)r_U \tag{8}$$

which is slide 18's first line (Ross's 9.589% in [[L03-01-tax-shield-mm-taxes]] §5; Lista R3 Ex. 13,
Ross 16.19, printed p. 578). **With $g>0$ and a constant debt, $D/V$ drifts down, so no constant
WACC exists** — use APV.

![Cost of capital against D/V from 0 to 90 percent: r_E rising steeply from 12 percent, flat r_U = 12 percent dashed, after-tax WACC falling gently from 12 percent, flat r_D = 5 percent dotted and after-tax r_D = 3 percent; markers at D/V = 25 percent show r_E = 14.33 percent and WACC 11.5 percent](figures/L03-wacc-taxes.png)
*Figure — the slide-17 picture (Berk Figure 16.7, p. 478) redrawn with the slide-28 project's numbers and safe debt: $r_E$ from (13) of note 01, after-tax WACC from (4). At $D/V=25\%$: $r_E=14.33\%$, $r_{WACC}=11.5\%$. Source: slides 12, 16–18, 28–30.*

$r_U$ — the pre-tax WACC — is flat: the assets' risk does not depend on financing. The after-tax
WACC falls linearly in $D/V$ with slope $-\tau r_D=-2$ points per 100% of leverage; Berk's version
curves upward at high leverage only because there $r_D$ rises with default risk.

---

## 3 · C — the two methods, step by step (slides 19–24)

| Step | **APV** (slides 20–21) | **WACC** (slide 22) |
|---|---|---|
| 1 | unlevered after-tax FCF | unlevered after-tax FCF |
| 2 | unlevered $\beta_U$ from comparables | unlevered $\beta_U$ from comparables |
| 3 | $V_U$: discount FCF at $r_U$ | **relever** $\beta_U$ at the target $D/E$ → $r_E$ |
| 4 | add $V_{ITS}$: PV of tax savings on current and future **incremental** interest | $r_D$ from similar projects' debt |
| 5 | — | after-tax WACC (1); $V_L=\sum_t FCF_t/(1+r_{WACC})^t$ (slide 23) |

APV details (slide 21): a temporary increase in debt → value the shield **as an annuity, not a
perpetuity**; use the **appropriate $r_{ITS}$**; use the **marginal** tax rate (the firm's rate
*including* the project). Higgins (p. 322) writes APV as
$$APV=NPV_{\text{all-equity}}+PV_{\text{interest tax shields}}+PV_{\text{any other side effects}}$$
— *"valuation by parts"*, needed "when the firm's capital structure is changing over time, or when
the project's debt capacity differs from that implicit in the WACC" (pp. 321–322).

**Slide 24, the map:**

| Method | Cash flows | Discount rate |
|---|---|---|
| APV | unlevered FCF | unlevered (asset) cost of capital $r_U$ |
| | interest tax shield | tax-shield cost of capital $r_{ITS}$ |
| WACC | unlevered FCF | after-tax WACC $r_{WACC}$ |

If leverage changes a lot over time, $r_{WACC}$ must be computed period by period (slide 23).

---

## 4 · C — equivalence when $D/E$ is constant (slides 25–27)

WACC method with growth $g$:

$$V_L=\frac{FCF_1}{r_{WACC}-g} \tag{9}$$

Substitute (1), written with $V_L=D+E$:

$$V_L=\frac{FCF_1}{\frac{E}{V_L}r_E+\frac{D}{V_L}r_D(1-\tau)-g} \tag{10}$$

Split $r_D(1-\tau)=r_D-r_D\tau$ and use (12) of note 01, $\frac{E}{V_L}r_E+\frac{D}{V_L}r_D=r_U$
(constant $D/E$):

$$V_L=\frac{FCF_1}{r_U-\frac{D}{V_L}r_D\tau-g} \tag{11}$$

Cross-multiply:

$$V_L(r_U-g)-Dr_D\tau=FCF_1 \tag{12}$$

Move $Dr_D\tau$ right and divide by $r_U-g$:

$$\boxed{\;V_L=\underbrace{\frac{FCF_1}{r_U-g}}_{=V_U}+\underbrace{\frac{Dr_D\tau}{r_U-g}}_{=V_{ITS}}\;} \tag{13}$$

> **Equivalence (slide 27).** (13) is APV with the continuous-target shield (15) of note 01. The
> one assumption used is (12) of note 01 — **$D/E$ constant, hence $r_{ITS}=r_U$**. Drop it and
> step (10)→(11) fails.

---

## 5 · Worked — the 60,000 project, both ways (slides 28–31)

**Data.** Investment 60,000 today; unlevered FCF 7,500 in year 1, growing 4%
($7{,}500\to7{,}500\times1.04=7{,}800\to7{,}800\times1.04=8{,}112\dots$); $\tau=40\%$; target
$D/(D+E)=25\%$; $r_E=14.33\%$, $r_D=5\%$ pre-tax.

**WACC method.**

$$r_{WACC}=0.75\times14.333\%+0.25\times5\%\times(1-0.40)=10.75\%+0.75\%=11.5\%$$

(with the slide's rounded $14.33\%$: $10.7475\%+0.75\%=11.4975\%$, printed 11.5%; the exact $r_E$ is
$12\%+\frac13(12\%-5\%)=14.333\ldots\%$ from (13) of note 01.)

$$V_L=\frac{7{,}500}{0.115-0.04}=\frac{7{,}500}{0.075}=100{,}000,\qquad NPV=100{,}000-60{,}000=40{,}000$$

**APV method.** $D=0.25\times100{,}000=25{,}000$ (slide 30). Unlevered cost of capital, from (12)
of note 01:

$$r_U=0.75\times14.333\%+0.25\times5\%=10.75\%+1.25\%=12\%$$

$$V_U=\frac{7{,}500}{0.12-0.04}=\frac{7{,}500}{0.08}=93{,}750$$

Debt grows at 4% with the firm, so the shield does too, discounted at $r_U$ (slide 31):

$$V_{ITS}=\frac{25{,}000\times0.05\times0.40}{0.12-0.04}=\frac{500}{0.08}=6{,}250$$

$$V_L=93{,}750+6{,}250=100{,}000,\qquad NPV=40{,}000\ ✓$$

## 6 · Worked — APV's flexibility: a fixed 60,000 loan repaid in year 5 (slide 32)

New policy: borrow 60,000 at $t=0$, pay 5% interest, repay at $t=5$. $V_U$ is unchanged at 93,750.

| Year | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| Net borrowing | 60,000 | | | | | −60,000 |
| Interest (5%) | | −3,000 | −3,000 | −3,000 | −3,000 | −3,000 |
| ITS (40%) | | 1,200 | 1,200 | 1,200 | 1,200 | 1,200 |

The schedule is fixed in currency, so the shield is as risky as the debt: $r_{ITS}=r_D=5\%$, an
annuity (slide 21):

$$\frac{1-1.05^{-5}}{0.05}=\frac{1-0.783526}{0.05}=4.329477$$

$$V_{ITS}=1{,}200\times4.329477=5{,}195.37\approx5{,}195$$

$$V_L=93{,}750+5{,}195=98{,}945,\qquad NPV=38{,}945$$

> **Why no WACC here.** $D/V_L$ starts at $60{,}000/98{,}945=61\%$ and drops to zero after year 5:
> there is no single $r_{WACC}$ to plug into (9). Berk's Example 16.4 (p. 476) is the same
> calculation: 2 billion of ten-year 6% bonds, $\tau=35\%$, shield
> $0.35\times120=42$ million a year, $PV=42\times\frac{1}{0.06}\big(1-\frac{1}{1.06^{10}}\big)=42\times7.360087=309$ million.

![Left: three bars, WACC method 100,000, APV with constant D/V split into V_U 93,750 and V_ITS 6,250 totalling 100,000, APV with the 60,000 loan split into 93,750 and 5,195 totalling 98,945, with the 60,000 investment as a dashed line. Right: yearly interest tax shields, growing from 500 under the 25 percent target and 1,200 for five years under the loan](figures/L03-apv-vs-wacc.png)
*Figure — the slide-28 project valued three ways; right panel: the two shield streams being discounted, $500(1.04)^{t-1}$ at $r_U$ and 1,200 for five years at $r_D$. Source: slides 28–32; eqs. (9), (13).*

The loan's shields are larger early (1,200 against 500) yet worth less in total because they stop
after five years; the target-ratio shields are small, risky and perpetual. **What the shield is
worth depends on the debt policy, which is why APV asks for it explicitly.**

---

## 7 · C — Appendix: the WACC formula derived (slides 54–61)

**Assumptions (slide 54):** $V_L=D+E=V_U+V_{ITS}$; the firm keeps a constant leverage ratio
(continuously adjusted); $r_U$ is not time-varying. Then the expected return on the levered firm's
assets equals that of its claims,

$$r_L=\frac{D}{D+E}r_D+\frac{E}{D+E}r_E \tag{14}$$

and, under the constant-ratio assumption, $r_L=r_U$ in every period (note 01 (12)).

**Cash flow and one-period value (slide 55).** Investors receive the unlevered FCF plus the shield:

$$C_{L,t+1}=FCF_{t+1}+r_DD_t\tau \tag{15}$$

$$V_{L,t}=\frac{FCF_{t+1}+r_DD_t\tau+V_{L,t+1}}{1+r_L} \tag{16}$$

**Iterate (slides 56–57).** (16) one period later:
$V_{L,t+1}=\frac{FCF_{t+2}+r_DD_{t+1}\tau+V_{L,t+2}}{1+r_L}$. Substituting it into (16):

$$V_{L,t}=\frac{C_{L,t+1}}{1+r_L}+\frac{C_{L,t+2}}{(1+r_L)^2}+\frac{V_{L,t+2}}{(1+r_L)^2}$$

After $N$ substitutions:

$$V_{L,t}=\sum_{i=1}^{N}\frac{C_{L,t+i}}{(1+r_L)^i}+\frac{V_{L,t+N}}{(1+r_L)^N}$$

and with $V_{L,t+N}/(1+r_L)^N\to0$ as $N\to\infty$ (slide 57):

$$V_{L,t}=\sum_{i=1}^{\infty}\frac{C_{L,t+i}}{(1+r_L)^i} \tag{17}$$

— the going-concern formula; unusable in practice because it needs every period's shield (slide 58).

**Fold the shield into the rate (slides 59–60).** Multiply (16) by $1+r_L$ and move the shield left:

$$V_{L,t}(1+r_L)-r_DD_t\tau=FCF_{t+1}+V_{L,t+1}$$

Write $r_DD_t\tau=V_{L,t}\,r_D\frac{D_t}{V_{L,t}}\tau$ and factor $V_{L,t}$:

$$V_{L,t}\Big(1+r_L-r_D\frac{D_t}{V_{L,t}}\tau\Big)=FCF_{t+1}+V_{L,t+1}$$

$$V_{L,t}=\frac{FCF_{t+1}+V_{L,t+1}}{1+r_L-r_D\frac{D_t}{V_{L,t}}\tau} \tag{18}$$

Expand the denominator with (14) and $V_{L,t}=D_t+E_t$:

$$1+r_L-r_D\frac{D_t}{V_{L,t}}\tau=1+\frac{D_t}{D_t+E_t}r_D+\frac{E_t}{D_t+E_t}r_E-r_D\frac{D_t}{D_t+E_t}\tau$$

$$=1+\frac{D_t}{D_t+E_t}r_D(1-\tau)+\frac{E_t}{D_t+E_t}r_E=1+r_{WACC} \tag{19}$$

**Result (slide 61).** Substituting (19) into (18), $V_{L,t}=\frac{FCF_{t+1}+V_{L,t+1}}{1+r_{WACC}}$,
and the same iteration as (17) gives

$$\boxed{\;V_{L,t}=\sum_{i=1}^{\infty}\frac{FCF_{t+i}}{(1+r_{WACC})^i}\;} \tag{20}$$

> **Read (19) carefully.** The step $r_L=r_U$ was not even needed for (19) — it is an identity in
> $D_t/V_{L,t}$. What makes (20) useful is that **$r_{WACC}$ is the same number every period**, which
> requires a constant $D_t/V_{L,t}$ (and constant $r_E,r_D$, which the constant ratio and constant
> $r_U$ deliver). Slide 61's summand prints $FCF_{L,t+i}$; it is the unlevered $FCF_{t+i}$.

---

## 8 · C — which $r_D$ goes into the shield? (slides 62–63)

The expected return on debt is defined by

$$D_t=\frac{E[C_{t+1}+D_{t+1}]}{1+r_D}\iff r_D=\frac{E[C_{t+1}+D_{t+1}]-D_t}{D_t} \tag{21}$$

**Safe bond** (slide 62): issued at par, face 1,000, coupon 5%: $E[C_{t+1}]=50$,
$E[D_{t+1}]=1{,}000$, so $r_D=\frac{1050-1000}{1000}=5\%$ — coupon rate = expected return.

**Risky bond** (slide 63): $E[C_{t+1}+D_{t+1}]=700<1{,}050$ and $D_t=525$:

$$r_D=\frac{700-525}{525}=33.33\%$$

Is the expected interest deduction $525\times33.33\%=175$? **No.** The deduction is the **interest
actually paid** — the coupon — so the rate that sets the shield is

$$\bar r_D=\frac{E[C_{t+1}]}{D_t},\qquad\text{after-tax cost of debt}=r_D-\tau\,\bar r_D \tag{22}$$

**Illustration (own assumption: the 50 coupon is paid, so $E[C_{t+1}]=50$ — the slide does not split
the 700; $\tau=35\%$ as on slide 2):** $\bar r_D=50/525=9.52\%$, after-tax cost
$33.33\%-0.35\times9.52\%=33.33\%-3.33\%=30.00\%$, against the naive
$33.33\%\times(1-0.35)=21.67\%$. **Using $r_D(1-\tau)$ with a distressed bond overstates the shield
by a factor of $175/50=3.5$.** The expected return includes compensation for expected default
losses (here principal); those are not deductible interest. Compare
[[../L02/L02-07-mm2-wacc-cost-of-debt|L02 §2A.10]]: the yield is not $r_D$ either.

---

## Links

- Before: [[L03-01-tax-shield-mm-taxes]] (the three $V_{ITS}$ closed forms, $r_{ITS}$).
- After: [[L03-04-static-trade-off]] §6 — APV with a distress term, $V_L=V_U+V_{ITS}-PV(\text{bankruptcy costs})$.
- Topic 2A: unlevering comparables and the pre-tax WACC, [[../L02/L02-07-mm2-wacc-cost-of-debt|L02 MM II and WACC]].
- Rules: [[../../rules/03_benchmark_mm|rules/03]].
- Practice: PS2 Ex. 2(a)–(e) ([PS2](../../Listas/PS2.pdf), p. 2: $r_E$ before and after, new WACC,
  shield under a continuous target, interest as 20% of FCF, fixed perpetual debt);
  [[../../Listas/lista-r3-mm-taxes-tradeoff|Lista R3]] Ex. 4 (Higgins 8.23, p. 333), Ex. 6 (Berk
  16.11, p. 492), Ex. 9 (Grinblatt–Titman 13.15–13.16, p. 494), Ex. 13 (Ross 16.19, p. 578).
- Code: [[L03-08-python]] §1–§2.
