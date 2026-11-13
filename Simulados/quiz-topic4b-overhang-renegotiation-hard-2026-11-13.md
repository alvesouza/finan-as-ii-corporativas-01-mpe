---
quiz: "Topic 4B — Asset substitution, debt overhang and renegotiation (hard, conceptual)"
tags:
  subst: "Asset substitution and its mitigation"
  overhang: "Debt overhang and its fixes"
  reneg: "Renegotiation, strategic default and default as insurance"
  ident: "Separating adverse selection from moral hazard"
---

## subst

Q: A levered firm run for its shareholders can choose, after borrowing, a safe positive-NPV project or a risky negative-NPV one, and no contract can specify the choice. If lenders anticipate the choice when they lend, who ends up bearing the cost of risk shifting?
- The creditors, because they hold the equivalent of a short put on the firm's assets, and the risky choice raises the value of that put, moving value from them to the shareholders after the loan is made.
- Nobody, because risk shifting is a transfer from creditors to shareholders and transfers net out; the value of the firm's assets is the same whichever project is chosen once the debt is priced fairly.
- Taxpayers, because creditors who lose from the risky choice push the firm into bankruptcy, and the resulting distress costs are partly covered by the tax shield the levered firm had been receiving.
- The shareholders, because lenders price the risky choice into the loan, raising the rate or refusing to lend, so the lost NPV returns to them as dearer credit or forgone investment, as in moral hazard.
<!-- YW5zOjM= -->
> Equity is a call on firm value with strike equal to the face of debt, so after borrowing it prefers variance. Rational lenders foresee this and price the loan on the risky project (in the example, new debt breaks down or demands a face of 220). The NPV destroyed is a real loss, not a transfer, and it falls ex ante on the party that cannot commit: the shareholders.
> Ref: Topic 4B slides 2–13, 18; Amaro de Matos Ch. 3 §3.1.3 (p. 71); Tirole Ch. 3 §3.2 (p. 115)
> Similar: Lista Topic 4, Ex. 2 (Grinblatt 16.1); Lista Topic 4, Ex. 6 (Berk 16.26); Lista R7, Ex. 4

