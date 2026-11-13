---
quiz: "Liquidity and risk management (hard) — liquidity shocks, maturity, hedging"
tags:
  liq: "Liquidity shocks, cutoffs, credit lines and hoarding"
  mat: "Maturity, free cash flow and excess cash"
  hedge: "Hedging and indexed debt"
---

## liq

Q: A firm invests $I$ at date 0; at date 1 it must reinvest a random $\rho$ to continue, and continuation yields $\rho_1 = p_H R$ in expectation, of which only $\rho_0 = p_H(R - B/\Delta p)$ is pledgeable. When the balance sheet is too weak for the first best but strong enough to be financed, where does the optimal cutoff $\rho^*$ lie, and why?
- $\rho^* = \rho_0$: investors finance only the shocks the date-1 market would refinance, since a rescue beyond pledgeable income is a loss that no competitive investor would accept.
- $\rho^* > \rho_1$: continuation also preserves the manager's rent $p_H B/\Delta p$, which counts in the firm's value, so the firm rescues even some shocks above the expected income $p_H R$.
- $\rho_0 < \rho^* < \rho_1$: NPV rises with the cutoff up to $\rho_1$ and pledgeable income peaks at $\rho_0$, so the firm trades some NPV for pledgeability but never cuts below $\rho_0$.
- $\rho^* = \rho_1$: the first-best cutoff always survives, and a weak balance sheet only scales down the date-0 investment, because liquidity and scale are two separate decisions.
<!-- YW5zOjI= -->
> $U_b(\rho^*) = r + F(\rho^*)p_H R - I - \int_0^{\rho^*}\rho f(\rho)d\rho$ rises with $\rho^*$ until $\rho_1$; pledgeable income $r + F(\rho^*)\rho_0 - \int_0^{\rho^*}\rho f(\rho)d\rho$ rises until $\rho_0$. In the intermediate region the binding break-even fixes $\rho^* \in (\rho_0, \rho_1)$: liquidation is ex post inefficient (some shocks below $p_H R$ are not met) to raise the cash investors can recover, but cutting below $\rho_0$ would lower both NPV and pledgeable income. $\rho_1$ already contains the manager's rent.
> Ref: Tirole Ch. 5 §5.2.1 (pp. 202–204), §5.3.2 (pp. 209–210)
> Similar: Lista R6, Ex. 13 (Tirole 5.6); Lista R6, Ex. 8 (Tirole 5.5)

Q: A firm with no date-1 income needs a reinvestment $\rho$ at date 1 and should continue whenever $\rho \le \rho^*$, where $\rho^*$ exceeds the date-1 pledgeable income $\rho_0 = p_H(R - B/\Delta p)$. Which way of preparing for the shock implements this policy?
- Secure at date 0 a nonrevocable credit line of $\rho^* - \rho_0$ plus the right to dilute existing claims at date 1, or a line of $\rho^*$ with no right to dilute.
- Wait and see: at date 1 the firm sells new shares to fresh investors, who will pay up to the full continuation value $\rho_1 = p_H R$, which already exceeds the cutoff $\rho^*$.
- Secure a credit line of $\rho^* - \rho_0$ and forbid any dilution at date 1, since new shares issued then would only transfer value away from the initial investors.
- Secure a revocable credit line of $\rho^*$: the bank will honour it for every $\rho \le \rho^*$, because continuation is efficient there and the bank shares in its value.
<!-- YW5zOjA= -->
> Returning to the market at date 1, the firm can raise at most the pledgeable income $\rho_0$ by diluting old claims; investors never pay more than the firm is worth to them. Shocks in $(\rho_0, \rho^*]$ must be covered by liquidity arranged in advance: a line of $\rho^*$ with no dilution, or $\rho^* - \rho_0$ with dilution rights. The line must be nonrevocable: for $\rho > \rho_0$ the bank loses money on the rescue and would walk away. Forbidding dilution with only $\rho^* - \rho_0$ leaves the firm short.
> Ref: Tirole Ch. 5 §5.2.3 (credit lines for cash-poor firms, pp. 205–206)
> Similar: Lista R6, Ex. 14 (Tirole 5.10), part (iv); Lista R6, Ex. 7 (Tirole 5.2)

