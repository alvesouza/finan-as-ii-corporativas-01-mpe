---
quiz: "Topic 4A — Moral hazard and financing capacity (hard, conceptual)"
tags:
  ic: "IC, pledgeable income and credit rationing"
  var: "Variable investment, equity multiplier and cash-flow sensitivity"
  secur: "Debt vs. equity and maximal incentives"
  pledge: "Monitoring, diversification and collateral"
---

## ic

Q: In the fixed-investment Holmström–Tirole model — wealth $A$, investment $I>A$, return $R$ or 0, success probability $p_H$ if diligent and $p_L=p_H-\Delta p$ if shirking, private benefit $B$ from shirking, risk-neutral competitive investors — a borrower with $A$ below the threshold $\bar A$ is turned down even though she offers a higher interest rate. Why does the higher rate not help?
- A higher rate attracts riskier borrowers into the pool, as in Stiglitz–Weiss, so lenders who cannot tell borrowers apart see their expected return fall once the rate rises above a critical level.
- Lenders demand a risk premium that rises with loan size, and a borrower with little wealth needs a loan so large that the premium pushes the required repayment above the project's return $R$.
- A higher repayment leaves her less than $B/\Delta p$ on success, so she would shirk and the project would lose value; investors can never be promised more than $p_H(R-B/\Delta p)$, whatever the rate.
- Her wealth is too small to serve as collateral, and lenders refuse unsecured loans at any rate, so the refusal reflects a lack of collateral rather than any problem with her incentives once funded.
<!-- YW5zOjI= -->
> The IC $\Delta p R_f \ge B$ caps what can be promised to investors at $R - B/\Delta p$ per success. Raising the rate raises $R_u$, cuts $R_f$ below $B/\Delta p$, and the borrower shirks, which by (A2) makes the project worthless to lend to. Rationing comes from the borrower's inability to commit, with one borrower type and risk-neutral lenders: no pool to worsen, no risk premium.
> Ref: Topic 4A slides 2–7, 25–35; Tirole Ch. 3 §3.2 (p. 115)
> Similar: Lista R4, Ex. 6 (Tirole 3.15); Lista R4, Ex. 5 (Tirole 3.1)

Q: In the fixed-investment moral-hazard model, financing requires $A \ge \bar A = p_H B/\Delta p-(p_H R-I)$, where $A$ is the borrower's wealth, $B$ the private benefit from shirking, $\Delta p=p_H-p_L$ the effect of diligence on the success probability, $R$ the return on success and $I$ the investment. Which statement about $\bar A$ is correct?
- Holding $p_H$ and the NPV fixed, a larger $\Delta p$ lowers $\bar A$: success is more informative about diligence, so a smaller stake $B/\Delta p$ suffices and more income can be pledged.
- A richer borrower faces a lower $\bar A$, since her wealth adds to pledgeable income one for one, so the threshold falls as $A$ rises and in the end every project of a wealthy borrower gets financed.
- A larger $B$ lowers $\bar A$, since a borrower who enjoys a bigger private benefit values the project more and accepts a smaller share of the return, which frees more of the income for investors.
- A higher NPV $p_H R-I$ raises $\bar A$, since a more valuable project needs a larger reward to keep the borrower diligent, so the rent left to her grows faster than the income that can be pledged.
<!-- YW5zOjA= -->
> $\bar A$ rises in $B$ and falls in $\Delta p/p_H$ and in the NPV. It does not depend on $A$: it is the cutoff $A$ is compared with. Pledgeable income $p_H(R - B/\Delta p)$ is also independent of $A$; wealth matters only because it reduces what must be raised, $I - A$. A larger $B$ tightens the IC, it does not loosen it.
> Ref: Topic 4A slides 25–34; Tirole Ch. 3 §3.2 (p. 115)
> Similar: Lista R4, Ex. 6 (Tirole 3.15); Lista R7, Ex. 12 (Tirole 3.3)

