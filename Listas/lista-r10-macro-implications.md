---
tags: [exercise-list, ricca-r10, macro-implications, credit-rationing, asset-values, aggregate-liquidity, political-economy]
date: 2026-11-12
---

# Exercise list R10 — Macroeconomic implications of corporate-finance frictions

Course topic 9 (ementário): what credit rationing does to the whole economy — the market rate of interest and the balance-sheet channel, wealth dynamics and poverty traps, investment's response to output prices, the equilibrium value of specialized assets (Shleifer–Vishny), the supply of and demand for aggregate liquidity, and the international and political-economy side (borrowing abroad, time-consistent public policy, exchange-rate policy, the soft budget constraint). Tirole Ch. 13–16 are the only course chapters on this material. This list holds **15 real exercises**: every end-of-chapter exercise of Ch. 13, 14, 15 and 16 except 14.2 and 14.3 (they belong to the M&A list), plus Review Problems 5 and 6 of Part VII, which work the Ch. 16 and Ch. 15 models. Review Problem 1 is left out: it is 26 knowledge questions across the whole book, with no answer in the book. Because the pool is the whole set, the tiers are relative: Tier 1 = one market-clearing condition or one constraint to rewrite; Tier 3 = general-equilibrium or multi-period problems. Statements are copied verbatim from the book for personal study; pages are printed, with the PDF page in brackets. Every model a statement invokes is copied under **Context needed to solve it**. Links: [[Map/exercises-index|exercise index]] · [[rules/09_implicacoes_macro|rules]].

| Topic block | Exercises |
|---|---|
| Credit rationing and the interest rate; balance-sheet channel (Tirole §13.2, §13.5) | 1, 11 |
| Wealth dynamics, poverty traps (Tirole §13.4) | 14 |
| Equilibrium value of specialized assets, resale markets (Tirole §14.2) | 6, 7 |
| Aggregate liquidity: inside vs. outside liquidity, liquidity premium (Tirole Ch. 15) | 3, 8, 10, 12, 13 |
| International finance and political economy (Tirole Ch. 16) | 2, 4, 5, 9, 15 |

## References

| # | Tier | Book | Ch. | Exercise | Printed p. (PDF) | Answer in book | Trains |
|---|---|---|---|---|---|---|---|
| 1 | Easy | Tirole | Ch. 13 | 13.1 | 493 (506) | yes, pp. 616–617 | Market rate of interest from loanable-funds clearing with a wealth cutoff $A^*(r)$; better investor protection raises $r$ |
| 2 | Easy | Tirole | Ch. 16 | 16.2 | 564–565 (577) | yes, p. 622 | Time-consistent vs. committed public policy: $\gamma'(\tau^*) = R$ ex post vs. a higher $\tau$ under commitment |
| 3 | Easy | Tirole | Ch. 15 | 15.3 | 532 (545) | yes, p. 621 | Imperfectly correlated liquidity shocks: the corporate sector is self-sufficient iff $\theta \leqslant \theta^*$ |
| 4 | Easy | Tirole | Part VII | Review Problem 5 | 628–629 (641) | yes, p. 635 | Ex post taxation of investor income and foreign finance: $B_0'(t^*) = \theta^*$; value of commitment; discrimination |
| 5 | Easy | Tirole | Ch. 16 | 16.1 | 563–564 (576) | yes, p. 622 | Borrowing abroad: diversion as a private benefit; public debt overhang; time-inconsistent institutions; exchange rate and international collateral |
| 6 | Exam | Tirole | Ch. 14 | 14.1 | 515 (528) | no | Shleifer–Vishny with decreasing returns: the resale price falls with the buyer's own investment, so the investment externality can turn negative |
| 7 | Exam | Tirole | Ch. 14 | 14.4 | 516 (529) | yes, p. 619 | Optimal resale cutoff $\rho_0^* \in (\hat\rho_0 - \Delta\rho, \hat\rho_0)$: too few asset reallocations |
| 8 | Exam | Tirole | Part VII | Review Problem 6 | 629–630 (642) | yes, p. 635 | Inside liquidity: unit cost of preserved investment, shortage under correlated shocks, why the stock index wastes liquidity |
| 9 | Exam | Tirole | Ch. 16 | 16.4 | 566 (579) | no | Soft budget constraint: a time-inconsistent bailout makes firms hoard no liquidity |
| 10 | Exam | Tirole | Ch. 15 | 15.2 | 531–532 (544) | yes, pp. 620–621 | Continuation threshold $y^*$ as a function of net worth, need for date-0 liquidity, state-independent threshold under a macro shock |
| 11 | Exam | Tirole | Ch. 13 | 13.3 | 494 (507) | yes, pp. 617–618 | First- vs. second-best investment as functions of the output price; when credit rationing amplifies price responses |
| 12 | Really hard | Tirole | Ch. 15 | 15.1 | 530–531 (543) | yes, pp. 619–620 | Downsizing $J^* < I^*$ iff $\rho > 1/(1-\lambda)$; outside liquidity $L^*$ and liquidity premium; wasting liquidity with the stock index |
| 13 | Really hard | Tirole | Ch. 15 | 15.4 | 532 (545) | yes, p. 621 | Liquidity asset pricing when investment needs liquidity: liquid and illiquid assets are complements |
| 14 | Really hard | Tirole | Ch. 13 | 13.2 | 493–494 (506) | yes, p. 617 | Warm-glow dynasties, convergence of wealth, poverty traps, multiple steady states with an endogenous interest rate |
| 15 | Really hard | Tirole | Ch. 16 | 16.3 | 565–566 (578) | yes, p. 623 | Exchange-rate policy: under- vs. overspending of reserves with and without commitment; externality of nontradable debt |

## Tier 1 — Easy

### 1. Investor protection and the interest rate
**Source:** Tirole, Ch. 13, Exercise 13.1, p. 493 (PDF 506) · Answer in book: yes, pp. 616–617

**Exercise 13.1 (improved governance).** There are two dates, *t* = 0, 1, and a continuum of mass 1 of firms. Firms are identical except for the initial wealth $A$ initially owned by their entrepreneur. $A$ is distributed according to continuous cumulative distribution $G(A)$ with density $g(A)$ on $[0, I]$.

Each entrepreneur has a fixed-size project, and must invest $I$, and therefore borrow $I - A$, at date 0 in order to undertake it. Those entrepreneurs who do not invest themselves, invest their wealth in other firms. The savings function of nonentrepreneurs (consumers) is an increasing function $S(r)$, where $r$ is the interest rate, with $S(r) = 0$ for $r < 0$ (so total savings equal $S(r)$ plus the wealth of unfinanced entrepreneurs). Entrepreneurs have utility $c_0 + c_1$ from consumptions $c_0$ and $c_1$.

A project, if financed, yields $R > 0$ at date 1 with probability $p$ and 0 with probability $1 - p$. The probability of success is $p_H$ if the entrepreneur works and $p_L = p_H - \Delta p$ if she shirks. The entrepreneur obtains private benefit $B$ by shirking and 0 otherwise. Assume $p_H R > I > p_H(R - B/\Delta p)$, that financing cannot occur if the entrepreneur is provided with incentives to misbehave, and that the equilibrium interest rate is strictly positive.

(i) What is the pledgeable income? Write the financing condition.

(ii) Give the expression determining the market rate of interest. How does this interest rate change when improved investor protection lowers $B$?

#### Context needed to solve it

None: the statement is self-contained (it is the fixed-investment model of Tirole §3.2 with an endogenous interest rate, as in §13.2).

---

### 2. Time-consistent government policy
**Source:** Tirole, Ch. 16, Exercise 16.2, pp. 564–565 (PDF 577) · Answer in book: yes, p. 622

**Exercise 16.2 (time-consistent government policy).** Consider a unit mass of identical entrepreneurs with variable-investment projects. The timing is summarized in Figure 16.11.

Figure 16.11 (timeline, left to right; p. 564, PDF 577)

| Step 1 | Step 2 | Step 3 | Step 4 |
|---|---|---|---|
| Representative entrepreneur invests $I$, borrows $I - A$. | Government selects $\tau$. | Entrepreneurial moral hazard: behaves — Pr(success) $p_H + \tau$, private benefit 0; misbehaves — Pr(success) $p_L + \tau$, private benefit $BI$. | Outcome: $RI$ with probability $p + \tau$, 0 with probability $1 - (p + \tau)$. |

