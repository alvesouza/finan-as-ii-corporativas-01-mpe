---
quiz: "Corporate governance, control rights and activism (hard, conceptual)"
tags:
  free: "Separation of ownership and control, free riding and large shareholders"
  mon: "Active vs speculative monitoring, bank vs public debt"
  ctrl: "Allocation of control rights between insiders and investors"
  act: "Proxy contests, boards and leverage as discipline"
---

## free

Q: A minority blockholder holds a fraction $\alpha < 1/2$ of an otherwise diffusely held firm; after paying for research it may draw a value improvement $Z$ and then bid for the remaining shares, while small holders tender only if the premium covers the expected improvement. As $\alpha$ grows, what happens to the takeover premium, to the cutoff improvement that triggers a bid, and to the firm's market value?
- The premium rises, since a larger block gives the bidder more bargaining power over the fringe, while the cutoff and the market value stay unchanged, because the block itself creates no new value.
- The premium falls and so does the cutoff, since the gain on its own block lets the bidder act on smaller improvements; more bids and more research raise market value even as each bid pays less.
- The premium falls because the fringe free-rides less once a large holder exists, but market value falls too, since a larger block entrenches the holder and makes the firm a harder target.
- The premium and the cutoff both rise, since a larger holder bids only for large improvements it can share with fewer holders, so takeovers are rarer but each one adds more market value.
<!-- YW5zOjE= -->
> The bidder's profit condition $\tfrac12 Z - (\tfrac12 - \alpha)\pi - c \ge 0$ is relaxed by a larger $\alpha$, so the cutoff $Z^c(\alpha)$ falls. Small holders demand $\pi^*(\alpha) = E[Z \mid \text{bid is profitable}]$, which falls with the cutoff. Research intensity $I^*(\alpha)$ rises, so $V(\alpha,q) = q + I^*\{1 - F(Z^c)\}E[Z \mid Z \ge Z^c]$ rises (Shleifer–Vishny). Bargaining power plays no role: the free-rider condition sets the premium. Entrenchment is not part of this model.
> Ref: Amaro de Matos Ch. 8 §8.1.2, Prop. 8.1.1 (pp. 196–198); Tirole Ch. 1 §1.4 (p. 36); Tirole Ch. 11 §11.5.2 (pp. 432–434)
> Similar: Lista R8, Ex. 7 (Amaro de Matos 8.1.5 #5); Lista R9, Ex. 5 (Amaro de Matos 8.1.5 #1)

Q: A proposed law makes it harder for large outside shareholders to extract private benefits from the partial control they exert over management. Through the lens of the free-rider problem in monitoring, what is the most defensible prediction?
- Monitoring rises, since blockholders who can no longer divert value will turn to raising share value instead, which they share with small investors, so all holders gain from the law.
- Nothing changes for monitoring, since private benefits are a pure transfer from minority holders, and transfers alter the split of value among investors but never the incentive to monitor.
- Monitoring rises, since small shareholders protected by the law will now monitor managers themselves, as the gains from monitoring are no longer captured by one large holder.
- Monitoring falls, since its gains to share value go to every holder while its cost is borne by the blockholder alone; less expropriation must be weighed against weaker oversight.
<!-- YW5zOjM= -->
> Monitoring is a public good among shareholders: the blockholder pays all of its cost and gets only its pro-rata share of the gain. Private benefits of control are part of what pays for monitoring and for holding an undiversified block, so cutting them weakens oversight and may discourage blocks from forming. Small holders still free-ride, because each one's gain from monitoring is tiny. So the law trades less diversion against less monitoring, and its net effect is ambiguous.
> Ref: Tirole Ch. 1 §1.1 (p. 15), §1.4 (p. 36); Tirole Ch. 9 §9.3 (p. 366); Grinblatt & Titman Ch. 18 (pp. 627–655)
> Similar: Lista R8, Ex. 4 (Grinblatt & Titman 18.5); Lista R8, Ex. 3 (Grinblatt & Titman 18.2)

## mon

Q: Which statement best distinguishes active monitoring from speculative monitoring of a firm by outside investors?
- Active monitors intervene to raise the value of the firm; speculators only measure the value managers have already created, and their trades make the stock price a better base for pay.
- Active monitors trade on information to profit from mispricing; speculators sit on the board and intervene in strategy, which is why speculation needs a concentrated stake to be worthwhile.
- Both forms intervene in management; they differ only in stake size, since a small stake gives exit as the only threat while a large one gives voice, so the information gathered is the same.
- Speculators intervene before decisions and active monitors after them, so speculation is forward-looking voice, while active monitoring only audits past decisions without changing them.
<!-- YW5zOjA= -->
> Active monitoring is voice: a large investor or bank collects information about the firm's prospects and uses it to change management's choices. Speculative monitoring is exit: it does not change the firm's policy but measures the value of assets in place, and that information enters the stock price. A price that carries it is a better performance measure for stock-based pay. Speculators need liquidity traders to hide behind in order to profit from their information. The two differ in what they do with information, not only in the size of the stake.
> Ref: Tirole Ch. 8 §8.1 (p. 333), §8.2 (p. 338); Tirole Ch. 9 §9.2 (p. 356)
> Similar: Lista R8, Ex. 2 (Ross CQ 1.15, institutional investors and activism)

Q: In the active-monitor model, a monitor can cut the entrepreneur's private benefit from misbehaving from $B$ to $b < B$ at a private cost $c$, and monitoring capital is abundant. The project costs $I$, pays $R$ on success, and succeeds with probability $p_H$ (behave) or $p_L$ (misbehave), $\Delta p = p_H - p_L$. Why do firms with high net worth $A$ borrow only from uninformed investors?
- Because a monitor earns a rent when the firm is strong, since its stake $R_m \ge c/\Delta p$ then exceeds its contribution, so the entrepreneur picks public debt even though monitoring would raise the NPV.
- Because monitoring cuts the probability of failure only for weak firms, so for a strong firm the gain from lowering $B$ to $b$ is zero, and the cost $c$ is then pure waste borne by its investors.
- Because monitoring lowers the NPV by $c$ and pays off only by raising pledgeable income; once $p_H(R - B/\Delta p) \ge I - A$ holds, the firm has no financing gap to close and saves the cost.
- Because public debt is more liquid, so strong firms pay a lower rate on it, and that liquidity premium exceeds the reduction in agency cost from $p_H B/\Delta p$ to $p_H b/\Delta p$.
<!-- YW5zOjI= -->
> With a monitor the funding condition becomes $p_H(R - b/\Delta p) \ge I - A + c$ and the entrepreneur's payoff is $p_H R - I - c$. Without one it is $p_H R - I$. Monitoring is a costly way to raise pledgeable income, so only firms that cannot fund themselves otherwise use it. With abundant monitoring capital the monitor earns no rent, since $I_m = p_H R_m - c$. Scarce monitoring capital would give it a rent, but that is a different assumption. The probability of success does not change with $A$.
> Ref: Tirole Ch. 9 §9.2.1 (pp. 356–358)
> Similar: Lista R8, Ex. 11 (Tirole 9.1)

Q: A project costs $I$, pays $R$ on success and succeeds with probability $p_H$ if the entrepreneur behaves or $p_L$ if she misbehaves and takes private benefit $B$; a monitor at cost $c$ can cut that benefit to $b$. Suppose $p_H R > p_L R + B > I$ and $p_L R > p_H(R - b/\Delta p) - c$, with $\Delta p = p_H - p_L$. Why do the weakest firms that still invest issue junk bonds instead of borrowing from a monitor?
- Giving up on incentives frees the whole of $p_L R$ for investors, since no stake is needed when misbehaviour is tolerated; this beats monitored pledgeable income, at the cost of a lower NPV.
- Junk bonds raise the NPV relative to monitoring, since the private benefit $B$ counts as surplus and exceeds the cost $c$, so weak firms choose them because they are the most efficient option.
- A monitor refuses to lend to weak firms, since its stake $c/\Delta p$ cannot be paid when $A$ is low, so junk bonds are the only option left even though the monitor would be more efficient.
- Junk bonds carry a high promised yield, which strengthens the entrepreneur's incentive to behave, so the probability of success rises to $p_H$ and investors are repaid as with safe debt.
<!-- YW5zOjA= -->
> If misbehaviour is accepted, no incentive stake is needed, so the pledgeable income is $p_L R$. By the second assumption this exceeds the monitored income $p_H(R - b/\Delta p) - c$. The NPV is lower, though: $p_L R + B - I < p_H R - I - c$ because $(\Delta p)R > c + B$. As $A$ falls, the firm moves from high-quality public debt to monitored finance to junk bonds, each step giving up NPV for pledgeable income. The monitor's stake does not depend on $A$, and a high promised yield does not create effort incentives.
> Ref: Tirole Ch. 9 §9.2.1 (pp. 356–358); Tirole, Answers to Selected Exercises, Ex. 9.1 (pp. 606–607)
> Similar: Lista R8, Ex. 11 (Tirole 9.1)

## ctrl

Q: An entrepreneur with net worth $A$ needs $I$; the project pays $R$ on success with probability $p_H$ (behave) or $p_L$ (misbehave, private benefit $B$), $\Delta p = p_H - p_L$. An interim action raises the success probability by $\tau$ and costs insiders $\gamma > \tau R$, so it destroys value, and it cannot be contracted on, only the right to choose it. When is giving that right to investors optimal?
- When $(p_H + \tau)R - \gamma \ge I - A$, since investor control is chosen whenever the project's value net of the action's cost covers what the investors put in.
- When $\gamma - \tau R$ is smaller than $\tau B/\Delta p$, since investors can then compensate the entrepreneur ex post for the private cost of the action they impose.
- When $p_H(R - B/\Delta p) \ge I - A$, since investors then break even under either allocation and choose the one that raises their own expected income.
- When $p_H(R - B/\Delta p) < I - A \le (p_H + \tau)(R - B/\Delta p)$, since only investor control then raises pledgeable income enough to fund the project.
<!-- YW5zOjM= -->
> Investors bear none of $\gamma$ and share in the gain, so they take the action, which raises pledgeable income by $\tau(R - B/\Delta p)$ and lowers the NPV by $\gamma - \tau R$. The entrepreneur keeps control when she can fund the project without giving it up, and gives it up only when that is the only way to be funded. There is no renegotiation ex post, because she has no cash left to buy the right back. Utility is nontransferable, so the Coasian argument fails.
> Ref: Tirole Ch. 10 §10.2.1 (pp. 389–391); Amaro de Matos Ch. 5 §5.1.3 (p. 131)
> Similar: Lista R8, Ex. 9 (Tirole 10.7); Lista R8, Ex. 13 (Tirole 10.8)

Q: Investors can hold the right to a "damage control" action that raises the success probability from $p_L$ to $p_L + \nu$ only when the entrepreneur misbehaves, leaves $p_H$ unchanged, and costs her $\gamma$ (she succeeds with $p_H$ if she behaves, with $p_L$ if she misbehaves and takes private benefit $B$; success pays $R$). Why can investor control here make financing harder?
- Because the cost $\gamma$ of the action falls on investors, who must reimburse the entrepreneur for it, so pledgeable income falls by exactly $\gamma$ whenever investors hold the right.
- Because investors will cushion misbehaviour, which narrows the gap between behaving and shirking to $\Delta p - \nu$, so the stake needed for effort rises to $B/(\Delta p - \nu)$.
- Because the action raises the success probability whatever she does, so investors gain less from effort and cut her stake below $B/\Delta p$, which breaks her incentives.
- Because investors never use the right in equilibrium, since she behaves, so the right adds no income while she still demands compensation $\gamma$ for granting it to them.
<!-- YW5zOjE= -->
> If investors hold the right, they exercise it, since it is weakly dominant for them. Misbehaving is then less costly for the entrepreneur, and the incentive constraint becomes $(\Delta p - \nu)R_b \ge B$. The financing condition tightens to $p_H[R - B/(\Delta p - \nu)] \ge I - A$. This action interacts with effort, so the usual result that control raises pledgeable income reverses. The action does not change $p_H$, and its cost falls on the entrepreneur.
> Ref: Tirole Ch. 10 §10.2.1 (pp. 389–391); Tirole, Answers to Selected Exercises, Ex. 10.5 (p. 613)
> Similar: Lista R8, Ex. 8 (Tirole 10.5); Lista R8, Ex. 10 (Tirole 10.6)

Q: Control over $K$ decisions can be split between the entrepreneur and investors. Moving decision $k$ to investors raises the success probability by $\tau_k$ and costs the entrepreneur $\gamma_k$; success pays $R$, and the financing constraint binds. Which allocation is optimal, and how does it change as the entrepreneur's net worth $A$ falls?
- Investors get exactly the rights with $\tau_k R \ge \gamma_k$, the first-best set; a lower $A$ is met by giving investors a larger cash claim, since control is never given up just to raise funds.
- Investors get the rights with the largest $\tau_k$ whatever their $\gamma_k$, since only the gain in success probability matters to them; a lower $A$ adds rights in decreasing order of $\tau_k$.
- Investors get every right with $\tau_k R/\gamma_k \ge \theta$ for a threshold $\theta < 1$; as $A$ falls, $\theta$ falls, so weaker firms also give up rights whose transfer destroys some value.
- Investors get the rights with the smallest $\gamma_k$, since those are cheapest for the entrepreneur to give up; as $A$ falls, $\theta$ rises, so weaker firms keep more rights to protect their benefits.
<!-- YW5zOjI= -->
> The derivative of the Lagrangian with respect to $x_k$ is $(\tau_k R - \gamma_k) + \mu\tau_k(R - B/\Delta p)$. Rights are ranked by investors' relative willingness to pay, $\tau_k R/\gamma_k$, and a binding financing constraint ($\mu > 0$) pushes the threshold below 1. All first-best rights are given up, plus some inefficient ones. A weaker balance sheet raises $\mu$ and lowers $\theta$, so more rights are given up. Cash is the efficient currency for paying investors, but at the margin it has already run out.
> Ref: Tirole Ch. 10 §10.2.2 (pp. 392–393); Amaro de Matos Ch. 5 §5.1.4 (p. 133)
> Similar: Lista R8, Ex. 14 (Tirole 10.9)

## act

Q: In a control contest between an incumbent and a rival management team, each owns shares and enjoys private benefits from control, while passive shareholders vote for the incumbent with a probability that is higher when the incumbent is the more able team. Which statement about voting and the incumbent's financing choice is correct?
- Each team votes by its private signal of ability, since it owns cash-flow rights, so its votes reveal who is better and passive holders follow them; debt plays no role in the contest.
- Passive holders' votes are uninformative, since they cannot observe ability, so the contest is decided by the contenders' own blocks; debt helps the incumbent by making the firm worth less to the rival.
- The incumbent votes for itself only if able, while the rival always votes for itself; issuing debt hurts the incumbent, since it lowers its stake in equity and so its share of the votes.
- Each team votes for itself whatever it believes, since control benefits outweigh its cash-flow stake; passive votes decide the outcome, and swapping debt for equity raises the incumbent's vote share.
<!-- YW5zOjM= -->
> A contender gains its control benefit only if it wins, and loses only its fraction of the value difference if the less able team runs the firm, so it always votes for itself. Its own votes therefore carry no information. The outcome rests on passive shareholders, who back the incumbent with probability $q_1 > q_2$ when it is more able. A debt-for-equity swap raises the incumbent's equity fraction $\alpha_I(D) = \alpha Y/E(D)$, so it controls more votes. That is why the incumbent's choice of debt determines whether the outcome is a successful tender offer, a proxy fight or no contest.
> Ref: Amaro de Matos Ch. 8 §8.2.4 (pp. 214–216); Tirole Ch. 1 §1.4 (p. 36)
> Similar: Lista R8, Ex. 6 (Amaro de Matos 8.2.6 #10)

Q: Three otherwise identical firms differ in board power: in firm 1 the board controls investment, operations and financing; in firm 2 it controls financing but cannot monitor investment or operations; in firm 3 it controls almost nothing. How are their debt ratios likely to rank?
- Firm 2 borrows most, using debt to discipline managers it cannot monitor directly; firm 1 sets debt by the tax and distress trade-off alone; firm 3's managers keep debt low to keep slack.
- Firm 1 borrows most, since a strong board can bear more distress risk; firm 2 borrows least, since its board has no say over investment; firm 3 sits in between, set by its managers' preferences.
- Firm 3 borrows most, since managers free of oversight value the tax shield on their own bonuses; firm 1 borrows least, since a strong board needs no extra cash from debt; firm 2 sits in between.
- All three choose the same debt ratio, since under MM the financing choice is irrelevant to value; who controls financing affects only the split of value between creditors and shareholders.
<!-- YW5zOjA= -->
> Debt commits free cash flow to creditors and threatens liquidation, so it disciplines managers. A board that controls financing but not investment uses that lever because it has no other. A board with full control can stop waste directly, so it chooses leverage on tax and distress grounds only. Entrenched managers who set their own financing prefer low debt to keep slack and lower the risk of default. MM irrelevance does not hold once agency costs depend on leverage.
> Ref: Tirole Ch. 1 §1.3 (p. 29), §1.6 (p. 51); Tirole Ch. 5 §5.6 (p. 225); Higgins Ch. 6 §6.2.6 (p. 219)
> Similar: Lista R8, Ex. 5 (Grinblatt & Titman 18.4)