Q: In the fixed-investment moral-hazard model with competitive risk-neutral lenders and a zero risk-free rate, a borrower whose wealth is above the financing threshold gets funded. Who bears the agency cost of her unobservable effort, and in what form?
- The lenders, who are repaid only on success and so lose a share of the private benefit on every loan, which they recoup by charging the funded borrowers a premium over the fair rate on the loan.
- The funded borrower, who pays an interest rate above the default-adjusted fair rate by an amount tied to the private benefit, so her surplus falls short of the project's NPV by that amount.
- Nobody, because the incentive constraint holds for every borrower in the population, so all projects with positive NPV are financed and the market reaches the first-best allocation of credit.
- Borrowers below the threshold, who are shut out of positive-NPV projects; a funded borrower pays the default-adjusted fair rate and keeps the full NPV, so the cost takes the form of rationing.
<!-- YW5zOjM= -->
> With competitive lenders the IR binds: $p_H R_u = I - A$, the loan rate is $1/p_H - 1$, which only prices default, and the borrower's utility is $p_H R - I$, the full NPV. The incentive problem bites only at the extensive margin: borrowers with $A < \bar A$ cannot be funded at any rate. In the variable-investment version it also bites on scale.
> Ref: Topic 4A slides 31–37; Tirole Ch. 3 §3.2 (p. 115)
> Similar: Lista R4, Ex. 8 (Tirole 3.13); Lista R4, Ex. 5 (Tirole 3.1)

## var

Q: In the variable-investment moral-hazard model a project of scale $I$ returns $RI$ on success with constant returns; $\rho_1=p_H R$ is the expected return per unit invested and $\rho_0=p_H(R-B/\Delta p)$ the pledgeable return per unit, with $\rho_0<1<\rho_1$, $B$ the private benefit per unit, $\Delta p$ the effect of diligence on success, and $A$ the borrower's wealth. What limits the investment, and what does the equity multiplier depend on?
- Investment is limited because $\rho_1<1$ at large scale, and the multiplier $1/(1-\rho_1)$ rises with the project's NPV per unit, so more profitable firms can lever up their wealth further.
- Each unit adds $\rho_0<1$ of pledgeable income but costs 1, so $I=A/(1-\rho_0)$; the multiplier rises with $\rho_0$, so with lower $B$ or higher $\Delta p$, and does not depend on $\rho_1$.
- Investment is limited by diminishing returns to scale, and the multiplier $\rho_1/\rho_0$ measures how far the NPV exceeds the pledgeable income, so it rises when the private benefit $B$ grows.
- Investment is unbounded because $\rho_1>1$ makes each extra unit profitable, and the borrower's wealth only affects the loan rate, which falls as $A$ rises in proportion to $1/(1-\rho_0)$.
<!-- YW5zOjE= -->
> Lenders break even iff $\rho_0 I \ge I - A$, so the maximum scale is $I = kA$ with $k = 1/(1-\rho_0)$. Returns are constant and $\rho_1 > 1$ throughout; scale is capped because each unit is only partly pledgeable. The multiplier depends on the agency parameters through $\rho_0$, not on the NPV $\rho_1 - 1$, which only makes the borrower want to invest as much as possible.
> Ref: Topic 4A slides 25–30; Tirole Ch. 3 §3.4 (p. 127)
> Similar: Lista R4, Ex. 7 (Tirole 3.8); Lista R4, Ex. 12 (Tirole 3.5)

Q: In the variable-investment moral-hazard model — expected return per unit $\rho_1$, pledgeable return per unit $\rho_0$ with $\rho_0<1<\rho_1$, investment $I=A/(1-\rho_0)$, competitive lenders — what is one extra unit of wealth $A$ worth to the borrower, and what does that imply for investment–cash-flow sensitivity?
- $1$: by MM a unit of internal cash is worth exactly one unit of outside funds, so investment depends on cash flow only through the project's NPV and not through how much wealth the firm holds.
- $1/(1-\rho_0)$: each unit of wealth supports that many units of investment, so its value to the borrower equals the extra investment it unlocks, counted at cost, with no premium on internal funds.
- $\rho_1-1$: the borrower earns the NPV per unit on the extra unit she invests, so a unit of cash raises her payoff by the project's margin, and the size of the multiplier plays no role in its value.
- $(\rho_1-\rho_0)/(1-\rho_0)>1$: the unit funds itself and unlocks extra borrowing on which she earns the NPV, so internal funds carry a premium and constrained investment rises with cash flow.
<!-- YW5zOjM= -->
> The borrower's payoff is total value minus what lenders get: $\rho_1 I - (I - A) = A(\rho_1-\rho_0)/(1-\rho_0)$. The shadow value of a unit of wealth therefore exceeds 1, which is the model's reading of Fazzari–Petersen: cash relaxes the borrowing constraint, so constrained firms invest more when cash flow rises. In the fixed-investment version only firms just below $\bar A$ respond.
> Ref: Topic 4A slides 38–39; Tirole Ch. 3 §3.4 (p. 127)
> Similar: Lista R4, Ex. 11 (Tirole 3.11); Lista R4, Ex. 14 (Tirole 3.20)