The cost of the policy for the country is $\gamma(\tau)I$ (where $\gamma'(0) = 0$, $\gamma'(\tau) > 0$, for $\tau > 0$, $\gamma'(1 - p_H) = \infty$, $\gamma'' > 0$).

All investors are domestic investors (there are no foreign lenders and, when choosing $\tau$, the government maximizes social welfare, equal to entrepreneurs' welfare plus investors' welfare).

Assume that

$$(p_H + \tau)R > 1 > (p_H + \tau)\left(R - \frac{B}{\Delta p}\right)$$

in the relevant range of values of $\tau$, and that it is never optimal to induce entrepreneurs to misbehave. Everyone is risk neutral, and the entrepreneurs are protected by limited liability.

(i) • Show that, when expecting policy $\tau$, entrepreneurs invest

$$I(\tau) = \frac{A}{1 - (p_H + \tau)(R - B/\Delta p)}.$$

• What is the equilibrium value $\tau^*$?

(ii) What value would the government choose if it selected $\tau$ *before* entrepreneurs borrow?

(iii) Informally explain how your answer to (i) would change if investors were foreign investors and the government discounted their welfare relative to that of domestic residents.

#### Context needed to solve it

None beyond Figure 16.11, transcribed above (the variable-investment model is restated in the statement).

---

### 3. Imperfectly correlated liquidity shocks
**Source:** Tirole, Ch. 15, Exercise 15.3, p. 532 (PDF 545) · Answer in book: yes, p. 621

**Exercise 15.3 (imperfectly correlated shocks).** This exercise extends the analysis of Section 15.3 to allow for imperfect correlation among the shocks faced by the firms. As in Section 15.3.1, there is a mass 1 of *ex ante* identical entrepreneurs. Each entrepreneur has a constant-returns-to-scale project. An investment of size $I$ at date 0 yields $\rho_1 I$ at date 2, of which $\rho_0 I$ is pledgeable, provided that the liquidity shock $\rho I$ is met at date 1. $\rho$ is equal to $\rho_L$ with probability $(1 - \lambda)$ and $\rho_H$ with probability $\lambda$, with $\rho_L < \rho_0 < \rho_H < \rho_1$ and $(1 - \lambda)(\rho_H - \rho_0) < 1$. As usual, entrepreneurs and investors are risk neutral, and the latter demand a rate of return equal to 0 (see Figure 15.11).

Figure 15.11 (timeline, left to right; p. 532, PDF 545)

| Date 0 | Date 1 | Date 1 → 2 | Date 2 |
|---|---|---|---|
| Representative entrepreneur borrows $I - A$, invests $I$. | Liquidity need $\rho I$ realized. Then either "Continue" or "Liquidate". | (If continue) Moral hazard. | Expected income $\rho_1 I$, of which $\rho_0 I$ is pledgeable. |

The new feature is that shocks are imperfectly correlated: for a fraction $1 - \theta$ of entrepreneurs, shocks are drawn independently ($\theta = 0$ in Section 15.2.1). A fraction $\theta$ of entrepreneurs face the same shock, $\rho_L$ with probability $(1 - \lambda)$ and $\rho_H$ with probability $\lambda$ ($\theta = 1$ in Section 15.3.1).

There is no outside store of value, and the long-term projects are the only investment projects available to the corporate sector.

Show that the private sector is self-sufficient (i.e., the efficient allocation can be implemented using the inside liquidity created by the long-term projects) if and only if $\theta \leqslant \theta^*$, where

$$(1 - \theta^*)(I - A) = \theta^*(\rho_H - \rho_0)I,$$

where $I$ is independent of $\theta$.

#### Context needed to solve it

*From Tirole §15.2.1 "The Sufficiency Result", pp. 518–520 (PDF 531–533):*

There are three periods, $t = 0, 1, 2$. Investors are risk neutral and the market rate of interest in the economy is 0. The economy is also populated by a large number—technically a continuum of mass 1—of ex ante identical, risk-neutral entrepreneurs. The representative entrepreneur at date 0 has wealth $A$, borrows $I - A$, and invests $I$. At date 1, a given firm faces liquidity shock $\rho I$, with

$$\rho = \begin{cases} \rho_L & \text{with probability } 1 - \lambda \text{ (healthy firm)},\\ \rho_H > \rho_L & \text{with probability } \lambda \text{ (firm in distress)}.\end{cases}$$

The firm can continue only if it finds funds to defray its liquidity shock; otherwise, it is liquidated. We normalize the liquidation value at 0.

In the case of continuation, the firm's date-2 expected income is denoted by $\rho_1 I$, of which only $\rho_0 I < \rho_1 I$ is pledgeable to investors (see Figure 15.1, identical to Figure 15.11 above).³

Let us assume that

$$\rho_L < \rho_0 < \rho_H < \rho_1 \qquad (15.1)$$

and

$$(1 - \lambda)(\rho_H - \rho_L) < 1. \qquad (15.2)$$

[…] Let us in a first step ignore this difficulty […] and assume that somehow investors can commit to any probability $x$ in $[0, 1]$ of continuation in the adverse state of nature and that they do not demand an extra return for this (that is, they just want to recoup the extra loss $x(\rho_H - \rho_0)I$ induced by continuation in that state). […]

The investors' outlay at date 0 is equal to $I - A$, their expected outlay at date 1 is $((1 - \lambda)\rho_L + \lambda\rho_H x)I$, and their expected income is $(1 - \lambda + \lambda x)\rho_0 I$. Hence, the investors' breakeven constraint is

$$[1 + (1 - \lambda)\rho_L + \lambda\rho_H x]I - A \leqslant [1 - \lambda + \lambda x]\rho_0 I.$$

The efficient allocation is defined as the one that maximizes the representative entrepreneur's utility subject to the constraint that investors break even at their IMRS. […] This efficient allocation solves

$$\max_{\{I, x\}} \{(1 - \lambda + \lambda x)(\rho_1 - \rho_0)I\} \quad \text{s.t.} \quad [1 + (1 - \lambda)\rho_L + \lambda\rho_H x]I - A \leqslant [1 - \lambda + \lambda x]\rho_0 I.$$

[…] the unit cost of effective investment is

$$c(x) \equiv \frac{1 + (1 - \lambda)\rho_L + \lambda\rho_H x}{1 - \lambda + \lambda x}.$$

The program yielding the efficient allocation becomes $\max_{\{x\}} \left\{\dfrac{(\rho_1 - \rho_0)A}{c(x) - \rho_0}\right\}$. The optimal $x$ must therefore minimize $c(x)$, which, together with condition (15.2), implies that $x = 1$.

Let us now write the investors' breakeven constraint for the policy of never liquidating:

$$[(1 - \lambda)(\rho_0 - \rho_L) + \lambda(\rho_0 - \rho_H)]I = I - A \quad\text{or}\quad (\rho_0 - \bar\rho)I = I - A,$$

where $\bar\rho \equiv (1 - \lambda)\rho_L + \lambda\rho_H$ is the expected liquidity shock per unit of investment. Lastly, we assume that $\rho_1 > 1 + \bar\rho$ […]. To sum up, the efficient allocation is given by

$$x = 1 \quad\text{and}\quad I = \frac{A}{(1 + \bar\rho) - \rho_0}.$$

*15.2.1.3 The Sufficiency Result.* Next we assume that investors cannot pledge their future earnings and therefore cannot directly commit to reinject cash at date 1 in the firm when they lose money on this reinjection ($\rho_H > \rho_0$); we ask whether the efficient allocation can nevertheless be implemented.

Assume that the shocks are drawn independently across firms, and so there is no macroeconomic uncertainty. Because the corporate sector is a net borrower, $I - A > 0$, the investors' breakeven condition implies that investors' profit in the healthy firms (those facing a low shock at date 1) more than offsets the loss that they incur in the others:

$$(1 - \lambda)(\rho_0 - \rho_L) > \lambda(\rho_H - \rho_0). \qquad (15.3)$$

We can define (gross) inside liquidity as the value, $(1 - \lambda)(\rho_0 - \rho_L)I$, of healthy firms. Condition (15.3) states that the (gross) inside liquidity exceeds the net refinancing need, $\lambda(\rho_H - \rho_0)I$, of firms facing a high liquidity shock […].

*From Tirole footnote 3, p. 519 (PDF 532):* The wedge between date-2 value and pledgeable income can, as in Chapter 5, be motivated by moral-hazard considerations: […] $\rho_1 \equiv p_H R$ and $\rho_0 = p_H[R - B/\Delta p]$.

*From Tirole §15.3.1 "Aggregate Shocks and the Value of Outside Liquidity", p. 523 (PDF 536):*

Suppose now that liquidity shocks are perfectly correlated across firms in the model of Section 15.2 […]. In this polar case, and in the absence of outside liquidity, firms cannot continue when $\rho = \rho_H > \rho_0$: $x = 0$. […] Because all firms are valueless in the bad state of nature, distressed firms cannot meet liquidity shocks by selling (even indirectly through a financial intermediary) shares in healthy ones.

---

### 4. Property-rights institutions and international finance
**Source:** Tirole, Part VII, Review Problem 5, pp. 628–629 (PDF 641) · Answer in book: yes, p. 635

**Review Problem 5 (property rights institutions and international finance).** Consider a country with a continuum of identical firms (of mass 1). The representative firm is described as in Section 3.4. That is, it has initial wealth $A$ and has a variable-investment project. As usual, let

$$\rho_0 \equiv p_H\left(R - \frac{B}{\Delta p}\right) < 1 < \rho_1 \equiv p_H R.$$

To finance their investment, the domestic firms must borrow from domestic residents and from foreign investors. Domestic residents have limited savings $S_D < \rho_0 A/(1 - \rho_0)$. Foreign investors have unlimited amounts of money to lend at the market rate of return. The rate of return demanded by foreigners and domestic residents is 0.

After the financing has been secured, the country's government chooses a tax rate $t \geqslant 0$ on income received by *investors*. This tax rate does not apply to the entrepreneurs and does not discriminate between domestic and foreign investors.

To close the model, assume that the government transforms tax proceeds $t\mathcal{I}$ (for an amount of investor income $\mathcal{I}$) into $B_0(t)\mathcal{I}$, where

$$B_0' > 0, \quad B_0'' < 0, \quad\text{and}\quad B_0'(0) = 1.$$

(That is, tax collection is wasteful here.) Assume that these benefits $B_0(t)\mathcal{I}$ are returned to entrepreneurs in proportion to the tax income collected. Thus the representative entrepreneur's equilibrium NPV is

$$(\rho_1 - 1)I - t^*\rho_0 I + B_0(t^*)\rho_0 I.$$

The government maximizes the sum of the welfares of the entrepreneurs and of the domestic investors, and puts no weight on foreign investors (see Figure 1).

Figure 1 (timeline, left to right; p. 629, PDF 642)

| Step 1 | Step 2 | Step 3 | Step 4 |
|---|---|---|---|
| Financing: $S_D$ by domestic investors, $I - A - S_D$ by foreign investors. | Moral hazard. | Government sets tax rate $t$. | Incomes accrues. Returns paid to investors. Taxes paid to government. |

(i) Solve for a rational expectation equilibrium $(I^*, t^*, \theta^*)$, where $I^*$ is the representative entrepreneur's investment, $t^*$ is the equilibrium tax rate, and $\theta^*$, equal to $S_D/(I^* - A)$, is the fraction of external financing brought by domestic residents.

(ii) How does the entrepreneur's welfare change with domestic savings $S_D$?

(iii) What tax rate would prevail if the government were able to commit on the tax rate before the financing stage?

(iv) How would your answer to question (i) change if the government were still unable to commit to a tax rate and furthermore could discriminate between domestic and foreign investors?

#### Context needed to solve it

*From Tirole §3.4.1 "The Continuous-Investment Model", p. 127 (PDF 140):*

[…] we now assume that there are constant returns to scale in the investment technology. An investment $I \in [0, \infty)$ yields income $RI$, proportional to $I$, in the case of success, and 0 in the case of failure. The borrower's private benefit from misbehaving is also taken to be proportional to investment. As before, the borrower has a choice between behaving, in which case she derives no private benefit and the probability of success is $p_H$, and misbehaving, that is, enjoying private benefit $BI$, and reducing the probability of success to $p_L = p_H - \Delta p < p_H$. […]

The borrower initially has cash $A$, and must therefore borrow $I - A$ to finance a project of size $I$. A loan agreement specifies that the lenders (who as before are assumed to make no profit) and the borrower receive 0 each in the case of failure, and $R_l$ and $R_b$, respectively, in the case of success, where $R_l + R_b = RI$.

As in Section 3.2, we assume that investment has positive NPV (net present value), here per unit of investment, if the borrower behaves,

$$p_H R > 1, \qquad (3.7)$$

but negative NPV otherwise,

$$1 > p_L R + B, \qquad (3.8)$$

so that unless one can control the agency problem the investment cannot be funded. We also make an assumption that guarantees that the equilibrium investment is finite:

$$p_H R < 1 + \frac{p_H B}{\Delta p}. \qquad (3.9)$$

*From Tirole §3.4.2 "The Lenders' Credit Analysis", pp. 127–128 (PDF 140–141):*

Following the steps of Section 3.2, the incentive compatibility and the breakeven conditions are

$$(\Delta p)R_b \geqslant BI \qquad (IC_b)$$

and

$$p_H(RI - R_b) \geqslant I - A. \qquad (IR_l)$$

In equilibrium, competitive lenders make no profit on the contract that is most advantageous for the borrower; the borrower's net utility is therefore equal to the social surplus brought about by the investment:

$$U_b = (p_H R - 1)I. \qquad (3.10)$$

From (3.10) it is optimal for the borrower to invest as much as possible. […] Substituting $(IC_b)$ into $(IR_l)$, we obtain

$$I \leqslant kA, \qquad (3.11)$$

where

$$k = \frac{1}{1 - p_H(R - B/\Delta p)} > 1. \qquad (3.12)$$

---

### 5. Borrowing abroad
**Source:** Tirole, Ch. 16, Exercise 16.1, pp. 563–564 (PDF 576) · Answer in book: yes, p. 622

**Exercise 16.1 (borrowing abroad).** Consider a small country with a mass 1 of identical entrepreneurs. There is a single (tradable) good. The representative entrepreneur has initial wealth $A$ and a variable-investment constant-returns-to-scale project. A project of size $I \in [0, \infty)$ at date 1 yields at date 2 verifiable revenue $RI$ with probability $p$ and 0 with probability $1 - p$. The probability $p$ is not subject to moral hazard. There is moral hazard, though: instead of investing $I$ in the firm, the entrepreneur can invest it abroad and get private return $\mu I$, where $\mu < 1$. The investors are unable to seize the return from this alternative investment. Everyone is risk neutral, has discount factor 1 (i.e., has utility equal to the undiscounted sum of consumptions at dates 1 and 2), and the entrepreneur is protected by limited liability.

One will assume that

$$pR > 1 > pR - \mu.$$

(i) Compute the representative entrepreneur's borrowing capacity and utility. Show that the outcome is the same as in a situation in which the entrepreneur cannot divert funds and invest them abroad, but can enjoy a private benefit per unit of investment $B = \mu$. Explain why.

(ii) Adopt the convention that the payment to investors, $R_l$, is a debt payment. Suppose that the entrepreneurs' projects are independent and that the government imposes a per-unit-of-income tax on successful projects and offers a guarantee/compensation $\sigma$ on private debt (so $\tau RI$ is the tax on successful projects and $\sigma R_l$ is the investors' payoff in the case of bankruptcy). Show that the borrowing capacity and entrepreneur utility are the same as in (i).

