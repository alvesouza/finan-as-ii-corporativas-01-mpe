---
tags: [notes, lecture-02, mm-benchmark, mm1, arbitrage, homemade-leverage, put-call-parity]
date: 2026-10-24
status: taught
source: "Topic 2A slides 82–96 (2A.8); Amaro de Matos Ch. 2 §2.1.1 (pp. 41–42, Prop. 2.1.1 MM1, eq. 2.3); Tirole Ch. 2 §2.2 (p. 78); Ross Fundamentos 9e Cap. 16 §16.2 (pp. 543, 545–546, 'alavancagem caseira'), §16.3 (p. 547); Berk Fundamentals 2e Ch. 16 §16.2 (pp. 466–469, MM Proposition I eq. 16.1, homemade leverage). Examples: the slides' arbitrage tables (87, 89) and portfolios (95–96); numbers on the entrepreneur economy built here."
---

# 2A.8 · MM I: the arbitrage proof, homemade leverage, and put–call parity

> **Claim.** In a frictionless economy the value of a firm does not depend on its capital
> structure (MM I). Proof by contradiction: if two firms with the same assets but different
> financing had different values, an investor could sell the dear one, rebuild it from the cheap
> one's securities — **undoing** or **creating** leverage on personal account — and pocket the
> difference. With risky debt the same fact is **put–call parity**: equity is a call, debt is a
> safe bond minus a put, and call + bond − put is the asset, whatever the strike.

Prev: [[L02-05-entrepreneur-example]] · Next: [[L02-07-mm2-wacc-cost-of-debt]] · Map: [[L02-00-map]]

**Notation.**

| Symbol | Meaning | Range |
|---|---|---|
| $X$ | random liquidating payoff of each firm at $t=1$ (e.g. resale value) | $>0$ |
| $E_1,D_1$; $V_1=D_1+E_1$ | firm 1: equity, **safe** debt, total value | $>0$ |
| $E_2$; $V_2=E_2$ | firm 2: all equity, total value | $>0$ |
| $R_f=1+r_f$ | gross risk-free rate | $>0$ |
| $\alpha$ | fraction of a firm's securities traded by the arbitrageur | $(0,1]$ |
| $K$ | face value of (possibly risky) debt | $\ge0$ |
| $C(K),P(K)$ | prices of a call / put on $X$ with strike $K$ | $\ge0$ |
| $V(K)$ | firm value when debt has face $K$ | — |

---

## 1 · C — The statement (slides 82–85)

Assumptions: the six of [[L02-04-complete-markets-state-prices]] §1 (slide 82 repeats them).

> **MM I (slide 83).** *In a frictionless economy, total firm value is independent of the
> capital structure choice.*

Set-up (slides 84–85): firms 1 and 2 are identical except for financing; both pay $X$ at
$t=1$. Firm 1 has equity $E_1$ and safe debt $D_1$; firm 2 has no debt. $V_1=D_1+E_1$,
$V_2=E_2$. Goal: $V_1=V_2$. Complete markets let one go long or short each of $E_1,D_1,V_1,E_2,V_2$.

**Payoffs at $t=1$ (slide 86):** firm 1's debtholders get $R_fD_1$, its shareholders
$X-R_fD_1$; firm 2's shareholders get $X$.

---

## 2 · C — Safe debt: the two arbitrage steps (slides 86–89)

**Step 1 — suppose $V_2>V_1$.** Sell the overpriced, buy the underpriced, matching payoffs:

| Trade | Investment ($t=0$) | Payoff ($t=1$) |
|---|---|---|
| Short-sell $\alpha$ of firm 2's equity | $-\alpha V_2$ | $-\alpha X$ |
| Buy $\alpha V_2/V_1$ of firm 1's debt | $(\alpha V_2/V_1)D_1$ | $(\alpha V_2/V_1)R_fD_1$ |
| Buy $\alpha V_2/V_1$ of firm 1's equity | $(\alpha V_2/V_1)E_1$ | $(\alpha V_2/V_1)(X-R_fD_1)$ |

Total investment:

$$-\alpha V_2+\frac{\alpha V_2}{V_1}(D_1+E_1)=-\alpha V_2+\frac{\alpha V_2}{V_1}(V_1)=0\tag{6.1}$$

Total payoff — the $R_fD_1$ terms cancel:

