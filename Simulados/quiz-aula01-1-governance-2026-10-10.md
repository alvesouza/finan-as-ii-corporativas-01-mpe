---
quiz: "Class 1 · Quiz 1 — Insiders, outsiders and corporate governance"
tags:
  asym: "Information asymmetries"
  gov: "Governance and the agency problem"
  instr: "Incentive instruments and evidence"
---

## asym

Q: After raising outside funds, a founder can quietly shift her attention to an easier side project, which lowers the probability that the funded project succeeds; investors observe only success or failure. Which asymmetry is this, and why does a complete-markets Arrow–Debreu benchmark have nothing to say about it?
- Adverse selection: the founder privately knows her own type before signing, and Arrow–Debreu prices all claims as if types were public, so the misallocation of funds to bad types goes unpriced.
- Moral hazard: the action comes after financing and before the outcome and cannot be contracted on, while Arrow–Debreu assumes every action is contractible, so there is nothing to govern.
- Hidden knowledge: the founder learns the realized income first and can under-report it, while Arrow–Debreu assumes income is verifiable, so diversion of reported cash is ruled out by assumption.
- Moral hazard: the action is unobserved, but Arrow–Debreu handles it by trading state-contingent claims on effort, so the benchmark prices it through a separate market for each effort level.
<!-- YW5zOjE= -->
> The choice of effort or project after the money arrives is moral hazard, the "in between" asymmetry. Arrow–Debreu "said little about the firms' financial choices and about their governance" precisely because all actions are contractible there. Effort is not a state of nature, so there is no state-contingent market for it; adverse selection is pre-contract, hidden knowledge is post-outcome.
> Ref: Tirole, Introduction, pp. 1–2; Class 1 notes §1
> Similar: Ross Fundamentos, Cap. 1, CQ 1.7 (p. 22)

Q: Classify three frictions by timing: (i) the founder knows, before signing, whether her market really exists; (ii) once the project runs, she sees the accounts first and could report a smaller success than the one realized; (iii) after funding, she chooses how hard to work. Which mapping is correct?
- (i) moral hazard, because her market knowledge shapes her later effort; (ii) adverse selection, because she has better information than investors; (iii) hidden knowledge, because effort is private.
- (i) adverse selection; (ii) moral hazard, because misreporting is an action she takes; (iii) hidden knowledge, because only she knows her effort once the outcome is realized.
- (i) hidden knowledge, because the market state is learned privately; (ii) moral hazard, because reporting is a choice; (iii) adverse selection, because hard workers self-select into financing.
- (i) adverse selection, before the contract; (ii) hidden knowledge of realized income, after the outcome; (iii) moral hazard, between financing and outcome.
<!-- YW5zOjM= -->
> Tirole sorts the three asymmetries by timing: adverse selection before the contract, hidden knowledge of realized income after the outcome, and moral hazard in between. The distractors swap labels by appealing to who "chooses" or who "knows", which every asymmetry involves; timing is what separates them.
> Ref: Tirole, Introduction, pp. 1–2; Class 1 notes §1 (table of asymmetries)
> Similar: Ross Fundamentos, Cap. 1, CQ 1.7 (p. 22)

## gov

Q: Tirole adopts the Shleifer–Vishny definition of corporate governance. Which statement is consistent with that definition as the course uses it?
- Governance is the ways suppliers of finance assure themselves of a return on their investment, so it is defined from the outsiders' side and boards matter only through it.
- Governance is the set of rules that make the firm maximize the joint surplus of all its stakeholders, so employees and suppliers count as much as the providers of finance do.
- Governance is the internal organization of the board of directors, so its quality is measured by board size, independence and committee structure rather than by investors' returns.
- Governance is the set of protections that shield managers from short-term market pressure, so that they can pursue long-run value without the threat of takeovers or dismissal.
<!-- YW5zOjA= -->
> The definition is "the ways in which suppliers of finance to corporations assure themselves of getting a return on their investment" — Tirole calls it the narrow, orthodox view, written entirely from the outsiders' side. The stakeholder view is discussed later in Ch. 1 but is not the definition adopted; board structure is an instrument, not the definition; shielding managers is close to entrenchment.
> Ref: Tirole, Ch. 1 §1.1, p. 15; Class 1 notes §2.1
> Similar: Ross Fundamentos, Cap. 1, CQ 1.6 (p. 22)