Q: Compare two commitments. (1) A credit line funds every reinvestment need $\rho \le \rho^*$, with $\rho_0 < \rho^* < \rho_1$. (2) To motivate date-0 effort, a contract refuses to fund a date-1 project after a low date-0 profit, although that project's pledgeable income exceeds its cost. Which commitment survives renegotiation once the date-1 information is known?
- Both: competitive investors write efficient contracts at date 0, and an efficient contract leaves no gains from trade to be shared by the parties once the date-0 outcome is known.
- Only the second: refusing to fund after a low profit is efficient ex post, while the line is stretched to every $\rho$ up to $\rho_1$, since both parties gain from the extra continuation.
- Neither: the line is renegotiated down when $\rho$ is small, as the bank pays the firm not to draw on it, and the refusal is renegotiated whenever the project has negative NPV.
- Only the first: inside the line continuation is efficient and the borrower's rent cannot be squeezed, while after a low profit both sides gain from funding a project that pays for itself.
<!-- YW5zOjM= -->
> For $\rho \le \rho^* < p_H R$ continuing is efficient, so paying the firm not to draw would destroy surplus; for $\rho^* < \rho \le p_H R$ extending the line is efficient but the borrower cannot compensate the lender, because her stake $B/\Delta p$ is incompressible. So the line is renegotiation-proof. The termination threat is different: if the project's pledgeable income exceeds its cost, investors themselves want to fund it ex post, the threat is not credible, and date-0 incentives must be paid in money, which uses up pledgeable income.
> Ref: Tirole Ch. 5 §5.2.3, remark on renegotiation (pp. 205–206); Tirole Ch. 5 exercises 5.1 and 5.2 (p. 229)
> Similar: Lista R6, Ex. 6 (Tirole 5.1), part (iii); Lista R6, Ex. 7 (Tirole 5.2), parts (iii)–(iv)

Q: Identical firms face a perfectly correlated liquidity shock, low ($\rho_L < \rho_0$) or high ($\rho_H > \rho_0$, probability $\lambda$), and Treasury bonds paying 1 at date 1 are scarce, so they trade at $q - 1 = \lambda(\rho_1 - \rho_H)/(\rho_H - \rho_0)$. Why would a security paying 1 only in the low-shock state sell at $1 - \lambda$, with no premium?
- It is risky and firms discount risk: the Treasury premium rewards the certainty of the payoff rather than its timing, so a state-contingent claim carries a risk discount instead of a premium.
- In the low-shock state firms cover their needs by issuing claims, so cash there is worth only its face value; the premium sits on the bad-state payoff, when every firm needs cash at once.
- Its payoff is perfectly correlated with the firms' own profits, so holding it adds no diversification to their portfolios, whereas the premium on Treasuries rewards diversification across states.
- The premium on Treasuries reflects their scarcity, and the government can issue the new claim in any amount, so competition among issuers drives its price down to its expected payoff.
<!-- YW5zOjE= -->
> Everyone is risk neutral, so no risk discount exists. A firm values a unit of date-1 cash above par only where it relaxes the continuation constraint: in the high-shock state, where the shortfall $\rho_H - \rho_0$ cannot be raised on the market. In the low state the shock is below $\rho_0$ and met by dilution, so the good-state claim is priced at its expected payoff, $q' = 1 - \lambda$, whatever its supply. A Treasury bond is a good-state claim plus a bad-state claim, and all of its premium sits on the second.
> Ref: Tirole Ch. 5 §5.2 (pp. 202–206) and exercise 5.5 (p. 231); Tirole Ch. 15 §15.3.1 (p. 523)
> Similar: Lista R6, Ex. 8 (Tirole 5.5); Lista R10, Ex. 13 (Tirole 15.4)

## mat

Q: A firm of scale $I$ earns a verifiable short-term income $rI$ at date 1 that exceeds its optimal reinvestment cutoff, $r > \rho^*$; the manager cannot steal the cash but decides whether to reinvest it. What role does short-term debt play?
- None: the short-term income is verifiable and fully pledgeable, so it acts exactly like extra initial cash $A$, raising the scale of investment but leaving the continuation rule unchanged.
- It lets the firm dilute its initial investors at date 1, so that cash raised on top of $rI$ covers every shock up to the full continuation value $\rho_1$ and the first best is restored.
- It disciplines under-investment: with $r > \rho^*$ the manager prefers to sit on the cash, so a fixed repayment forces her to keep reinvesting it up to the cutoff $\rho^*$ set ex ante.
- It pumps $(r - \rho^*)I$ out, so retained cash covers shocks up to $\rho^*$ only; holding all of $rI$, the manager would reinvest whenever $\rho \le r$, beyond what investors accept.
<!-- YW5zOjM= -->
> Under the free-cash-flow assumption the manager, who enjoys continuation rents, would reinvest whenever she has the cash, i.e. for all $\rho \le r$. The optimal cutoff is lower, so $P_1 = (r - \rho^*)I$ must be paid out at date 1 and she must be denied the right to dilute. A larger $r$ is not like more cash $A$: it lowers the optimal $\rho^*$ (from $\int_0^{\rho^*}F(\rho)d\rho = 1 - r$), so it changes the continuation rule, not only the scale.
> Ref: Tirole Ch. 5 §5.6.1 (optimal claim maturity, p. 226)
> Similar: Lista R6, Ex. 10 (Tirole 5.7); Lista R6, Ex. 2 (Ross CQ 19.10)

