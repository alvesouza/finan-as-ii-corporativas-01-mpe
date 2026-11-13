---
quiz: "Topic 3 — Asymmetric information (hard, conceptual)"
tags:
  lemons: "Lemons, cross-subsidies, breakdown and credit bureaus"
  pecking: "Pecking order and information sensitivity"
  sw: "Stiglitz–Weiss rationing"
  signal: "Signalling: collateral, retained stakes, IPO underpricing"
---

## lemons

Q: In a two-type credit lemons model — penniless borrowers, investment $I$, return $R$ on success and 0 on failure, success probability $p$ for good types and $q<p$ for bad types, prior success probability $m$ — suppose $qR > I$ and $mR \ge I$, so one pooling loan finances both types. What does asymmetric information cost society in this case?
- The good type's lost surplus is a deadweight loss, since paying more than its fair rate leads it to cut effort, and the project's success probability falls below its full-information level.
- Nothing in aggregate: every project has positive NPV and is funded, so the good type's overpayment is exactly the bad type's subsidy, a pure transfer with no loss in total surplus.
- The cross-subsidy is itself the inefficiency, because bad types now invest in projects that would not be financed at their own fair rate, which destroys value relative to the first best.
- A risk premium on the pooled loan, since investors who cannot tell the types apart face extra uncertainty about repayment and demand compensation that is lost to both types of borrower.
<!-- YW5zOjE= -->
> With $qR > I$ both projects are worth funding, and pooling at $mR_u = I$ funds both. The good type pays $I(p/m-1)$ more than its fair cost and the bad type gains the same amount in aggregate, since $\alpha p/m + (1-\alpha)q/m = 1$: pure redistribution. Efficiency is lost only when the pool funds negative-NPV bad types ($qR < I \le mR$, overinvestment) or breaks down ($mR < I$). Effort is not a choice in this model, and investors are risk-neutral.
> Ref: Topic 3 slides 4–27; Tirole Ch. 6 §6.2 (pp. 241–243)
> Similar: Lista Topic 3, Ex. 8 (Tirole 6.2); Lista R7, Ex. 11 (Tirole 6.2)

Q: In a lemons credit model, good types succeed with probability $p$ and bad types with $q<p$, $\alpha$ is the share of good types, $m=\alpha p+(1-\alpha)q$, the project returns $R$ or 0, costs $I$, and borrowers are protected by limited liability. If $pR > I > mR$, why can't a good borrower get funded by offering lenders a higher repayment?
- Offering a higher repayment would attract only bad types, exactly as in Stiglitz–Weiss, so lenders rationally read a high offered rate as the mark of a bad borrower and turn the application down.
- The good type could raise the repayment, but its own net value would turn negative, since at any repayment above the pooled rate the good project no longer covers the cost of the investment.
- Lenders are risk-averse here, so the higher repayment raises the variance of their payoff by more than its mean, and their certainty-equivalent return stays below the cost of the investment.
- Limited liability caps the repayment at the project's return, any offer is mimicked so lenders keep the prior, and even the full return pledged is worth less to them than the cost of the investment.
<!-- YW5zOjM= -->
> Whatever the good type offers, the bad type offers the same, so beliefs stay at $m$. The most a lender can be promised is $R$, worth $mR < I$: breakdown, with positive-NPV good projects unfunded ($\alpha < \alpha^* = (I/R-q)/(p-q)$). The good type's value $p(R-R_u)$ stays non-negative up to $R_u = R$, so it is willing; the problem is that no pledge can cover $I$. There is no Stiglitz–Weiss sorting: both types earn the same $R$ on success.
> Ref: Topic 3 slides 12–19; Tirole Ch. 6 §6.2 (p. 241)
> Similar: Lista Topic 3, Ex. 6 (Tirole 6.1); Lista R5, Ex. 6 (Tirole 6.1)

