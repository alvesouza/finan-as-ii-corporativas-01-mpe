---
tags: [notes, lecture-02, mm-benchmark, complete-markets, state-prices, arbitrage]
date: 2026-10-24
status: taught
source: "Topic 2A slides 46–54 (2A.6); Amaro de Matos Ch. 1 §1.2.1–1.2.4 (pp. 18, 21–25; Prop. 1.2.1 p. 22; eqs. 1.12–1.14); Tirole Ch. 2 §2.2 (p. 78, notes 8–9). Example: stock 2 → (1.9, 2.4), bond 1 → 1.05 (slides 52–54)."
---

# 2A.6 · The frictionless benchmark, contingent claims and state prices

> **Claim.** The benchmark's assumptions are chosen so that **a security is nothing but its
> payoff vector.** In a complete market every payoff vector can be built from traded securities,
> and no arbitrage then forces one **positive price per state**. Any asset's price is its payoffs
> times those state prices — a linear rule. Every later MM result is this linearity applied to
> debt and equity.

Prev: [[L02-03-debt-vs-equity-claims]] · Next: [[L02-05-entrepreneur-example]] · Map: [[L02-00-map]]

**Notation.**

| Symbol | Meaning | Range |
|---|---|---|
| $s\in S=\{s_1,\dots,s_N\}$ | states of the world at $t=1$ | $N$ finite |
| $cc_s$ | contingent claim: pays 1 in state $s$, 0 otherwise | — |
| $p_s$ | price at $t=0$ of $cc_s$ (state price) | $>0$ |
| $x,y$ | units of stock and bond in a replicating portfolio | $\mathbb{R}$ (short allowed) |
| $S_0,B_0$ | prices of the stock and the bond | $>0$ |
| $\pi_s=p_s/\sum_k p_k$ | risk-neutral probability of state $s$ | $(0,1)$ |
| $q_s$ | true probability of state $s$ | $(0,1)$ |

---

## 1 · C — The strong assumptions (slides 46–47, repeated on 82)

In a frictionless benchmark the capital structure is irrelevant (MM). The assumptions:

1. **Competitive and complete markets**: price-takers; the cash flow of any (new) security can be
   replicated by existing ones.
2. Individuals and firms trade **at the same prices** (e.g. borrow at the same rate).
3. **No taxes, bankruptcy or other transaction costs.**
4. **Financing neither affects the assets' cash flows nor conveys information.**
5. **Fixed (exogenous) operating cash flow** — investment is given.
6. **Symmetric information.**

> **What each one buys.** (1) makes every claim priceable by replication; (2) makes homemade
> leverage a perfect substitute for corporate leverage; (3) keeps the total payoff the same for
> every split; (4)–(5) keep the "pie" fixed while it is sliced; (6) lets outsiders price new claims
> correctly. Relaxing (3) gives [[../L03/L03-00-map|L03]]; relaxing (4)–(6) gives the agency and
> asymmetric-information topics.

---

## 2 · C — States, contingent claims, completeness, no arbitrage (slides 48–51)

A **state** is a scenario for tomorrow ($\{\text{sun},\text{rain}\}$; GDP growth
$\{-3\%,0\%,+3\%\}$). A **contingent claim** $cc_s$ pays 1 in state $s$ and 0 otherwise; with
three states the three claims are the rows of the identity matrix (slide 49).

- **Complete market:** every $cc_s$ can be **synthesised** by buying and short-selling traded
  securities — the claims need not trade themselves (slide 50). Amaro de Matos (p. 21): a unique
  replicating portfolio exists for every payoff iff the number of securities with linearly
  independent payoffs equals the number of states, $N=K$.
- **Law of one price:** assets or portfolios with the same payoff trade at the same price.
- **Arbitrage** (slide 51): a *free lunch* — positive cash today, no obligation tomorrow; or a
  *money machine* — zero cost today, a payoff $\ge0$ in every state and $>0$ with positive
  probability. It cannot survive if a single rational investor prefers more to less.

---

## 3 · C — Worked example: state prices from a stock and a bond (slides 52–54)

| | Price $t=0$ | Slump | Boom |
|---|---|---|---|
| Stock | 2 | 1.9 | 2.4 |
| Bond | 1 | 1.05 | 1.05 |

A portfolio of $x$ stocks and $y$ bonds pays $1.9x+1.05y$ (slump) and $2.4x+1.05y$ (boom) and
costs $2x+y$.

**$cc_1$ (boom claim): pay $(0,1)$.**

$$1.9x+1.05y=0\tag{4.1}$$
$$2.4x+1.05y=1\tag{4.2}$$