Q: With decreasing returns to scale $R(I)$, a firm earns short-term income $rI$, faces a reinvestment need $\rho I$ and pays out $(r - \rho^*)I$ as short-term debt, where $\rho^*$ is its continuation cutoff. How does the maturity of its debt respond to a stronger balance sheet, that is, more net worth $A$?
- Maturity lengthens: more net worth eases the scarcity of pledgeable income, so the firm raises its cutoff $\rho^*$, keeps more liquidity and pays out less per unit as short-term debt.
- Maturity shortens: a strong firm can count on refinancing at date 1, so it needs less long-term commitment and pays out more of $rI$ to its creditors, which raises $r - \rho^*$.
- Maturity is unaffected: investment and liquidity needs both scale with $A$ in proportion, so the cutoff $\rho^*$ and the short-term debt per unit, $r - \rho^*$, do not move with $A$.
- Maturity shortens: as in Diamond (1991), strong firms expect upgrades and want to reprice their debt soon, so they issue more short-term debt and lower the cutoff $\rho^*$.
<!-- YW5zOjA= -->
> A weak balance sheet makes pledgeable income scarce; the firm raises it by continuing less often, i.e. keeping less liquidity and sweeping more of the date-1 cash flow to creditors. So $dI/dA > 0$ and $d\rho^*/dA > 0$: short-term debt per unit, $r - \rho^*$, falls with $A$. The "no effect" option is the constant-returns benchmark, where $\rho^*$ solves $\int_0^{\rho^*}F = 1 - r$ independently of $A$; decreasing returns link scale and continuation. Diamond's repricing logic concerns credit ratings, not net worth.
> Ref: Tirole Ch. 5 §5.6.1 (p. 226) and exercise 5.7 (p. 232); Amaro de Matos Ch. 5 §5.2.3 (pp. 139–142)
> Similar: Lista R6, Ex. 10 (Tirole 5.7); Lista Topic 5, Ex. 8 (Tirole 5.7)

Q: A firm without moral hazard borrows from many lenders who cannot observe one another's claims; its date-1 cash $r$, net of short-term repayments, funds a deepening investment that raises the probability of the date-2 payoff. Why does such opaque lending bias maturity toward the short term?
- Short-term claims carry a lower rate because lenders demand a term premium on long-term claims, so the entrepreneur minimises funding costs by tilting the mix toward short-term debt.
- Lenders fear a coordination failure at date 1 and each wants to be paid before the others run, so short-term debt is a defensive claim, as in a bank run with many depositors.
- A lender who secretly trades long-term for short-term claims is paid from the reinvestment fund; the lower success odds hit all long-term holders, and no one internalises that.
- The entrepreneur uses short-term debt to commit not to overinvest the date-1 cash, and with many lenders that commitment is cheaper, so the efficient structure is mostly short-term.
<!-- YW5zOjI= -->
> At the first best $\tau'(I_1^*)R = 1$, and the short/long split is indeterminate. With opaque books, the entrepreneur and any one lender gain from a secret swap of long-term for short-term claims: $\delta U_b = (R_l/R)\delta r_l > 0$. The cost, a lower success probability, is spread over every long-term claimant. In equilibrium $r_b = 0$, the reinvestment satisfies $\tau'(I_1)R_b = 1$ with $I_1 < I_1^*$: too little deepening, too much short-term debt. There is no term premium with risk-neutral lenders, no run, and no moral hazard to discipline.
> Ref: Tirole Ch. 5 exercise 5.9 (p. 233); Tirole Ch. 5 §5.6 (pp. 226–228)
> Similar: Lista R6, Ex. 11 (Tirole 5.9); Lista Topic 5, Ex. 9 (Tirole 5.9)