Q: A credit bureau publishes a noisy public signal of each borrower's type in a two-type lemons credit market, and lenders price each loan on the posterior. When does the bureau raise total surplus, rather than only redistributing it between the types?
- When the signal changes which projects are funded, by no longer financing negative-NPV bad types or by reviving a pool that had broken down; otherwise it only shrinks the cross-subsidy.
- Always, because the good type pays a rate closer to its fair rate, and the good type's gain in utility counts as a social gain, while the higher rate paid by the bad type is just a cost borne by lenders.
- Never, because lenders break even with or without the bureau, so better information can only move surplus between borrowers and cannot change the total value of the projects that end up financed.
- Whenever the signal is informative, since posterior rates move toward the full-information rates, and any mispricing of a loan is a deadweight loss whatever happens to the set of funded projects.
<!-- YW5zOjA= -->
> With both types funded before and after, the signal moves rates toward each type's fair rate: the good type gains (8 to 9.27 in the slides) and the bad type loses the same in expectation. Surplus rises only when the set of funded projects changes, as in the overinvestment case where bad types with a bad signal are no longer funded (value rises from 32.5). Lenders' zero profit does not make information worthless: it can change allocations.
> Ref: Topic 3 slides 28–37; Tirole Ch. 6 §6.2 (p. 241)
> Similar: Lista Topic 3, Ex. 13 (Tirole 6.7); Lista Topic 3, Ex. 9 (Tirole 6.6); Lista R7, Ex. 19 (Tirole 6.7)

## pecking