Q: Compare a firm with thousands of small shareholders and a professional manager with a firm in which a family holds a controlling block and the remaining shares are dispersed. Which statement correctly locates the central agency conflict in the second firm?
- The conflict is the same as in the first firm, between the manager and shareholders as a group, because a controlling block only changes who sits on the board, not who bears the cost of monitoring.
- The conflict disappears, because a controlling shareholder internalizes the whole value of the firm and therefore has the same objective as every minority shareholder.
- The conflict moves to the controller versus the minority: the controller can monitor the manager well, so the open question becomes who monitors the controller.
- The conflict moves to creditors versus shareholders, because a family block raises leverage and the main divergence becomes asset substitution against lenders.
<!-- YW5zOjI= -->
> Tirole contrasts the Anglo-Saxon shape (dispersed owners vs. manager) with the continental-European shape (controlling shareholder vs. minority). The controller has the incentive to watch the manager, but it does not own the whole firm, so its objective can diverge from the minority's — hence "who monitors the controller".
> Ref: Tirole, Ch. 1 §1.1, p. 15; Class 1 notes §2.1
> Similar: Ross Fundamentos, Cap. 1, CQ 1.15 (p. 23)

Q: A shareholder owns a fraction $\alpha \in (0,1)$ of a firm. Monitoring the manager costs her $c > 0$ privately and raises total firm value by $\Delta V > 0$. Which pair of conditions shows why monitoring is under-supplied when ownership is dispersed?
- She monitors iff $\alpha\,\Delta V \ge c$, while monitoring is efficient iff $\Delta V \ge c$; for $\alpha < 1$ every $c \in (\alpha\Delta V, \Delta V]$ is valuable but not undertaken.
- She monitors iff $\Delta V \ge c$, while monitoring is efficient iff $\alpha\,\Delta V \ge c$; for $\alpha < 1$ she monitors more often than is efficient because she ignores the others.
- She monitors iff $\alpha\,\Delta V \ge \alpha c$, while monitoring is efficient iff $\Delta V \ge c$; the two conditions coincide, so dispersion changes nothing.
- She monitors iff $\Delta V \ge c/\alpha$, while monitoring is efficient iff $\Delta V \ge \alpha c$; for $\alpha < 1$ she monitors whenever the social planner would.
<!-- YW5zOjA= -->
> She bears the whole cost $c$ but captures only $\alpha\,\Delta V$, so she monitors iff $\alpha\Delta V \ge c$. The planner counts the whole gain, $\Delta V \ge c$. With $\alpha<1$ there is a range of valuable monitoring nobody supplies: monitoring is a public good among shareholders, the Berle–Means mechanism. The third option scales the cost by $\alpha$, which would be true only if she could share the cost.
> Ref: Tirole, Ch. 1 §1.1, pp. 15–16; Class 1 notes §2.1
> Similar: Ross Fundamentos, Cap. 1, CQ 1.15 (p. 23)

## instr

Q: Jensen and Murphy find that a 1,000-dollar rise in shareholder wealth moves the median large-firm CEO's wealth by about 3.25 dollars, and Hall and Liebman, counting options properly, report a mean near 25 and a median near 5.30 dollars per 1,000. Which conclusion does Tirole's discussion support?
- Incentives are clearly strong enough once options are counted, so the grocer analogy is obsolete and larger stakes would add risk without adding effort.
- Pay–performance sensitivity is too low by any standard, so the optimal contract gives the CEO a stake close to 100% of the firm, as an owner-manager would hold.
- Pay–performance sensitivity is nearly zero, so CEO pay is unrelated to performance and boards should replace stock-based pay with fixed salaries.
- Measured sensitivity looks weak, but a larger stake is not always better: a risk-averse manager with her wealth in one firm may refuse risky, valuable projects.
<!-- YW5zOjM= -->
> The numbers are quoted from Tirole p. 24. The grocer who keeps a fraction of a cent per dollar "would start eating the apples", but Tirole also warns that too large a stake makes a risk-averse manager refuse good risky projects. So the right stake is interior: the question is how much of the pie the insider must keep, never "incentives or none".
> Ref: Tirole, Ch. 1 §1.2, pp. 20–25; Class 1 notes §2.4
> Similar: Ross Fundamentos, Cap. 1, CQ 1.16 (p. 23)

