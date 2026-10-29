---
tags: [notes, lecture-02, mm-benchmark, mm2, wacc, cost-of-debt, yield]
date: 2026-10-24
status: taught
source: "Topic 2A slides 97–105 (2A.9–2A.10); Ross Fundamentos 9e Cap. 16 §16.3 (pp. 547–549, eq. 16.1, Exemplo 16.3); Berk Fundamentals 2e Ch. 16 §16.2 (pp. 469–471, eq. 16.3, Fig. 16.5); Amaro de Matos Ch. 2 §2.1.2 (pp. 42–43, Prop. 2.1.2 MM2, eq. 2.4). Examples: entrepreneur economy extended to risky debt (built here from slides 55–56); Ross' Ricardo S/A; Berk's coffee shop."
---

# 2A.9–2A.10 · MM II, the WACC, and why $r_D$ is neither the coupon nor the yield

> **Claim.** MM I fixes the value of the assets and their cash flows, hence $r_A$. Since $r_A$
> is the value-weighted average of $r_E$ and $r_D$, more of the "cheap" debt must make equity
> dearer: $r_E=r_A+\frac{D}{E}(r_A-r_D)$ (MM II). It is linear in $D/E$ while debt is safe and
> bends — in a two-state economy, goes flat — once $r_D$ starts rising. The WACC is $r_A$ and does
> not move. The $r_D$ in these formulas is an **expected** return; a risky bond's promised yield
> overstates it.

Prev: [[L02-06-mm1-arbitrage-put-call]] · Next: [[L02-08-formulas]] · Map: [[L02-00-map]]

**Notation.**

| Symbol | Meaning | Range |
|---|---|---|
| $r_A=r_{WACC}=r_U$ | expected return on assets = WACC = return on unlevered equity | — |
| $r_E,r_D$ | expected returns on levered equity and on debt | — |
| $x=D/E$ | market debt-to-equity ratio | $\ge0$ |
| $V_L=D_L+E_L$, $V_U=E_U$ | value of the levered and of the unlevered firm | $>0$ |
| $F$ | face value of one-period debt | $\ge0$ |
| $y$ | yield to maturity: $D=F/(1+y)$ | — |
| $p$, $C$ | default probability; expected recovery in default, $C<F$ | $p\in[0,1]$ |
| $p_1,p_2$ | boom / slump state prices of the entrepreneur economy | 0.357, 0.595 |

---

## 1 · C — MM II, derived (slides 97–99)

**Puzzle (slide 97):** if the mix is irrelevant, why does debt require a lower return than equity?
**Answer:** issuing debt makes equity riskier and so more costly — **even riskless debt** does
(the entrepreneur example): it is not (only) about default.

MM I says $A$ is independent of $D,E$; the cash flows $\tilde C_A$ are too (benchmark assumption
4); so from $A=E[\tilde C_A]/(1+r_A)$ the return $r_A$ is independent of $D,E$ (slide 98). Start
from the identity (1.10) (slide 99):

$$r_A=\frac{E}{E+D}\,r_E+\frac{D}{E+D}\,r_D\tag{7.1}$$

Multiply by $(E+D)/E$:

$$\frac{E+D}{E}\,r_A=r_E+\frac{D}{E}\,r_D$$

Write $\frac{E+D}{E}r_A=r_A+\frac{D}{E}r_A$ and solve for $r_E$:

$$\boxed{\;r_E=r_A+\frac{D}{E}\,(r_A-r_D)\;}\tag{7.2}$$

> **MM II (slide 97).** *A firm's cost of equity increases as the market value debt-to-equity
> ratio increases; for low levels of debt, debt is risk-free and the increase is linear.*
> Since $r_A$ is fixed and $r_A>r_D$, $r_E$ rises with $D/E$; with $r_D=r_f$ fixed the slope is
> the constant $r_A-r_f$.

Same result in the books: Ross eq. [16.1] $R_E=R_A+(R_A-R_D)\times(D/E)$ (p. 548);
Berk eq. 16.3 $r_E=r_U+\frac{D}{E}(r_U-r_D)$ (p. 471); Amaro de Matos **Proposition 2.1.2
(MM2)**, $R_s=R^u_s+(R^u_s-R_b)\frac{B}{S}$ (eq. 2.4, p. 43), derived from
$R_s=E[V_j-B_j]/S=R^u_s\frac{V}{S}-R_b\frac{B}{S}$.

---

## 2 · C — When debt turns risky (slide 100)