Q: Which mechanism correctly explains how a feature of the debt contract reduces shareholders' incentive to shift risk onto creditors?
- Long-term debt mitigates risk shifting because its rate is fixed at issuance, so shareholders cannot shift risk onto creditors through a later repricing of the debt when the firm's risk changes.
- Convertible debt mitigates risk shifting because creditors can convert and share in the upside if a gamble pays off, so shareholders no longer capture all the gains that make risk attractive to them.
- Issuing claims junior to the existing debt mitigates risk shifting because junior holders absorb the losses on a risky project first, which protects the senior creditors from the shift in risk.
- Debtor-in-possession financing mitigates risk shifting because the new senior lender monitors the project choice, so the old creditors no longer need covenants that restrict the firm's investments.
<!-- YW5zOjE= -->
> Risk shifting comes from the convexity of equity's payoff. Conversion caps that convexity by handing creditors part of the upside. Short-term debt (not long-term) works by repricing risk at each rollover; covenants restrict project choice directly. Junior claims leave equity's call unchanged, and DIP financing addresses debt overhang, not risk shifting.
> Ref: Topic 4B slides 14–18; Amaro de Matos Ch. 3 §3.1.3 (p. 71)
> Similar: Lista R7, Ex. 3 (Amaro de Matos 3.1.5 #7); Lista Topic 4, Ex. 4 (Grinblatt 16.11); Lista Topic 4, Ex. 14 (Tirole 7.3)

## overhang

Q: Debt overhang and asset substitution both arise because shareholders control investment once debt is in place. Which statement tells them apart correctly?
- Overhang is underinvestment: equity pays all of a positive-NPV project's cost but creditors get part of the gain; asset substitution is a distorted choice: equity takes risk because its payoff is convex.
- Overhang is excessive risk taking: equity gambles because creditors bear the losses; asset substitution is underinvestment: equity rejects good projects because part of their gain goes to creditors.
- Overhang arises only when debt is risk-free, since then every gain from investment goes to equity; asset substitution arises only when debt is risky, since only then can losses be shifted to creditors.
- Overhang and asset substitution are one distortion seen from two sides: in both, equity rejects safe projects, and the label depends only on whether the rejected project is new or already in place.
<!-- YW5zOjA= -->
> Overhang (Myers 1977): debt in place taxes new investment at a rate tied to the default probability, so equity may reject a project with positive NPV (in the example, +50 to equity for a cost of 60). With riskless debt the tax is zero and there is no overhang. Asset substitution distorts which project is taken, towards variance, even at negative NPV.
> Ref: Topic 4B slides 2–3, 19–26; Tirole Ch. 3 §3.3 (p. 125); Higgins 13e Ch. 6 §6.2.3 (p. 208)
> Similar: Lista R7, Ex. 10 (Amaro de Matos 3.1.5 #9); Lista Topic 4, Ex. 7 (Grinblatt–Titman 16.12–16.13)

Q: A distressed firm with risky debt outstanding has a positive-NPV project that can be run only inside the firm and must be financed with new money. Why does giving the new financing priority over the existing debt, as in DIP financing, help where junior new financing does not?
- Senior new debt is cheaper because it is safer, and the lower rate cuts the cost of the project below its gain to equity, whereas junior debt carries a higher rate that makes the project's NPV negative.
- Seniority gives the new lender control rights in court, which let it force the shareholders to invest, whereas junior lenders have no control rights and must rely on the shareholders' own choice.
- Senior new claims are repaid first from the combined assets, so part of the project is funded out of the old creditors' recovery in default, while junior claims leave the old creditors' windfall intact.
- Junior new debt adds to the face value equity must repay before receiving anything, which raises the default probability, whereas senior debt is excluded from that face value by bankruptcy law.
<!-- YW5zOjI= -->
> Overhang exists because old creditors capture part of the project's value in default. A senior claim draws on that value first, so old creditors share in financing the project and the tax on new investment falls; a junior claim stands behind them and cannot claw back their windfall. The NPV does not depend on the financing rate, and the project must sit inside the firm, otherwise it could be ring-fenced.
> Ref: Topic 4B slides 24, 31; Tirole Ch. 3 §3.3 (p. 125)
> Similar: Lista Topic 4, Ex. 1 (Grinblatt 16.14); Lista R7, Ex. 9 (Grinblatt–Titman 16.3)

## reneg

Q: Creditors of a firm in debt overhang offer to cut the face value of debt so that the shareholders will invest in a positive-NPV project, but they cannot make the cut conditional on the investment. When does the unconditional write-down still lead to investment?
- Always, because any write-down raises the market value of debt by lowering the default probability, so creditors gain whether or not the shareholders end up carrying out the project.
- When, after the write-down, equity's value net of the investment cost is at least its value from keeping the concession without investing; otherwise the cut is a pure transfer.
- Never, because shareholders always prefer to pocket the concession and keep their cash, so only a write-down made contingent on investment in a contract can restore the incentive to invest.
- Only when creditors are dispersed bondholders, since dispersed creditors cannot coordinate a conditional deal, while a single bank would insist on writing the investment into the agreement.
<!-- YW5zOjE= -->
> After the cut, equity compares investing (new equity value minus the cost) with not investing (equity value with the lower face value). In the example both give 110, so investment is weakly optimal and the unconditional deal works. With a larger cut or a smaller project, equity takes the concession and does not invest. Few creditors and bank debt make renegotiation easier, but they do not change this comparison.
> Ref: Topic 4B slides 27–31; Tirole Ch. 3 §3.3 (p. 125)
> Similar: Lista Topic 4, Ex. 12 (Tirole 3.6); Lista Topic 4, Ex. 3 (Berk 16.25)

Q: In the fixed-investment moral-hazard model, financing requires $A\ge\bar A=p_H B/\Delta p-(p_H R-I)$, with wealth $A$, private benefit $B$, success probabilities $p_H$ and $p_L=p_H-\Delta p$, return $R$ and investment $I$, and the borrower gets nothing on failure. If everyone expects that after a failure the debt will be renegotiated, leaving the borrower a payoff $w>0$, what happens?
- $\bar A$ falls, since the expected payoff $w$ raises the borrower's utility from the project, and a borrower who values the project more needs a smaller share of the success return to stay diligent.
- $\bar A$ is unchanged, since renegotiation happens after the effort choice and is efficient ex post, so by the Coase argument it cannot affect any decision taken before the outcome is known.
- $\bar A$ falls, since creditors recover more after a failure under renegotiation than under liquidation, which raises the income pledgeable to investors and loosens their break-even condition.
- $\bar A$ rises, since $w$ rewards failure, so diligence now needs $\Delta p(R_f-w)\ge B$ with $R_f$ her success payoff; the extra stake cuts pledgeable income, and more borrowers are rationed.
<!-- YW5zOjM= -->
> Anticipated renegotiation softens debt. The IC becomes $\Delta p(R_f - w) \ge B$, so $R_f = w + B/\Delta p$, and pledgeable income falls by $p_H w$ plus the $(1-p_H)w$ paid on failure: the cutoff rises, credit is rationed more or priced higher. This is the ex ante cost of an ex post efficient renegotiation, the same logic as too-big-to-fail.
> Ref: Topic 4B slides 37–40; Topic 4A slides 25–30; Tirole Ch. 3 §3.2 (p. 115)
> Similar: Lista Topic 4, Ex. 12 (Tirole 3.6); Lista Topic 4, Ex. 15 (Tirole 4.9)

Q: A program offers loan modifications only to borrowers who are already delinquent, and some borrowers who could pay stop paying once it is announced. Which reading fits the lecture's distinction between kinds of default?
- Strategic default: borrowers with enough cash choose not to pay in order to qualify for better terms, an ex ante cost of renegotiation, unlike a liquidity default by a borrower who lacks the cash.
- Liquidity default: the announcement lowers the market value of borrowers' collateral, so borrowers who had the cash can no longer refinance, and their missed payments reflect a lack of funds.
- Debt overhang: borrowers expect most of any repayment to go to the lender, so they stop paying, and the drop in repayment is the ex post inefficiency that renegotiation is designed to remove.
- Adverse selection: the program draws the riskiest borrowers into the loan pool, and their higher default rate reflects a change in the composition of borrowers, not in any borrower's behaviour.
<!-- YW5zOjA= -->
> Default is strategic when the borrower can repay but chooses not to, because defaulting now pays (Mayer et al., 2014); a liquidity default happens when the cash is not there. Relief conditioned on delinquency raises the payoff of defaulting for borrowers who can pay. The pool of existing borrowers did not change, and overhang concerns new investment, not repayment.
> Ref: Topic 4B slides 39–40; Tirole Ch. 3 §3.8 (p. 141)
> Similar: Lista Topic 4, Ex. 17 (original); Lista R7, Ex. 15 (Amaro de Matos 5.2.5 #2)

Q: A risk-averse borrower with utility $u$ owes $D$, holds liquid assets $A$ that creditors cannot seize, and earns random income $Y$ with cdf $F$; in default she keeps $A+E$ and bears a non-pecuniary cost $\sigma$, so she defaults when $Y<Y^*$, where $u(A+Y^*-D)=u(A+E)-\sigma$. What does a more generous protected income $E$ do?
- It lowers the default probability, $\partial p/\partial E<0$, since a borrower who keeps more in default is less desperate and repays more often, which also lowers equilibrium interest rates.
- It leaves default unchanged, $\partial p/\partial E=0$, since $E$ matters only for cash-flow defaults with $A+Y<D$, which depend on income alone and not on what the court lets the borrower keep.
- It raises default, $\partial p/\partial E=F'(Y^*)u'(A+E)/u'(A+Y^*-D)>0$: more insurance against low income, but more default and so higher rates, which makes the ex ante welfare effect ambiguous.
- It raises default, $\partial p/\partial E>0$, and welfare rises without ambiguity, because a risk-averse borrower values the insurance and lenders absorb the extra defaults at no cost to her.
<!-- YW5zOjI= -->
> Implicit differentiation of the cutoff gives $\partial Y^*/\partial E = u'(A+E)/u'(A+Y^*-D) > 0$, so $p = F(Y^*)$ rises. Default works as insurance: it guarantees $A+E$ when income is low. But more borrowers who could pay now default, lenders price that in, and the borrower pays for the insurance through the rate, so the welfare effect has two sides (Indarte, 2023).
> Ref: Topic 4B slides 41–44
> Similar: Lista Topic 4, Ex. 16 (original); Lista Topic 4, Ex. 17 (original)

## ident

Q: In Karlan and Zinman's experiment a borrower takes up a loan at a randomly assigned offer rate $r_o\in\{r_L,r_H\}$, some high-offer takers are then surprised with a lower contract rate $r_c=r_L$, and the rate on future loans is randomised independently. Which comparison isolates adverse selection?
- Takers of the low offer, $r_o=r_c=r_L$, against high-offer takers surprised with $r_c=r_L$: same repayment terms but different terms at selection, so a gap in default reflects who chose to borrow.
- High-offer takers kept at $r_c=r_H$ against high-offer takers surprised with $r_c=r_L$: same selection, different repayment terms, so a gap in default reflects the riskier pool the high rate drew.
- Borrowers given a low future rate against those given the normal future rate: a low future rate attracts safer borrowers at take-up, so a gap in default reflects selection on the future terms.
- Takers of the high offer against people who turned it down: those who declined are the safer types, so the gap in default between the two groups measures the selection caused by the high offer.
<!-- YW5zOjA= -->
> Both groups in the right comparison repay at $r_L$, so incentives are identical; they differ only in the rate at which they chose to borrow, which is the selection effect ($\beta_o > 0$). The second comparison holds selection fixed and varies repayment terms: that is hidden action ($\beta_c$). The future rate is revealed after take-up, so it cannot select anyone; decliners have no repayment data.
> Ref: Topic 4B slides 45–58
> Similar: Lista Topic 4, Ex. 18 (original); Lista Topic 4, Ex. 19 (original)

Q: In Karlan and Zinman's design the offer rate, the contract rate and the rate on future loans are all randomised. Which distinction can the experiment still not draw?
- Between the effect of the contract rate on effort and the effect of dynamic repayment incentives, since both operate after take-up and move the same default outcome in the same direction.
- Between selection on unobserved risk type and selection on unobserved anticipated effort, since both are fixed at take-up and enter default through the offer rate in exactly the same way.
- Between hidden information and hidden action as a whole, since any rate that changes after take-up also changes who would have taken up the loan, so randomisation cannot hold the pool fixed.
- Between selection by borrowers and screening by the lender, since the lender approves applicants after seeing the offer they accepted, so a default gap across offers may reflect its approval rule.
<!-- YW5zOjE= -->
> Hidden information here includes both who is risky and who plans to exert little effort: both are decided before the surprise, so both load on $\beta_o$ and cannot be split. The two hidden-action channels are separated by independent randomisation ($\beta_c > 0$ contract rate, $\beta_b < 0$ dynamic incentive). Surprises come after take-up, so the pool is held fixed, and lender decisions are randomised, not chosen.
> Ref: Topic 4B slides 45–58
> Similar: Lista Topic 4, Ex. 18 (original); Lista Topic 4, Ex. 19 (original)