Q: A risk-neutral manager is paid either one share, worth the end-of-period price $P$, or one stock option with strike $K$, worth $\max(0, P - K)$. Today the expected price is far below $K$. She can take a gamble that is a mean-preserving spread of $P$. How does each contract affect her incentive to take it?
- Both payoffs are linear in $P$ on the relevant range, so a mean-preserving spread leaves the expected value of both contracts unchanged and she is indifferent under either.
- The option payoff is convex in $P$, so a mean-preserving spread raises its expected value and she gambles; the share is linear in $P$, so the spread leaves her expected pay as is.
- The option payoff is concave in $P$, so a mean-preserving spread lowers its expected value and she avoids risk; the share is linear in $P$, so she is indifferent to the spread.
- The share payoff is convex in $P$ because of limited liability, so she gambles with shares; the option is flat below $K$, so under water she has no reason to change the spread.
<!-- YW5zOjE= -->
> $\max(0,P-K)$ is convex, so by Jensen's inequality a mean-preserving spread raises its expectation; under water the option is worth little unless something remarkable happens, so the manager has nothing to lose from a wild gamble — gambling for resurrection. The share pays $P$, linear, so a risk-neutral holder is indifferent to a spread.
> Ref: Tirole, Ch. 1 §1.2.2, pp. 21–23; Class 1 notes §2.4
> Similar: Amaro de Matos, §3.1.5, exercise 3 (p. 77)

Q: Classify four watchers by Tirole's monitoring distinction: a bank renegotiating a covenant, a rating agency downgrading the firm, a large shareholder sitting on the board, and a short-term lender refusing to roll over a loan.
- Active: the rating agency and the large shareholder, since both shape future policy; speculative: the bank and the short-term lender, since both are creditors who act only through prices.
- Active: all four, because each one changes the firm's future behaviour; the speculative label applies only to anonymous stock-market traders who never contact the firm.
- Active: the bank and the large shareholder, who use control rights to change policy; speculative: the rating agency and the short-term lender, who judge past results and act via prices or exit.
- Active: the bank and the short-term lender, since both hold debt with covenants; speculative: the rating agency and the large shareholder, since both hold claims whose value moves with the share price.
<!-- YW5zOjI= -->
> Active monitoring is forward-looking intervention with control rights (board seat, renegotiation). Speculative monitoring is backward-looking: it "takes a picture" of what the firm has done and disciplines through prices and the threat of leaving (analysts, rating agencies, a lender who refuses to roll over). The split is about the mode of action, not the type of claim.
> Ref: Tirole, Ch. 1 §1.2, pp. 25–28; Class 1 notes §2.4
> Similar: Ross Fundamentos, Cap. 1, CQ 1.7 (p. 22)

Q: Country X reports few corporate scandals and has little outside finance; country Y reports many scandals and has large equity and bond markets. What does Tirole's iceberg argument allow you to infer about governance in the two countries?
- Very little from scandal counts: observed misbehaviour is a selected tip, and few scandals can reflect strong governance or simply too little outside money to divert.
- That X has better governance, because the number of observed scandals is a direct measure of how often insiders expropriate outsiders in a given legal system.
- That Y has better governance, because large markets exist only where investors are protected, so its scandals reveal that monitoring works and detects misconduct.
- That both have equal governance once scandals are scaled by market size, because the ratio of scandals to outside finance is the iceberg's correct summary statistic.
<!-- YW5zOjA= -->
> Tirole's iceberg: what we see is the misbehaviour that got through; beneath it are "the averted ones" (covenants, boards, auditors, lenders who refused). Scandal counts are a selected sample, and a country with little outside finance may have little to steal. No single ratio repairs that selection problem.
> Ref: Tirole, Ch. 1 §1.1.2, pp. 17–20; Class 1 notes §2.3
> Similar: Ross Fundamentos, Cap. 1, CQ 1.15 (p. 23)

Q: Gilson finds that 52% of financially distressed firms replace senior management, against 19% of firms with equally poor stock returns but no distress. How does this fact bear on the Modigliani–Miller claim that financial structure only splits the corporate pie?
- It supports MM: turnover is a reallocation of control among existing claimants, so it changes who receives the pie but leaves the firm's total cash flow untouched.
- It is unrelated to MM, which concerns the market value of claims, whereas turnover concerns personnel; MM's irrelevance holds whatever the management team does.
- It supports MM only if investors are risk neutral, because then expected cash flow is the same before and after the change in management and the split is all that varies.
- It undercuts MM: leverage changes the manager's threat of dismissal and hence her non-contractible behaviour, so the level of debt can change the size of the pie itself.
<!-- YW5zOjM= -->
> Distress, not just poor performance, raises turnover, so debt is an implicit incentive — a governance device. If debt changes what managers do and those actions cannot be contracted on, income depends on the financial structure, which is exactly where Tirole says MM breaks: "the split of the pie matters".
> Ref: Tirole, Ch. 1 §1.2.3, pp. 25–26; Ch. 2 §2.2, p. 79; Class 1 notes §2.4, §3.3
> Similar: Ross Fundamentos, Cap. 16, CQ 16.2 (p. 575)
