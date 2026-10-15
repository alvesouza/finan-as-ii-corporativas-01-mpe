---
quiz: "Class 1 · Quiz 2 — The Modigliani–Miller benchmark and the stylized facts"
tags:
  mm: "Modigliani–Miller benchmark"
  facts: "Stylized facts of corporate financing"
---

## mm

Q: A firm's income $R \ge 0$ is random; it has issued debt with face value $D > 0$ and the residual goes to equity, both under limited liability. Which state-by-state identity drives Tirole's value-additivity argument, and why does $D$ disappear?
- $\max(0, R-D) + \min(R, D) = R - D$ in every state, so total value is $E(R) - D$ and $D$ disappears only when the debt is riskless and priced at face value.
- $\max(0, R-D) + \min(R, D) = \max(R, D)$ in every state, so total value is $E[\max(R,D)]$, which is independent of $D$ only when $D$ lies below the support of $R$.
- $\max(0, R-D) + \min(R, D) = R$ in every state: if $R \ge D$ the sum is $(R-D)+D$, if $R<D$ it is $0+R$, so taking expectations leaves $E(R)$, free of $D$.
- $\max(0, R-D) + \min(R, D) = R$ only on average, not state by state, so total value equals $E(R)$ after integrating over the distribution of $R$ against the face value $D$.
<!-- YW5zOjI= -->
> The case split gives $R$ in both cases, state by state, so $V_E+V_D=E[\max(0,R-D)]+E[\min(R,D)]=E(R)$ with no $D$ left. The identity is exact pointwise, which is what lets it survive risk aversion (state prices) as well.
> Ref: Tirole, Ch. 2 §2.2, p. 78; Class 1 notes §3.1
> Similar: Ross Fundamentos, Cap. 16, CQ 16.2 (p. 575)

Q: Investors are risk averse, and $q(\omega) > 0$ is the price today of one unit of income in state $\omega$. The firm's income in state $\omega$ is $R(\omega) \ge 0$, split between debt with face value $D$ and equity. What is the total value of the firm, and does it depend on $D$?
- $\sum_\omega q(\omega) R(\omega)$, independent of $D$: apply state prices to the pointwise identity $\max(0,R-D)+\min(R,D)=R$, so additivity needs no risk neutrality.
- $E[R]$, independent of $D$: state prices only rescale probabilities, so under risk aversion the firm is still worth its expected income as in the risk-neutral case.
- $\sum_\omega q(\omega) R(\omega)$ plus a term in $D$: the debt carries a risk premium that equity does not, so total value rises with $D$ when investors are risk averse.
- $\sum_\omega q(\omega)\max(0, R(\omega)-D)$, decreasing in $D$: with risk aversion only equity is priced by state prices, while debt is valued at its face amount $D$.
<!-- YW5zOjA= -->
> Tirole's footnote: risk neutrality is not needed, because with state-contingent prices the sum of the two claims' values is $\sum q(\omega)[\max(0,R-D)+\min(R,D)]=\sum q(\omega)R(\omega)$. The value is not $E[R]$ under risk aversion, and debt is priced by the same state prices as equity.
> Ref: Tirole, Ch. 2 §2.2, p. 78 (footnotes 8–9); Class 1 notes §3.1
> Similar: Amaro de Matos, §2.1.5, exercise 2 (p. 48)

P: An all-equity firm lives at dates $t=0,1,2,\dots$. At date $t$ it earns revenue $R_t$, pays a dividend $d_t$ per share, has $n_t$ shares, and sinks investment $I_t$; $P_t$ is the end-of-date share price and $\beta$ the discount factor. Arbitrage: $P_t = \beta E[d_{t+1} + P_{t+1}]$. Cash identity: $R_t + P_t(n_t - n_{t-1}) = n_{t-1}d_t + I_t$. Let $V_t \equiv n_t P_t$.