In contrast, compute the impact on entrepreneurs when the government starts at date 1 with an inherited public debt outstanding to foreign lenders equal to $D$ ($\leqslant A$) per entrepreneur and must finance it through an income tax on successful projects.

(iii) Coming back to question (i), suppose that the government can through its governance institutions or other policies affect the return $\mu$ on investments abroad. There are two levels $\mu_L < \mu_H$ (where both levels satisfy the conditions in (i)). The choice between the two levels involves no cost (but affects behavior!). The government's objective function is to maximize the representative entrepreneur's welfare.

Assuming that all borrowing is foreign borrowing, what is the representative entrepreneur's utility when

(a) the government can commit to $\mu$ before foreign investors invest;

(b) the government chooses $\mu$ after they have invested (but before the entrepreneurs select their action)?

(iv) Suppose now that the output $RI$ (in the case of success) is in terms of a nontradable good (but the endowment $A$ and the investment $I$ are in tradable goods). Another sector of the economy (the "export sector") will receive $\mathcal{R}$ in tradable goods at date 2. All domestic agents have utility from date-2 consumptions $c$ and $c^*$ of nontradable and tradable goods equal to $c + c^*$ (so the two goods are perfect substitutes for domestic residents, while foreigners consume only the tradable good). Define the date-2 exchange rate $e \geqslant 1$ as the price of tradables in terms of nontradables. Compute the borrowing capacity and the exchange rate. (One will, for example, assume that funds fraudulently invested abroad cannot be reimported and must be consumed abroad. So they yield $\mu$ rather than $e\mu$.)

#### Context needed to solve it

None: the statement is self-contained. For the comparison in (i), the basic model is the one copied in exercise 4 above (Tirole §3.4: $(\Delta p)R_b \geqslant BI$, $p_H(RI - R_b) \geqslant I - A$, $I \leqslant A/[1 - p_H(R - B/\Delta p)]$, $U_b = (p_H R - 1)I$).

---

## Tier 2 — Exam level

### 6. Shleifer–Vishny with decreasing returns to scale
**Source:** Tirole, Ch. 14, Exercise 14.1, p. 515 (PDF 528) · Answer in book: no

**Exercise 14.1 (investment externalities in an industry with decreasing returns to scale).** Suppose that the entrepreneur's limited attention, say, induces decreasing returns to scale. Income in the case of success is $R(I)$, where $R' > 0$, $R'' < 0$, $R'(0) = \infty$, $R'(\infty) = 0$. Redo the analysis of the Schleifer–Vishny model with this modification, and determine the sign of the investment externality.

#### Context needed to solve it

*From Tirole §14.2.2 "Industry-Wide Shocks and Distress Sales: The Shleifer–Vishny Model", pp. 500–503 (PDF 513–516):*

This subsection, building on Shleifer and Vishny (1992), endogenizes the resale price in the two-firm, continuous-investment version of the model of Section 4.3.1. Let us restate the key ingredients of this model.

*Investment and redeployability.* There are two firms in the industry. The "industry" is here defined as a group of symmetric firms using the same equipment/assets. For simplicity, we assume that the two firms do not compete in the same product market (see below for a discussion of this hypothesis). Each firm is run by an entrepreneur, who has initial cash $A_i$.

Initially, firm $i$ invests $I_i$, and therefore borrows $I_i - A_i$ from some ex ante competitive lender ("lender $i$"). Then, there is a costless "learning period." At the end of the learning period, each firm learns whether it is "productive" (which has probability $x$), or "unproductive," i.e., "in distress" (which has probability $1 - x$). Being unproductive means that the firm will always be unsuccessful regardless of whether the entrepreneur behaves. For example, there may be no demand for the firm's output. Its assets are then useless if left in place. A productive firm is described as in the variable-investment model of Section 3.4 (which, incidentally, corresponds to the case $x = 1$).

If both firms are productive, each manages its initial investment. Firm $i$'s profit is either 0 or $RI_i$. Borrower $i$'s private benefit is 0 (if she behaves) or $BI_i$ (if she does not). The associated probabilities of success are $p_H$ and $p_L$, respectively.

If firm $j$ is in distress, it sells its assets, which now have no internal use.¹⁰ We assume that potential buyers outside the industry do not have the knowledge to operate these assets. Only firm $i$ (if it itself is not in distress) can buy it. There has been no initial contract that would specify the transfer price in the case of distress. Rather, this transfer price is determined through bargaining after distress occurs. We will later determine the per-unit transfer price $P$. The entrepreneur in firm $i$ then manages $(I_1 + I_2)$ units of assets, and obtains private benefit 0 (if she behaves) or $B(I_1 + I_2)$ (if she does not). Similarly, the income is either 0 or $R(I_1 + I_2)$. Probabilities of success are $p_H$ if the entrepreneur behaves and $p_L$ if she does not. Firm $i$ has just grown bigger through the acquisition.

As usual, we assume that in the absence of adverse shock ($x = 1$), projects are viable only if the borrower behaves,

$$\rho_1 \equiv p_H R > 1 > p_L R + B, \qquad (14.1)$$

and we make a further assumption guaranteeing that loans are finite (even for $x$ close to 1):

$$p_H R < 1 + \frac{p_H B}{\Delta p} \quad\text{or}\quad \rho_0 \equiv p_H\left(R - \frac{B}{\Delta p}\right) < 1. \qquad (14.2)$$

