---
tags: [notes, lecture-03, trade-off-theory, optimal-capital-structure, bankruptcy-costs, tax-shield]
date: 2026-10-24
status: taught
source: "Aula/Topic2B.pdf slides 41–45 (block 2B.7, the static trade-off model); Berk Fundamentals 2e §16.5 pp. 480–482 (Eq. 16.10, Figure 16.8); Ross Fundamentos 9e §16.6 pp. 558–562 (Figures 16.6–16.8, the static theory, management recommendations); Higgins 13e Ch. 6 p. 213 (three firm-specific factors); Amaro de Matos §2.1.3 p. 45 (Prop. 2.1.3), §2.2.5 pp. 54–55"
---

# 2B.7 · The static trade-off: $V(K)$, the first-order condition, and $K^*$

> **Claim.** In one period with risk-neutral investors, a firm that promises $K$ to creditors is
> worth $V(K)=V_U+\frac{1}{1+r_f}\big[\tau\,E[\min(X,K)]-C\,H(K)\big]$: **the tax saved on
> everything creditors are paid, minus the expected default cost.** Raising $K$ saves $\tau$ in
> solvent states only and raises the default probability, so the optimum equates
> $\tau[1-H(K^*)]=C\,h(K^*)$. **$K^*$ rises with $\tau$ and falls with $C$; with $C=0$ the firm
> wants all the debt it can issue, with $\tau=0$ any safe debt will do — MM again.**

Prev: [[L03-03-debt-puzzle-bankruptcy-costs]] · Next: [[L03-05-bank-capital-dividend-irrelevance]] · Map: [[L03-00-map]]

**Notation (slides 41–42).**

| Symbol | Meaning | Range |
|---|---|---|
| $t=0,1$ | debt issued at $0$, repaid at $1$ | |
| $K$ | **total** repayment promised at $t=1$ (principal + interest) | $\geq0$ |
| $X$ | random cash flow at $t=1$, density $h$ on $[\underline X,\bar X]$ | $0\le\underline X<\bar X$ |
| $H(a)$ | c.d.f., $\Pr(X\le a)$; $H(K)$ is the **default probability** | $[0,1]$ |
| $\tau$ | tax rate, paid only if solvent ($X\ge K$); the **full** $K$ is deductible | $[0,1)$ |
| $C$ | fixed deadweight cost of bankruptcy ($X<K$), with $C<\underline X$ | $\geq0$ |
| $r_f$ | required expected return of every (risk-neutral) investor | $>-1$ |
| $V_U$, $E(K)$, $D(K)$, $V(K)$ | unlevered value; market values of equity, debt, and the firm | |
| $S(K)$ | $E[\min(X,K)]=\int_{\underline X}^K xh(x)dx+K[1-H(K)]$ | |
| $K^*$ | value-maximizing $K$ | $[\underline X,\bar X]$ |

**Which assumption does what.** The full deductibility of $K$ is "for simplicity" (slide 41) — it
makes the shield of a solvent firm exactly $\tau K$. No tax in default means the shield there is
$\tau X$ — the whole tax bill. $C<\underline X$ keeps creditors' payoff $X-C$ positive, so limited
liability never binds. Risk neutrality makes $1/(1+r_f)$ the only discount factor.

---

## 1 · C — the unlevered firm and safe debt (slide 42)

**The default probability (slide 41):**

$$H(a)=\Pr(X\le a)=\int_{\underline X}^{a}h(x)\,dx \tag{1}$$

**Unlevered.** The firm pays $\tau X$ in every state; investors get $(1-\tau)X$:

$$V_U=\frac{1}{1+r_f}\int_{\underline X}^{\bar X}(1-\tau)X\,h(X)\,dX=\frac{(1-\tau)E[X]}{1+r_f} \tag{2}$$

**Safe debt, $K<\underline X$.** Default never happens. Equity gets $(1-\tau)(X-K)$, debt gets $K$:

$$V_L(K)=\frac{1}{1+r_f}\int_{\underline X}^{\bar X}\big[(1-\tau)(X-K)+K\big]h(X)\,dX$$

Integrate each term ($\int h=1$):

$$V_L(K)=\frac{(1-\tau)E[X-K]}{1+r_f}+\frac{K}{1+r_f}$$

Write $(1-\tau)E[X-K]+K=(1-\tau)E[X]+\tau K$:

$$V_L(K)=V_U+\frac{\tau K}{1+r_f}\qquad(K<\underline X) \tag{3}$$

— **one-period MM I with taxes**: the shield $\tau K$ is safe, discounted at $r_f$
([[L03-01-tax-shield-mm-taxes]] (5) is the perpetual version).

## 2 · C — risky debt: equity, debt, firm (slides 43–44)

**Equity (slide 43)** — paid only when solvent, after tax:

$$E(K)=\frac{1}{1+r_f}\int_{K}^{\bar X}(1-\tau)(X-K)\,h(X)\,dX \tag{4}$$

**Debt** — in default creditors take $X$ and bear $C$; when solvent they get $K$:

$$D(K)=\frac{1}{1+r_f}\int_{\underline X}^{K}(X-C)\,h(X)\,dX+\frac{1}{1+r_f}\int_{K}^{\bar X}K\,h(X)\,dX$$

and $\int_K^{\bar X}h=1-H(K)$:

$$D(K)=\frac{1}{1+r_f}\int_{\underline X}^{K}(X-C)\,h(X)\,dX+\frac{K[1-H(K)]}{1+r_f} \tag{5}$$

(Slide 43 labels the first line "the market value of debt" twice; (4) is equity.)

**Adding (4) and (5) (slide 44), every step.** Put both over $1+r_f$:

$$(1+r_f)V(K)=\int_K^{\bar X}\big[(1-\tau)(X-K)+K\big]h\,dX+\int_{\underline X}^K(X-C)h\,dX$$

Rewrite each integrand around the unlevered payoff $(1-\tau)X$:
$(1-\tau)(X-K)+K=(1-\tau)X+\tau K$ and $X-C=(1-\tau)X+\tau X-C$. Then

$$(1+r_f)V(K)=\int_{\underline X}^{\bar X}(1-\tau)X\,h\,dX+\int_K^{\bar X}\tau K\,h\,dX+\int_{\underline X}^K(\tau X-C)\,h\,dX$$

The first integral is $(1+r_f)V_U$ by (2); the second is $\tau K[1-H(K)]$; the third splits into
$\tau\int_{\underline X}^KXh\,dX-C\,H(K)$ by (1). Dividing by $1+r_f$:

$$\boxed{\;V(K)=V_U+\frac{1}{1+r_f}\Big[\tau\Big(\int_{\underline X}^{K}x\,h(x)\,dx+K[1-H(K)]\Big)-C\,H(K)\Big]\;} \tag{6}$$

**Read (6).** The round bracket is $S(K)=E[\min(X,K)]$ — what the firm pays out to creditors before
the cost $C$:

$$V(K)=V_U+\underbrace{\frac{\tau\,S(K)}{1+r_f}}_{V_{ITS}}-\underbrace{\frac{C\,H(K)}{1+r_f}}_{PV(\text{bankruptcy costs})} \tag{7}$$

which is slide 45's $V_L=V_U+V_{ITS}-PV(\text{bankruptcy costs})$, Berk's Eq. (16.10) (p. 481),
and Ross's Figure 16.6 (p. 559) in a formula.

**A second reading.** From (5), $\int_{\underline X}^Kx\,h\,dx+K[1-H(K)]=(1+r_f)D(K)+C\,H(K)$.
Substitute into (6):

$$V(K)=V_U+\tau D(K)-\frac{(1-\tau)\,C\,H(K)}{1+r_f} \tag{8}$$

With $C=0$:

$$V(K)=V_U+\tau D(K) \tag{9}$$

— **Amaro's Proposition 2.1.3** (p. 45): with no deadweight cost, risky debt still adds exactly
$\tau$ times its market value. **Default alone costs nothing** ([[L03-03-debt-puzzle-bankruptcy-costs]] §3).

## 3 · C — the marginal condition (slides 44–45)

Differentiate each piece of (6) in $K$. By Leibniz's rule,

$$\frac{d}{dK}\int_{\underline X}^{K}x\,h(x)\,dx=K\,h(K)$$

$$\frac{d}{dK}\Big(K[1-H(K)]\Big)=[1-H(K)]-K\,h(K)$$

Their sum is $1-H(K)$ — the $K\,h(K)$ terms cancel: the creditors' gain in the marginal state
exactly offsets the loss of the marginal solvent state. And $\frac{d}{dK}C\,H(K)=C\,h(K)$. So

