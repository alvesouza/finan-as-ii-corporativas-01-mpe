---
quiz: "Class 1 · Quiz 3 — Pledgeable income and credit rationing"
tags:
  fim: "Fixed-investment model: derivation"
  cs: "Comparative statics and the MM limit"
  interp: "Interpretation and links to the facts"
---

## fim

P: Tirole's fixed-investment model. An entrepreneur with net worth $A$ needs investment $I > A$ and borrows $I - A$. The project yields verifiable income $R$ on success and $0$ on failure. If she behaves, success has probability $p_H$ and she gets no private benefit; if she shirks, success has probability $p_L < p_H$ and she enjoys private benefit $B > 0$. Let $\Delta p \equiv p_H - p_L$. Everyone is risk neutral, the interest rate is $0$, she has limited liability, and lenders are competitive. The contract pays her $R_b$ and the lenders $R_l = R - R_b$ on success, and both $0$ on failure.

Q: Which incentive constraint must the contract satisfy, and what minimum stake on success does it imply?
- $p_H R_b \ge p_L R_b + B$, which reduces to $R_b \ge B/p_L$: the stake must cover the private benefit scaled by the shirking odds
- $p_H R_b \ge B$, which reduces to $R_b \ge B/p_H$: the expected stake from behaving must cover the private benefit
- $p_H R_b \ge p_L R_b + B$, which reduces to $R_b \ge p_H B/\Delta p$: the stake must cover the agency rent on success
- $p_H R_b \ge p_L R_b + B$, which reduces to $R_b \ge B/\Delta p$: the stake must make behaving at least as good as shirking
<!-- YW5zOjM= -->
> Behaving gives $p_HR_b$; shirking gives $p_LR_b+B$. The constraint $(\Delta p)R_b\ge B$ gives the minimum stake $B/\Delta p$, paid on success. $p_HB/\Delta p$ is the agency rent, an expected payoff, not the stake.
> Ref: Tirole, Ch. 3 §3.2.2, p. 116, constraint (ICb); Class 1 notes §5
> Similar: Tirole, Ch. 3, exercise 3.2 (p. 144)

Q: What is the expected pledgeable income $\mathcal{P}$ — the most lenders can expect without destroying her incentive to behave?
- $\mathcal{P} = p_H R - B$, since lenders get expected income less the private benefit she gives up by behaving
- $\mathcal{P} = p_H\left(R - B/\Delta p\right)$, since lenders can be promised at most $R - B/\Delta p$ on success
- $\mathcal{P} = p_H R - B/\Delta p$, since the minimum stake is deducted from expected income once, at face value
- $\mathcal{P} = \Delta p\,(R - B)$, since only the effort-driven part of the success probability backs the loan
<!-- YW5zOjE= -->
> The maximum promise on success is $R-B/\Delta p$, received with probability $p_H$, so $\mathcal{P}=p_H(R-B/\Delta p)$. The third option forgets that the stake is paid only on success and must be weighted by $p_H$.
> Ref: Tirole, Ch. 3 §3.2.2, p. 116; Class 1 notes §5
> Similar: Tirole, Ch. 3, exercise 3.1 (p. 144)

Q: Lenders fund the project only if $\mathcal{P} \ge I - A$. Which threshold $\bar{A}$ on net worth does this give, and what are its two terms?
- $\bar{A} = B/\Delta p - (p_H R - I)$: the minimum stake on success minus the project's net present value
- $\bar{A} = p_H B/\Delta p + (p_H R - I)$: the agency rent plus the net present value the lenders must also be paid
- $\bar{A} = p_H B/\Delta p - (p_H R - I)$: the agency rent minus the project's net present value
- $\bar{A} = p_H B/\Delta p - (R - I)$: the agency rent minus the project's income net of the outlay on success
<!-- YW5zOjI= -->
> $p_H(R-B/\Delta p)\ge I-A \iff A\ge p_HB/\Delta p-(p_HR-I)$, equation (3.3). Funding needs net worth at least equal to the agency rent net of the NPV; equivalently $\mathcal{P}-(I-A)=A-\bar A$.
> Ref: Tirole, Ch. 3 §3.2.2, p. 117, equation (3.3); Class 1 notes §5
> Similar: Tirole, Ch. 3, exercise 3.15 (p. 150)

## cs