Subtract (4.1) from (4.2): $0.5x=1$, so $x=2$. Substitute into (4.1):
$1.9(2)+1.05y=0$, so $y=-3.8/1.05$ (short 3.8/1.05 bonds). By the law of one price,

$$p_1=2x+y=2(2)+\Bigl(-\frac{3.8}{1.05}\Bigr)=4-3.6190=0.381\tag{4.3}$$

**$cc_2$ (slump claim): pay $(1,0)$.**

$$1.9x+1.05y=1,\qquad 2.4x+1.05y=0$$

Subtracting: $-0.5x=1$, so $x=-2$; then $2.4(-2)+1.05y=0$, so $y=4.8/1.05$:

$$p_2=2(-2)+\frac{4.8}{1.05}=-4+4.5714=0.571\tag{4.4}$$

**Check: the bond.** A riskless payoff of 1.05 in both states is $1.05\,cc_1+1.05\,cc_2$:
$1.05(0.380952+0.571429)=1.05\times0.952381=1.000$. So $p_1+p_2=1/1.05$, the price of a sure
unit, and $r_f=5\%$.

**Any asset (slide 54).** An asset paying $x$ in the slump and $y$ in the boom is $y$ units of
$cc_1$ plus $x$ units of $cc_2$:

$$\text{price}=0.381\,y+0.571\,x\tag{4.5}$$

> **The price operator is linear in payoffs.** (4.5) is the whole content of complete markets
> plus no arbitrage; MM I is (4.5) applied to $\min(\tilde A,F)+\max(\tilde A-F,0)=\tilde A$.

---

## 4 · U — Why state prices are not probabilities

The two states may be equally likely, yet $p_2>p_1$: a unit in the slump costs more. Slide 67
gives the reason in the next example: risk-averse agents' marginal utility is higher when they
are poorer, so they pay more for consumption in bad times.

Normalising the state prices gives **risk-neutral probabilities** (Amaro de Matos eq. 1.13, p. 24):

$$\pi_s=\frac{p_s}{\sum_k p_k},\qquad \text{price}=\frac{1}{1+r_f}\sum_s\pi_s\,\text{payoff}_s\tag{4.6}$$

Here $p_1=0.4/1.05$ and $p_2=0.6/1.05$ exactly (from (4.3): $4-3.8/1.05=(4.2-3.8)/1.05$), so
$\pi_{\text{boom}}=0.4$ and $\pi_{\text{slump}}=0.6$: the bad state is over-weighted relative to
any "true" 50/50. Amaro de Matos (p. 25) stresses that $\pi$ *"does not necessarily correspond
to the vector of real probabilities"*; with the true ones, one discounts at a risk-adjusted rate
instead, or weights by the **state-price deflator** $\delta_j=p_j/q_j$, the ratio of marginal
utilities (p. 25).

---

## 5 · G — The theorems behind the example

- **Proposition 1.2.1 (Amaro de Matos, p. 22):** absence of arbitrage is equivalent to the
  existence of a strictly positive state-price vector with $V=\Phi\psi$ (Farkas' lemma).
- **Uniqueness** needs completeness: then $\psi=\Phi^{-1}V$ (p. 23). With $N<K$ several state-price
  vectors price the traded assets, and a new payoff can have a range of no-arbitrage values (p. 24).
- **§1.2.3 (p. 23):** with complete markets and no arbitrage, every *financial* investment has
  zero NPV — positive NPV can only come from real projects whose payoffs are not yet spanned at
  their cost, the "arbitrage across the firm's boundary" of [[L02-02-cash-flows-npv-irr]] §3.

---

## Links

- The same machinery on the entrepreneur's firm → [[L02-05-entrepreneur-example]]; on any capital
  structure → [[L02-06-mm1-arbitrage-put-call]].
- Rules: [[../../rules/03_benchmark_mm|rules/03 — MM benchmark]].
- Interactive: [The State-Price Balance Sheet](companions/companion-mm-state-prices.html) — set
  $p_b$, $p_s$ and read $r_f=1/(p_b+p_s)-1$ and every value.
- Python: `state_prices` (solves (4.1)–(4.2) for any two securities) in [[L02-10-python]].
- **Practice.** PS2 Ex. 1(a) (state prices in a complete two-state economy;
  [PS2](../../Listas/PS2.pdf) p. 1); [lista-r2](../../Listas/lista-r2-valuation.md) #14 (Amaro
  1.2.6 #5, p. 28) and #15 (Amaro 1.2.6 #4, p. 28).
