---
quiz: "Executive compensation and managerial incentives (hard, conceptual)"
tags:
  ppp: "Pay level, pay-for-performance, stock and options"
  risk: "Risk sharing, relative performance and filtering"
  power: "Power of incentive schemes and what pay is based on"
  short: "Short-termism, accounting bonuses and golden parachutes"
---

## ppp

Q: Critics compare a CEO's annual pay with that of sports stars and film celebrities and conclude that it is excessive. From an incentive standpoint, which observation should drive the assessment instead?
- The level of pay, since a well-paid CEO has more to lose from being fired and therefore works harder, so high pay is itself the main incentive device and should be judged by its size.
- The share of pay given in cash, since cash cannot be manipulated, while stock-based pay is set by the market and so carries no incentive beyond what the share price already contains.
- How much the CEO's wealth moves with shareholder value; a high level buys little incentive if pay barely tracks performance, and the level is set by the market for managerial talent.
- The ratio of CEO pay to average worker pay, since incentives inside the firm depend on fairness, so a high ratio lowers effort among employees by more than it raises the CEO's own effort.
<!-- YW5zOjI= -->
> Incentives come from the sensitivity of the manager's wealth to the value she creates, through the shares and options she holds and the risk of dismissal, not from the level of pay. The level has to satisfy her participation constraint in a competitive market for talent, which is the point of the comparison with stars. A large level with a flat profile is costly and motivates little. A modest level with a steep profile can motivate a lot. Fear of losing a well-paid job is an implicit incentive, but it does not make the level the measure of incentives.
> Ref: Tirole Ch. 1 §1.2 (p. 20); Ross *Fundamentos* Cap. 1 §1.4 (p. 12)
> Similar: Lista R8b, Ex. 1 (Ross CQ 1.16)

Q: Managers own a small fraction of a firm financed half by debt. The firm borrows heavily to buy back shares, so that debt becomes most of its value, and managers do not tender, so their fraction of the equity rises. Which prediction about their incentives is most defensible?
- Less perk consumption and empire building, as they bear more of each wasted unit and debt drains free cash, but an ambiguous pull on risk: levered equity rewards it, a concentrated stake deters it.
- More perk consumption, since higher leverage shifts losses to creditors so managers bear less of each wasted unit, together with less risk-taking, because creditors now control investment directly.
- No change in incentives, since the recapitalisation only swaps one claim for another at fair prices, so by MM the value of the managers' stake and their marginal incentives are left exactly as before.
- More long-term investment, since the larger stake lengthens managers' horizon, and debt holders, now the main claimants, prefer slow projects whose returns arrive after the debt has matured.
<!-- YW5zOjA= -->
> A higher equity fraction $\alpha$ means managers bear more of each unit of value they waste, so perks fall, as in Jensen–Meckling, and contractual debt service removes free cash flow. On risk the effect is ambiguous. Equity is now a more option-like claim, which rewards risk-shifting, while the managers' wealth is less diversified, which makes them more cautious. Heavy debt service and debt overhang tend to cut long-horizon projects, not encourage them. MM irrelevance does not hold once leverage changes incentives.
> Ref: Amaro de Matos Ch. 3 §3.1.1 (pp. 64–66), §3.1.3 (p. 71); Tirole Ch. 5 §5.6 (p. 225); Grinblatt & Titman Ch. 18 (pp. 627–655)
> Similar: Lista R8b, Ex. 9 (Grinblatt & Titman 18.8); Lista R8b, Ex. 2 (Berk Ch. 22, Problem 3)