$$-\alpha X+\frac{\alpha V_2}{V_1}R_fD_1+\frac{\alpha V_2}{V_1}(X-R_fD_1)=-\alpha X+\frac{\alpha V_2}{V_1}X=\alpha X\Bigl(\frac{V_2}{V_1}-1\Bigr)>0\tag{6.2}$$

A zero-cost portfolio paying a positive amount in every state: a **money machine**. Buying firm
1's debt **and** equity in proportion **undoes firm 1's leverage** (slide 88).

**Step 2 — suppose $V_1>V_2$.**

| Trade | Investment ($t=0$) | Payoff ($t=1$) |
|---|---|---|
| Buy $\alpha V_1/V_2$ of firm 2's equity | $(\alpha V_1/V_2)V_2=\alpha V_1$ | $(\alpha V_1/V_2)X$ |
| Borrow $\alpha D_1$ personally | $-\alpha D_1$ | $-\alpha R_fD_1$ |
| Short-sell $\alpha$ of firm 1's equity | $-\alpha E_1$ | $-\alpha(X-R_fD_1)$ |

$$\text{investment}=\alpha V_1-\alpha D_1-\alpha E_1=\alpha\bigl[V_1-(E_1+D_1)\bigr]=0\tag{6.3}$$
$$\text{payoff}=\frac{\alpha V_1}{V_2}X-\alpha R_fD_1-\alpha X+\alpha R_fD_1=\alpha X\Bigl(\frac{V_1}{V_2}-1\Bigr)>0\tag{6.4}$$

The arbitrageur **levers up firm 2 on personal account** — homemade leverage (slide 89). Both
steps fail only if $V_1=V_2$. $\blacksquare$