Q: Which recursion for $V_t$ follows from substituting the cash identity at date $t+1$?
- $V_t = \beta E[R_{t+1} + V_{t+1}]$, because investment is sunk and drops out of the identity once dividends are replaced
- $V_t = \beta E[R_{t+1} - I_{t+1} - (n_{t+1}-n_t)P_{t+1} + V_{t+1}]$, with the issuance term kept separately
- $V_t = \beta E[d_{t+1} + V_{t+1}]$, since each share's dividend is the only cash that leaves the firm at date $t+1$
- $V_t = \beta E[R_{t+1} - I_{t+1} + V_{t+1}]$, after the issuance term and $n_t P_{t+1}$ combine into $n_{t+1}P_{t+1}$
<!-- YW5zOjM= -->
> $V_t=\beta E[n_t d_{t+1}+n_tP_{t+1}]$; the identity at $t+1$ gives $n_t d_{t+1}=R_{t+1}-I_{t+1}+(n_{t+1}-n_t)P_{t+1}$; adding $n_tP_{t+1}$ yields $n_{t+1}P_{t+1}=V_{t+1}$. Iterating gives $V_t=E[\sum_{\tau\ge1}\beta^\tau(R_{t+\tau}-I_{t+\tau})]$.
> Ref: Tirole, Ch. 2 §2.2, p. 78; Class 1 notes §3.2
> Similar: Ross Fundamentos, Cap. 16, CQ 16.2 (p. 575)

Q: Suppose the firm raises its dividend at date $t+1$ and finances it by issuing new shares at $P_{t+1}$. Why does this leave $V_t$ unchanged?
- Because the new shares are issued at a discount, and the discount exactly offsets the higher dividend in the cash identity, leaving revenue minus investment as before.
- Because new shareholders pay $P_{t+1}$ per share, exactly what the shares are worth, so issuance moves cash without creating value and the term merges into $V_{t+1}$.
- Because dividends are irrelevant only when the firm has no investment, so with $I_{t+1}=0$ the higher payout is absorbed entirely by the lower share price.
- Because the discount factor $\beta$ adjusts to the new payout policy, so the higher dividend is discounted more heavily and the present value is restored exactly.
<!-- YW5zOjE= -->
> The issuance term $(n_{t+1}-n_t)P_{t+1}$ is cash in at a fair price; it funds the extra dividend and combines with $n_tP_{t+1}$ into $V_{t+1}$. What remains is revenue minus investment: value depends on real decisions only. No discount, no condition on $I$, no change in $\beta$ is involved.
> Ref: Tirole, Ch. 2 §2.2, p. 78; Class 1 notes §3.2
> Similar: Ross Fundamentos, Cap. 16, problem 16.8 (p. 577)

P:

Q: Tirole says the split of the corporate pie matters "whenever managerial decisions cannot be perfectly specified contractually". In which scenario does Modigliani–Miller fail for exactly that reason?
- Investors are risk averse, so equity and debt carry different risk premia and the firm's value now depends on how its income is divided between the two claims.
- The firm switches from paying dividends to repurchasing shares, so the number of shares outstanding falls and the share price rises by the same proportion as before.
- The firm issues junior instead of senior debt, so creditors bear more default risk and demand a higher promised rate on the same expected repayment.
- A higher face value of debt changes the manager's non-contractible effort, so the distribution of income itself, and hence expected income, depends on the debt level.
<!-- YW5zOjM= -->
> MM fails when income depends on the claim structure through incentives: if debt changes what the manager does and that cannot be contracted, $E(R)$ moves with $D$. Risk aversion, payout form and seniority all leave value additivity intact.
> Ref: Tirole, Ch. 2 §2.2, p. 79; Class 1 notes §3.3
> Similar: Ross Fundamentos, Cap. 16, CQ 16.4 (p. 575)

## facts

Q: Rajan and Zingales find that in 1984–86 new share issues were about 65% of US external financing while buybacks and other equity reductions were about 68%. Which reading matches Tirole's own caveat about these numbers?
- Net equity issuance was negative, and since retentions are also shareholders' money, the puzzle is why leaving profits in is easier than buying new shares.
- Net equity issuance was negative, which shows that shareholders contributed nothing to US firms in the period, so all investment was financed by creditors.
- Gross equity issuance was large, which shows that equity was the main source of finance, and the buybacks reflect a tax motive that is unrelated to financing.
- Net equity issuance was close to zero, which is exactly what MM predicts, because firms should be indifferent between issuing and retiring their own shares.
<!-- YW5zOjA= -->
> "Basically all external financing was debt" — but Tirole warns not to over-read "internal": retentions are cash shareholders agree to leave in the firm. The real puzzle is the cost of the other route, new shares. MM predicts no particular pattern at all, not zero net issuance.
> Ref: Tirole, Ch. 2 §2.5, p. 97; Class 1 notes §4
> Similar: Higgins 13e, Ch. 4, problem 4.5 (p. 135)

