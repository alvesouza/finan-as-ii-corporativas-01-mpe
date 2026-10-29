---
tags: [notes, lecture-03, bank-capital, admati, payout-policy, dividend-irrelevance, mm]
date: 2026-10-24
status: taught
source: "Aula/Topic2B.pdf slides 46–51 (blocks 2B.8–2B.9); Amaro de Matos Ch. 4 §4.1 pp. 99–101 (Prop. 4.1.1 'MM3', Eqs. 4.1–4.5, 4.7); Berk Fundamentals 2e §17.2 pp. 503–508 (Genron, Table 17.1, MM dividend irrelevance); Ross Fundamentos 9e §17.2 pp. 587–589 (Wharton Corporation, homemade dividends)"
---

# 2B.8–2B.9 · Bank capital, and why payout policy is irrelevant too

> **Claim.** The lecture's tools settle a live policy debate: of the three standard objections to
> higher bank equity requirements, **two are MM fallacies** (a lower ROE and "expensive" equity
> leave the WACC unchanged) and **one is a private cost that is a public transfer** (the lost tax
> shield). The same zero-NPV logic then extends to payout: **with the investment plan fixed, a
> higher dividend must be financed by issuing claims, and value is
> $V_t=E\big[\sum_i\delta^i(X_{t+i}-I_{t+i})\big]$ whatever the payout.**

Prev: [[L03-04-static-trade-off]] · Next: [[L03-06-formulas]] · Map: [[L03-00-map]]

**Notation.** §1: $r_U$, $r_E$, $r_D$, $\tau$, $D/V$, $E/V$ as in [[L03-01-tax-shield-mm-taxes]];
ROE here is the expected return on book-equal-to-market equity. §2 (slides 49–51): $X_t$ random cash
flow of period $t$; $D_t$ **per-share dividend** (not debt!); $I_t$ investment; $n_t$ shares
outstanding at the end of $t$; $P_t$ ex-dividend share price at the end of $t$; $\delta$ the
discount factor; $V_t=n_tP_t$.

---

## 1 · C — the bank capital debate (slides 46–47)

After the 2007–08 crisis regulators proposed higher capital (equity) requirements. Banks argued
this would hurt credit and growth. Admati, DeMarzo, Hellwig and Pfleiderer (2013): **"bank equity
is not socially expensive"** — larger capital requirements, less leverage, using the arguments of
this lecture. The slide asks: true or false?

**Illustration (own, built on the slide-28 rates):** a bank's assets earn $r_U=12\%$, its debt is
safe at $r_D=5\%$; the requirement moves $E/V$ from 25% to 50%.

**Statement 1** — *"Increased equity requirements will hurt bank shareholders since it would lower
the banks' return on equity (ROE)."* Without taxes, by MM II ([[L03-01-tax-shield-mm-taxes]] (13)):

$$r_E\big|_{E/V=25\%}=12\%+\frac{0.75}{0.25}(12\%-5\%)=12\%+3\times7\%=33\%$$

$$r_E\big|_{E/V=50\%}=12\%+\frac{0.50}{0.50}(12\%-5\%)=19\%$$

ROE falls — **but so does the risk it compensates**: with $\beta_D=0$, $\beta_E=\frac{V}{E}\beta_U$
halves from $4\beta_U$ to $2\beta_U$. 33% was the fair return for a riskier claim; 19% is the fair
return for a safer one. Shareholders' wealth is unchanged (MM I). **False** — the ROE–leverage link
of Topic 1 ([[../L01/L01-05-ratios-dupont-roic|L01 ROE and leverage]]) is a statement about
**risk**, not value.

**Statement 2** — *"... increase the funding costs for banks because they must use more equity,
which has a higher required return."* The WACC with no taxes:

$$0.25\times33\%+0.75\times5\%=8.25\%+3.75\%=12\%,\qquad 0.50\times19\%+0.50\times5\%=9.5\%+2.5\%=12\%$$

**False** — the required return on equity is not a fixed price: it **falls** as leverage falls,
exactly offsetting the shift in weights ([[../L02/L02-07-mm2-wacc-cost-of-debt|L02 MM II]]).