$$(1+r_f)\,V'(K)=\underbrace{\tau\,[1-H(K)]}_{\text{marginal tax benefit}}-\underbrace{C\,h(K)}_{\text{marginal expected bankruptcy cost}} \tag{10}$$

**Slide 44's "two effects".** An extra unit of promised repayment (i) saves $\tau$, but only in
**solvent** states — probability $1-H(K)$; in default states all tax is already avoided; (ii)
pushes probability mass $h(K)$ into default, each unit costing $C$.

**First-order condition (slide 45).** *"The optimal debt level $K^*$ is such that the marginal
benefit of debt equals the marginal expected bankruptcy costs"*:

$$\boxed{\;\tau\,[1-H(K^*)]=C\,h(K^*)\;} \tag{11}$$

**Second-order condition.** Differentiate (10) again:

$$(1+r_f)\,V''(K)=-\tau\,h(K)-C\,h'(K)<0 \tag{12}$$

at an interior maximum.

**The safe region.** For $K<\underline X$, $H=h=0$ and (10) gives $V'(K)=\tau/(1+r_f)>0$: **the firm
never stops below $\underline X$** — it always takes all the safe debt it can, so $K^*\ge\underline X$.

## 4 · C — comparative statics: $K^*$ rises with $\tau$, falls with $C$ (slide 45)

Write (11) as $F(K^*;\tau,C)=0$ with $F\equiv\tau[1-H(K)]-C\,h(K)$. The partial derivatives:

$$F_K=-\tau h(K)-C h'(K),\qquad F_\tau=1-H(K),\qquad F_C=-h(K)$$

By the implicit function theorem $dK^*/dx=-F_x/F_K$, and $F_K<0$ by (12):