Once $D$ is large enough to default with positive probability, $r_D$ also rises with $x=D/E$.
Differentiate (7.2), $r_E=r_A+x\,(r_A-r_D(x))$, with $r_A$ constant (product rule on the second term):

$$\frac{\partial r_E}{\partial x}=(r_A-r_D)-x\,\frac{\partial r_D}{\partial x}\tag{7.3}$$

> **Read the slide's display with care.** Slide 100 prints
> $\frac{\partial r_E}{\partial(D/E)}=r_A-\frac{\partial r_D}{\partial(D/E)}$; differentiating
> (7.2) gives (7.3), with $-r_D$ in the first term and the factor $D/E$ on the second. The
> conclusion is the slide's: the two effects can offset, and *"with a finite number of states …
> $r_E$ is strictly increasing in $D/E$ and then it becomes flat while $r_D$ increases."*

**Worked: the flat region in the entrepreneur economy** (built here on slides 55–56: $X_s=1.05$,
$X_b=3.15$, probabilities 1/2, $p_1=1/2.8$, $p_2=1/1.05-1/2.8$). Let the face be
$F\in(1.05,\ 3.15)$: debt is paid in the boom and defaults in the slump, taking the slump's 1.05.

$$D(F)=p_1F+p_2(1.05)=\frac{F}{2.8}+0.625\tag{7.4}$$

Equity pays $3.15-F$ in the boom and 0 in the slump:

$$E(F)=p_1(3.15-F)=\frac{3.15-F}{2.8}\tag{7.5}$$

Its expected payoff is $\tfrac12(3.15-F)$, so

$$r_E=\frac{\tfrac12(3.15-F)}{(3.15-F)/2.8}-1=\frac{2.8}{2}-1=40\%,\qquad r_D=\frac{\tfrac12F+\tfrac12(1.05)}{F/2.8+0.625}-1\tag{7.6}$$

**$r_E$ is 40% for every risky face value**: equity is now a pure boom claim, and a boom claim
returns $q/p_1-1=0.5\times2.8-1=40\%$ however many units of it one holds. $r_D$ rises from
$1.05/1-1=5\%$ at $F=1.05$ toward $2.1/1.75-1=20\%=r_A$ as $F\to3.15$ (debt becomes the whole
firm). At $F=2.1$: $D=0.75+0.625=1.375$, $E=1.05/2.8=0.375$, $x=3.667$,
$r_D=1.575/1.375-1=14.55\%$; check (7.2):

$$r_E=20\%+3.667\,(20\%-14.55\%)=20\%+3.667\times5.45\%=20\%+20\%=40\%\ \checkmark$$

and (7.3) is zero there: $x\,\partial r_D/\partial x=r_A-r_D$ exactly.

![Expected returns against D/E in the entrepreneur economy: r_E linear from 20% to 40% up to D/E = 1.33, then flat at 40%; r_D at 5% then rising toward 20%; r_A flat at 20%](figures/L02-mm2.png)
*MM II (7.2) in both regions: linear while debt is safe (slides 75–77), flat once it is risky (7.6, slide 100); $r_A=r_{WACC}=20\%$ throughout.*

The kink at $D/E=1.33$ is the face value 1.05 that exhausts the slump payoff. To its right the
WACC still averages to 20%: equity's weight shrinks while debt's return climbs toward 20%.

> **Interactive companion.** [The State-Price Balance Sheet](companions/companion-mm-state-prices.html)
> — drag $F$ past the slump payoff: the right panel's $r_E$ stops rising exactly where $r_D$
> leaves $r_f$; press "Risky debt, F = 2.1" for the case above.

---

## 3 · C — The WACC and conservation of value (slides 101–102)

$r_A$ **is** the weighted average cost of capital, $r_{WACC}$, and by MM I it does not depend on
$D,E$. Another statement of MM I:

$$D_L+E_L=V_L=V_U=E_U\tag{7.7}$$

value of the levered firm (any $D_L,E_L$) = value of the unlevered, all-equity firm. Hence

$$r_A=r_{WACC}=\frac{E}{D+E}\,r_E+\frac{D}{D+E}\,r_D=r_U\tag{7.8}$$

and (7.2) becomes

$$r_E=r_U+\frac{D}{E}\,(r_U-r_D)\tag{7.9}$$

> **Slide 102's first display swaps the weights** — it prints $\frac{D}{D+E}r_E+\frac{E}{D+E}r_D$.
> The correct weights are (7.8)'s: equity's return times equity's share.

> **Conservation of value (slide 102):** *"With perfect capital markets, financial transactions
> neither add nor destroy value, but instead represent a repackaging of risk (and therefore
> return)."*