## secur

Q: A project returns $R_S$ on success and $R_F$ on failure, $R_S>R_F>0$; diligence raises the success probability by $\Delta p$, shirking yields private benefit $B$, and $R_f^S, R_f^F$ are the borrower's payoffs on success and failure. Why is selling investors a share $\alpha$ of the project's equity dominated by debt?
- Equity leaves the borrower $(1-\alpha)R_F$ on failure, a reward for shirking; incentives depend only on the spread $R_f^S-R_f^F$, so that payoff is unpledged rent, which debt removes by setting $R_f^F=0$.
- Equity makes investors bear the project's risk, and since they price that risk, the share $\alpha$ needed to raise $I-A$ exceeds what debt requires, and this risk premium is what makes debt dominate.
- Equity is dominated because issuing it reveals the borrower's private information about $R_S$, so its price drops at issue, while debt with face $R_F$ is riskless and immune to any such revelation.
- Equity is dominated only when $R_F$ is close to zero, as the two claims then differ the most; for large $R_F$ the borrower's failure payoff $(1-\alpha)R_F$ strengthens her incentive to be diligent.
<!-- YW5zOjA= -->
> The IC is $\Delta p(R_f^S - R_f^F) \ge B$. Under equity, $R_f^S - R_f^F = (1-\alpha)(R_S - R_F)$, so meeting the IC also hands her $(1-\alpha)R_F$ in failure, income that cannot be pledged. Debt sets $R_f^F = 0$, maximising pledgeable income, so $\bar A_{debt} < \bar A_{equity}$. Investors are risk-neutral and information is symmetric; the result is about incentives only.
> Ref: Topic 4A slides 47–65; Tirole Ch. 3 §3.5 (p. 130), §3.6 (p. 132)
> Similar: Lista R4, Ex. 10 (Tirole 3.18)

Q: In the two-outcome moral-hazard model the optimal contract gives the borrower nothing on failure, which debt implements. Which change to the model would make that contract strictly worse than some alternative contract?
- Letting investors observe the borrower's effort, since contracts could then require diligence directly, and a zero failure payoff would only expose the borrower to default that serves no purpose.
- Giving the borrower some initial wealth, since a borrower who invests her own funds already has skin in the game and would rather hold equity than face a fixed repayment on the loan.
- Making the borrower risk-averse, since a contract that leaves her nothing on failure imposes risk, and the optimum then trades incentives against insurance; distress costs would also weigh on debt.
- Making the success return $R_S$ uncertain to investors, since debt would then become information-sensitive, so the borrower would prefer an equity claim sharing that uncertainty proportionally.
<!-- YW5zOjI= -->
> Maximal incentives rely on risk neutrality: with a risk-averse borrower, $R_f^F = 0$ loads all the project risk on her, so the optimum pays something on failure. Observable effort makes every split of cash flows equivalent (MM), not strictly worse. Initial wealth changes the amount raised, not the shape of the optimal claim. Distress costs and agency conflicts (overhang, asset substitution) are the other limits.
> Ref: Topic 4A slides 66–67; Tirole Ch. 3 §3.6 (p. 132)
> Similar: Lista R4, Ex. 9 (Tirole 3.2); Lista R4, Ex. 15 (Tirole 3.21)

## pledge

