---
quiz: "Topic 5 (hard) — Nonverifiable income, termination, debt structure and sovereign debt"
tags:
  term: "Strategic default and the threat of termination"
  struct: "Debt structure: number of creditors and maturity"
  sov: "Sovereign debt: default sets, prices and borrowing capacity"
---

## term

Q: An entrepreneur's date-1 income $\tilde R_1 \in \{0, R_1\}$ is nonverifiable. The lender offers $\{D, \gamma_0, \gamma_1\}$: repayment $D$, and continuation probability $\gamma_1$ if $D$ is paid, $\gamma_0$ if not. Continuation is worth $E(\tilde R_2)$ to the borrower; liquidation gives the lender $L$, with $L < E(\tilde R_2)$ and $L < I - A$. Which description of the optimal contract is correct?
- $\gamma_0 = 0$: a report of failure always triggers liquidation, since any continuation after non-payment would make strategic default free, so the loan could never be repaid.
- $\gamma_1 = 1$ and the incentive constraint binds, $D = (1-\gamma_0)E(\tilde R_2)$: liquidating after repayment costs more in incentives than its recovery $L$ adds to the lender.
- $\gamma_1 < 1$: liquidating with some probability even after repayment raises the lender's recovery by $L$ per unit of probability, relaxing break-even at no cost to incentives.
- The incentive constraint is slack, $D < (\gamma_1-\gamma_0)E(\tilde R_2)$: the lender keeps a safety margin so that the borrower strictly prefers to repay in every state.
<!-- YW5zOjE= -->
> The lecture's three claims. (IR) binds, so $D > 0$ and $\gamma_1 > \gamma_0$. $\gamma_1 = 1$: raising $\gamma_1$ by $\varepsilon$ adds $\varepsilon E(\tilde R_2)$ to the slack of $(\gamma_1-\gamma_0)E(\tilde R_2) \ge D$, while $D$ only has to rise by $\varepsilon L$ to keep the lender whole, and the borrower gains $p\varepsilon[E(\tilde R_2) - L] > 0$. (IC) binds: raising $\gamma_0$ and $D$ together gains $(1-p)\varepsilon[E(\tilde R_2) - L]$. The liquidation probability $1-\gamma_0 = (I-A)/[pE(\tilde R_2) + (1-p)L]$ is interior in general, so $\gamma_0 = 0$ is not the rule.
> Ref: Topic 5 slides 4–11; Tirole Ch. 3 §3.8 (nonverifiable income, strategic default, p. 141); Amaro de Matos Ch. 5 §5.2.1 (pp. 134–137)
> Similar: Lista Topic 5, Ex. 3 (Amaro de Matos 5.2.5 #1); Lista Topic 5, Ex. 7 (Tirole 3.14)

Q: In a termination model with nonverifiable date-1 income, success probability $p$, a loan of $I - A$, a continuation value $E(\tilde R_2)$ to the borrower and a liquidation value $L < E(\tilde R_2)$ to the lender, the liquidation probability after a default report is $1-\gamma_0 = (I-A)/[pE(\tilde R_2) + (1-p)L]$. Through which channel does a higher $L$ lower it?
- A higher $L$ raises the borrower's own payoff after liquidation, so strategic default becomes less tempting and the same repayment $D$ is enforced with a smaller liquidation threat.
- A higher $L$ lets the borrower bribe the lender more cheaply once termination is decided, so renegotiation replaces part of the liquidation and its probability falls.
- A higher $L$ raises the value of continuing relative to stopping, so the borrower has more to lose from a default and repays more often for any given threat.
- A higher $L$ raises the lender's recovery after a default report, so break-even needs a smaller $D$, and a smaller $D$ is enforced by a smaller gap $(1-\gamma_0)E(\tilde R_2)$.
<!-- YW5zOjM= -->
> Solve the two binding constraints: $pD + (1-p)(1-\gamma_0)L = I - A$ and $D = (1-\gamma_0)E(\tilde R_2)$. $L$ enters only the lender's break-even: more recovery after a default report means less must be collected as $D$, and the incentive constraint then needs a smaller liquidation threat. The borrower gets nothing on liquidation, so $L$ does not touch her incentives; $E(\tilde R_2)$ is the separate "more to lose" channel; and a bribe must exceed $L$, so a higher $L$ makes renegotiation dearer, not cheaper.
> Ref: Topic 5 slides 7–11; Amaro de Matos Ch. 5 §5.2.1 (pp. 134–137)
> Similar: Lista Topic 5, Ex. 3 (Amaro de Matos 5.2.5 #1); Lista R7, Ex. 13

Q: Nonverifiable date-1 income is repaid only because non-payment triggers liquidation, which gives the lender $L$ but destroys a continuation value $E(\tilde R_2) > L$. Suppose that after the termination decision, but before it is carried out, the borrower can offer the lender a payment. What does this possibility do?
- The lender accepts any offer above $L$, so not paying costs the borrower only about $L$; ex ante less repayment is credible, and the loan is smaller, dearer or not made at all.
- It improves welfare: the deadweight loss $E(\tilde R_2) - L$ disappears whenever termination is triggered, and since the borrower pays the bribe, the lender's break-even is unaffected.
- It is neutral: lenders anticipate the bribe and raise the repayment $D$ by the same amount, so the borrower's incentive to report truthfully and the loan terms are unchanged.
- It hurts only the lender, whose bargaining power falls ex post, while the borrower's ex ante payoff is unchanged because she captures the whole surplus $E(\tilde R_2) - L$.
<!-- YW5zOjA= -->
> Renegotiation is efficient ex post and harmful ex ante. A borrower who diverted the income can pay a bribe slightly above $L$ (and below $E(\tilde R_2)$) and keep the project, so not paying costs her about $L$ instead of $E(\tilde R_2)$. The incentive constraint now caps $D$ near $L$, pledgeable income falls, and with $L < I - A$ financing may fail. The same two-sided nature of renegotiation appears in Topic 4B (it cures debt overhang ex post but softens incentives ex ante).
> Ref: Topic 5 slide 12; Topic 4B slides 27–31, 37–40; Tirole Ch. 3 §3.8 (p. 141)
> Similar: Lista Topic 5, Ex. 13 (Tirole 4.9); Lista Topic 5, Ex. 4 (Amaro de Matos 5.1.6 #3)

Q: A financially weak firm faces a deep-pocketed rival that can prey at date 0, destroying both firms' date-0 duopoly profit $D$, and gains $M - D$ if the weak firm is not refinanced at date 1. The weak firm's contract refinances with probability $z^S$ after date-0 success and $z^F$ after failure, and that gap is what motivates the entrepreneur's date-0 effort. What tension must the optimal contract resolve?
- Refinancing must become more sensitive to date-0 profit, with a larger $z^S - z^F$, so the rival expects predation to be met by harsher termination of the weak firm and is deterred.
- The entrepreneur must be paid more after a date-0 failure than after a success, $R_b^{FS} > R_b^{SS}$, so that predation, which causes failure, leaves her incentives intact.
- Deterring predation requires $z^S - z^F \le D/(M-D)$, a refinancing rule insensitive to date-0 profit, which weakens the very termination threat that motivates date-0 effort.
- The weak firm must pay its entrepreneur a date-0 bonus $r_b^S > 0$ after success, since retained earnings let it refinance alone and so remove the rival's gain $M - D$.
<!-- YW5zOjI= -->
> The predation-deterrence constraint is $D \ge (z^S - z^F)(M - D)$: the rival's date-0 cost must exceed its expected date-1 gain from lowering the weak firm's refinancing probability from $z^S$ to $z^F$. Date-0 incentives need $z^S R_b^S - z^F R_b^F \ge B_0/\Delta p$, i.e. a performance-sensitive continuation rule. The two pull in opposite directions. With fully general contracts (Tirole 7.7), $r_b^S = 0$ and $R_b^{SS} \ge R_b^{FS} = B/\Delta p$: rewarding failure is costly and is used only up to the incentive floor. Harsher termination is exactly what the predator wants.
> Ref: Tirole Ch. 7 §7.1.2 (Bolton–Scharfstein, pp. 290–294); Topic 5 slides 3, 6
> Similar: Lista Topic 5, Ex. 6 (Tirole 7.7); Lista R6, Ex. 7 (Tirole 5.2)

## struct

Q: A firm's assets are split between two creditors, and the pieces are worth more together than apart (synergy $\Delta > 0$). Compared with a single creditor, the creditors collect more after a strategic default but less after a liquidity default. When does the two-creditor structure lower the liquidation probability $\beta_\circ$?
- When the first-period success probability $q$ is high: defaults are then mostly strategic, and each creditor's veto over the synergy makes the manager's buy-back costlier.
- When $q$ is low: liquidity defaults are then frequent, and two creditors bidding against each other raise the price that outside buyers must pay for the assets.
- Always: the hold-up power of each creditor raises the recovery after both kinds of default, so the denominator of $\beta_\circ$ rises for every value of $q$.
- Never: dispersed creditors fail to coordinate, which lowers the recovery after both kinds of default, so $\beta_\circ$ rises for every value of $q$ and liquidation is more frequent.
<!-- YW5zOjA= -->
> $\beta_\circ = K/[q(y - S) + (1-q)L_\circ]$. With two creditors the manager keeps $S = y/2 - \Delta/6$ in a buy-back, so creditors get $y/2 + \Delta/6$; but the outside buyer's share also shrinks, fewer buyers show up, and $\overline L_\circ = L_\circ - \alpha^2\Delta^2/(36\bar c)$. The denominator rises iff $q\Delta/6 > (1-q)\alpha^2\Delta^2/(36\bar c)$, i.e. for $q$ above a threshold. Hold-up power deters strategic default but scares off buyers in a genuine failure.
> Ref: Amaro de Matos Ch. 5 §5.2.2 (Bolton–Scharfstein 1996, pp. 137–139); Topic 5 slides 2–3
> Similar: Lista Topic 5, Ex. 10 (Amaro de Matos 5.2.5 #2); Lista R7, Ex. 15

Q: In Diamond's (1991) model, lenders receive nonverifiable news at date 1 and upgrade or downgrade a borrower whose type, good or bad, only she knows; good firms enjoy a control rent $C$ while they keep control. Which statement about the good firms' maturity choice is correct?
- Good firms always prefer long-term debt, because it insures them against being repriced after a downgrade; short-term debt is chosen only by bad firms, which reveals their type.
- Good firms always prefer short-term debt, because the threat of liquidation after a downgrade disciplines management and so lowers the date-0 interest rate at every rating.
- With liquidation after a downgrade, the most highly rated firms switch to long-term debt, because they have the largest control rent $C$ to lose and the most to protect.
- Without liquidation they prefer short-term debt, to reprice after an upgrade; if a downgrade means liquidation, low-rated good firms, often downgraded, prefer long-term debt.
<!-- YW5zOjM= -->
> Long-term debt locks in the date-0 pooled price, so good firms subsidise bad ones for both periods; short-term debt lets an upgraded (good) firm refinance at a fair price. Without liquidation the payoff rises with the debt's value after a downgrade, and short-term debt wins (Lemma 5.2.1). If a downgraded short-term borrower is liquidated, the good firm loses $X + C$ in that state: $U_{ST} - U_{LT} = e(\widehat C - C)$, and with a low rating the downgrade probability $e$ is high, so long-term debt wins; with a high rating it reverses.
> Ref: Amaro de Matos Ch. 5 §5.2.3 (Diamond 1991, pp. 139–142)
> Similar: Lista Topic 5, Ex. 5 (Amaro de Matos 5.2.5 #5); Lista Topic 5, Ex. 12 (Amaro de Matos 5.2.5 #6)

## sov

Q: A small open economy with concave utility $u$ issues one-period non-contingent bonds and cannot be forced to repay; $B'$ is next period's assets ($B' < 0$ is debt), $y$ is output, i.i.d. with cdf $F$, and $V^d(y)$ and $V^c(B,y)$ are the values of defaulting and repaying. Which statement about default sets and the bond price $q(B')$ is correct?
- Default is likelier when output is high, as the country then lives better in autarky; default sets are upper intervals of $y$, and $q(B')$ rises with current output through that threshold.
- Default is likelier at low output, where concavity makes a net repayment cost more utility; default sets are lower intervals, and $q(B') = [1 - F(y^*(B'))]/(1+r)$ depends on $B'$ alone.
- Default depends on debt but not on output, as $V^d$ and $V^c$ shift equally with $y$; each default set is either empty or all of $Y$, so $q(B')$ is either $1/(1+r)$ or $0$.
- Default is likelier when output is low, since lenders refuse to roll over then; default sets are lower intervals, and $q(B')$ still depends on current $y$ through the threshold $y^*(B')$.
<!-- YW5zOjE= -->
> Claim 4: since $u(x) - u(x - k)$ rises as $x$ falls, a net repayment hurts more in a recession, so if $y_2 \in D(B)$ then every $y_1 \le y_2$ is too: $D(B) = [\underline y, y^*(B)]$. Claim 2 ($V^c$ rises with $B$, $V^d$ does not) makes default sets shrink as assets rise, so $q$ rises in $B'$. With i.i.d. output the default probability is $F(y^*(B'))$, the same whatever today's $y$; the price actually paid still varies with $y$, because the chosen $B'$ does. With persistent output, $q(B', y)$ would depend on $y$ through the conditional distribution of $y'$.
> Ref: Topic 5 slides 18, 21, 23–27
> Similar: Lista Topic 5, Ex. 14 and Ex. 15 (original exercises on the slides)

Q: In the i.i.d. sovereign-debt model with permanent exclusion after default ($\theta = 0$) and no output cost ($h(y) = y$), one proves: if the default set $D(B)$ is non-empty, no bond position $\hat B$ on offer gives a net capital inflow $B - q(\hat B)\hat B > 0$. What does this result say?
- The country can never borrow: any debt makes default possible in some state, so no net inflow is ever available, and in equilibrium the country holds $B' = 0$ in every period.
- It hinges on $h(y) = y$: with an output cost $h(y) < y$ default is costlier, so default states can coexist with net inflows and the country rolls its debt over in a recession.
- At debt levels where default is possible the market offers only net repayment; a debt-free country has $D(0) = \emptyset$ and can borrow, and output costs strengthen the result.
- Default occurs only when lenders refuse new loans for reasons unrelated to fundamentals, so a default set is non-empty only during a self-fulfilling run on the country's debt.
<!-- YW5zOjI= -->
> Proof: for $y \in D(B)$, $V^d(y) > V^c(B,y) \ge u(y + B - q(\hat B)\hat B) + \beta E[V^o(\hat B, \tilde y')]$, and $V^d(y) = u(y) + \beta E[V^d(\tilde y')]$ with $V^o \ge V^d$, so $u(y) > u(y + B - q\hat B)$: the flow must be a net repayment. The result restricts flows only where default is possible; at $B = 0$ choosing $B' = 0$ already matches autarky, so $D(0) = \emptyset$ and borrowing is open. With $h(y) < y$ the bound tightens to $B - q\hat B < -[y - h(y)]$; only $\theta = 0$ is essential. Reading it as "no borrowing" is the common mistake.
> Ref: Topic 5 slides 17–22, 25
> Similar: Lista Topic 5, Ex. 16 (original exercise on Claim 3, parts (b), (d), (e))

Q: In an i.i.d. sovereign-debt model with permanent exclusion after default, a country whose default set $D(B)$ is non-empty can never obtain a net inflow $B - q(\hat B)\hat B > 0$. What happens to this result if a defaulter instead regains market access with probability $\theta > 0$ each period?
- It can fail: default may return the country to markets debt-free, worth $V^o(0,\cdot) \ge V^o(\hat B,\cdot)$, whereas rolling over keeps the debt; that can beat a small inflow.
- It fails because lenders now recover part of the defaulted debt at re-entry, so bond prices stay high in default states and the country can borrow even where $D(B)$ is non-empty.
- It holds a fortiori: re-entry lowers the value of default $V^d$, since the country must face its lenders again, so default sets shrink and inflows become even rarer.
- It is unaffected: $\theta$ enters $V^d$ only through $V^d$ itself, so the comparison between default and an inflow does not change; only an output cost $h(y) < y$ could alter it.
<!-- YW5zOjA= -->
> With re-entry, $V^d(y) = u(h(y)) + \beta E[\theta V^o(0, \tilde y') + (1-\theta)V^d(\tilde y')]$, and the right side of the key inequality becomes $\beta\theta E[V^o(\hat B, \cdot) - V^o(0, \cdot)] + \beta(1-\theta)E[V^o(\hat B, \cdot) - V^d(\cdot)]$. The second term is still $\ge 0$, but the first is $\le 0$ for $\hat B < 0$, because $V^o$ is nondecreasing in assets (Claim 1). Default now wipes out the debt, which rolling over does not. There is no recovery in this model, and $V^d$ rises, not falls, with $\theta$.
> Ref: Topic 5 slides 17, 20, 23, 25
> Similar: Lista Topic 5, Ex. 16(f) (original exercise)

Q: In the Eaton–Gersovitz model with i.i.d. output, permanent exclusion after default and no output cost, very little debt can be sustained. Why, and what do an output cost in autarky and a positive re-entry probability do to the country's borrowing capacity?
- Little debt because lenders can seize nothing; an output cost lowers capacity, since recessions in autarky make default states more frequent, and re-entry raises it, since lenders expect the country back.
- Little debt because, as in Bulow and Rogoff, a defaulter can still save abroad and smooth its consumption; output costs and re-entry barely matter, since the saving option already sets the punishment.
- Little debt because the world interest rate exceeds the country's growth rate; an output cost raises capacity and re-entry raises it too, since both make lenders more willing to roll the debt over.
- The only punishment is losing the use of non-contingent bonds to smooth small shocks, worth little; an output cost adds a sure loss in each autarky period and raises capacity, re-entry cuts it.
<!-- YW5zOjM= -->
> A sovereign's debt is worth what it loses by walking away. With $h(y) = y$ that is only the smoothing value of one-period bonds, small for modest i.i.d. shocks (a grid solution of the original exercise sustains risk-free debt near 1% of mean output). A 2% output cost raises it to about 42%; re-entry with probability 0.5 cuts it to under 4%, since the punishment lasts two periods on average. Here exclusion is outright, so the Bulow–Rogoff saving channel (which gives no lending at all) is absent, and lenders never seize anything.
> Ref: Topic 5 slides 17, 20, 24, 29; Tirole Ch. 3 §3.8 (sovereign debt literature, pp. 143–144)
> Similar: Lista Topic 5, Ex. 17 (original exercise, part (e)); Lista Topic 5, Ex. 14