*U-layer, Ross Exemplo 16.3 (p. 549):* WACC (no taxes) 12%, borrowing at 8%. Target 20% debt,
$D/E=0.2/0.8=0.25$:

$$R_E=12\%+(12\%-8\%)\times0.25=12\%+1\%=13\%;\qquad \text{CMPC}=0.8(13\%)+0.2(8\%)=10.4\%+1.6\%=12\%$$

At 50% debt, $D/E=1$: $R_E=12\%+4\%=16\%$ and $0.5(16\%)+0.5(8\%)=12\%$.

*U-layer, Berk Fig. 16.5 (p. 471):* the coffee shop's WACC stays at 15% for
$D=0,\ 6{,}000,\ 15{,}000,\ 27{,}000$ while $r_E$ goes $15\%\to17.5\%\to25\%\to75\%$ and $r_D$
rises to 8.3% at the last level, where debt has become risky:
$75\%\times0.1+8.33\%\times0.9=7.5\%+7.5\%=15\%$.

---

## 4 · C — $r_D$ is not the coupon, and not the yield (slides 103–105)

$r_D$ is the **expected return investors require today** on the firm's debt. It is not the
interest rate contracted in the past: macroeconomic conditions and the firm's fundamentals
(default risk) change (slide 103). It is not the yield either. For one-period debt of face $F$:

$$D=\frac{F}{1+y}\qquad\text{(yield: discounts the promised payment)}\tag{7.10}$$
$$D=\frac{F(1-p)+C\,p}{1+r_D}\qquad\text{(expected return: discounts the expected payment)}\tag{7.11}$$

Equate (7.10) and (7.11) and solve:

$$\frac{1+y}{1+r_D}=\frac{F}{F(1-p)+Cp}$$

With $p>0$ and $C<F$, $F(1-p)+Cp=F-p(F-C)<F$, so the right side exceeds 1:

$$\boxed{\;y>r_D\quad\text{whenever debt is risky}\;}\tag{7.12}$$

**The yield overestimates the debt cost of capital** (slide 105). Using it in (7.8) overstates
the WACC.

**Worked (the $F=2.1$ case of §2).** $D=1.375$; default in the slump ($p=0.5$) with recovery $C=1.05$:

$$y=\frac{2.1}{1.375}-1=52.73\%$$
$$r_D=\frac{2.1(1-0.5)+1.05(0.5)}{1.375}-1=\frac{1.05+0.525}{1.375}-1=\frac{1.575}{1.375}-1=14.55\%$$

The 38-point gap is expected default loss. The remaining $14.55\%-5\%$ over $r_f$ is a **risk
premium**: the debt defaults in the slump, the expensive state, so it carries systematic risk.

---

## 5 · G — The beta form of MM II (Amaro de Matos p. 43)

Linearity of covariance turns (7.2) into
$\beta_s=\beta^u_s\bigl(1+\frac{B}{S}\bigr)-\beta_d\frac{B}{S}$, and the average cost of capital
$\bar R=\frac{S}{S+B}R_s+\frac{B}{S+B}R_b$ has beta $\bar\beta=\frac{S}{S+B}\beta_s+\frac{B}{S+B}\beta_d$
— the relevering formula (1.12) of [[L02-01-present-value-capm-betas]] with risky debt.

---

## Links

- The identity behind (7.1) → [[L02-01-present-value-capm-betas]] §5; the safe-debt tables →
  [[L02-05-entrepreneur-example]] §6–7; MM I → [[L02-06-mm1-arbitrage-put-call]].
- With taxes the WACC falls in $D/V$ and $V_L=V_U+\tau D$ → [[../L03/L03-00-map|L03]]; ROE and P/E
  moving with leverage → [[../L01/L01-00-map|L01]].
- Rules: [[../../rules/03_benchmark_mm|rules/03 — MM benchmark]].
- Python: `mm2_rE`, `yield_vs_rD` → [[L02-10-python]].
- **Practice.** PS2 Ex. 1(e) ($r_D,r_E,r_A$ across $D$; [PS2](../../Listas/PS2.pdf) p. 1);
  PS2 Ex. 4(a–b) (beta and expected return after a debt-financed repurchase; pp. 2–3);
  [lista-r3](../../Listas/lista-r3-mm-taxes-tradeoff.md) #5 (Berk Ch. 16 Ex. 16.5, p. 491);
  [lista-r2](../../Listas/lista-r2-valuation.md) #4 (Berk Ch. 13 Ex. 4, p. 403).