**Statement 3** — *"... because they reduce the ability of banks to benefit from the tax shield
associated with interest payments on debt."* With $\tau=40\%$ and a continuous target, by (4) of
[[L03-02-after-tax-wacc-apv]]:

$$r_{WACC}\big|_{D/V=75\%}=12\%-0.40\times5\%\times0.75=10.5\%,\qquad r_{WACC}\big|_{D/V=50\%}=12\%-0.40\times5\%\times0.50=11.0\%$$

**True for the bank, but not a social cost**: the 0.5 point is the tax shield
$\tau r_D D$, a transfer from taxpayers. Less leverage moves it back; the economy's resources are
the same. Slide 47's counterpoint completes the case: leverage carries a **negative externality** —
it "raises the probability of a bank failure, weakening the financial system and imposing losses on
the broader economy" — a cost of debt the bank does not bear, so the private trade-off
([[L03-04-static-trade-off]] (11)) chooses **too much** leverage from society's view.

> **The pattern.** A claim that "equity is expensive" is either an MM fallacy (statements 1–2) or
> a claim about a subsidy (statement 3). Neither is a social cost of equity.

---

## 2 · C — MM dividend irrelevance (slides 48–51)

**Slide 48.** The MM logic applies to **all** purely financial transactions, since each has zero
NPV: other instruments (convertibles, preferred stock), the choice between long- and short-term
debt, risk management — and payout. ***MM dividend irrelevance proposition:*** *a firm's total
market value is independent of its dividend policy.* (Berk p. 508: "holding fixed the investment
policy of a firm, the firm's choice of dividend policy is irrelevant and does not affect the
initial share price"; Amaro **Proposition 4.1.1 (MM3)**, p. 100.)

**Setup (slide 49).** Investment policy fixed ⇒ a change in payout must be met by a change in
financing. All-equity firm, risk-neutral investors; at $t=1,2,\dots$ it generates $X_t$, pays a
per-share dividend $D_t$, invests $I_t$, has $n_t$ shares.

**Pricing (slide 50).** The end-of-$t$ price is the discounted value of next period's dividend and
price:

$$P_t=\delta E[D_{t+1}+P_{t+1}] \tag{1}$$

**Sources = uses (slide 50).** New shareholders of period $t$ buy at $P_t$ and do not receive $D_t$,
so the dividend to the **old** shares plus investment is paid by the cash flow plus the issue:

$$\underbrace{n_{t-1}D_t+I_t}_{\text{uses of funds}}=\underbrace{X_t+P_t(n_t-n_{t-1})}_{\text{sources (earned or raised)}} \tag{2}$$

**Total value (slide 51).** Multiply (1) by $n_t$:

$$V_t=n_tP_t=\delta E[n_tD_{t+1}+n_tP_{t+1}] \tag{3}$$

Write (2) for period $t+1$ and solve for the dividend bill:

$$n_tD_{t+1}=X_{t+1}-I_{t+1}+P_{t+1}(n_{t+1}-n_t) \tag{4}$$

Substitute (4) into (3):

$$V_t=\delta E\big[X_{t+1}-I_{t+1}+P_{t+1}(n_{t+1}-n_t)+n_tP_{t+1}\big]$$

The $n_tP_{t+1}$ terms cancel, leaving $P_{t+1}n_{t+1}=V_{t+1}$:

$$V_t=\delta E[X_{t+1}-I_{t+1}+V_{t+1}] \tag{5}$$

**Solve recursively.** (5) at $t+1$ inside (5) at $t$:
$V_t=\delta E[X_{t+1}-I_{t+1}]+\delta^2E[X_{t+2}-I_{t+2}]+\delta^2E[V_{t+2}]$; after $N$ steps the
remainder is $\delta^NE[V_{t+N}]\to0$ (Amaro p. 100: "Assuming that $V$ is always finite and $r$ is
positive"), so

$$\boxed{\;V_t=E\Big[\sum_{i=1}^{+\infty}\delta^i\,(X_{t+i}-I_{t+i})\Big]\;} \tag{6}$$

(slide 51 prints the summand as $X_{t+1}-I_{t+1}$; it is $X_{t+i}-I_{t+i}$, as in Amaro's (4.5),
p. 100). **No $D$ appears in (6).** The value of the all-equity firm does not depend on the payout
policy **as long as the investment plan $I_t$ is fixed**; the result extends to debt issuance and
to risk aversion (slide 51).

**The substitution is the economics** (Amaro p. 100): "an increase in dividends is exactly
compensated by the issue of new equity, so that both effects cancel out". Amaro's (4.7) (p. 101)
shows the dividend view is the same number:
$V_t=\sum_\tau\frac{D_{t+\tau}}{(1+r)^\tau}-\sum_\tau\frac{m_{t+\tau}p_{t+\tau}}{(1+r)^\tau}$ —
dividends minus the PV of the equity raised to pay them.

## 3 · Worked — two textbook firms, every policy

**Ross's Wharton Corporation (§17.2, p. 588).** All-equity, 100 shares, cash flow 10,000 in each of
the next two years (then dissolved), required return 10%.

*Policy A — dividend = cash flow:* 100 per share each year.

$$P_0=\frac{100}{1.10}+\frac{100}{1.10^2}=90.909+82.645=173.55$$

*Policy B — 110 per share at date 1:* 11,000 paid against 10,000 earned, so 1,000 of new shares
are sold at date 1. The new holders require $1{,}000\times1.10=1{,}100$ at date 2, leaving
$10{,}000-1{,}100=8{,}900$ for the old shares, 89 per share:

$$P_0=\frac{110}{1.10}+\frac{89}{1.10^2}=100.000+73.554=173.55$$

**Homemade dividends** (p. 589): an investor who wanted 100 and 100 reinvests 10 of the 110 at 10%
and has $89+11=100$ at date 2; one who wanted 110 and 89 sells 10 of stock at date 1 and gives up
$10\times1.1=11$.

**Berk's Genron (§17.2, pp. 503–507).** 20 million of excess cash, no debt, 10 million shares, FCF
48 million a year forever, $r_U=12\%$: enterprise value $48/0.12=400$, total value 420.

| Policy | Today | Each later year | Share price |
|---|---|---|---|
| 1 — pay the cash as a dividend | 2.00 | $48/10=4.80$ | cum $2+4.80/0.12=2+40=42$; ex 40 |
| 2 — repurchase $20/42=0.476$ m shares | 0 | $48/9.524=5.04$ | $5.04/0.12=42$ |
| 3 — issue $28/42=0.67$ m shares, pay 48 now | $48/10.67=4.50$ | 4.50 | $4.50+4.50/0.12=4.50+37.50=42$ |

**42 in every row** (Berk Table 17.1, p. 507). *"Although dividends do determine share prices, a
firm's choice of dividend policy does not"* (p. 508). Berk's two COMMON MISTAKE boxes are the
pitfalls: a repurchase does not raise the price "because supply falls" (assets fall too, p. 506),
and the **bird-in-the-hand** view that higher current dividends raise the price is wrong in perfect
markets (p. 508).

> **The one sentence.** A payout is a financial transaction: it moves value between the firm's
> cash and the shareholders' pockets, and between old and new shareholders at a fair price; only
> the investment plan $\{I_t\}$ — and frictions such as taxes (Berk §17.3) — can change $V$.

---

## Links

- Before: [[L03-04-static-trade-off]] (the private trade-off that the externality distorts);
  [[L03-01-tax-shield-mm-taxes]] (MM II with and without taxes).
- Topic 1 and 2A: [[../L01/L01-05-ratios-dupont-roic|L01 ROE and leverage]];
  [[../L02/L02-07-mm2-wacc-cost-of-debt|L02 MM II and WACC]].
- Rules: [[../../rules/03_benchmark_mm|rules/03]] (MM3, Amaro p. 100).
- Practice: PS2 Ex. 1(f) ([PS2](../../Listas/PS2.pdf), p. 1: a debt-financed dividend in a no-tax
  world); [[../../Listas/lista-r3-mm-taxes-tradeoff|Lista R3]] Ex. 2 (Berk 17.7, p. 528);
  quiz block `pol` of [[../../Simulados/quiz-topic2b-taxes-tradeoff-2026-10-24|quiz Topic 2B]].
- Code: [[L03-08-python]] §4 (the recursion (5) checked on random payout policies).