*Loan agreements.* Lender $i$ and entrepreneur $i$ secretly sign at the start a loan agreement specifying the amount of the loan $I_i - A_i$ and the stake $R_{bi}$ of entrepreneur $i$ in the case of success (in the absence of purchase of firm $j$'s assets). […]

*Summary of timing.* The timing is summarized in Figure 14.1 (where "MH$i$" stands for "moral hazard in firm $i$").

Figure 14.1 (two parallel timelines, one per firm, left to right; p. 501, PDF 514): Firm 1: $I_1$ → Loan agreement 1 → Learning period: No distress (prob. $x$) or Distress (prob. $1 - x$) → Transfer of asset (from a firm in distress to the other) → MH1 → Outcome 1. Firm 2: $I_2$ → Loan agreement 2 → Learning period: No distress (prob. $x$) or Distress (prob. $1 - x$) → Transfer of asset → MH2 → Outcome 2.

*Correlation of shocks.* The shocks affecting the demands for the two products may be correlated. We allow for an arbitrary level of correlation. The conditional probabilities (given firm $i$'s state) that firm $j$ is productive or in distress are stated in Table 14.1. For consistency, the parameters must be such that the probability that firm $j$ is productive is $x$:

$$x\mu + (1 - x)(1 - \nu) = x \iff x(1 - \mu) = (1 - x)(1 - \nu). \qquad (14.3)$$

Table 14.1 (conditional probability that firm $j$ is …)

| when firm $i$ is | productive | in distress |
|---|---|---|
| productive (prob. $x$) | $\mu$ | $1 - \mu$ |
| in distress (prob. $1 - x$) | $1 - \nu$ | $\nu$ |

*Nonconcurrent risks.* In the first polar case, at most one firm is in distress. Put differently, if firm $i$ is in distress then firm $j$ is not: $\nu = 0$. The consistency condition (14.3) then implies $\mu = (2x - 1)/x$ (which naturally requires that $x \geqslant \frac12$).

*Identical shock.* The other polar case is that of perfectly correlated environments. There are only two states of nature: either both firms are productive or both are in distress. This corresponds to $\mu = \nu = 1$.

*Transfer price.* If both firms are in distress (which has probability $(1 - x)\nu$), the four participants (entrepreneurs, lenders) receive no ex post revenue. If neither is in distress (which has probability $x\mu$), no sale occurs and the model is the standard variable-investment one.

So let us consider the more interesting case in which firm 1, say, is in distress and firm 2 is not. We then assume that lender 1 makes a take-it-or-leave-it offer to lender 2 (see the third remark below for more general bargaining powers). Let $P$ denote the per-unit price demanded by lender 1.

Note that lender 2 must adjust entrepreneur 2's incentive scheme to account for the increased investment and therefore for the increased private benefit from not behaving (now equal to $B(I_1 + I_2)$ instead of $BI_2$). Assume that entrepreneur 2's incentive compatibility constraint is binding in the absence of a purchase ($(\Delta p)R_{b2} = BI_2$), which actually turns out to be optimal. Then, lender 2 must raise entrepreneur 2's income in the case of success by $\delta R_{b2}$ such that¹²

$$(\Delta p)(\delta R_{b2}) = BI_1.$$

So, entrepreneur 2's rent increases by $[p_H B/\Delta p]I_1$ and the transfer price is

$$PI_1 = p_H\left(R - \frac{B}{\Delta p}\right)I_1 = \rho_0 I_1.$$

The transfer price is simply the pledgeable income: $P = \rho_0$. […] From (14.2), we see that $P < 1$.

So, the asset is sold at a discount even though the seller has the bargaining power. […] Because firm 1 has the bargaining power, lender 2 actually gains nothing from firm 1's distress, while entrepreneur 2 pockets the extra agency rent $p_H BI_1/\Delta p = (\rho_1 - \rho_0)I_1$.

*Entrepreneurs' expected utility.* Suppose entrepreneur $i$ maximizes her net utility. As usual, the lenders' zero-profit condition implies that the borrower receives the full surplus associated with investment:

$$U_{bi} = [xp_H RI_i - I_i] + [(1 - x)(1 - \nu)PI_i] + \left[x(1 - \mu)\frac{p_H B}{\Delta p}I_j\right]. \qquad (14.4)$$

The first term in brackets in the expression of $U_{bi}$ corresponds to the case in which distress sales are impossible. The second term comes from lender $i$'s revenue from the sales of assets if only firm $i$ is in distress. The third term represents the expected windfall gain from firm $j$'s distress.

We can rewrite (14.4) as

$$U_{bi} = [x\rho_i + (1 - x)(1 - \nu)\rho_0 - 1]I_i + [x(1 - \mu)(\rho_1 - \rho_0)]I_j. \qquad (14.5)$$

So let

$$\alpha \equiv x\rho_1 + (1 - x)(1 - \nu)\rho_0 - 1 \quad\text{and}\quad \kappa \equiv x(1 - \mu)(\rho_1 - \rho_0) > 0.$$

Using (14.4), we can rewrite borrower $i$'s net utility $U_{bi}$ as

$$U_{bi} = \alpha I_i + \kappa I_j. \qquad (14.6)$$

*Borrowing capacity.* Because lender $i$ expects no surplus from the purchase of firm $j$'s assets when the latter is in distress, lender $i$'s expected profit is

$$xp_H(RI_i - R_{bi}) + (1 - x)(1 - \nu)PI_i - (I_i - A_i) = 0,$$

where $R_{bi}$ is borrower $i$'s income when firm $i$ does not purchase firm $j$'s assets and is successful. Incentive compatibility requires that $(\Delta p)R_{bi} \geqslant BI_i$, and, as usual, this inequality is satisfied with equality in order to maximize pledgeable income and therefore debt capacity. Using these two equations, firm $i$'s maximal investment is $I_i = kA_i$, where

$$k = \frac{1}{1 - \rho_0[x + (1 - x)(1 - \nu)]}. \qquad (14.7)$$

[…] (a) *Low correlation* ($\nu < \nu^*$). Then $\alpha > 0$ and the firms invest up to their borrowing capacity: $I_i = kA_i$. While each firm's investment is independent of the existence of the other firm, each firm derives a positive externality from this existence in the form of asset redeployability. (b) *High correlation* ($\nu > \nu^*$). Then $\alpha < 0$, and no firm invests, even though coordinated investment could be profitable (if $\alpha + \kappa > 0$). […]

*Remark (decreasing returns to scale).* Investment externalities are here positive. A firm's investment allows it to stand by to purchase the other firm's assets if the latter is in distress. On the other hand, if (due to entrepreneurial limited attention, for example) returns to investment were decreasing rather than constant, investment externalities could become negative, as a more active firm is less eager to take on new tasks. That is, the transfer price a firm in distress can get for its assets is lower, the higher the level of existing investment by the other firm.

*From Tirole footnotes 10 and 12, p. 500 (PDF 513):* 10. In particular, the entrepreneur in firm $j$ cannot enjoy private benefit $BI_j$ by keeping the assets. 12. The new incentive constraint is $(\Delta p)(R_{b2} + \delta R_{b2}) \geqslant B(I_2 + I_1)$.

---

### 7. Inefficiently low volume of asset reallocations
**Source:** Tirole, Ch. 14, Exercise 14.4, p. 516 (PDF 529) · Answer in book: yes, p. 619

**Exercise 14.4 (inefficiently low volume of asset reallocations).** This exercise applies the logic of corporate risk management developed in Chapter 5 to show that, even with frictionless resale markets, there will be an inefficiently low volume of transactions in the secondary market.

There are three dates, $t = 0, 1, 2$, and at least two firms $i = 1, 2$.

Firm 1, the firm of interest, is managed by a risk-neutral entrepreneur, who owns initial wealth $A$ at date 0 and is protected by limited liability. This firm invests at a variable investment level $I \in [0, \infty)$. The per-unit profitability of investment is random and learned at date 1. The investment yields $RI$ with probability $p + \tau$ and 0 with probability $1 - (p + \tau)$. The random variable $\tau$ is drawn from a continuous distribution. The variable $p$ is equal to $p_H$ if the entrepreneur behaves (no private benefit) and $p_L$ if the entrepreneur misbehaves (private benefit $BI$). Let

$$\rho_1 = (p_H + \tau)R$$

and

$$\rho_0 = (p_H + \tau)\left(R - \frac{B}{\Delta p}\right) \equiv \rho_1 - \Delta\rho$$

denote the random continuation per-unit NPV and pledgeable income when the entrepreneur behaves and the realization of profitability is $\tau$. The distribution on $\tau$ induces a cumulative distribution function $F(\rho_0)$ on $[\underline\rho_0, \bar\rho_0]$.

At date 1, the firm may either continue or resell assets $I$ to firm 2 (or to a competitive market). Firm 2 has a known level $\hat\rho_0$ of per-unit pledgeable income per unit of investment (its NPV per unit of investment is in general larger than this).

Firms 1 and 2 do not contract with each other at date 0. Rather, investors in firm 1 make a take-it-or-leave-it offer to firm 2 at date 1 if firm 1's initial contract specifies that assets ought to be reallocated.

Assume for simplicity that the contract between firm 1's investors and the entrepreneur can be contingent on the realization of $\rho_0$.

Show that at the optimal contract assets are resold whenever $\rho_0 < \rho_0^*$, where

$$\rho_0^* < \hat\rho_0,$$

and so the volume of asset reallocations is inefficiently low.

#### Context needed to solve it

*From Tirole §14.2.2, pp. 501–502 (PDF 514–515)* — the take-it-or-leave-it price paid by an acquirer is its pledgeable income per unit:

[…] lender 1 makes a take-it-or-leave-it offer to lender 2 […]. Note that lender 2 must adjust entrepreneur 2's incentive scheme to account for the increased investment and therefore for the increased private benefit from not behaving […]. So, entrepreneur 2's rent increases by $[p_H B/\Delta p]I_1$ and the transfer price is $PI_1 = p_H(R - B/\Delta p)I_1 = \rho_0 I_1$. The transfer price is simply the pledgeable income: $P = \rho_0$. […] So, the asset is sold at a discount even though the seller has the bargaining power. In this sense, the asset market exhibits some degree of *illiquidity*. Indeed, while reallocation of assets is here efficient as assets in the firm in distress have a zero productivity, it could be inefficient in an environment in which productivity does not fall to 0, but is still lower than the productivity following a reallocation to the other firm (see Exercise 14.4).

---

### 8. Inside liquidity
**Source:** Tirole, Part VII, Review Problem 6, pp. 629–630 (PDF 642) · Answer in book: yes, p. 635

**Review Problem 6 (inside liquidity).** Consider the variable-investment model with two possible values of liquidity shocks (0 and $\rho$ per unit of investment). The timing is described in Figure 2.

Figure 2 (timeline, left to right; p. 629, PDF 642)

| Date 0 | Date 1 | Date 1 → 2 | Date 2 |
|---|---|---|---|
| Entrepreneur has wealth $A$, invests $I$, borrows $I - A$. | Firm is "intact" (no reinvestment needed) with probability $1 - \lambda$, and "distressed" (reinvestment $\rho$ per salvaged unit) with probability $\lambda$. | Moral hazard. | Success ($R$ per unit) with probability $p$ and failure (0) with probability $1 - p$, for the salvaged investment. |

Investors and entrepreneurs are risk neutral, the entrepreneur is protected by limited liability and the rate of interest in the economy is 0. If the firm is in distress (suffers a liquidity shock), a reinvestment $\rho xI$ allows it to salvage a fraction $x \in [0, 1]$ of the investment (so there is no constraint to salvage all or nothing, even though, as we will see, the solution will be a "corner solution").

Continuation is subject to moral hazard. The probability of success is $p_H$ if the entrepreneur behaves and $p_L$ is she misbehaves. The private benefit of misbehaving is $BxI$. The project yields $RxI$ in the case of success and 0 in the case of failure. Let

$$\rho_0 \equiv p_H\left(R - \frac{B}{\Delta p}\right) < c \equiv \min\left\{1 + \lambda\rho, \frac{1}{1 - \lambda}\right\} < \rho_1 \equiv p_H R.$$

In the first two questions, one will assume that there is a costless outside store of value (there are assets that at per-unit cost $q = 1$ at date 0 yield a return equal to 1 at date 1).

(i) Show that, when choosing $x$, the entrepreneur can borrow up to

$$I = \frac{A}{(1 + \lambda\rho x) - [1 - \lambda + \lambda x]\rho_0}.$$

(ii) Compute the borrower's utility and show that

$$x = 1 \quad\text{if and only if}\quad (1 - \lambda)\rho \leqslant 1$$

(and $x = 0$ otherwise).

(Hint: write the borrower's utility as a function of the "average unit cost of preserved investment.")

(iii) Suppose now that there is no outside store of value. There is mass 1 of (*ex ante* identical) entrepreneurs. The only liquidity in the economy is the inside liquidity created by the securities issued by the firms. One will assume that $\rho_0 < \rho < 1/[1 - \lambda]$. Is there enough liquidity if the firms' liquidity shocks are perfectly correlated? If not, what is the level of the liquidity shortage?

(iv) Consider question (iii) except that the liquidity shocks faced by the entrepreneurs are independently distributed. Show that the firms' holding the stock index may not be optimal. What should be done?

#### Context needed to solve it

*From Tirole §15.2.2 "Wasting Inside Liquidity", pp. 521–522 (PDF 534–535)* — what "holding the stock index" means and the remedy:

[…] the "natural implementation," namely, the policy that consists in each firm holding the stock index, that is, a representative portfolio of claims on all firms in the economy, in general does not work. […] Why does this "self-provision" of liquidity result in a waste of liquidity? Firms that face a low liquidity shock at date 1 have excess cash […]. At date 1, they either redistribute the excess cash to or invest it on behalf of their owners; they have no incentive to invest in distressed firms, in which the reinvestment cost exceeds the pledgeable income. […] in order to force healthy firms to redispatch cash to distressed ones at date 1, firms must at date 0 pool their liquidity and organize a system of (or akin to) credit lines. For example, shares are deposited with one (or an arbitrary number of) financial institutions; each firm is then entitled to draw on a credit line […]. The financial institution can raise the cash needed to honor the credit lines by selling at date 1 shares it holds in firms to date-1 investors.

---

### 9. Time consistency and the soft budget constraint
**Source:** Tirole, Ch. 16, Exercise 16.4, p. 566 (PDF 579) · Answer in book: no

**Exercise 16.4 (time consistency and the soft budget constraint).** A firm is run by a risk-neutral entrepreneur with wealth $A$, and has a fixed-size project with investment cost $I$. The project, if undertaken at date 0, will deliver a verifiable income, $y \in \{y_L, y_H\}$ in the case of success and 0 in the case of failure, at date 2, provided that one worker is employed in the firm. The project yields nothing if it is interrupted (the worker is laid off). $y = y_H$ with probability $\rho$ and $y = y_L < y_H$ with probability $1 - \rho$.

Moreover, in the case of "continuation" and regardless of the value of $y$, the entrepreneur may behave (the income is $y$ for certain, the entrepreneur receives no private benefit) or misbehave (the income is $y$ with probability $p_L$ and 0 with probability $1 - p_L$, the entrepreneur receives private benefit $B$). The entrepreneur is protected by limited liability. Let

$$\mathcal{R} \equiv \frac{B}{1 - p_L}.$$

(One will assume that $B$ is small enough that it is worth inducing the entrepreneur to behave in the case of continuation.) The (risk-neutral) worker is paid $w$ in the case of continuation and 0 otherwise. He obtains unemployment benefit paid by the state $w_u < w$ when laid off. We take $w$ and $w_u$ as given. (Note: they could be endogenized through some efficiency wage and incentive-to-search stories, but take these as exogenous for this exercise.)

Figure 16.12 (timeline, left to right; p. 566, PDF 579)

| Date 0 | Date 1 | Date 1 → 2 | Date 2 |
|---|---|---|---|
| Entrepreneur invests $I$, borrows $I - A$. Entrepreneur and investors choose liquidity $L$. Entrepreneur hires one worker. | Productivity $y \in \{y_L, y_H\}$ is revealed. Firm continues (keeps worker, pays him $w$), or stops (lays worker off). | Moral hazard (in the case of continuation): the entrepreneur behaves or misbehaves. | Realization of income ($y$ or 0). |

Assume that the interest rate in the economy is 0 and that

$$w < y_L < w + \mathcal{R}$$

and

$$I - A \leqslant \rho(y_H - w - \mathcal{R}) + (1 - \rho)(y_L - w - \mathcal{R}).$$

(i) Write the firm's NPV depending on whether the firm continues ($x = 1$) or stops ($x = 0$) when productivity is low ($y = y_L$). Show that $x^* = 1$. Assuming a perfectly functioning capital market at date 1, what is the amount of liquidity that is needed to complement capital market refinancing?

(ii) Introduce a government that can at date 1 bring a subsidy $s \geqslant 0$ to the firm (it is a pure subsidy: the government takes no ownership stake in exchange). The shadow cost of public funds is $\lambda$, and so the cost of subsidy $s$ for the taxpayers is $(1 + \lambda)s$. The government maximizes total welfare (entrepreneur, investors, worker, taxpayers). Assuming that

$$\lambda[(w - w_u) + \mathcal{R}] \leqslant (1 + \lambda)y_L$$

and that the government selects its subsidy at date 1 (having observed the realization of $y$), what is the liquidity $L$ chosen by entrepreneur and investors at date 0?

How would the government (contingent) choice of $s$ be affected if the government could commit to $s$ at date 0, before the investors and the entrepreneur write their contract?

#### Context needed to solve it

None beyond Figure 16.12, transcribed above.

---

### 10. News about prospects and aggregate liquidity
**Source:** Tirole, Ch. 15, Exercise 15.2, pp. 531–532 (PDF 544) · Answer in book: yes, pp. 620–621

**Exercise 15.2 (news about prospects and aggregate liquidity).** Consider an economy with a continuum of identical risk-neutral entrepreneurs. The representative entrepreneur has a fixed-size investment project costing $I$, and limited personal wealth $A < I$. The project, if undertaken, will deliver a random but verifiable income $y \in [0, 1]$, with cumulative distribution function $G(y)$ and density $g(y)$, provided that a reinvestment $J$ is made after $y$ is learned, but before $y$ is produced. The project yields nothing if it is interrupted.

Moreover, in the case of "continuation" (that is, if $J$ is sunk), and regardless of the value of $y$, the entrepreneur may behave, in which case income is $y$ for certain, or misbehave, in which case income is $y$ with probability $p_L$ and 0 with probability $1 - p_L$. The entrepreneur, who is protected by limited liability, obtains private benefit $B$ when misbehaving (and no private benefit otherwise). Let

$$\mathcal{R} \equiv \frac{B}{1 - p_L}$$

(one will assume that $B$ is small enough that, in the relevant range, it is worth inducing the entrepreneur to behave in the case of continuation).

The timing is summarized in Figure 15.10.

Figure 15.10 (timeline, left to right; p. 531, PDF 544)

| Date 0 | Date 1 | Date 1 (continued) | Date 2 |
|---|---|---|---|
| Representative entrepreneur invests $I$? If so, she borrows $I - A$. | Firms' idiosyncratic productivities $y$ revealed (drawn from $G(\cdot)$). Depending on its productivity realization, each firm decides whether to continue (and spend $J$). | Moral hazard (in the case of continuation): the entrepreneur behaves or misbehaves. | Realization of income ($y$ or 0). |

The rate of interest in the economy is equal to 0.

(i) Compute the NPV and the investors' net income as functions of the threshold $y^*$ for continuation.

(ii) Let $y_0^* \equiv J$ and $y_1^* = J + \mathcal{R}$.

Define $A_0^*$ and $A_1^*$ by

$$I - A_k^* \equiv \int_{y_k^*}^1 y\,dG(y) - [1 - G(y_k^*)][J + \mathcal{R}],$$

for $k \in \{0, 1\}$.

• What are the date-0 investment policy (investment/no investment) and the date-1 reinvestment policy (the threshold $y^*$) as functions of $A$? (Hint: distinguish three regions $A \geqslant A_0^*$, $A \leqslant A_1^*$, and $A_1^* < A < A_0^*$.)

• Argue that, for $A > A_1^*$, the entrepreneur must arrange at date 0 for her firm's date-1 liquidity.

(iii) • Is there enough inside liquidity if productivities are drawn *independently* from the distribution $G(\cdot)$? Why?

(iv) Suppose, in contrast, that there is a macroeconomic shock $\theta$ that is revealed at the beginning of date 1. (One will denote by $E_\theta[\cdot]$ the date-0 expectations over the random variable $\theta$.) Let $y^*(\theta)$ denote the state-contingent threshold.

• Write the date-0 financing constraint.

• Show that the optimal threshold when liquidity is abundant is actually state independent: there exists $y^*$ such that

$$y^*(\theta) = y^* \quad\text{for all } \theta.$$

• Show that the second-best allocation can be implemented when there are at least

$$\min_{\{\theta\}} \int_{y^*}^1 (y - J - \mathcal{R})\,dG(y \mid \theta)$$

units of outside liquidity delivering 1 unit of good for certain at date 1.

• What would happen if there were few such stores of value?

#### Context needed to solve it

None beyond Figure 15.10, transcribed above.

---

### 11. Market conditions with and without credit rationing
**Source:** Tirole, Ch. 13, Exercise 13.3, p. 494 (PDF 507) · Answer in book: yes, pp. 617–618

**Exercise 13.3 (impact of market conditions with and without credit rationing).** This analysis pursues that of Section 13.5.1. There, we compared the sensitivity of investment with the output price (or installed-base investment) in the presence or absence of credit rationing, focusing on either the fixed-investment variant or the constant-returns-to-scale variant. We now assume decreasing returns to scale.

The representative entrepreneur (there is a unit mass of such entrepreneurs) has initial wealth $A$, is risk neutral and protected by limited liability, and invests $I + K$, where $I$ is the scale of investment and $K$ a fixed cost that is unrelated to scale. We assume that $K \geqslant A$, and so investors are unable to finance by themselves even a small investment.

An entrepreneur is successful with probability $p$ and fails with probability $1 - p$. We assume that the shocks faced by the entrepreneurs are independent. This hypothesis is consistent with the assumption made below that the output price is deterministic. When successful, the entrepreneur produces $R(I)$ units of a good (with $R(0) = 0$, $R' > 0$, $R'' < 0$, $R'(0) = \infty$, $R'(\infty) = 0$); an entrepreneur who fails produces nothing. For concreteness, let

$$R(I) = I^\alpha, \quad\text{with } 0 < \alpha < 1.$$

As usual, the probability of success is endogenous: $p \in \{p_L, p_H\}$. Misbehavior, $p = p_L$ (respectively, good behavior, $p = p_H$), brings about private benefit $BI$ (respectively, no private benefit). To prevent moral hazard, the entrepreneur must receive reward $R_b$ in the case of success, such that

$$(\Delta p)R_b \geqslant BI.$$

The product sells at price $P$ per unit. Presumably, investors are risk neutral and demand rate of return 0.

Suppose that the fixed cost $K$ is "not too large" (so that the entrepreneur wants to invest in the absence of credit rationing), and that

$$\frac{p_H B}{\Delta p} < \frac{1 - \alpha}{\alpha}.$$

(i) Derive the first- and second-best investment levels as functions of $P$. Show that they coincide for $P \geqslant P_0$ for some $P_0$.

(ii) Using a diagram, argue that there exists a region of output prices in which the second-best investment is more responsive than the first-best investment to the output price.

(iii) How would you analyze the impact of the existence of an installed-base level of investment $I_0$?

#### Context needed to solve it

*From Tirole §13.5.1 "Heuristics", pp. 489–491 (PDF 502–504):*

To obtain some first intuition as to how past investment crowds out current investment, let us start with a static model, with first a fixed investment, and then variable investment.

*13.5.1.1 Fixed Investment Size.* Consider, thus, the fixed-investment model. There is a mass 1 of entrepreneurs. At investment cost $I$, an entrepreneur can produce $R$ units of a good with probability $p$ (and 0 units with probability $1 - p$). The final price per unit of output is $P$. Presumably, $P$ depends on past industry investment, but we do not need to go into detail at this stage. The probability of success is $p_H$ if the entrepreneur behaves (no private benefit) and $p_L = p_H - \Delta p$ if she misbehaves (private benefit $B$). We assume that the output realizations are independent across entrepreneurs (there is no aggregate uncertainty); this assumption is consistent with the assumption made above that the output price is deterministic.

Entrepreneurs are risk neutral and are protected by limited liability. The distribution of assets in the population of entrepreneurs is given by the cumulative distribution function $G(A)$ on $[0, \infty)$. Investors are risk neutral and demand rate of return equal to 0. Assume that it is optimal to provide the entrepreneurs with incentives to behave.

Varying $P$, let us compare the level of aggregate investment under credit rationing ($B > 0$) and in its absence ($B = 0$), and show that the first- and second-best levels of investment are as depicted in Figure 13.11.

Figure 13.11 (p. 490, PDF 503): investment $I$ (vertical axis) against the price $P$ (horizontal axis). $I^{\text{FB}}$ is 0 for $P < I/p_H R$ and jumps to the flat level $I$ at $P = I/p_H R$. Below $I/p_H R$, $I^{\text{SB}} = I^{\text{FB}} = 0$. Above it, $I^{\text{SB}}$ starts on the vertical segment at $P = I/p_H R$ and rises, concave, toward $I^{\text{FB}}$ from below.

Conditional on receiving financing, an entrepreneur's incentive constraint is $(\Delta p)R_b \geqslant B$, and so the financing condition can be written as $A \geqslant \bar A$, where

$$p_H\left[PR - \frac{B}{\Delta p}\right] = I - \bar A.$$

The fraction of entrepreneurs who are able to raise funds is

$$X \equiv 1 - G\left(I - p_H\left[PR - \frac{B}{\Delta p}\right]\right), \qquad (13.13)$$

or, equivalently, total investment is $I^{\text{SB}} = XI$, as long as the NPV is positive, i.e., as long as $p_H PR - I \geqslant 0$.

*In the positive-NPV range* ($P \geqslant I/p_H R$), aggregate investment increases with $P$ as long as $B > 0$. […] *aggregate investment is always more responsive to the output price under credit rationing than with no (or little) credit rationing*, since investment does not move with the output price in this range in the absence of credit rationing.

This illustrates the *net worth effect* […].

To complete this analysis, we can now endogenize the product price by assuming the existence of a prior "fraction" $X_0$ of similar firms that were able to raise financing in the past. The output price is then a decreasing function of total output, $p_H(X_0 + X)R$:

$$P = P(p_H(X_0 + X)R) \quad\text{with } P' < 0. \qquad (13.14)$$

An equilibrium is then a "level of investment" $XI$, where $X$ is obtained from (13.13) and (13.14):

$$X = 1 - G\left(I - p_H\left(P(p_H(X_0 + X)R)R - \frac{B}{\Delta p}\right)\right).$$

Note that as $X_0$ grows, $X$ must decrease (a crowding-out effect (if $X$ increased, then $P$ would decrease, and so $X$ would decrease after all)) but $X_0 + X$ must increase (there is less than full crowding out (if $X_0 + X$ decreased, then $P$ would increase, and $X$ would increase after all)).

The increased sensitivity of investment under credit rationing, however, is not a general conclusion, as can also be seen from Figure 13.11. A small increase in $P$ from the negative-NPV to the positive-NPV region raises the first-best investment dramatically, but the second-best one less so as not all firms get on board. […]

*13.5.1.2 Variable Investment Size.* Next consider the variable-investment model of Section 3.4: the number of units of output produced in the case of success is $RI$, the private benefit in the case of misbehavior $BI$. To be incentivized to behave, an entrepreneur with investment size $I$ must receive $R_b$ in the case of success, such that $(\Delta p)R_b \geqslant BI$. For a given output price $P$, an entrepreneur with assets $A$ can borrow up to the level at which pledgeable income is equal to investors' outlay:

$$p_H\left(PR - \frac{B}{\Delta p}\right)I = I - A \quad\text{or}\quad I = \frac{A}{1 + (p_H B/\Delta p) - p_H PR}.$$

Assuming, without loss of generality, that all entrepreneurs have the same net worth $A$, let us analyze the impact of a prior level of investment $I_0$ on current investment. Total output is then $p_H R(I_0 + I)$. Because $P = P(p_H R(I_0 + I))$, with $P' < 0$,

$$I = I^{\text{SB}} = \frac{A}{1 + (p_H B/\Delta p) - p_H P(p_H R(I_0 + I))R}. \qquad (13.15)$$

By the same reasoning as in the fixed-investment version, condition (13.15) implies that previous investment partially crowds out current investment: $-1 < \partial I^{\text{SB}}/\partial I_0 < 0$.

Let us now compare this sensitivity to that obtained in the absence of credit rationing. In this first-best benchmark, firms maximize their NPV, regardless of their solvency: $\max_I \{(p_H PR - 1)I\}$. Competitive equilibrium in this constant-returns-to-scale environment implies that unit revenue is equal to unit cost, or

$$p_H P(p_H R(I_0 + I))R = 1. \qquad (13.16)$$

Thus, in the absence of credit constraint, past investment fully crowds out current investment: $\partial I/\partial I_0 = -1$. This is due to what might be labeled a *hindering effect* of credit rationing: because part of the benefit from investment expansion accrues to the entrepreneurs and is therefore nonpledgeable, investors are less keen than entrepreneurs to expand as the market becomes more profitable. And so credit rationing may make investment relatively less responsive to market conditions.

Exercise 13.3 pursues this analysis in the intermediate context of variable investment and decreasing returns to scale.

---

## Tier 3 — Really hard

### 12. Downsizing and aggregate liquidity
**Source:** Tirole, Ch. 15, Exercise 15.1, pp. 530–531 (PDF 543) · Answer in book: yes, pp. 619–620

**Exercise 15.1 (downsizing and aggregate liquidity).** Consider the variable-investment model with *decreasing* returns to scale and a liquidity shock. There is a unit mass of identical entrepreneurs. The timing for a given entrepreneur is in Figure 15.9.

Figure 15.9 (timeline, left to right; p. 530, PDF 543)

| Date 0 | Date 1 | Date 1 → 2 | Date 2 |
|---|---|---|---|
| Entrepreneur has wealth $A$, borrows $I - A$. | Firm is intact (no reinvestment needed) with probability $1 - \lambda$, and distressed (reinvestment $\rho$ per salvaged unit) with probability $\lambda$. | Moral hazard. | Outcome: success (profit $R(J)$) with probability $p_\bullet$, failure (profit 0) with probability $1 - p_\bullet$. |

At date 1, an amount $J$, $0 \leqslant J \leqslant I$, is rescued. In the absence of a liquidity shock (event has probability $1 - \lambda$), of course $J = I$. But in the face of a liquidity shock (which has probability $\lambda$), the investment is downsized to $J \leqslant I$ (the cost of continuation is then $\rho J$). The shock is verifiable. Let $R(J)$ denote the profit in the case of success.

The moral-hazard stage is described as it usually is: the probability of success is $p_H$ if the entrepreneur works and $p_L = p_H - \Delta p$ if she shirks. The entrepreneur obtains private benefit $BJ$ by misbehaving and 0 otherwise. Investors and entrepreneur are risk neutral, and the latter is protected by limited liability.

Economic agents do not discount the future (which does not imply that rates of interest are always 0!).

From now on, use $J$ for the amount that is salvaged when there is a liquidity shock (as we noted, the corresponding amount is $I$ in the absence of shock).

Assume that $R(0) = 0$, $R' > 0$, $R'' < 0$, $R'(0) = \infty$, $R'(\infty) = 0$.

(i) Assume that there is plenty of liquidity in the economy, so that the firms have access to a store of value (by paying $q = 1$ at date 0, they receive 1 at date 1).

Show that downsizing occurs in the case of a liquidity shock,

$$J^* < I^*,$$

if and only if

$$\rho > \frac{1}{1 - \lambda}.$$

(Hints: (1) write the incentive constraints (the sharing rule can be adjusted to the realization of the shock) and infer the pledgeable income; (2) maximize the entrepreneur's utility (employ the usual trick) subject to the investors' breakeven condition, ignoring the constraint $J \leqslant I$; let $\mu$ denote the shadow price of the constraint; (3) derive the stated result.)

(ii) Suppose that the liquidity shocks are *perfectly correlated.*

• What is the minimal number $L^*$ of outside stores of value (delivering 1 unit of good each at date 1) needed to support the allocation described in (i)?

• Argue that if $L < L^*$, then $q > 1$ and $J < I$ *a fortiori* if $\rho > 1/(1 - \lambda)$.

Derive the equations giving the liquidity premium $(q - 1)$ under these assumptions.

(iii) Suppose now that the liquidity shocks are independent across firms.

• Argue that (provided that the entrepreneurs borrow at date 0) there is enough liquidity to support the allocation derived in (i).

• Suppose that each entrepreneur holds the stock index. When will this provide enough liquidity? How can one prevent this potential waste of liquidity?

#### Context needed to solve it

*From Tirole §15.2.2 "Wasting Inside Liquidity", pp. 521–522 (PDF 534–535):*

The sufficiency result by itself only states that the corporate sector produces enough inside liquidity to support its optimal reinvestment policy. It is silent on how the latter can be implemented.

Let us first point out that the "natural implementation," namely, the policy that consists in each firm holding the stock index, that is, a representative portfolio of claims on all firms in the economy, in general does not work. The date-1 value of the index is $(\rho_0 - \bar\rho)I$. To see this, note that the corporate sector will return $\rho_0 I$ to investors at date 2. The average reinvestment cost, however, is $((1 - \lambda)\rho_L + \lambda\rho_H)I = \bar\rho I$, which must be financed at date 1 by issuing new shares on the corporate sector date-2 income and thereby diluting existing shareholders.

Thus, if all firms hold equal shares in the index, those with a high liquidity shock can meet it by reselling shares if and only if

$$(\rho_H - \rho_0)I \leqslant (\rho_0 - \bar\rho)I \quad\text{or}\quad \rho_H + \bar\rho \leqslant 2\rho_0. \qquad (15.4)$$

If $\rho_H + \bar\rho > 2\rho_0$, then holding the stock index does not allow the firms facing the high liquidity shock to continue.

Why does this "self-provision" of liquidity result in a waste of liquidity? Firms that face a low liquidity shock at date 1 have excess cash for two reasons: first (reasoning in terms of per unit of investment), they can raise up to $\rho_0$ when they need only $\rho_L$; second, they have invested in the stock index, with resulting value $\rho_0 - \bar\rho$. This excess liquidity is, of course, not fully wasted as the extra profit is partly reappropriated by distressed firms that own a fraction of the stock index and therefore own part of the healthy firms. Still, healthy firms do have excess liquidity. At date 1, they either redistribute the excess cash to or invest it on behalf of their owners; they have no incentive to invest in distressed firms, in which the reinvestment cost exceeds the pledgeable income.

[…] in order to force healthy firms to redispatch cash to distressed ones at date 1, firms must at date 0 pool their liquidity and organize a system of (or akin to) credit lines. For example, shares are deposited with one (or an arbitrary number of) financial institutions; each firm is then entitled to draw on a credit line up to a cap of $\rho_H I$. The financial institution can raise the cash needed to honor the credit lines by selling at date 1 shares it holds in firms to date-1 investors. From the net-borrower assumption, the proceeds of such sales can cover the financing of the credit lines: $(1 - \lambda)(\rho_0 - \rho_L)I > \lambda(\rho_H - \rho_0)I$.

(In this passage $\rho_L$, $\rho_H$, $\bar\rho = (1 - \lambda)\rho_L + \lambda\rho_H$, $\rho_0$ are the per-unit shocks and pledgeable income of the constant-returns model of §15.2.1; see exercise 3.)

*From Tirole §15.3.1 "Aggregate Shocks and the Value of Outside Liquidity", p. 523 (PDF 536):*

[…] Here we introduce outside stores of value into the picture. For simplicity, there are $L^S$ such stores of value. A store of value yields 1 unit of good at date 1 for certain. Its date-0 price is $q$; because the market rate of interest is equal to 0 and investors can buy the store of value, $q \geqslant 1$. Furthermore, if $q = 1$, then the corporate sector is able to implement its efficient allocation. If $q > 1$, then the corporate sector must hold all stores of value. […] $q > 1$ only if firms compete with each other for the scarce liquidity. The date-0 price $q$ adjusts to the level at which the demand for liquid assets is equal to the supply: $L = L^S$.

---

### 13. Complementarity between liquid and illiquid assets
**Source:** Tirole, Ch. 15, Exercise 15.4, p. 532 (PDF 545) · Answer in book: yes, p. 621

**Exercise 15.4 (complementarity between liquid and illiquid assets).** Go through the analysis of Section 15.3.1 assuming that entrepreneurs do not want to invest in projects that are discontinued in the adverse state of nature:

$$(1 - \lambda)\rho_1 < 1 + (1 - \lambda)\rho_L.$$

Show that an increase in the supply $L^S$ of liquid assets increases the investment $I$ in illiquid ones.

#### Context needed to solve it

*From Tirole §15.2.1 "The Sufficiency Result", pp. 518–520 (PDF 531–533)* — the model of Section 15.3.1 is that of Section 15.2:

There are three periods, $t = 0, 1, 2$. Investors are risk neutral and the market rate of interest in the economy is 0. The economy is also populated by a large number—technically a continuum of mass 1—of ex ante identical, risk-neutral entrepreneurs. The representative entrepreneur at date 0 has wealth $A$, borrows $I - A$, and invests $I$. At date 1, a given firm faces liquidity shock $\rho I$, with $\rho = \rho_L$ with probability $1 - \lambda$ (healthy firm) and $\rho = \rho_H > \rho_L$ with probability $\lambda$ (firm in distress). The firm can continue only if it finds funds to defray its liquidity shock; otherwise, it is liquidated. We normalize the liquidation value at 0. In the case of continuation, the firm's date-2 expected income is denoted by $\rho_1 I$, of which only $\rho_0 I < \rho_1 I$ is pledgeable to investors (see Figure 15.1).

Figure 15.1 (p. 519, PDF 532; identical to Figure 15.11): Date 0 — Representative entrepreneur borrows $I - A$, invests $I$. Date 1 — Liquidity need $\rho I$ realized; then "Continue" (→ Moral hazard) or "Liquidate". Date 2 — Expected income $\rho_1 I$, of which $\rho_0 I$ is pledgeable.

Let us assume that

$$\rho_L < \rho_0 < \rho_H < \rho_1 \qquad (15.1)$$

and

$$(1 - \lambda)(\rho_H - \rho_L) < 1. \qquad (15.2)$$

[…] the unit cost of effective investment is $c(x) \equiv \dfrac{1 + (1 - \lambda)\rho_L + \lambda\rho_H x}{1 - \lambda + \lambda x}$ […] where $\bar\rho \equiv (1 - \lambda)\rho_L + \lambda\rho_H$ is the expected liquidity shock per unit of investment. Lastly, we assume that $\rho_1 > 1 + \bar\rho$, and so entrepreneurs prefer investing to consuming $A$ (the project's NPV is positive). To sum up, the efficient allocation is given by $x = 1$ and $I = \dfrac{A}{(1 + \bar\rho) - \rho_0}$.

*From Tirole §15.3.1 "Aggregate Shocks and the Value of Outside Liquidity", pp. 523–525 (PDF 536–538):*

Suppose now that liquidity shocks are perfectly correlated across firms in the model of Section 15.2 (that firms face the same shock is the starkest way of introducing an aggregate shock; Exercise 15.3 studies the more general case of imperfectly correlated shocks). In this polar case, and in the absence of outside liquidity, firms cannot continue when $\rho = \rho_H > \rho_0$: $x = 0$.

We will assume that the entrepreneurs prefer investing to consuming even if the investment is liquidated in the bad state of nature, i.e., that, per unit of investment, the expected output $(1 - \lambda)\rho_1$ exceeds the sum of the initial investment cost, 1, and the expected reinvestment cost, $(1 - \lambda)\rho_L$:

$$(1 - \lambda)\rho_1 > 1 + (1 - \lambda)\rho_L.$$

(This positive-NPV assumption is more stringent than the previous one: $\rho_1 > 1 + \bar\rho$.)

[…] Here we introduce outside stores of value into the picture. For simplicity, there are $L^S$ such stores of value. A store of value yields 1 unit of good at date 1 for certain. Its date-0 price is $q$; because the market rate of interest is equal to 0 and investors can buy the store of value, $q \geqslant 1$. Furthermore, if $q = 1$, then the corporate sector is able to implement its efficient allocation. If $q > 1$, then the corporate sector must hold all stores of value.

In the bad state of nature, the representative firm continues with probability $x$. Equivalently, a fraction $1 - x$ of its investment is liquidated. For ease of exposition, we will work under the latter interpretation.

The liquidity need in the bad state, $\rho_H xI$, must not exceed the sum of the amount $\rho_0 xI$, which can be raised by returning to the capital market at date 1, and of the income $L$ associated with a date-0 purchase of outside liquidity in amount $L$. And so

$$(\rho_H - \rho_0)xI \leqslant L.$$

The investors' breakeven constraint condition states that the total investor date-0 outlay to pay for illiquid and liquid assets should be recouped from the pledgeable income:

$$[I + qL] - A \leqslant L + (1 - \lambda)(\rho_0 - \rho_L)I + \lambda(\rho_0 - \rho_H)xI.$$

To make things interesting, we will assume that $L^S$ is not so large that $q = 1$ […]. $q > 1$ only if firms compete with each other for the scarce liquidity. The date-0 price $q$ adjusts to the level at which the demand for liquid assets is equal to the supply: $L = L^S$.

Let

$$U_b = [(1 - \lambda)(\rho_1 - \rho_L) + \lambda(\rho_1 - \rho_H)x]I - (q - 1)(\rho_H - \rho_0)xI - I \qquad (15.5)$$

denote the representative borrower's utility or net present value, given that an amount of liquidity $L = (\rho_H - \rho_0)xI$ is required to bring a fraction $x$ of investment to completion in the bad state of nature. The investors' breakeven constraint can be rewritten as

$$[(1 - \lambda)(\rho_0 - \rho_L) + \lambda(\rho_0 - \rho_H)x]I - (q - 1)(\rho_H - \rho_0)xI \geqslant I - A. \qquad (15.6)$$

This constraint yields the investment level $I$ as a function of $x$ and $q$. Substituting into (15.5),

$$U_b = \frac{\rho_1 - c(x, q)}{c(x, q) - \rho_0}A,$$

where

$$c(x, q) = \frac{1 + (1 - \lambda)\rho_L + \lambda\rho_H x + (q - 1)(\rho_H - \rho_0)x}{1 - \lambda + \lambda x}$$

is the cost of effective investment, that is, the average cost of bringing 1 unit of investment to completion. Let $\bar q$ be given by

$$\frac{\partial c}{\partial x}(x, \bar q) = 0 \iff (1 - \lambda)(\rho_H - \rho_L) + \frac{(1 - \lambda)}{\lambda}(\rho_H - \rho_0)(\bar q - 1) = 1.$$

Then $x = 1$ if $q < \bar q$, $= 0$ if $q > \bar q$, $\in [0, 1]$ if $q = \bar q$.

For $q < \bar q$, the demand for liquid assets is given by

$$L^D = (\rho_H - \rho_0)I = \frac{\rho_H - \rho_0}{c(1, q) - \rho_0}A.$$

The equilibrium in the market for liquidity is depicted in Figure 15.3, where

$$\bar L^S \equiv \frac{(\rho_H - \rho_0)A}{1 + \bar\rho - \rho_0}$$

is the lowest amount of outside liquidity such that the market clearing price for liquidity is $q = 1$.

Figure 15.3 (p. 524, PDF 537): price $q$ (vertical axis) against quantity $L^D, L^S$ (horizontal axis). The demand $L^D$ is horizontal at $q = \bar q$ for small quantities, then decreasing in $q$ down to $q = 1$, which it reaches at $\bar L^S$; three vertical supply lines $L_1^S < L_2^S < L_3^S$ cut it on the flat part, on the decreasing part, and on the floor $q = 1$, respectively.

Figure 15.3 illustrates the three regions. When liquidity is very scarce ($L^S = L_1^S$ for example), there is liquidation ($x < 1$); the price of liquid assets is then the highest price, $\bar q$, that firms are willing to pay in order to hold this liquidity and be able to salvage their assets in the bad state of nature. As the supply of liquidity $L^S$ increases, $x$ increases. Once $x$ reaches 1, the price of liquid assets adjusts. A lower price increases the firms' borrowing capacity and, indirectly, the demand for liquid assets, which are a complementary input into the production process. […] Finally, for $L^S \geqslant \bar L^S$ […], there is an excess supply of liquidity. The market price is then $q = 1$, and the excess liquidity, $L^S - \bar L^S$, is absorbed by individual investors, who demand a rate of return equal to 0.

*Does liquidity crowd investment in or out?* […] Whether liquid assets crowd in or out illiquid ones depends on whether the entrepreneurs are willing to invest without continuing in the adverse state of nature ($(1 - \lambda)\rho_1 > 1 + (1 - \lambda)\rho_L$) or not. In the former case, which we have just analyzed, the purchase of liquid assets first comes at the expense of investment: liquid assets crowd out illiquid ones. For larger amounts of liquidity ($L \geqslant \bar L^S$), $x = 1$ and liquid assets and investment are necessarily complements: a larger stock of liquid assets lowers the liquidity premium $(q - 1)$ and thereby the cost of investment.

When investing yields a negative NPV per unit of investment when the investment is liquidated in the adverse state ($(1 - \lambda)\rho_1 < 1 + (1 - \lambda)\rho_L$), entrepreneurs invest only if they can complement their illiquid investment with liquidity. In this case, liquid and illiquid investments are always complements (see Exercise 15.4).

*From Tirole footnote 18, p. 525 (PDF 538):* For $L^S < \underline L^S$, $x < 1$ and $q = \bar q$. Investment is then given by $[1 + (1 - \lambda)\rho_L - (1 - \lambda)\rho_0]I + [(\bar q - 1) + \lambda]L^S = A$. For $L^S \in [\underline L^S, \bar L^S]$, $x = 1$ and $q \leqslant \bar q$. Furthermore, $L^S = (\rho_H - \rho_0)I$ and $I = \dfrac{A}{1 + \bar\rho + (q - 1)(\rho_H - \rho_0) - \rho_0}$.

---

### 14. Dynamics of income inequality
**Source:** Tirole, Ch. 13, Exercise 13.2, pp. 493–494 (PDF 506) · Answer in book: yes, p. 617

**Exercise 13.2 (dynamics of income inequality).** (This exercise builds on the analysis of Section 13.4 and on Matsuyama (2000).)

(i) Consider the "warm-glow" model: generations are indexed by $t = 0, 1, \ldots, \infty$. Each generation lives for one period; each individual has exactly one heir. A generation-$t$ individual has utility from consumption $c_t$ and bequest $\mathcal{L}_t$ equal to

$$\left(\frac{c_t}{1 - a}\right)^{1-a}\left(\frac{\mathcal{L}_t}{a}\right)^a$$

with $0 < a < 1$.

What is the individual's utility from income $y_t$?

(ii) Consider the entrepreneurship model of Section 13.4, with two twists:

• variable-size investment (instead of a fixed-size one),

• intraperiod rate of interest $r$ (so investors demand $(1 + r)$ times their outlay, in expectation); $r$ is assumed constant for simplicity.

One will assume that $p_H = 1$ and that each generation $t$ is born with endowment $\hat A$ (to which is added bequest $\mathcal{L}_{t-1}$, so $A_t = \hat A + \mathcal{L}_{t-1}$). See Figure 13.12.

Figure 13.12 (timeline of generation $t$, left to right; p. 494, PDF 507)

| Start of period | Moral hazard | Outcome | End of period |
|---|---|---|---|
| $\mathcal{L}_{t-1}$ received. Asset $\hat A + \mathcal{L}_{t-1}$. Investment in project of (endogenous) size $I$. | Behaves: Pr(success) 1, private benefit 0. Misbehaves: Pr(success) $p_L$, private benefit $BI$. | Outcome: success/failure. Income $y_t$. | Consumption. Bequest (to generation $t + 1$). |

A successful project delivers $RI \geqslant (1 + r)I$, an unsuccessful one 0. The private benefit from misbehaving, $BI$, is also proportional to investment.

Let

$$\rho_1 \equiv R \quad\text{and}\quad \rho_0 \equiv R - \frac{B}{\Delta p}.$$

Assume that

$$a(\rho_1 - \rho_0) < 1 - \frac{\rho_0}{1 + r}.$$

Show that each dynasty's long-term wealth converges to

$$A_\infty \equiv \frac{\hat A}{1 - a(\rho_1 - \rho_0)/(1 - \rho_0/(1 + r))},$$

regardless of its initial total wealth $A_0$ (that is, $\hat A$ plus the bequest from generation $-1$, if any).

(iii) Now assume that there is a minimal investment scale $\underline I > 0$ below which nothing can be produced. For $I \geqslant \underline I$, the technology is as above (constant returns to scale, profit $RI$ in the case of success, private benefit $BI$ in the case of misbehavior, etc.).

Compute the threshold $A_0^*$ under which the dynasty remains one of lenders (at rate $r$) and never makes it to entrepreneurship.

What is the limit wealth $A_\infty^L$ of these poor dynasties? (The limit wealth of dynasties starting with $A_0 \geqslant A_0^*$ is still $A_\infty$.)

(iv) Finally, close the model by assuming that investors are domestic investors and by describing the equilibrium in the loan market. Focus on *steady states*. Show that multiple steady states may coexist:

• one in which everyone (investors, entrepreneurs) has the same wealth and

$$\rho_1 = 1 + r,$$

• others, with unequal wealth distribution, in which $\rho_1 > 1 + r$, a fraction $\kappa$ of the population is poor (lends), and a fraction $1 - \kappa$ is rich (borrows to undertake projects).

#### Context needed to solve it

*From Tirole §13.4.2.1 "The Warm-Glow Model", pp. 484–485 (PDF 497–498):*

We study long-lived lineages of short-lived family members. Parents become entrepreneurs if they have sufficient funds, earn income, and finally leave wealth as a bequest to their children, who may then use this wealth to undertake projects of their own, and so forth. […] For the purposes of this section, we first bypass the difficulty in a somewhat ad hoc way by using the warm-glow model, which enables us to discuss dynamics without worrying about dynamic programming. Namely, suppose that the following conditions hold.

• Individuals live for one period. An individual living at date $t$ has exactly one heir who lives at date $t + 1$, and so on.

• Individuals are "altruistic" in a rather specific way. Rather than caring about the utility of their heirs, they derive utility from the bequest they make to their heirs. We will assume that a generation-$t$ individual derives utility from her own consumption $c_t$ and from the bequest $\mathcal{L}_t$ to her heir. Assume further that the utility function is a Cobb–Douglas utility function:

$$\left(\frac{c_t}{1 - a}\right)^{1-a}\left(\frac{\mathcal{L}_t}{a}\right)^a,$$

where $a \in (0, 1)$ is the (impure) altruism parameter.

Then the utility from income $y_t$ is (taking logs)

$$\log U_t(y_t) = \max_{\{c_t, \mathcal{L}_t\}}\{(1 - a)\log c_t + a\log\mathcal{L}_t\} \quad\text{s.t.}\quad c_t + \mathcal{L}_t = y_t.$$

*From Tirole §13.4.2.2 "Lineages of Entrepreneurs in the Warm-Glow Model", pp. 485–487 (PDF 498–500):*

Let us now consider a "warm-glow lineage" in which each generation $t$ is a would-be entrepreneur, who

• is born with some exogenous endowment $\hat A$, to which is added the bequest $\mathcal{L}_{t-1}$ made by generation $t - 1$;

• invests this total asset either in a storage technology yielding an interest rate equal to 0 (i.e., preserving the wealth) or in a fixed-size project as described in Section 13.2.1; and

• finally uses the proceed of this investment (her "income") for consumption $c_t$ and bequest $\mathcal{L}_t$ to the next generation.

The timing is summarized in Figure 13.7.

Figure 13.7 (p. 486, PDF 499): same layout as Figure 13.12, with: Asset $\hat A + \mathcal{L}_{t-1}$; Storage (return: 0) *or* investment in project of size $I$ → Moral hazard (if investment): Behaves — Pr(success) $p_H$, private benefit 0; Misbehaves — Pr(success) $p_L$, private benefit $B$ → Outcome: success/failure (if investment); Income $y_t$ → Consumption $c_t = (1 - a)y_t$ → Bequest $\mathcal{L}_t = ay_t$.

Let us assume that the intraperiod rate of interest in the economy is equal to 0.

As in the rest of the book, the private benefit $B$ obtained by misbehaving is expressed in terms of money. So in the case of misbehavior the entrepreneur's utility from income $y_t$ and private benefit $B$ is $y_t + B$. As usual, we will assume that investment has a positive NPV if and only if the entrepreneur is induced to behave: $p_H R > I > p_L R + B$. It will also prove convenient to assume that success is a sure thing in the case of good behavior: $p_H = 1$.

Lastly, let $\bar A$ be defined (as in equation (13.4)) by the equality between the pledgeable income and the investors' outlay:

$$p_H\left(R - \frac{B}{\Delta p}\right) = I - \bar A \quad\text{or (using } p_H = 1\text{)}\quad \bar A = I - \left(R - \frac{B}{\Delta p}\right).$$

**Assumption 13.1.** $\dfrac{\hat A + a(R - I)}{1 - a} > \bar A > \dfrac{\hat A}{1 - a}$.

(a) *Lineage stuck in a poverty trap.* Suppose that generation $t$ receives bequest $\mathcal{L}_{t-1} < \bar A - \hat A$. Generation $t$'s total wealth is then insufficient to have access to funds. Generation $t$ must therefore invest $[\hat A + \mathcal{L}_{t-1}]$ into the low-return storage technology, and so $y_t = \hat A + \mathcal{L}_{t-1}$. With warm-glow preferences, bequests to generation $t + 1$ are $\mathcal{L}_t = ay_t = a(\hat A + \mathcal{L}_{t-1})$, […] The dynasty's total wealth per generation converges to $A_\infty < \bar A$, given by

$$A_\infty = \hat A + aA_\infty \quad\text{or}\quad A_\infty = \frac{\hat A}{1 - a} < \bar A.$$

The lineage is stuck in a poverty trap.

(b) *Rich, entrepreneurial lineage.* By contrast, suppose that generation $t$'s initial wealth exceeds $\bar A$: $\mathcal{L}_{t-1} > \bar A - \hat A$ or $A_t \equiv \hat A + \mathcal{L}_{t-1} > \bar A$. Generation $t$ has enough pledgeable income to offset the inventors' outlay $I - (\hat A + \mathcal{L}_{t-1})$. Under risk neutrality, generation $t$ selects the highest NPV solution and therefore prefers becoming an entrepreneur to investing in the storage technology. The NPV is then $p_H R - I = R - I > 0$, and so the entrepreneur's end-of-period income after reimbursing lenders is $y_t = (R - I) + A_t$ (recall that the capital market is competitive, and so the entire NPV goes to the entrepreneur). Generation $(t + 1)$'s total wealth at the beginning of period $t + 1$ is therefore $A_{t+1} = \hat A + a(R - I + A_t)$. […] The lineage's beginning-of-period wealth converges to $A_\infty$, where

$$A_\infty = \hat A + a(R - I + A_\infty) \quad\text{or}\quad A_\infty = \frac{\hat A + a(R - I)}{1 - a}.$$

Figure 13.8 (p. 487, PDF 500): next generation's wealth $A_{t+1}$ against current wealth $A_t$. Two increasing lines with slope $a$: $A_{t+1} = \hat A + aA_t$ for $A_t < \bar A$ (fixed point $\hat A/(1 - a)$) and $A_{t+1} = \hat A + a(R - I + A_t)$ for $A_t > \bar A$ (fixed point $[\hat A + a(R - I)]/(1 - a)$); two initial wealths $A^-$ just below $\bar A$ and $A^+$ just above it converge to the low and the high fixed point, respectively.

Figure 13.8 illustrates cases (a) and (b) and shows that a small difference in initial wealth (points $A^-$ and $A^+$, respectively, in Figure 13.8) can make a big difference: for the current generation (as we know from Chapter 3) and even more for further generations.

Note, finally, that in the Arrow–Debreu world of no agency cost ($B = 0$), long-term incomes of different lineages would converge to $[\hat A + a(R - I)]/(1 - a)$ regardless of the lineage's initial wealth (rather than diverge as in Figure 13.8). A stronger investor protection, for example, reduces the dependency on wealth and generates a more equal long-run income distribution.

---

### 15. Political economy of exchange-rate policies
**Source:** Tirole, Ch. 16, Exercise 16.3, pp. 565–566 (PDF 578) · Answer in book: yes, p. 623

**Exercise 16.3 (political economy of exchange rate policies).** Consider a country that has liberalized its capital account. There are two goods: a tradable good (the only one consumed by foreigners) and a nontradable good.

• The only investors are foreign investors, with preferences over date-0 and date-1 consumptions

$$c_0^* + c_1^*,$$

where an asterisk refers to the tradable good.

• The country is populated by a unit mass of domestic entrepreneurs endowed with a constant-returns-to-scale technology. The representative entrepreneur (1) invests $I$ units of tradables in equipment (where $I$ is endogenous), (2) produces $RI$ units of tradables in the case of success, and 0 in the case of failure, and $SI$ units of nontradables for certain. We assume that firms' outcomes are independent (there is no macroeconomic shock).

The model is a variation on the standard variable-investment model:

• Each entrepreneur is initially endowed with $A$ units of tradables (her only wealth), borrows $I - A$.

• There is moral hazard. The probability of success in the tradable-good activity is $p_H$ if the entrepreneur behaves, and $p_L$ otherwise. The entrepreneur receives private benefit $BI$ in *tradables* by misbehaving and 0 otherwise.

• An entrepreneur's utility is $c_1 + u(c_1^*) + v(g^*)$, where $c_1$ is the consumption of nontradables, $c_1^*$ the consumption of the tradable good, and $g^*$ the level of public good supplied by the government. $u$ and $v$ are concave.

We add a government. The government has international reserves $\mathcal{R}^*$, of which it consumes $g^*$ to produce a public good. The rest, $\mathcal{R}^* - g^*$, is dumped on the currency market at the end. So, $e$, the price of tradables in terms of nontradables, is given *ex post* by

$$p_H RI + \mathcal{R}^* - g^* = c_1^*(e) + d^* + \frac{d}{e},$$

where $I$ is the representative entrepreneur's investment, $d^*$ is the entrepreneurs' average reimbursed debt in tradables and $d$ is the average reimbursed debt in nontradables. The government cares only about the welfare of entrepreneurs, i.e., does not internalize that of the foreigners.

The timing is summarized in Table 16.1, where "t" and "nt" stand for "tradables" and "nontradables," respectively.

Table 16.1 (p. 565, PDF 578)

| | Date 0 | Date 1 | | |
|---|---|---|---|---|
| (government) | Government selects $g^*$ (commitment) | Government selects $g^*$ (noncommitment) | | |
| nt | | | $SI$ | Exchange rate determined |
| t | Entrepreneur borrows $I - A$ | Entrepreneur takes private benefit $BI$, or none | Outcome $RI$ or 0 | Exchange rate determined |

Consider financing contracts in which

• investors receive $R_l^* = RI - R_b^*$ in tradables in the case of success, and 0 in the case of failure;

• investors have nominal claims $R_l^S$ and $R_l^F$ in nontradables in the cases of success and failure, respectively.

(i) Relate $(d, d^*)$ and $(R_l^*, R_l^S, R_l^F)$.

(ii) Fixing an expected exchange rate $e$, determine the investment $I$ of the representative entrepreneur in this constant-returns-to-scale model assuming that $\rho_0 \equiv p_H(R - B/\Delta p) < 1 - (S/e)$ in the relevant range.

Show that $R_l^F = SI$ and that

$$I = \frac{A}{1 - [(S/e) + \rho_0]}.$$

(iii) Compare the exchange rate and the welfare of entrepreneurs when the government chooses $g^*$ after the private sector borrows abroad ("noncommitment") and when the government can commit to $g^*$ before entrepreneurs borrow abroad ("commitment").

Assume that the exchange rate depreciates as government expenditures $g^*$ grow. Show that $v'(g^*) > e$ under commitment (underspending) and $v'(g^*) < e$ under noncommitment (overspending).

(iv) Show that there is an externality among borrowers when the government cannot commit.

#### Context needed to solve it

None beyond Table 16.1, transcribed above (the variable-investment model is restated in the statement).