Q: Managers know the value of the firm's assets in place better than the market, act for existing shareholders, and have a positive-NPV project that must be financed externally. Why may the firm pass up the project, and why does riskless debt avoid the problem?
- New shares sell at a fair price only for bad firms, so good firms issue equity anyway to show confidence, and riskless debt is avoided because its fixed payments reveal nothing about the value of the assets.
- Issuing any security reveals the firm's type and lowers its price by the full value of the private information, and riskless debt avoids this only because interest payments are tax-deductible for the issuer.
- Equity sold at a pooled price below its true value hands new shareholders a transfer that can exceed the project's NPV, while riskless debt is priced correctly whatever managers know, so nothing is transferred.
- Managers fear that the price drop at the announcement will invite a takeover, and riskless debt avoids this because creditors gain control rights that shield the managers from the market for corporate control.
<!-- YW5zOjI= -->
> In Myers–Majluf, a good firm's shares are underpriced at the pooled price. Issuing them gives new shareholders part of the assets in place for less than their value; when that dilution exceeds the NPV, existing shareholders prefer to forgo the project, and an issue announcement is read as bad news. Riskless debt pays the same in every state, so private information about the assets does not affect its price: information insensitivity, not taxes, is the reason.
> Ref: Topic 3 slides 38–39; Tirole Ch. 6 §6.1 (p. 237); Amaro de Matos Ch. 3 §3.2.3 (p. 85); Ross Cap. 16 §16.8 (p. 564)
> Similar: Lista Topic 3, Ex. 11 (Amaro de Matos 3.2.6 #4); Lista Topic 3, Ex. 15 (Tirole 6.5); Lista R5, Ex. 12 (Amaro de Matos 3.2.6 #5)

Q: Debt is the optimal outside claim in two course models with a project paying $R_S$ on success or $R_F$ on failure, $0<R_F<I$: one where the borrower privately knows her success probability, one where her effort is unobservable. With $R_u$ the investors' payoff and $R_f$ the borrower's, superscripts $S$ and $F$ for the outcome, which statement gives the right reason in each model?
- Adverse selection: pledging all of $R_F$ minimises the information-sensitive spread $R_u^S-R_u^F$. Moral hazard: a failure payoff $R_f^F=0$ maximises the reward spread that buys effort.
- Adverse selection: debt leaves the borrower $R_f^F=0$, which deters bad types from applying. Moral hazard: pledging all of $R_F$ makes the investors' claim insensitive to the effort the borrower chooses.
- In both models debt is optimal for one reason: its tax shield $\tau r_D D$ raises pledgeable income, so a borrower can raise more with debt than with equity for the same expected payoff to herself.
- In both models debt is optimal because investors are risk-averse, and a fixed claim of $R_F$ in failure gives them the least risk per unit raised, while equity would require a premium above $I$.
<!-- YW5zOjA= -->
> Under adverse selection the good type's utility is NPV $+(m-p)(R_u^S-R_u^F)$ with $m<p$, so she minimises the spread: $R_u^F = R_F$, a debt claim (bad types still pool, they do not drop out). Under moral hazard the IC is $\Delta p(R_f^S-R_f^F) \ge B$, and any payoff on failure is unpledged rent, so $R_f^F = 0$. Same contract, two different frictions; both models have risk-neutral investors and no taxes.
> Ref: Topic 3 slides 40–46; Topic 4A slides 47–65; Tirole Ch. 6 §6.2 (p. 241); Tirole Ch. 3 §3.6 (p. 132)
> Similar: Lista Topic 3, Ex. 12 (Tirole 6.8); Lista R4, Ex. 10 (Tirole 3.18)

## sw

Q: In the Stiglitz–Weiss example a safe type succeeds with probability $p_L$ and a risky type with $p_H<p_L$, both projects have the same mean $\bar R$, a loan of $I$ is made at rate $r$, failure pays 0, and $m$ is the pool's average success probability. Why does the lender's expected return drop discontinuously at $r^*=\bar R/(p_L I)-1$?
- At $r^*$ the higher repayment leads every borrower to switch to a riskier project, so the success probability of each loan falls from $p_L$ to $p_H$ even though the pool itself is unchanged.
- At $r^*$ the risky type's surplus $\bar R-p_H(1+r)I$ reaches zero first, so risky borrowers leave, and the lender loses the high interest it was earning on the loans that succeed.
- At $r^*$ the safe type's surplus $\bar R-p_L(1+r)I$ hits zero, so safe borrowers leave, and the lender's return per unit lent falls from $m(1+r)$ to $p_H(1+r)$ on the risky pool left.
- At $r^*$ the repayment $(1+r)I$ exceeds $\bar R$, so every borrower defaults in expectation, and the lender's return falls to the share of the loan it recovers when the projects fail.
<!-- YW5zOjI= -->
> A borrower's surplus is $\bar R - p_i(1+r)I$: the safe type repays more often, so a higher rate hurts it more and it exits first, at $r^*$. Below $r^*$ the lender earns $m(1+r)$; just above it, only $p_H(1+r)$. The return is non-monotone in $r$, supply bends backward, and the lender may prefer to ration at a rate below the market-clearing one. The type pool, not each borrower's project choice, is what changes.
> Ref: Topic 3 slides 47–55; Tirole Ch. 3 §3.1 (p. 113); Tirole Ch. 6 §6.1, fn. 5 (p. 240)
> Similar: Lista Topic 3, Ex. 16 (original); Lista Topic 3, Ex. 17 (original)

Q: Raising the loan rate drives safe borrowers out first in Stiglitz–Weiss, but not in the two-type lemons credit model, where both types earn the same $R$ on success and differ only in success probability. What explains the difference?
- In the lemons model borrowers are risk-averse, so both types value the loan by the same certainty equivalent, while in Stiglitz–Weiss borrowers are risk-neutral and each type compares only expected payoffs.
- In the lemons model both types get $R-R_u$ on success, so both stay until $R_u=R$; in Stiglitz–Weiss the safe type's success payoff is smaller, so its surplus hits zero at a lower rate than the risky type's.
- In the lemons model the bad type's project has negative NPV and is never funded, so there is no pool to worsen, while in Stiglitz–Weiss both types are funded at low rates and the pool shifts with $r$.
- In the lemons model lenders observe collateral and sort the types, so raising the rate never changes the pool, while in Stiglitz–Weiss collateral is unavailable and the rate is the only screening tool.
<!-- YW5zOjE= -->
> Lemons: type $i$ gets $p_i(R-R_u)$, positive for both until $R_u = R$, so the rate cannot change the mix; the market fails by breakdown, not by sorting. Stiglitz–Weiss: equal means with a mean-preserving spread, so the safe type's success payoff $R_L$ is lower and its participation constraint binds first. Both models assume risk-neutral agents, and the lemons model allows $qR > I$.
> Ref: Topic 3 slides 4–19, 47–55; Tirole Ch. 6 §6.2 (p. 241)
> Similar: Lista Topic 3, Ex. 17 (original); Lista Topic 3, Ex. 8 (Tirole 6.2)

## signal

Q: Collateral worth less to lenders than to the borrower, a large stake retained by the owner at an IPO, short debt maturity and high payouts are all used to signal a good type. What do they share as signalling devices?
- Each is a transfer from bad types to good types that leaves total surplus unchanged, so the separating outcome is efficient and the only effect of the signal is to remove the cross-subsidy.
- Each costs nothing in equilibrium, because bad types never mimic the good type's choice, so the cost of the signal is never incurred and the good type obtains its full-information payoff.
- Each works only when investors are risk-averse, because the signal lowers the variance of the investors' payoff, and a risk-neutral investor would ignore it and price the firm at the prior.
- Each is costlier for a bad type than for a good one, and the good type bears a real loss to separate, such as undiversified risk on a retained stake or a deadweight loss on seized collateral.
<!-- YW5zOjM= -->
> These are dissipative signals: separation works because the cost differs by type (single crossing), and the good type still pays it on the equilibrium path. In Leland–Pyle the high type retains $\tilde\alpha$ and bears the risk cost $\rho\tilde\alpha^2\sigma^2/2$; with collateral, $(1-\delta)C$ is lost on failure. Mimicking is deterred, not costless, and the lenders in the collateral model are risk-neutral.
> Ref: Topic 3 slides 56–82; Tirole Ch. 6 §6.3 (p. 249); Amaro de Matos Ch. 3 §3.2.2 (p. 82)
> Similar: Lista Topic 3, Ex. 14 (Amaro de Matos 3.2.6 #2); Lista Topic 3, Ex. 10 (Tirole 6.10); Lista R5, Ex. 4 (Berk 17.14–17.18)

Q: Collateral worth $C$ to a borrower is worth $\delta C$ to a lender, with $0<\delta<1$; good types succeed with probability $p$, bad types with $q<p$, both projects have positive NPV, and $\alpha$ is the share of good types, with $m=\alpha p+(1-\alpha)q$. When does the good type prefer the separating collateral contract to pooling without collateral?
- When $\alpha$ is low or $p-q$ large: the pooling discount $I(p/m-1)$ grows with the bad types' weight, while the separating contract, pinned by no-mimicking and break-even, does not involve $\alpha$.
- When $\delta$ is close to 0, because collateral that is almost worthless to the lender is cheap for the good type to post, so even a small amount separates the types at a negligible deadweight loss.
- Always, because separation removes the cross-subsidy entirely and lets the good type borrow at $I/p$ with no collateral cost, which is its symmetric-information payoff whatever the value of $\alpha$.
- When $\alpha$ is high, because with few bad types the no-mimicking constraint is slack, so the good type posts little collateral, while with many bad types the collateral needed becomes prohibitive.
<!-- YW5zOjA= -->
> The good type's problem has two binding constraints: the bad type's no-mimicking condition (relative to $qR - I$) and the lender's break-even. Neither involves $\alpha$, so the cost of separating, $(1-p)(1-\delta)C_G$ plus the repayment premium, is fixed; the pooling loss $I(p/m-1)$ rises as $\alpha$ falls or $p-q$ widens. A low $\delta$ makes signalling dearer, since more of $C$ is destroyed, and separation never gives the full-information payoff.
> Ref: Topic 3 slides 56–67; Tirole Ch. 6 §6.3, Application 5 (pp. 251–253)
> Similar: Lista Topic 3, Ex. 18 (original); Lista Topic 3, Ex. 19 (original)

Q: In Rock's IPO model the issue is worth $V_G$ or $V_B$, informed investors holding a share $\lambda$ of capital subscribe only to good issues, uninformed investors cannot tell issues apart, oversubscribed issues are rationed pro rata, and the issuer knows no more than the uninformed. Why is the offer price set below the issue's unconditional expected value?
- The issuer leaves money on the table to signal that the issue is good, and only issuers of good firms can afford the lost proceeds, so underpricing separates the good issuers from the bad ones.
- Uninformed investors are risk-averse and rationing makes their allocation random, so they require a discount to bear allocation risk, which disappears only if shares are allotted by lottery.
- Uninformed investors get full allocations of bad issues and are rationed in good ones, so they break even only below the unconditional value; the discount rises with $\lambda$ and with $V_G-V_B$.
- Informed investors bid up good issues in the aftermarket, so the offer price must be lower to compensate the issuer, and the discount shrinks as the informed share $\lambda$ of capital rises.
<!-- YW5zOjI= -->
> Winner's curse: the uninformed receive everything they ask for when the issue is bad and only a fraction when it is good, so their allocation-weighted expected value is below $\hat V$. Their break-even price is $P_0 = (\hat V - \lambda\alpha V_G)/(1-\lambda\alpha) < \hat V$, where $\alpha$ here is the prior probability of a good issue. With $\lambda = 0$ the discount vanishes. The issuer has no private information, so this is not a signalling story.
> Ref: Topic 3 slides 83–90; Amaro de Matos Ch. 6 §6.2.2 (p. 163); Ross Cap. 15 §15.5 (p. 504); Berk Ch. 14 §14.3 (p. 425)
> Similar: Lista Topic 3, Ex. 7 (Amaro de Matos 6.2.7 #4, #6); Lista Topic 3, Ex. 1 (Ross Cap. 15, Q. 3); Lista R7, Ex. 6