Q: A board can grant its CEO either restricted shares or at-the-money call options with the same grant-date value. Which comparison of the two grants is correct?
- The two are equivalent for incentives, since both are claims on the same equity and cost the firm the same, so the manager's choices over effort and risk are identical under either grant.
- Options reduce risk-taking, since the manager loses the whole grant when the price ends below the strike, so a CEO paid in options becomes more cautious than one paid in shares.
- Options give weaker incentives per dollar, since part of their value is time value the manager cannot influence, so restricted shares always dominate options for any target level of effort.
- Options pack more sensitivity to the share price per dollar near the strike, but their convex payoff rewards volatility, and once deep out of the money they lose most of their bite.
<!-- YW5zOjM= -->
> An option's value per dollar is more sensitive to the share price than a share's, so for the same cost it gives a steeper incentive near the strike. Its payoff, $\max[0, S_T - S]$, is convex, so higher volatility raises its value, which pushes toward risk-taking, not caution. Once the price falls far below the strike, the option's delta is close to zero and the incentive is gone, which is why options are often repriced. Shares give a linear exposure that stays the same in good and bad states.
> Ref: Amaro de Matos Ch. 3 §3.1.2, "Executive Stock Options" (pp. 70–71); Tirole Ch. 1 §1.2 (p. 20)
> Similar: Lista R8b, Ex. 10 (Amaro de Matos 3.1.5 #3); Lista R8b, Ex. 5 (Grinblatt & Titman 18.7)

## risk

Q: Shareholders with utility $U$ and a manager with utility $G$, both concave, share a payoff $\theta$ through a fee $f(\theta)$ that satisfies the Pareto condition $U'(\theta - f) = \lambda G'(f)$. Let $r_U = -U''/U'$ and $r_G = -G''/G'$ be their absolute risk aversions. What is the slope $f'(\theta)$, and what does it imply?
- $f' = r_G/(r_U + r_G)$: the more risk averse the manager, the more of each unit of payoff she bears, since a cautious manager needs a larger exposure before she is motivated.
- $f' = r_U/(r_U + r_G)$: risk goes to the more risk-tolerant side, so risk-neutral shareholders would pay the manager a flat fee, which leaves no exposure to motivate her effort.
- $f' = \lambda$: the slope equals the Pareto weight on the manager, so a manager with more bargaining power gets a steeper share of the payoff whatever their attitudes toward risk.
- $f' = 1/(1 + r_U r_G)$: the manager's share falls only when both sides are risk averse, so with risk-neutral shareholders she bears the whole payoff and is fully motivated.
<!-- YW5zOjE= -->
> Differentiating the Pareto condition gives $U''(1 - f') = \lambda G'' f'$; dividing by $U' = \lambda G'$ gives $r_U(1 - f') = r_G f'$, so $f' = r_U/(r_U + r_G)$. Each side bears risk in proportion to its risk tolerance. With $r_U \to 0$ the efficient fee is flat: efficient risk sharing fully insures the manager, which removes her incentives. That conflict is what the second-best schedule has to resolve. The weight $\lambda$ sets the level of the fee, not its slope.
> Ref: Amaro de Matos Ch. 3 §3.1.2, "Determining Optimal Fee Schedules" (pp. 66–68)
> Similar: Lista R8b, Ex. 11 (Amaro de Matos 3.1.5 #4); Lista R8b, Ex. 12 (Amaro de Matos 3.1.5 #6)

Q: When the manager's action is unobservable, the shareholders' optimal fee must also satisfy her incentive constraint, with multiplier $\psi$, so that $U'/G' = \lambda - \psi\,(\text{a term from the payoff technology})$, where $U$ and $G$ are the shareholders' and the manager's utilities. Why does this schedule depart from efficient risk sharing, and when does the departure disappear?
- It departs whenever shareholders are risk averse, since $\psi$ then measures their extra risk; it disappears once shareholders are risk neutral, whatever the manager's attitude toward risk.
- It departs because a binding incentive constraint, $\psi > 0$, makes pay track output more than risk sharing warrants; it disappears with a risk-neutral manager, who can bear all the risk.
- It departs because the Pareto weight $\lambda$ falls when the action is hidden, which lowers the manager's share; it disappears when $\lambda$ is set high enough to restore her reservation utility.
- It departs only when the fee is nonlinear, since a linear fee always shares risk efficiently; it disappears once the fee is restricted to a constant plus a share of the payoff, whatever $\psi$ is.
<!-- YW5zOjE= -->
> With $\psi > 0$ the ratio of marginal utilities varies with output beyond what the efficient condition $U'/G' = \lambda$ allows, so the manager bears more risk than efficient sharing would give her: this is the cost of incentives. A risk-neutral manager can bear all the risk at no cost, so selling her the firm gives first-best incentives. In Tirole's model this fails because of limited liability, which is why a rent survives there even with risk neutrality. Risk-neutral shareholders do not remove the distortion, and making the fee linear does not either.
> Ref: Amaro de Matos Ch. 3 §3.1.2 (pp. 68–70); Tirole Ch. 3 §3.2 (p. 115)
> Similar: Lista R8b, Ex. 14 (Amaro de Matos 3.1.5 #5)

Q: A board considers indexing its CEO's bonus to the results of rival firms in the same industry. When does this filtering improve the contract most, and what is its main risk?
- When rivals' results are uncorrelated with the firm's, since the index then adds independent information; its main risk is that the CEO earns less on average and leaves for a rival.
- Always, since any extra measure lowers the cost of incentives; it carries no risk, because the CEO cannot influence rivals' results and so cannot game an index built from them.
- When common shocks drive much of both firms' results, since netting them out cuts pay risk without dulling effort; its risk is that the CEO gains by hurting rivals or softening competition.
- When the CEO is risk neutral, since filtering then raises effort by making pay depend on rank; its main risk is that a rank-based bonus pays nothing in an industry-wide boom, which cuts effort.
<!-- YW5zOjI= -->
> Relative performance evaluation removes shocks that the CEO cannot control and that also hit rivals, such as oil prices for an oil major. It is most valuable when that common component is large, that is, when the correlation is high. An uncorrelated benchmark only adds noise. A measure is worth using only if it is informative about the CEO's own effort. Pay that depends on beating rivals rewards actions that hurt them or that soften competition, so it should be used with care in concentrated industries. Filtering matters because the manager is risk averse.
> Ref: Tirole Ch. 1 §1.2 (p. 20); Tirole Ch. 7 §7.1 (p. 283); Amaro de Matos Ch. 3 §3.1.2 (p. 70)
> Similar: Lista R8b, Ex. 7 (Grinblatt & Titman 18.6)

## power

Q: A sports club can pay its coach either on outcomes (wins and playoff success) or on an expert panel's assessment of the quality of his decisions, ignoring results. Which comparison is right?
- Outcome pay targets what the club values but loads the coach with luck and player quality he cannot control; decision-based pay filters that noise but rests on the panel's judgement, which he may play to.
- Outcome pay is always superior, since results cannot be manipulated, while decision-based pay is always inferior, because the experts lack information the coach has and so add pure noise to his pay.
- Decision-based pay is always superior, since it removes all risk from the coach's pay at no cost; outcome pay should be used only when no panel is available, as it adds noise without adding effort.
- The two are equivalent if the coach is risk neutral and differ only in timing, since outcome pay arrives at the end of the season while decision-based pay can be paid weekly, so the choice is about liquidity.
<!-- YW5zOjA= -->
> Paying on output aligns pay with the objective but exposes the agent to risk he does not control, which a risk-averse agent must be compensated for. Paying on evaluated inputs removes that noise. It relies, though, on an evaluator whose information is imperfect and who can be lobbied, and the coach may choose decisions that look good to the panel instead of decisions that win. The optimal contract uses both kinds of measure, each weighted by how much it tells about effort. Neither option dominates in general.
> Ref: Tirole Ch. 1 §1.2 (p. 20); Amaro de Matos Ch. 3 §3.1.2 (p. 70)
> Similar: Lista R8b, Ex. 6 (Grinblatt & Titman 18.9)

Q: An entrepreneur borrows $I - A$ for a project paying $R$ on success. With probability $x$ her interests are dissonant: taking her private benefit $B$ lowers the success probability from $p_H$ to $p_L$; with probability $1 - x$ taking $B$ coincides with $p_H$. She is paid $R_b$ on success and $\Delta p = p_H - p_L$. Why can a low-powered scheme, $R_b = 0$, be optimal when $x$ is small?
- Because it raises the NPV: congruent types behave anyway and dissonant types are rare, so dropping the stake removes a cost from the project and leaves its expected output unchanged.
- Because with $x$ small the dissonant type behaves even without a stake, since misbehaviour is then detected, so $R_b = 0$ keeps both effort and financing at no cost to investors.
- Because it is the only scheme investors accept when $x$ is small, since a positive stake $R_b$ then pays congruent types for nothing, and investors refuse any rent they can avoid.
- Because paying nothing loses only $x\Delta p R$ of expected output but saves the rent $p_H B/\Delta p$ paid to every type; when financing binds, the saved rent is worth the lower NPV.
<!-- YW5zOjM= -->
> With $R_b = 0$ the pledgeable income is $[(1 - x)p_H + x p_L]R = p_H R - x\Delta p R$. With $R_b = B/\Delta p$ it is $p_H(R - B/\Delta p)$. The low-powered scheme raises pledgeable income if and only if $x\Delta p R < p_H B/\Delta p$, which holds for small $x$. Its NPV is lower, because dissonant types shirk, so it is chosen only when funding requires it. For large $x$ a high-powered scheme is needed. Investors break even either way and do not choose the scheme.
> Ref: Tirole Ch. 3 §3.2 (pp. 115–117); Tirole, Answers to Selected Exercises, Ex. 3.10 (p. 575)
> Similar: Lista R8b, Ex. 13 (Tirole 3.10)

## short

Q: After a boom year, a firm's management asks for a large cash bonus because accounting profit was positive, although its return on book equity is below the shareholders' cost of equity. What is the strongest objection to a bonus tied to accounting profit?
- Accounting profit ignores the cost of equity, so it can reward value destruction; it pays managers for a boom they did not create; and it invites pulling earnings forward at the cost of long-run value.
- Accounting profit overstates value because it ignores interest expense, so a bonus on it pays managers for debt-financed growth; the boom itself is irrelevant, since it is already in the share price.
- The objection is only one of timing: a bonus on this year's profit should be deferred until the profit is realised in cash, after which accounting profit is a sound basis for pay at any level of returns.
- Bonuses should not depend on performance at all, since risk-averse managers value fixed pay more, so any bonus on profit costs shareholders more than it adds in effort, whatever the measure used.
<!-- YW5zOjA= -->
> Accounting earnings charge interest but not the opportunity cost of equity, so a positive profit with ROE below the cost of equity is an economic loss. A boom is a common shock that should be filtered out, as in relative performance evaluation. A bonus on current reported profit also rewards moving earnings forward and cutting long-term spending, which is the manipulation and short-termism problem. Interest is already deducted from net income. Refusing all performance pay would remove incentives altogether.
> Ref: Higgins Ch. 1 §1.7.3 (pp. 27–29); Tirole Ch. 7 §7.2 (p. 299)
> Similar: Lista R8b, Ex. 4 (Higgins 1.2)

Q: After funding, investors learn whether the manager's prospects are good or poor and can then dismiss her, which yields them $L$; a manager with poor prospects can secretly fake a good signal at a cost in success probability. With $q_H$ the success probability of a poor-prospect manager who behaves and $R$ the payoff on success, when is a golden parachute paid on admitting poor prospects the efficient way to deter manipulation?
- When $q_H R > L$, since keeping a poor-prospect manager is then efficient, so the parachute rewards her for staying and lets the board raise her chance of continuing at no loss of value.
- Never, since a parachute cuts the income pledgeable to investors one for one, while making tenure insensitive to the signal costs nothing in value, so insensitive tenure always dominates it.
- When $q_H R < L$, since keeping a poor-prospect manager then destroys value, so firing her and paying cash deters manipulation more cheaply than protecting her tenure in the bad state.
- Always, since a parachute is a pure transfer that leaves the NPV unchanged, so it should replace any use of tenure, whatever the relation between $q_H R$ and the termination value $L$.
<!-- YW5zOjI= -->
> There are two ways to pay the manager for honesty: continuation in the bad state, $z^q$, and cash, $T$. Holding pledgeable income fixed, replacing cash with continuation relaxes the no-manipulation constraint at rate $(q_H R - L)\,dz^q$. If $q_H R > L$, continuation is the cheaper currency and $T^* = 0$. If $q_H R < L$, continuation destroys value, so $z^{q*} = 0$ and a parachute $T^* > 0$ is optimal. A parachute does lower pledgeable income, and insensitive tenure costs NPV whenever continuation is inefficient.
> Ref: Tirole Ch. 7 §7.2.1 (pp. 301–305)
> Similar: Lista R8b, Ex. 15 (Tirole 7.9)