P: Same model: net worth $A$, investment $I > A$, income $R$ on success and $0$ on failure, success probability $p_H$ if she behaves and $p_L < p_H$ if she shirks with private benefit $B \ge 0$, $\Delta p = p_H - p_L$, risk neutrality, zero interest rate, limited liability, competitive lenders. She is funded iff $A \ge \bar{A} = p_H B/\Delta p - (p_H R - I)$; a higher $\bar{A}$ means she is harder to fund.

Q: What is $\partial \bar{A}/\partial p_L$, holding $p_H$, $B$, $R$ and $I$ fixed, and what does its sign mean?
- $p_H B/(\Delta p)^2 > 0$: as shirking succeeds more often anyway, output says less about effort, so funding gets harder
- $-p_H B/(\Delta p)^2 < 0$: as shirking becomes more likely to succeed anyway, the project is safer, so funding gets easier
- $p_H B/\Delta p > 0$: a higher $p_L$ raises the agency rent one for one with the private benefit, so funding gets harder
- $B/(\Delta p)^2 > 0$: a higher $p_L$ raises the minimum stake on success but leaves the agency rent unchanged
<!-- YW5zOjA= -->
> $\bar A$ depends on $p_L$ only through $\Delta p$; $\partial(p_HB/\Delta p)/\partial p_L=p_HB/(\Delta p)^2>0$. The likelihood ratio $\Delta p/p_H$ falls, so the outcome is a worse signal of effort. The project is not safer, because she behaves in equilibrium and succeeds with $p_H$.
> Ref: Tirole, Ch. 3 §3.2.2, p. 118; Class 1 notes §5, comparative statics
> Similar: Tirole, Ch. 3, exercise 3.10 (p. 148)

Q: What is $\partial \bar{A}/\partial p_H$, holding $p_L$, $B$, $R$ and $I$ fixed?
- $-R + p_L B/(\Delta p)^2$, ambiguous: a higher $p_H$ raises NPV but also raises the agency rent through its first factor
- $-R - p_H B/(\Delta p)^2 < 0$: a higher $p_H$ raises NPV and lowers the agency rent through the denominator
- $-R - p_L B/(\Delta p)^2 < 0$: a higher $p_H$ raises NPV and, net of both effects on the rent, lowers the agency rent
- $-R + B/\Delta p$, ambiguous: a higher $p_H$ raises NPV but raises the minimum stake that must be left on success
<!-- YW5zOjI= -->
> $\partial(p_HB/\Delta p)/\partial p_H=B(\Delta p-p_H)/(\Delta p)^2=-p_LB/(\Delta p)^2$, and $\partial[-(p_HR-I)]/\partial p_H=-R$. Both terms are negative, so funding gets easier. The second option ignores that $p_H$ also appears in the numerator.
> Ref: Tirole, Ch. 3 §3.2.2, p. 118; Class 1 notes §5, comparative statics
> Similar: Tirole, Ch. 3, exercise 3.15 (p. 150)

Q: Let the private benefit $B \to 0$, so that behaviour is effectively contractible. What happens to $\bar{A}$ and to funding?
- $\bar{A} \to p_H B/\Delta p$, the agency rent alone, so only founders with net worth above that rent are funded
- $\bar{A} \to I$, because without moral hazard lenders demand full collateral, so funding requires $A \ge I$
- $\bar{A} \to 0$, because the agency problem vanishes, so every founder with positive net worth is funded
- $\bar{A} \to -(p_H R - I) < 0$, so under (3.1) every positive-NPV project is funded whatever $A$: the MM world
<!-- YW5zOjM= -->
> With $B=0$ the agency rent vanishes and $\bar A=-(p_HR-I)$, negative whenever the NPV is positive, so net worth no longer matters: every positive-NPV project is funded, as in Modigliani–Miller. One assumption separates the two worlds.
> Ref: Tirole, Ch. 3 §3.2.2, p. 117; Ch. 2 §2.2, p. 79; Class 1 notes §5
> Similar: Tirole, Ch. 3, exercise 3.1 (p. 144)

## interp

P: Same model: net worth $A$, investment $I > A$, income $R$ on success and $0$ on failure, success probability $p_H$ if she behaves and $p_L < p_H$ if she shirks with private benefit $B > 0$, $\Delta p = p_H - p_L$, risk neutrality, zero interest rate, limited liability, competitive lenders. Funding requires $A \ge \bar{A} = p_H B/\Delta p - (p_H R - I)$. Assume the NPV $p_H R - I$ is positive and $p_L R - I + B < 0$.