> **Which assumption carries the proof?** The personal loan in Step 2 must cost the same $R_f$
> as the firm's: assumption 2 of the benchmark. With a higher personal borrowing rate, Step 2's
> payoff falls by $\alpha D_1(R_f^{\text{personal}}-R_f)$ and a band of values $V_1>V_2$
> survives (lista-r3 #15 works this case). Short sales (completeness) carry Step 1.

**Numerical illustration (built here on the entrepreneur economy).** Firm 1: $D_1=1$ (safe,
repays $R_fD_1=1.05$), $E_1=0.75$, $V_1=1.75$; $X\in\{1.05,\ 3.15\}$. Suppose firm 2 traded at
$V_2=1.80$. Step 1 with $\alpha=0.1$: short $0.1$ of firm 2 ($+0.18$ today); buy
$0.1\times1.80/1.75=0.102857$ of firm 1's debt and equity, costing
$0.102857\times(1+0.75)=0.18$. Net cost 0; payoff by (6.2)
$0.1X(1.80/1.75-1)=0.002857X$: $0.0030$ in the slump, $0.0090$ in the boom.

*U-layer:* Ross' Transmadruga (pp. 543, 545–546) and Berk's coffee shop (p. 469) make the same
point for a single investor: whoever prefers the levered structure can borrow personally and buy
the unlevered shares (*"alavancagem caseira"*); Berk: *"homemade leverage is a perfect substitute
for the use of leverage by the firm"* when investors borrow at the firm's rate.

---

## 3 · C — Risky debt is a safe bond minus a put (slides 90–92)

With face $K$ and $P(X<K)>0$, debt pays $\min\{K,X\}$. Case by case:

$$X\ge K:\quad K-\max\{K-X,0\}=K-0=K=\min\{K,X\}$$
$$X<K:\quad K-\max\{K-X,0\}=K-(K-X)=X=\min\{K,X\}$$

$$\min\{K,X\}=\underbrace{K}_{\text{risk-free bond, face }K}-\underbrace{\max\{K-X,0\}}_{\text{put on the assets, strike }K}\tag{6.5}$$

By the law of one price:

$$D=\frac{K}{1+r_f}-P(K)\tag{6.6}$$

For safe debt every $X\ge K$, so $P(K)=0$ and $D=K/(1+r_f)$. $P(K)$ is the **price discount** of
risky debt relative to a riskless bond of the same face (slide 92).

---

## 4 · C — Equity is a call; parity gives MM I (slides 93–96)

Equity pays $\max\{X-K,0\}$, a call on $X$ with strike $K$, so

$$E=C(K)\tag{6.7}$$

Add (6.6) and (6.7):

$$V(K)=\underbrace{C(K)}_{=E}+\underbrace{\frac{K}{1+r_f}-P(K)}_{=D}\tag{6.8}$$

**Why (6.8) does not depend on $K$ (slides 95–96).** For any strike, the portfolio "buy the call,
write the put, buy a bond of face $K$" pays:

| | Investment | $X<K$ | $X\ge K$ |
|---|---|---|---|
| Buy call, strike $K$ | $C(K)$ | 0 | $X-K$ |
| Write put, strike $K$ | $-P(K)$ | $-(K-X)$ | 0 |
| Buy bond, face $K$ | $K/(1+r_f)$ | $K$ | $K$ |
| **Total** | $V(K)$ | $X$ | $X$ |

Every column sums to $X$. Two portfolios with strikes $K_1,K_2$ both pay $X$, so by no arbitrage
$V(K_1)=V(K_2)$: **put–call parity is MM I with risky debt.**

**Worked check in the entrepreneur economy** ($p_1=1/2.8$ boom, $p_2=1/1.05-1/2.8$ slump,
$X\in\{1.05,3.15\}$, $1/(1+r_f)=p_1+p_2=0.952381$):

| | $K=1.05$ (safe) | $K=2.1$ (risky) |
|---|---|---|
| $C(K)=p_1\max(3.15-K,0)+p_2\max(1.05-K,0)$ | $0.357143\times2.1=0.75$ | $0.357143\times1.05=0.375$ |
| $K/(1+r_f)$ | $1.05\times0.952381=1.00$ | $2.1\times0.952381=2.00$ |
| $P(K)=p_1\max(K-3.15,0)+p_2\max(K-1.05,0)$ | 0 | $0.595238\times1.05=0.625$ |
| $D$ by (6.6) | $1.00-0=1.00$ | $2.00-0.625=1.375$ |
| $V(K)$ by (6.8) | $0.75+1.00-0=1.75$ | $0.375+2.00-0.625=1.75$ |

> **Interactive companion.** [The State-Price Balance Sheet](companions/companion-mm-state-prices.html)
> — the dashed box under the panels prints call + bond − put at the current $F$; drag $F$ from 0
> to 5 and the total stays at $A$.

---

## 5 · G — The state-price proof in one line (Amaro de Matos pp. 41–42)

With payoffs $V_j(T)$ in state $j$ and a strictly positive state-price vector $\psi$:
$B_j(T)=\min\{F,V_j(T)\}$, $S_j(T)=\max[0,V_j(T)-F]$, and

$$V_l=S+B=\sum_j\psi_j\bigl[B_j(T)+S_j(T)\bigr]=\sum_j\psi_jV_j(T)=V_u$$

— **Proposition 2.1.1 (MM1):** *"The market value of any firm is independent of its capital
structure,"* $V_l=V_u$ (eq. 2.3). Amaro de Matos notes it also means equity can be withdrawn for
consumption and replaced by debt *"without any side effect on the total value of the firm"*
(p. 42). Tirole (p. 78) proves it with risk-neutral expectations and adds the policy corollary:
the financial structure is irrelevant, and so is payout policy.

---

## Links

- The example that the proof generalises → [[L02-05-entrepreneur-example]]; the consequence for
  the cost of capital → [[L02-07-mm2-wacc-cost-of-debt]].
- Payoff shapes (3.1)–(3.4) → [[L02-03-debt-vs-equity-claims]].
- MM I with taxes, $V_L=V_U+\tau D$ → [[../L03/L03-00-map|L03]].
- Rules: [[../../rules/03_benchmark_mm|rules/03 — MM benchmark]].
- Python: `arbitrage_step1`, `put_call_value` with asserts → [[L02-10-python]].
- **Practice.** PS2 Ex. 1(b–d) (call and put prices on the project, the parity identity;
  [PS2](../../Listas/PS2.pdf) p. 1); [lista-r3](../../Listas/lista-r3-mm-taxes-tradeoff.md)
  #7 (Ross Cap. 16 Ex. 18, p. 578), #11 (Grinblatt–Titman Ex. 14.2–14.3, pp. 526–527),
  #15 (Amaro 2.1.5 #3–#4, p. 48).