Q: Shareholders of a firm holding a large cash pile push for a payout; the CFO replies that the cash protects the firm against shocks. Within the course's framework, when are the shareholders right?
- Always: under MM, cash is a zero-NPV asset whose return is taxed at the corporate level, so any balance above transaction needs lowers value, whatever the firm's exposure to shocks.
- When the cash exceeds what the firm needs to meet shocks it could not refinance on the market: beyond that it only frees managers from market discipline and invites perks.
- Never: cash lowers distress risk and earns the riskless rate, so it is a zero-NPV hedge, and managers who hold more of it are simply buying cheap insurance for the shareholders.
- Only when the firm has debt outstanding: extra cash then lowers default risk and transfers value to the creditors, so shareholders want it paid out before the debt matures.
<!-- YW5zOjE= -->
> Liquidity is valuable up to the shocks the market will not refinance ($\rho^* - \rho_0$ per unit in Tirole's model): that cash keeps the firm alive in states where continuation is efficient. Beyond that, idle cash earns less than the required return after tax and, more importantly, lets managers spend free of capital-market discipline (perks, empire building, overpriced acquisitions). That is why free cash flow is pumped out with debt. "Always" ignores the liquidity motive; "never" ignores agency.
> Ref: Tirole Ch. 5 §5.2.3 (pp. 205–206), §5.6.1 (p. 226); Berk Ch. 20 §20.2 (conservative financing policy, pp. 598–599)
> Similar: Lista R6, Ex. 1 (Ross CQ 19.1); Lista R6, Ex. 2 (Ross CQ 19.10); Lista R6, Ex. 5 (Berk 20.6)

## hedge

Q: A firm's random date-1 income $r$ is good news about its prospects: after reinvesting, success has probability $p + \tau(r)$, with $\tau' > 0$, and the manager must keep a stake $B/\Delta p$ in success. Why should its date-1 debt not be fully indexed to $r$?
- Good news raises the value of continuing by more than the date-1 market will refinance, as the manager's rent $[p_H + \tau(r)]B/\Delta p$ grows too, so the firm must keep part of the windfall.
- Full indexation leaves the firm's cash the same in every state, and risk-neutral investors gain nothing from insurance, so hedging is neutral and the firm may as well stay exposed to $r$.
- Good news makes it easier to raise funds at date 1, so the market finances all of the extra reinvestment; the firm should over-index instead, paying out more than the windfall when $r$ is high.
- Indexed contracts carry a fixed cost of writing and monitoring that is worth paying only for the downside, so the firm hedges low values of $r$ and keeps the upside as a free option.
<!-- YW5zOjA= -->
> The optimal cutoff is $\rho^*(r) = [p_H + \tau(r)][R + \mu(R - B/\Delta p)]/(1+\mu)$, which rises with $r$ through $\tau(r)$, while the refinancing capacity $[p_H + \tau(r)](R - B/\Delta p)$ rises less, because the rent rises too. Implementing $\rho^*(r)$ = retained cash + capacity gives $d^*(r) = r - [p_H + \tau(r)]B/[(1+\mu)\Delta p]$: not fully indexed, so the firm keeps some cash-flow risk. Risk neutrality does not make hedging neutral: it matters through liquidity. Fixed costs explain who hedges (size), not this partial hedge.
> Ref: Tirole Ch. 5 §5.4.1–5.4.2 (when is incomplete hedging optimal, pp. 213–219); Grinblatt–Titman Ch. 21
> Similar: Lista R6, Ex. 4 (Grinblatt–Titman 21.7); Lista R6, Ex. 3 (Grinblatt–Titman 21.1)

Q: Suppose the date-1 shock is a permanent shift in the output price $P$: the short-term income $Pr$ and the date-2 payoff $PR$ both scale with it, while the manager's private benefit $B$ does not. Why is fully indexed debt $d(P) = Pr - \ell_0$ optimal even though a high $P$ is good news?
- Because $P$ is independent of the reinvestment need $\rho$, and any shock independent of $\rho$ should be fully hedged, whatever it implies for the firm's prospects at date 2.
- Because the manager's rent rises with $P$, and full indexation is needed to keep her stake above $B/\Delta p$ in the high-price states, where shirking is most tempting.
- Because the rent $p_H B/\Delta p$ does not move with $P$, the cutoff and refinancing capacity rise one for one: the market funds the extra reinvestment and one cushion $\ell_0$ suffices.
- Because indexed debt shifts the price risk to lenders, who are better diversified than the entrepreneur, so full indexation is the risk-sharing optimum whatever the agency problem is.
<!-- YW5zOjI= -->
> $\rho^*(P) = p_H PR - \frac{\mu}{1+\mu}\frac{p_H B}{\Delta p}$ and date-1 pledgeable income $p_H(PR - B/\Delta p)$ both rise by $p_H R$ per unit of $P$, because the rent does not depend on $P$. The cash the firm must retain, $\ell_0 = \frac{1}{1+\mu}\frac{p_H B}{\Delta p}$, is the same in every state, hence $d(P) = Pr - \ell_0$. Contrast with income news that raises the success probability: there the rent rises with good news and the debt is only partially indexed. Independence of $P$ and $\rho$ alone does not deliver the result, and lenders are risk neutral.
> Ref: Tirole Ch. 5 §5.4.2 (pp. 217–219) and exercise 5.11 (p. 234)
> Similar: Lista R6, Ex. 9 (Tirole 5.11)