Q: A founder with $A < \bar{A}$ offers lenders a much higher repayment $R_l$ on success. Why do competitive lenders still refuse?
- A higher $R_l$ leaves her a stake below $B/\Delta p$, so she shirks; as $p_L R - I + B < 0$, a loan that tolerates it loses money
- A higher $R_l$ breaches limited liability, since she cannot repay more than $R$, so any promise above $p_H R$ is not credible
- A higher $R_l$ signals that her project is riskier than average, so lenders infer a lower $p_H$ and the breakeven fails
- A higher $R_l$ is usury above the competitive rate, so lenders who accept it are undercut by rivals at the zero rate
<!-- YW5zOjA= -->
> Raising $R_l$ lowers $R_b=R-R_l$ below the minimum stake, so she shirks. Assumption (3.2) means the project then has negative value even with $B$ counted, so lenders lose. This is moral hazard, not signalling (adverse selection), and not a limited-liability issue at $R_l\le R$.
> Ref: Tirole, Ch. 3 §3.2.1–3.2.2, pp. 116–117; Class 1 notes §5
> Similar: Tirole, Ch. 3, exercise 3.13 (p. 149)

Q: When she is funded, lenders break even with $p_H R_l = I - A$. What is the gross loan rate $1 + \iota = R_l/(I - A)$, and how should it be read?
- $1 + \iota = 1/(p_H - p_L)$, an incentive premium: the rate rises as effort becomes harder to infer from output
- $1 + \iota = 1/p_H$, a pure default premium: the investors' expected return is still the zero market rate
- $1 + \iota = 1/p_H$, the investors' expected gross return, which exceeds one to compensate them for moral hazard
- $1 + \iota = R/(I - A)$, the project's gross return per unit lent, all of which the lenders capture on success
<!-- YW5zOjE= -->
> From $p_HR_l=I-A$, $R_l/(I-A)=1/p_H$. The nominal rate exceeds the market rate only because the loan pays nothing on failure; lenders' expected return stays zero. It is not an incentive premium, and the founder, not the lenders, keeps the surplus.
> Ref: Tirole, Ch. 3 §3.2.1, p. 116; Class 1 notes §5
> Similar: Tirole, Ch. 3, exercise 3.13 (p. 149)

Q: Which description of the founder's net utility $U_b$, net of the consumption value of $A$, is correct?
- $U_b = p_H R_b - A$ for every $A$, rising smoothly with net worth, since a larger $A$ lowers $R_l$ and raises her stake
- $U_b = p_H B/\Delta p$ when funded, the agency rent, since lenders take the NPV and she keeps only the rent
- $U_b = (p_H R - I)\,A/I$, proportional to net worth, since she owns a fraction $A/I$ of the project's equity
- $U_b = 0$ if $A < \bar{A}$ and $p_H R - I$ if $A \ge \bar{A}$: a jump, since lenders leave her the whole NPV
<!-- YW5zOjM= -->
> With lenders at zero profit, $U_b=p_H(R-R_l)-A=p_HR-I$ once funded, equation (3.6). Utility jumps at $\bar A$: one more unit of net worth near the threshold is worth more than one unit to her, the shadow value of net worth exceeding one.
> Ref: Tirole, Ch. 3 §3.2.2, p. 117, equation (3.6); Class 1 notes §5
> Similar: Tirole, Ch. 3, exercise 3.20 (p. 152)

P:

Q: In the fixed-investment model, funding requires net worth $A$ at least $\bar{A} = p_H B/\Delta p - (p_H R - I)$, where $B$ is the private benefit from shirking. Which pair of Tirole's stylized facts does this threshold rationalize, and through which parameter?
- Reliance on retentions through $A$, since kept earnings raise net worth; and the value of investor protection and monitoring through $B$, which they lower
- The negative announcement return to equity through $B$, since issuing shares raises the private benefit; and high bank leverage through $p_H$, which banks raise
- The dominance of bonds in North America through $R$, since market finance raises income; and market timing through $I$, which falls in upswings
- The small share of new equity through $\Delta p$, since equity dilutes effort; and countercyclical bank finance through $A$, which rises in recessions
<!-- YW5zOjA= -->
> Net worth $A$ lowers the funding gap one for one, matching the reliance on internal funds; investor protection and monitoring work by lowering $B$, which lowers $\bar A$. Announcement returns need asymmetric information (Classes 11–12), which this model does not contain.
> Ref: Tirole, Ch. 3 §3.2.2, pp. 117–118; Ch. 2 §2.5–2.6, pp. 95–102; Class 1 notes §4–5
> Similar: Ross Fundamentos, Cap. 16, CQ 16.4 (p. 575)