Q: Two-day abnormal returns on announcement average −3.1% for common stock, −2.0% for convertible bonds and an insignificant −0.3% for straight bonds, while bank loan announcements raise the share price. What does MM predict, and what does the ranking point to?
- MM predicts the same negative return for every issue, equal to the issue's cost; the ranking just reflects that equity issues are larger and cost more to underwrite.
- MM predicts zero for every announcement; the ranking follows how sensitive each claim is to insiders' information, and the loan effect suggests bank monitoring.
- MM predicts a positive return for debt and a negative one for equity, because leverage adds value; the ranking confirms MM once the tax shield on debt is counted.
- MM predicts zero only for straight debt; equity falls because it dilutes earnings per share, which reduces value even with no change in the firm's cash flows.
<!-- YW5zOjE= -->
> If the split does not change the pie, announcing the split cannot move its value: every return should be zero. The more a claim's value depends on what insiders know, the worse the news; straight debt is least information-sensitive. A positive loan announcement is consistent with banks screening and monitoring. The explanation is asymmetric information (Classes 11–12), stated here as a fact only.
> Ref: Tirole, Ch. 2 §2.5, Table 2.6, p. 101; Class 1 notes §4
> Similar: Ross Fundamentos, Cap. 16, CQ 16.4 (p. 575)

Q: Leverage is typically around two times equity, banks near eleven, and high-debt firms tend to have steady cash flows and resaleable assets, while risky, intangible-heavy firms borrow little. Which explanation fits the class's argument best?
- Firms with intangible value borrow little because they need little external finance, since research and brands are funded entirely from retained earnings.
- Steady firms borrow more because MM implies that safe cash flows make debt cheaper than equity, so value rises with leverage until the debt becomes risky.
- Debt is easy against what outsiders can count on without trusting the insider — cash that arrives regardless of effort and assets that can be seized and sold.
- Banks borrow eleven times equity because regulation forces it, and the cross-firm pattern is unrelated to incentives, reflecting differences in tax rates by industry.
<!-- YW5zOjI= -->
> Collateral and effort-independent cash flow are pledgeable; value that depends on what the insider does next is not. That is the pledgeable-income logic of §3.2 (and Class 7). MM implies no cost advantage of debt; intangible firms are often the ones that most need outside money.
> Ref: Tirole, Ch. 2 §2.5, Table 2.4, pp. 98–100; Class 1 notes §4
> Similar: Ross Fundamentos, Cap. 16, CQ 16.4 (p. 575)

Q: In 2002, bonds were about 15.6% of US non-financial firms' liabilities against 2.3% in Germany, while loans were about 10% in the US against 43% in Germany. Why would this difference matter if a unit of debt is a unit of debt?
- It matters only for the tax treatment of interest, which differs across the two countries and therefore changes the after-tax cost of each form of debt.
- It matters because bank loans are always senior to bonds, so German firms face lower default costs and can sustain higher leverage at the same risk.
- It does not matter in the class's framework: by value additivity, the mix of lenders is a pure split of the pie and leaves firm value and behaviour unchanged.
- A bank can monitor and renegotiate, while dispersed bondholders mostly read prices and exit, so the lender mix changes what insiders can get away with.
<!-- YW5zOjM= -->
> Market-based vs. bank-based systems map onto active vs. speculative monitoring from Ch. 1. Once insiders' behaviour is non-contractible, who holds the debt affects incentives, so value additivity no longer settles the question.
> Ref: Tirole, Ch. 2 §2.5, Table 2.5, p. 99; Ch. 1 §1.2; Class 1 notes §4
> Similar: Ross Fundamentos, Cap. 1, CQ 1.7 (p. 22)

Q: Firms issue equity more often in upswings and after their own share price has risen, and buy shares back after it has fallen. Why is this timing a problem for the MM benchmark?
- MM predicts that firms should issue in booms because investment is more productive then, so timing confirms MM as long as investment rises with the cycle.
- MM gives firms no reason to time issues, so systematic timing suggests that financing costs vary with information or agency frictions over the cycle.
- MM predicts buybacks after price falls because shares are cheap, so the pattern confirms that managers maximize value by trading in their own shares.
- MM fails only for small firms, which are hit harder in downturns, so timing by large firms is consistent with the benchmark and needs no extra friction.
<!-- YW5zOjE= -->
> If financing were irrelevant, there would be nothing to gain from timing it; firms time it constantly. Tirole lists candidate explanations (milder adverse selection in good times, more productive investment, bubbles, irrational markets) without choosing; all require a departure from MM.
> Ref: Tirole, Ch. 2 §2.5, p. 101; §2.6, p. 102; Class 1 notes §4
> Similar: Higgins 13e, Ch. 4, problem 4.6 (p. 135)