Q: In the fixed-investment moral-hazard model a monitor can be hired who, at private cost $c$, cuts the borrower's private benefit from shirking from $B$ to $b<B$; monitoring is not observable by other investors, $R_m$ is the monitor's payoff on success and $\Delta p$ the effect of diligence on success. Why must the monitor hold a stake, and when does monitoring raise borrowing capacity?
- The monitor needs no stake, since competitive monitors are paid a fee equal to $c$ up front; capacity rises whenever $b<B$, because the borrower's required stake falls from $B/\Delta p$ to $b/\Delta p$.
- Without a stake the monitor would skip the costly effort, so it needs $\Delta p R_m \ge c$; capacity rises when $(b+c)/\Delta p<B/\Delta p$, so the two stakes together leave more for uninformed investors.
- The monitor needs a stake to bear part of the project's risk, as investors are risk-averse; capacity rises in every case, because monitoring raises $p_H$, the success probability under diligence.
- The monitor needs a stake equal to the borrower's $B/\Delta p$ so both share the same incentives; capacity rises only when the monitor's cost $c$ exceeds the private benefit $b$ left after monitoring.
<!-- YW5zOjE= -->
> Monitoring is itself a hidden action, so the monitor needs its own incentive stake $R_m \ge c/\Delta p$. Uninformed investors can then be promised $p_H[R - (b + c)/\Delta p]$, more than $p_H(R - B/\Delta p)$ iff $b + c < B$. Monitoring cuts the private benefit; it does not change $p_H$, and the stake is about incentives, not risk-bearing.
> Ref: Topic 4A slides 25–30; Tirole Ch. 3 Exercise 3.8 (p. 147)
> Similar: Lista R4, Ex. 7 (Tirole 3.8)

Q: A borrower runs two identical, independent projects, each with the same moral hazard: success probability $p_H$ if diligent and $p_L=p_H-\Delta p$ if shirking, private benefit $B$ per project shirked. Why can financing both jointly, with cross-pledging, raise pledgeable income per project?
- Pooling two independent projects lowers the variance of investors' total return, so risk-averse investors accept a lower expected return, which frees pledgeable income for the same total investment.
- Joint financing raises the NPV of each project, because the borrower can shift effort to whichever project looks more promising, and the extra NPV is shared between the borrower and the investors.
- Cross-pledging removes the moral hazard entirely, since by the law of large numbers investors can infer effort exactly from the joint outcome of two projects, so the full return $R$ becomes pledgeable.
- Paying the borrower only when both succeed ties her reward to the outcome most informative of diligence on both, so the expected rent per project needed to deter shirking falls below $p_H B/\Delta p$.
<!-- YW5zOjM= -->
> With reward $R_b$ only if both succeed, the binding IC (shirk on both) is $(p_H^2 - p_L^2)R_b \ge 2B$, so the rent per project is $(p_H B/\Delta p)\cdot p_H/(p_H + p_L) < p_H B/\Delta p$. The income of one project acts as collateral for the other. Two projects are far from the law of large numbers, investors are risk-neutral, and the NPV per project is unchanged.
> Ref: Tirole Ch. 4 §4.2 (p. 158); Topic 4A slides 25–30
> Similar: Lista R4, Ex. 13 (Tirole 4.10)

Q: Collateral worth $C$ to the borrower but less to lenders appears both in the moral-hazard financing model and in the two-type adverse-selection credit model. Which statement contrasts its role in the two correctly?
- Under moral hazard it can pay even with symmetric information, as seizing it on failure widens the reward spread and raises pledgeable income; under adverse selection with known types it is never posted.
- Under moral hazard it is never posted, as a deadweight loss on failure only lowers the NPV; under adverse selection it is posted even with symmetric information, as lenders always value a claim on the asset.
- In both models collateral plays the same role: it is posted only under asymmetric information about the borrower's type, and it would be dropped from the contract as soon as types became observable.
- In both models collateral is useful only when lenders value it at least as much as the borrower, because any deadweight loss on seizure makes posting it worse than borrowing at a higher interest rate.
<!-- YW5zOjA= -->
> Under moral hazard, losing collateral on failure punishes failure, which relaxes the IC and raises pledgeable income; a constrained borrower posts it despite the deadweight loss (Tirole §4.3; with zero liquidation cost it is equivalent to investing $A$). Under adverse selection with known types, collateral only destroys $(1-\delta)C$, so it is used only to separate types under asymmetric information.
> Ref: Topic 4A slide 36; Topic 3 slides 56–67; Tirole Ch. 4 §4.3 (p. 164); Tirole Ch. 6 §6.3 (p. 249)
> Similar: Lista R7, Ex. 16 (Tirole 4.17); Lista Topic 3, Ex. 18 (original)