$$\frac{dK^*}{d\tau}=\frac{1-H(K^*)}{\tau h(K^*)+C h'(K^*)}>0 \tag{13}$$

$$\frac{dK^*}{dC}=\frac{-h(K^*)}{\tau h(K^*)+C h'(K^*)}<0 \tag{14}$$

> **Slide 45: "$K^*$ increases with the tax benefits $\tau$; $K^*$ decreases with bankruptcy costs
> $C$."** (13)–(14) are those two sentences, signed by the second-order condition alone — they
> hold for any density $h$ that makes the optimum interior.

**The two landmarks.**

| Case | (10) becomes | Optimum |
|---|---|---|
| $C=0$ | $\tau[1-H(K)]\ge0$, zero only at $K=\bar X$ | $K^*=\bar X$: promise the top cash flow, **shield the whole tax bill**; $V=V_U+\tau E[X]/(1+r_f)=E[X]/(1+r_f)$ — the 100%-debt answer of [[L03-03-debt-puzzle-bankruptcy-costs]] §1 |
| $\tau=0$ | $-C\,h(K)\le0$ | **any $K\le\underline X$** gives $V_U$ (MM indifference over safe debt); risky debt only loses $C\,H(K)/(1+r_f)$ |

## 5 · Worked — uniform cash flow (the companion's calibration)

The slides leave $h$ general and give no numbers. **Calibration used here and in the companion
(declared, not the slides'):** $X\sim U[\underline X,\bar X]=U[50,150]$, $\tau=35\%$ (the rate of
slides 2 and 33), $C=20<\underline X$, $r_f=5\%$ (the debt rate of slide 32).

**Uniform pieces.** $h=\frac{1}{\bar X-\underline X}$, $H(K)=\frac{K-\underline X}{\bar X-\underline X}$, and
for $\underline X\le K\le\bar X$:

$$S(K)=\frac{K^2-\underline X^2}{2(\bar X-\underline X)}+\frac{K(\bar X-K)}{\bar X-\underline X} \tag{15}$$

**Optimum.** Substitute $h$ and $H$ into (11):

$$\tau\,\frac{\bar X-K^*}{\bar X-\underline X}=\frac{C}{\bar X-\underline X}$$

Multiply by $\bar X-\underline X$ and solve:

$$K^*=\bar X-\frac{C}{\tau}\quad\text{if }C<\tau(\bar X-\underline X);\qquad K^*=\underline X\ \text{otherwise} \tag{16}$$

($h'=0$, so (12) is $-\tau h<0$: the interior root is a maximum.) **Uniform $h$ makes (13)–(14)
explicit: $dK^*/d\tau=C/\tau^2>0$, $dK^*/dC=-1/\tau<0$.**

**The numbers, step by step.**

$$V_U=\frac{(1-0.35)\times100}{1.05}=\frac{65}{1.05}=61.9048$$

$$K^*=150-\frac{20}{0.35}=150-57.1429=92.8571\qquad(20<0.35\times100=35:\ \text{interior})$$

$$H(K^*)=\frac{92.8571-50}{100}=0.428571$$

$$S(K^*)=\frac{92.8571^2-50^2}{200}+\frac{92.8571\times57.1429}{100}=\frac{8622.45-2500}{200}+53.0612=30.6122+53.0612=83.6735$$

$$V_{ITS}=\frac{0.35\times83.6735}{1.05}=\frac{29.2857}{1.05}=27.8912$$

$$PV(\text{bankruptcy costs})=\frac{20\times0.428571}{1.05}=\frac{8.5714}{1.05}=8.1633$$

$$V(K^*)=61.9048+27.8912-8.1633=81.6327$$

**The claims.** By (5): $\int_{50}^{K^*}(x-20)\frac{dx}{100}=\frac{(8622.45-2500)/2-20\times42.8571}{100}=\frac{3061.22-857.14}{100}=22.0408$, so

$$D(K^*)=\frac{22.0408+92.8571\times0.571429}{1.05}=\frac{22.0408+53.0612}{1.05}=\frac{75.1020}{1.05}=71.5258$$

By (4): $E(K^*)=\frac{0.65}{1.05}\cdot\frac{(150-92.8571)^2}{2\times100}=\frac{0.65\times16.3265}{1.05}=10.1069$.

Check: $71.5258+10.1069=81.6327=V(K^*)$ ✓; and (8): $61.9048+0.35\times71.5258-\frac{0.65\times8.5714}{1.05}=61.9048+25.0340-5.3061=81.6327$ ✓.

| Debt policy | $V$ | vs. $V_U$ |
|---|---|---|
| none ($K=0$) | 61.9048 | — |
| largest safe debt ($K=\underline X=50$) | $61.9048+\frac{0.35\times50}{1.05}=61.9048+16.6667=78.5714$ | +16.67 |
| **optimum $K^*=92.86$** | **81.6327** | **+19.73** |
| default certain ($K\ge150$) | $61.9048+\frac{0.35\times100-20}{1.05}=61.9048+14.2857=76.1905$ | +14.29 |

At $K^*$: default probability 42.9%, $D/V=71.53/81.63=87.6\%$, promised yield
$K^*/D-1=92.857/71.526-1=29.8\%$ against an **expected** return of $r_f=5\%$ — the gap between yield
and expected return of [[../L02/L02-07-mm2-wacc-cost-of-debt|L02 §2A.10]].

![Left: firm value against debt repayment K from 0 to 180: V_U flat at 61.90, V_U plus the PV tax shield rising and flattening at 95.24 beyond K = 150, and V(K) with C = 20 rising linearly to 78.57 at K = 50, peaking at 81.63 at K* = 92.86 and falling to 76.19 beyond 150, the gap shaded as expected distress. Right: marginal tax benefit falling linearly from 0.333 at K = 50 to 0 at 150, crossing the flat marginal distress cost 0.190 at K* = 92.86](figures/L03-trade-off.png)
*Figure — the trade-off model with uniform $h$ on $[50,150]$, $\tau=35\%$, $C=20$, $r_f=5\%$: $V(K)$ from (6), the tax-shield-only curve ($C=0$, eq. (9)), and the marginal condition (10)–(11). $K^*=92.86$, $V^*=81.63$. Source: slides 42–45; calibration declared in §5.*

The shaded wedge is $C\,H(K)/(1+r_f)$: zero while debt is safe, then growing linearly with the
default probability. On the right, the marginal tax benefit is flat at $\tau/(1+r_f)=0.333$ over
safe debt and declines as solvent states run out; the distress cost jumps to
$C/(100\times1.05)=0.190$ once $K$ enters the support. Where they cross is $K^*$.

![Left: K* against the tax rate from 0 to 50 percent for C = 10, 20, 35: flat at the safe-debt corner 50 until tau = C/100, then rising as 150 - C/tau. Right: K* against C from 0 to 49 for tau = 25, 35, 45 percent: starting at 150 when C = 0 and falling linearly with slope -1/tau to the corner at 50](figures/L03-trade-off-statics.png)
*Figure — slide 45's comparative statics under (16): $K^*$ rises with $\tau$ (left) and falls with $C$ (right); the kinks are the switch to the corner $K^*=\underline X$ at $C=\tau(\bar X-\underline X)$. Source: eqs. (13)–(16).*

Both landmarks of §4 are visible: at $C=0$ every curve on the right starts at $\bar X=150$, and as
$\tau\to0$ every curve on the left falls to the safe-debt corner.

> **Interactive companion.** [The Trade-off Dial](companions/companion-static-trade-off.html) — move
> $\tau$, $C$, the support $[\underline X,\bar X]$ and $r_f$, watch $V(K)$ and the two marginal curves
> move and read $K^*$, $V(K^*)$, the shield, the expected distress cost and the default probability;
> set $C=0$ or $\tau=0$ to land on the two landmarks.

## 6 · C — from the model to the APV and to practice (slide 45; Ross pp. 560–562)

*"We can adjust the APV method to consider PV(bankruptcy costs)"* (slide 45): (7) is APV with a
third term — Higgins's "any other side effects" ([[L03-02-after-tax-wacc-apv]] §3).

**What the model says to a CFO** — Ross's recommendations (pp. 560–562) and Higgins's three
factors (p. 213), each one an object of (10):

| Practical advice | Where it sits in (10) |
|---|---|
| The shield matters only for firms that **pay tax**: tax-loss carry-forwards, other shields (depreciation) and, in Brazil, non-*lucro real* regimes lower the gain (Ross p. 560, 562) | the effective $\tau$ |
| Higher tax rate → more borrowing (Ross p. 562) | (13) |
| Riskier firms borrow less: "quanto maior a volatilidade do Lajir, menos uma empresa deveria tomar emprestado" (Ross p. 562) | $H$, $h$ — see the caveat below |
| Intangible assets, growth options, talent → costly distress → less debt (Ross p. 562; Higgins pp. 210–211) | $C$, (14) |

> **Caveat (an exact property of the model, not in the slides).** The slides sign $K^*$ in $\tau$
> and $C$ only. Volatility is **not** signed in general: with uniform $h$, $K^*=\bar X-C/\tau$
> depends on the top of the support, so a mean-preserving spread **raises** $K^*$ in the interior
> regime and **lowers** it in the corner regime $K^*=\underline X$. What does fall with volatility
> in the uniform case, in both regimes, is the value gain from debt, $V(K^*)-V_U$ (mean 100,
> $\tau=35\%$, $C=20$: 30.00 at width 20, 19.73 at width 100, 18.17 at width 140 — computed in
> [[L03-08-python]] §3). Pitfall 7 in [[L03-07-pitfalls]].

**Why "static".** Ross (p. 558): the theory takes the firm's assets and operations as fixed and
varies only the debt–equity mix — one period, one decision, no refinancing, no information
problems.

## 7 · G — the tax-shield underutilization link (Amaro §2.2.5, pp. 54–55)

DeAngelo and Masulis's force is already in (10): with $C=0$ the marginal benefit $\tau[1-H(K)]$
still **declines** with debt because shields are wasted in default states. On its own it never
turns negative (so $K^*=\bar X$); it is the deadweight cost $C\,h(K)$ that produces an interior
optimum — Amaro's $d(B)$ (p. 55).

---

## Links

- Before: [[L03-03-debt-puzzle-bankruptcy-costs]] (what $C$ stands for), [[L03-01-tax-shield-mm-taxes]] (the shield).
- Topic 2A: MM I with risky debt and put–call parity, [[../L02/L02-06-mm1-arbitrage-put-call|L02 MM I]];
  the two-state entrepreneur, [[../L02/L02-05-entrepreneur-example|L02 entrepreneur example]].
- Rules: [[../../rules/03_benchmark_mm|rules/03]] (taxes and default costs).
- Practice: [[../../Listas/lista-r3-mm-taxes-tradeoff|Lista R3]] Ex. 8 (Berk 16.22, p. 494), Ex. 10
  (Grinblatt–Titman 16.2, pp. 591–592: the two-state version of this model); PS2 Ex. 3(c)
  ([PS2](../../Listas/PS2.pdf), p. 2); quiz block `dist` of
  [[../../Simulados/quiz-topic2b-taxes-tradeoff-2026-10-24|quiz Topic 2B]].
- Code: [[L03-08-python]] §3 (general $h$, numerical $K^*$, a triangular density).
- Companion: [The Trade-off Dial](companions/companion-static-trade-off.html).
