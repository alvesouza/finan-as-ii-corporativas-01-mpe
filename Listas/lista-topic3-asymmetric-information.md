---
tags: [exercise-list, lecture-topic3, asymmetric-information]
date: 2026-11-10
---

# Exercise list — Topic 3: Asymmetric information (adverse selection, signalling, IPO underpricing)

One list for Prof. Ricca's Topic 3 lecture (`Aula/Topic_3.pdf`, mapped in [[Map/lectures-index|lectures-index]]): lemons in credit markets, pooling and market breakdown, credit bureaux, the pecking order, signalling (ratings, maturity, payout, retained ownership), Leland–Pyle and Rock's IPO underpricing. 15 real exercises ordered easy → really hard, copied verbatim from the course books for personal study (Ross statements stay in Portuguese); pages are printed, with the PDF page in brackets. Every block is taken unchanged from lists R5 and R7, where it already passed `tools/check_lists.py`; the last column says where. No book exercise covers the Stiglitz–Weiss model (block 3.6) or the costly-collateral separating contract (block 3.7) of the slides, so exercises 16–19 are **original exercises** written for those two blocks, with the user's agreement (2026-11-12): they open with an **Origin:** line instead of **Source:**, follow the slides' notation, have no book answer, and are solved in the solutions files. Links: [[Map/exercises-index|exercise index]] · [[rules/06_assimetria_informacao|rules]] · [[Listas/lista-r5-asymmetric-information|R5]] · [[Listas/lista-r7-lectures-3-5|R7]].

| Lecture block | Exercises |
|---|---|
| 3.2–3.3 Lemons, pooling, breakdown | 3, 6, 8 |
| 3.4 Credit bureau | 13 |
| 3.5 Pecking order (and Myers–Majluf) | 2, 4, 11, 12, 15 |
| 3.6 Stiglitz–Weiss credit rationing (original) | 16, 17 |
| 3.7 Signalling (ratings, maturity, payout; collateral, original) | 5, 9, 10, 18, 19 |
| 3.9 Leland–Pyle | 14 |
| 3.10 IPO underpricing (Rock) | 1, 7 |

## References

| # | Tier | Book | Ch. | Exercise | Printed p. (PDF) | Answer in book | Trains | From |
|---|---|---|---|---|---|---|---|---|
| 1 | Easy | Ross *Fundamentos* 9e | Cap. 15 | Questão 3 | 537 (561) | no | Winner's curse: rationing of underpriced IPOs lowers the uninformed buyer's expected gain | R7 ex. 1 |
| 2 | Easy | Grinblatt & Titman | Ch. 19 | 19.4 | 687 (700) | no | Why investment depends on internal cash (pecking order) | R5 ex. 3 |
| 3 | Easy | Berk | Ch. 16 | 16.29 | 496 (527) | no | Lemons problem in an equity issue vs. debt with distress costs | R5 ex. 5 |
| 4 | Easy | Grinblatt & Titman 2e | Ch. 19 | 19.6 | 687 (700) | no | Dilution from issuing undervalued equity and the incentive to pass up a positive-NPV project | R7 ex. 5 |
| 5 | Easy | Ross | Cap. 17 | CQ 17.6 | 614 (638) | no | Reading a dividend suspension as a signal about cash flows | R5 ex. 1 |
| 6 | Exam | Tirole | Ch. 6 | 6.1 | 273 (286) | yes, p. 595 | Privately known private benefit, cross-subsidies and market breakdown | R5 ex. 6 |
| 7 | Exam | Amaro de Matos | Ch. 6 | 6.2.7 #4, #6 | 175 (193) | yes, p. 269 (#6; #4 refers to Rock 1986) | Rock's model: allocation probabilities $\pi \le \pi'$ and why $p_0$ falls as $\alpha$ rises | R7 ex. 6 |
| 8 | Exam | Tirole | Ch. 6 | 6.2 (with 6.1 as Part 0) | 274 (287) | yes, p. 596 | Adverse selection on private benefits: pooling, cross-subsidies and credit-market breakdown | R7 ex. 11 |
| 9 | Exam | Tirole | Ch. 6 | 6.6 | 276 (289) | yes, p. 598 | Adverse selection and the purchase of a costly rating (certification) | R5 ex. 9 |
| 10 | Exam | Tirole | Ch. 6 | 6.10 | 279 (292) | yes, p. 600 | Short maturity as a costless signal of a good type | R5 ex. 10 |
| 11 | Exam | Amaro de Matos | Ch. 3 | 3.2.6 #4 | 95 (113) | yes, p. 260 | Myers–Majluf issue rule under different managerial objectives | R5 ex. 7 |
| 12 | Really hard | Tirole | Ch. 6 | 6.8 | 278 (291) | yes, p. 599 | Separating program and pecking order with variable investment | R5 ex. 14 |
| 13 | Really hard | Tirole | Ch. 6 | 6.7 | 276–278 (289) | yes, p. 599 | Padilla–Pagano: banks' ex ante choice to share default data, informational rents vs. borrower investment in $\alpha$ | R7 ex. 19 |
| 14 | Really hard | Amaro de Matos | Ch. 3 | 3.2.6 #2 | 95 (113) | no (p. 260 only cites Leland and Pyle 1977, p. 377) | Leland–Pyle signalling with mean-variance utility: when debt rises with insider ownership $\alpha$ | R7 ex. 20 |
| 15 | Really hard | Tirole | Ch. 6 | 6.5 | 275 (288) | yes, p. 597 | Continuum of types: issue cutoff, negative price reaction, comparative statics | R5 ex. 13 |
| 16 | Easy | Original | Topic 3 slides 47–55 | — | — | no (solutions file) | Stiglitz–Weiss: mean-preserving spread, $r^*$ and $r_{max}$, non-monotone lender return, equity removes the selection | new |
| 17 | Exam | Original | Topic 3 slides 47–55 | — | — | no (solutions file) | Why a higher rate does not clear the loan market: excess demand at $r^*$, non-clearing rate, comparative statics, two-rate outcome | new |
| 18 | Exam | Original | Topic 3 slides 56–67; Tirole §6.3 | — | — | no (solutions file) | Collateral as a signal: symmetric benchmark $C = 0$, pooling, least-cost separating contract | new |
| 19 | Really hard | Original | Topic 3 slides 56–67; Tirole §6.3 | — | — | no (solutions file) | Separating vs. pooling threshold $\hat\alpha$, deadweight cost $(1-\delta)C$, comparative statics in $\delta$ and $q$, welfare | new |

## Tier 1 — Easy

### 1. Winner's curse in IPO allocations
**Source:** Ross, Cap. 15, Questão 3 (Questões e problemas, Básico), p. 537 (PDF 561) · Answer in book: no

3. Subpreço de IPO [OA3] A Madeira S/A e a Metal S/A anunciaram IPOs a \$40 por ação. Uma delas está subavaliada em \$7 e a outra está superavaliada em \$5, mas você não tem como saber qual é qual. Você pretende comprar 1.000 ações de cada emissão. Se uma emissão estiver subprecificada, ela será racionada e você receberá apenas metade do seu pedido. Se você pudesse obter 1.000 ações da Madeira e 1.000 ações da Metal, qual seria seu ganho? Qual ganho você realmente espera? Qual princípio você ilustrou?

---

### 2. Investment and available cash
**Source:** Grinblatt, Ch. 19, Exercise 19.4, p. 687 (PDF 700) · Answer in book: no

Classical finance theory suggests that firms take projects with positive NPVs regardless of the amount of cash the firm has available. However, empirical evidence suggests that the amount that firms invest is heavily dependent on their available cash flows. Why might this be?

---

### 3. Leverage, agency costs and information (IST)
**Source:** Berk, Ch. 16, Exercise 16.29 (starred), p. 496 (PDF 527) · Answer in book: no

Info Systems Technology (IST) manufactures microprocessor chips for use in appliances and other applications. IST has no debt and 100 million shares outstanding. The correct price for these shares is either \$14.50 or \$12.50 per share. Investors view both possibilities as equally likely, so the shares currently trade for \$13.50.

IST must raise \$500 million to build a new production facility. Because the firm would suffer a large loss of both customers and engineering talent in the event of financial distress, managers believe that if IST borrows the \$500 million, the present value of financial distress costs will exceed any tax benefits by \$20 million. At the same time, because investors believe that managers know the correct share price, IST faces a lemons problem if it attempts to raise the \$500 million by issuing equity.

a. Suppose that if IST issues equity, the share price will remain \$13.50. To maximize the long-term share price of the firm once its true value is known, would managers choose to issue equity or borrow the \$500 million if:
   i. They know the correct value of the shares is \$12.50?
   ii. They know the correct value of the shares is \$14.50?

b. Given your answer to part (a), what should investors conclude if IST issues equity? What will happen to the share price?

c. Given your answer to part (a), what should investors conclude if IST issues debt? What will happen to the share price in that case?

d. How would your answers change if there were no distress costs, but only the tax benefits of leverage?

---

### 4. Issuing undervalued equity
**Source:** Grinblatt, Ch. 19, Exercise 19.6, p. 687 (PDF 700) · Answer in book: no

ABC Industries is considering an investment that requires the firm to issue new equity. The project will cost \$100, but will add \$120 to the firm's value. Although management believes the firm's value is \$1,000 without the new project, outside investors value the firm at \$600 without the project. If the firm currently has 100 shares outstanding, how many new shares must it issue to finance the project? Now assume that the true value of the firm will become known to the market shortly after the new equity has been issued. What will the firm's stock price be at this time if it chooses to finance this new investment? What will the stock price be if it chooses to pass up the investment?

---

### 5. Dividend suspension and the stock price
**Source:** Ross, Cap. 17, Exercise CQ 17.6 (Revisão de conceitos e questões instigantes), p. 614 (PDF 638) · Answer in book: no

Mês passado, a Companhia de Energia Elétrica de Angra dos Reis, que vinha tendo problemas com custos acima dos previstos em uma usina nuclear em construção, anunciou que estava “suspendendo temporariamente os pagamentos devido à diminuição dos fluxos de caixa associados a esse programa de investimentos”. O preço da ação da empresa caiu de \$28,50 para \$25 quando esse anúncio foi feito. Como você interpretaria essa mudança no preço da ação (ou seja, em sua opinião, o que teria causado isso)?


## Tier 2 — Exam level

### 6. Privately known private benefit and market breakdown
**Source:** Tirole, Ch. 6, Exercise 6.1, p. 273 (PDF 286) · Answer in book: yes, p. 595

Section 6.2 illustrated the possibility of market breakdown without the possibility of signaling. This exercise supplies another illustration. Let us consider the fixed-investment model of Section 3.2 and assume that only the borrower knows the private benefit associated with misbehavior. When the borrower has private information about this parameter, lenders are concerned that this private benefit might be high and induce the borrower to misbehave. In the parlance of information economics, the “bad types” are the types of borrower with high private benefit. We study the case of two possible levels of private benefit (see Exercise 6.2 for an extension to a continuum of possible types). The borrower wants to finance a fixed-size project costing $I$, and, for simplicity, has no equity ($A = 0$). The project yields $R$ (success) or 0 (failure). The probability of success is $p_H$ or $p_L$, depending on whether the borrower works or shirks, with $\Delta p \equiv p_H - p_L > 0$. There is no private benefit when working. The private benefit $B$ enjoyed by the borrower when shirking is either $B_L > 0$ or $B_H > B_L$. The borrower will be labeled a “good borrower” when $B = B_L$ and a “bad borrower” when $B = B_H$. At the date of contracting, the borrower knows the level of her private benefit, while the capital market puts (common knowledge) probabilities $\alpha$ that the borrower is a good borrower and $1 - \alpha$ that she is a bad borrower. All other parameters are common knowledge between the borrower and the lenders.

To make things interesting, let us assume that under asymmetric information, the lenders are uncertain about whether the project should be funded:

$$p_H\left(R - \frac{B_H}{\Delta p}\right) < I < p_H\left(R - \frac{B_L}{\Delta p}\right). \qquad (1)$$

Assume that investors cannot break even if the borrower shirks:

$$p_L R < I. \qquad (2)$$

(i) Note that the investor cannot finance only good borrowers. Assume that the entrepreneur receives no reward in the case of failure (this is indeed optimal); consider the effect of rewards $R_b$ in the case of success that are (a) smaller than $B_L/\Delta p$, (b) larger than $B_H/\Delta p$, (c) between these two values.

(ii) Show that there exists $\alpha^*$, $0 < \alpha^* < 1$, such that

- no financing occurs if $\alpha < \alpha^*$,
- financing is an equilibrium if $\alpha \geqslant \alpha^*$.

(iii) Describe the “cross-subsidies” between types that occur when borrowing is feasible.

#### Context needed to solve it

*From Tirole §3.2.1–3.2.2 (the fixed-investment model), pp. 115–117 (PDF 128–130):*

**3.2.1 The Fixed-Investment Model.** Variants of the following entrepreneurial model will be used in the following: an entrepreneur (also called the “insider” or the “borrower,” “she”) has a project. This project requires a fixed investment $I$. The entrepreneur initially has “assets” (“cash on hand” or “net worth”) $A < I$. For the moment we interpret these assets as being cash or liquid securities that can be used toward covering the cost of investment. […] The entrepreneur’s cash can either be invested in the project or used for consumption. To implement the project the entrepreneur must borrow $I - A$ from lenders. […]

*Project.* If undertaken, the project either succeeds, that is, yields verifiable income $R > 0$, or fails, that is, yields no income. The probability of success is denoted by $p$. The project is subject to moral hazard. The entrepreneur can “behave” (“work,” “exert effort,” “take no private benefit”) or “misbehave” (“shirk,” “take a private benefit”); or, equivalently, the entrepreneur chooses between a project with a high probability of success and another project which ceteris paribus she prefers (is easier to implement, is more fun, has greater spinoffs in the future for the entrepreneur, benefits a friend, delivers perks, is more “glamorous,” etc.) but has a lower probability of success.

Behaving yields probability $p = p_H$ of success and no private benefit to the entrepreneur, and misbehaving results in probability $p = p_L < p_H$ of success and private benefit $B > 0$ (measured in units of account) to the entrepreneur. In the “effort interpretation,” $B$ can also be interpreted as a disutility of effort saved by the entrepreneur when shirking. Let $\Delta p \equiv p_H - p_L$.

*Preferences and the loan agreement.* Both the borrower and the potential lenders (or “investors”) are risk neutral. For notational simplicity, there is no time preference; the rate of return expected by investors (which is also the riskless rate, due to risk neutrality) is taken to be 0. The borrower is protected by limited liability, and so her income cannot take negative values.

Lenders behave competitively in the sense that the loan, if any, makes zero profit. That is, we have in mind that several prospective lenders compete for issuing a loan to the borrower, and that, if the most attractive loan offer made a positive profit, the borrower could turn to an alternative lender and offer to switch for a slightly lower interest rate. […]

Let us turn to the loan contract. A contract first stipulates whether the project is financed. If so, it further specifies how the profit is shared between the lenders and the borrower. The borrower’s limited liability will imply that both sides receive 0 in the case of failure (the gross payoffs are the *ex post* monetary payoffs and take no account of past investments and private benefit). Intuitively, there is no point in specifying a positive transfer from the lenders to the borrower, as such a transfer can only weaken incentives, while it has no insurance benefit under risk neutrality. This property will be proved more rigorously and is here taken for granted. In the case of success, the two parties share the profit $R$; $R_b$ goes to the borrower and $R_l$ to the lenders. To sum up, we posit an incentive scheme for the entrepreneur of the following form: $R_b$ in the case of success, 0 in the case of failure.

The zero-profit constraint for the lenders can be written as

$$p_H R_l = I - A,$$

assuming that the loan agreement induces the borrower to behave (which under our assumptions will be the case). […] We summarize the timing in Figure 3.1.

*Figure 3.1 (timeline, left to right):* Loan agreement (sharing rule) → Investment → Moral hazard → Outcome.

We assume that the project is viable only in the absence of moral hazard. That is, the project has positive NPV if the entrepreneur behaves,

$$p_H R - I > 0, \qquad (3.1)$$

but negative NPV, even if one includes the borrower’s private benefit, if she does not,

$$p_L R - I + B < 0. \qquad (3.2)$$

[…]

**3.2.2 The Lenders’ Credit Analysis.** Because the project has negative NPV in the case of misbehavior, the loan agreement must be careful to preserve enough of a stake for the borrower in the enterprise. The borrower faces the following tradeoff once the financing has been secured: by misbehaving, she obtains private benefit $B$, but she reduces the probability of success from $p_H$ to $p_L$. Because she has stake $R_b$ in the firm’s income (she receives $R_b$ in the case of success and 0 in the case of failure), the borrower will therefore behave if the following “incentive compatibility constraint” is satisfied:

$$p_H R_b \geqslant p_L R_b + B \quad \text{or} \quad (\Delta p) R_b \geqslant B. \qquad (\text{IC}_b)$$

From this incentive compatibility constraint we infer that the highest income in the case of success that can be pledged to the lenders without jeopardizing the borrower’s incentives is $R - \dfrac{B}{\Delta p}$. The *(expected) pledgeable income* is then $\mathcal{P} = p_H\left(R - \dfrac{B}{\Delta p}\right)$.

Because the lenders must break even in order to be willing to finance the project, a necessary condition for the borrower to receive a loan is that the expected pledgeable income exceed the lenders’ initial outlay:

$$\mathcal{P} \equiv p_H\left(R - \frac{B}{\Delta p}\right) \geqslant I - A, \qquad (\text{IR}_l)$$

where “IR$_l$” stands for the lenders’ individual rationality constraint (which we will also often call the “breakeven constraint” or the “participation constraint”). Thus a necessary condition for financing to be arranged is

$$A \geqslant \bar{A} = p_H \frac{B}{\Delta p} - (p_H R - I). \qquad (3.3)$$

[…] Conversely, if $A \geqslant \bar{A}$, the entrepreneur is able to secure financing, and so condition (3.3) is both a necessary and a sufficient condition for financing.

*From Tirole §6.2 (privately-known-prospects model) and §6.2.1.2 (Asymmetric Information), pp. 241–243 (PDF 254–256) — the market-breakdown illustration the statement refers to:*

*Privately-known-prospects model.* A borrower/entrepreneur has no funds ($A = 0$) to finance a project costing $I$. The project yields $R$ in the case of success and 0 in the case of failure. The borrower and the lenders are risk neutral, and the borrower is protected by limited liability. The interest rate in the economy is normalized at 0.

The borrower can be one of two types. A good borrower has a probability of success equal to $p$. A bad borrower has a probability of success $q$. Assume that $p > q$ and that $pR > I$ (at least the good type is creditworthy). There are two subcases, which we will treat separately: either $pR > I > qR$ (only the good type is creditworthy), or $pR > qR > I$ (both types are creditworthy).

The borrower has private information about her type. The capital market, which is competitive and demands an expected rate of return equal to 0, puts probabilities $\alpha$ and $1 - \alpha$ on the borrower being a good or a bad type, respectively. Under asymmetric information, the capital market does not know whether it faces a “$p$-borrower” (a good borrower) or a “$q$-borrower” (a bad borrower). Let

$$m \equiv \alpha p + (1 - \alpha) q$$

denote the investors’ prior probability of success. […]

**6.2.1.2 Asymmetric Information.** […] Let us assume that the only feasible financial contracts are contracts that give the borrower a compensation $R_b \geqslant 0$ in the case of success and 0 in the case of failure. (The validity of this assumption will be discussed in the remark below on the optimality of contracts.) Such contracts necessarily pool the two types of borrower as each prefers receiving financing to not being funded, and conditional on being funded, prefers contracts with a higher compensation. The investors’ profit for such a contract is therefore on average:

$$[\alpha p + (1 - \alpha) q](R - R_b) - I = m(R - R_b) - I.$$

*No lending: $mR < I$.* This case can arise only if the bad borrower is not creditworthy. It then arises whenever the probability that the borrower is a bad borrower is large enough, or $\alpha < \alpha^*$, where

$$\alpha^*(pR - I) + (1 - \alpha^*)(qR - I) = 0.$$

Because the borrower cannot receive a negative compensation ($R_b \geqslant 0$), investors lose money if they choose to finance the project. Accordingly they do not and the market breaks down.

The good borrower is therefore hurt by the suspicion that she might be a bad one. There is underinvestment.

*Lending: $mR \geqslant I$.* This case corresponds either to the situation in which both types are creditworthy or to that in which the bad borrower is not creditworthy but $\alpha \geqslant \alpha^*$. The borrower’s compensation $R_b$ is then set so that investors break even on average:

$$m(R - R_b) = I.$$

This implies that, ex post, investors make money on the good type ($p(R - R_b) > I$) and lose money on the bad type ($q(R - R_b) < I$): there is cross-subsidization.

---

### 7. Rock's winner's curse model
**Source:** Amaro de Matos, Ch. 6, Exercises 6.2.7 #4 and #6, p. 175 (PDF 193) · Answer in book: yes, p. 269 (#6 solved; #4 only refers to Rock 1986, p. 192)

**#4.** Show that the probability of an uninformed investor receiving an allocation of an underpriced issue ($\pi$) is less than or equal to the probability of receiving an allocation of an overpriced issue ($\pi'$).

**#6.** When there are informed and uninformed investors, it is said that as the proportion of informed investors ($\alpha$) rises, the offer price ($p_0$) must fall to maintain the equilibrium. Explain why.

#### Context needed to solve it

*From Amaro de Matos §6.2.2 "Asymmetry between Investors", p. 163 (PDF 181):*

> The uninformed investors do not have a criterion to decide if an IPO is underpriced or not, so they will go either for all of them or for none. The informed investors, on the other hand, will go only for the underpriced issues, since they can distinguish between the two types.

> Suppose that the cost of information is $c$ per investor, the price per share in the public offer is $p^\circ$, and the true value per share is a random variable $v$, to which is associated a density of probability $f(v)$. Let $n$ be the total number of shares offered, $N$ be the total number of informed investors, and $\alpha$ be the fraction of shares allocated to them.

(The book writes $p^\circ$ in §6.2.2 and $p_0$ in the exercises; they are the same offer price.)

*From Amaro de Matos §6.2.2, p. 164 (PDF 182), equations typeset from the book:*

> Clearly, if $p^\circ > v$, there will be only uninformed investors interested, whereas if $p^\circ < v$, both kinds of investors will appear.

Break-even of the uninformed, eq. (6.7):
$$\int_0^{p^\circ} n(p^\circ - v)f(v)\,dv = (1-\alpha)\int_{p^\circ}^{\infty} n(v - p^\circ)f(v)\,dv$$

Break-even of the informed, eq. (6.8):
$$Nc = \alpha\int_{p^\circ}^{\infty} n(v - p^\circ)f(v)\,dv$$

which together give (6.9): $E(v) - p^\circ = \dfrac{Nc}{n} > 0$.

> If the demand is great enough—or for low enough prices—there may be an oversubscription, in which case the underwriter rations the available shares.

*From Amaro de Matos §6.2.3, p. 166 (PDF 184):*

> […] and it follows as before that as the proportion of informed investors ($\alpha$) rises, the offer price $p^\circ$ must fall in order to maintain the equilibrium.

*Note on $\pi$, $\pi'$:* the book uses these symbols only in exercise #4 and does not define them anywhere in §6.2. They are Rock's (1986) notation, which is not in `Livros/`, and mean what the statement says: the probability that an uninformed investor's order is filled for an underpriced issue ($\pi$) and for an overpriced issue ($\pi'$).

---

### 8. Pooling in credit markets with a continuum of types
**Source:** Tirole, Ch. 6, Exercise 6.2, p. 274 (PDF 287) · Answer in book: yes, p. 596

**Exercise 6.2 (more on pooling in credit markets).** Consider the model of Exercise 6.1, in which the borrower has private information about her benefit of misbehaving, except that the borrower's type is drawn from a continuous distribution instead of a binary one. We will also assume that there is a monopoly lender, who makes a credit offer to the borrower. The borrower has no equity ($A = 0$).

Only the borrower knows the private benefit $B$ of misbehaving. The lender only knows that this private benefit is drawn from an *ex ante* cumulative distribution $H(B)$ on an interval $[0, \bar B]$ (so, $H(0) = 0$, $H(\bar B) = 1$). (Alternatively, one can imagine that lenders face a population of borrowers with characteristic $B$ distributed according to distribution $H$, and are unable to tell different types of borrower apart in their credit analysis.) The lender knows all other parameters. For a loan agreement specifying share $R_b$ for the borrower in the case of success, and 0 in the case of failure, show that the lender's expected profit is

$$U_l = H((\Delta p)R_b)\,p_H(R - R_b) + [1 - H((\Delta p)R_b)]\,p_L(R - R_b) - I.$$

Show that

- the proportion of "high-quality borrowers" (that is, of borrowers who behave) is endogenous and increases with $R_b$;⁷⁸
- adverse selection reduces the quality of lending (if lending occurs, which as we will see cannot be taken for granted);
- there is an externality among different types of borrower, in that the low-quality types ($B$ large) force the lender to charge an interest rate that generates strictly positive profit on high-quality types (those with small $B$);
- the credit market may "break down," that is, it may be the case that no credit is extended at all even though the borrower may be creditworthy (that is, have a low private benefit). To illustrate this, suppose that $p_L = 0$ and $H$ is uniform ($H(B) = B/\bar B$). Show that if

$$\frac{p_H^2}{\bar B}\,\frac{R^2}{4} < I$$

(which is the case for $\bar B$ large enough), no loan agreement can enable the lender to recoup on average his investment.

⁷⁸ In this model, the loan agreement attracts all types of borrowers if it attracts any type willing to behave. It is easy to find variants of the model in which this is not the case and an increase in $R_b$ attracts higher-quality borrowers, where "higher-quality" refers to an *ex ante* selection effect and not only to an *ex post* behavior like here.

#### Context needed to solve it

**Part 0.** *From Tirole, Ch. 6, Exercise 6.1, p. 273 (PDF 286):*

**Exercise 6.1 (privately known private benefit and market breakdown).** Section 6.2 illustrated the possibility of market breakdown without the possibility of signaling. This exercise supplies another illustration. Let us consider the fixed-investment model of Section 3.2 and assume that *only the borrower knows the private benefit associated with misbehavior*. When the borrower has private information about this parameter, lenders are concerned that this private benefit might be high and induce the borrower to misbehave. In the parlance of information economics, the "bad types" are the types of borrower with high private benefit. We study the case of two possible levels of private benefit (see Exercise 6.2 for an extension to a continuum of possible types). The borrower wants to finance a fixed-size project costing $I$, and, for simplicity, has no equity ($A = 0$). The project yields $R$ (success) or 0 (failure). The probability of success is $p_H$ or $p_L$, depending on whether the borrower works or shirks, with $\Delta p \equiv p_H - p_L > 0$. There is no private benefit when working. The private benefit $B$ enjoyed by the borrower when shirking is either $B_L > 0$ or $B_H > B_L$. The borrower will be labeled a "good borrower" when $B = B_L$ and a "bad borrower" when $B = B_H$. At the date of contracting, the borrower knows the level of her private benefit, while the capital market puts (common knowledge) probabilities $\alpha$ that the borrower is a good borrower and $1 - \alpha$ that she is a bad borrower. All other parameters are common knowledge between the borrower and the lenders.

To make things interesting, let us assume that under asymmetric information, the lenders are uncertain about whether the project should be funded:

$$p_H\left(R - \frac{B_H}{\Delta p}\right) < I < p_H\left(R - \frac{B_L}{\Delta p}\right). \qquad (1)$$

Assume that investors cannot break even if the borrower shirks:

$$p_L R < I. \qquad (2)$$

(i) Note that the investor cannot finance only good borrowers. Assume that the entrepreneur receives no reward in the case of failure (this is indeed optimal); consider the effect of rewards $R_b$ in the case of success that are (a) smaller than $B_L/\Delta p$, (b) larger than $B_H/\Delta p$, (c) between these two values.

(ii) Show that there exists $\alpha^*$, $0 < \alpha^* < 1$, such that

- no financing occurs if $\alpha < \alpha^*$,
- financing is an equilibrium if $\alpha \geqslant \alpha^*$.

(iii) Describe the "cross-subsidies" between types that occur when borrowing is feasible.

*From Tirole §3.2.1 "The Fixed-Investment Model", pp. 115–116 (PDF 128–129):*

*Preferences and the loan agreement.* Both the borrower and the potential lenders (or "investors") are risk neutral. For notational simplicity, there is no time preference; the rate of return expected by investors (which is also the riskless rate, due to risk neutrality) is taken to be 0. The borrower is protected by limited liability, and so her income cannot take negative values.

[…] Let us turn to the loan contract. A contract first stipulates whether the project is financed. If so, it further specifies how the profit is shared between the lenders and the borrower. The borrower's limited liability will imply that both sides receive 0 in the case of failure […]. In the case of success, the two parties share the profit $R$; $R_b$ goes to the borrower and $R_l$ to the lenders. To sum up, we posit an incentive scheme for the entrepreneur of the following form: $R_b$ in the case of success, 0 in the case of failure.

*From Tirole §3.2.2 "The Lenders' Credit Analysis", p. 116 (PDF 129):*

[…] Because she has stake $R_b$ in the firm's income (she receives $R_b$ in the case of success and 0 in the case of failure), the borrower will therefore behave if the following "incentive compatibility constraint" is satisfied:

$$p_H R_b \geqslant p_L R_b + B \quad \text{or} \quad (\Delta p) R_b \geqslant B. \qquad (\text{IC}_b)$$

---

### 9. Adverse selection and ratings
**Source:** Tirole, Ch. 6, Exercise 6.6, p. 276 (PDF 289) · Answer in book: yes, p. 598

A borrower has assets *A* and must find financing for a fixed investment *I* > *A*. As usual, the project yields $R$ (success) or 0 (failure). The borrower is protected by limited liability. The probability of success is $p_H$ or $p_L$, depending on whether the borrower works or shirks, with $\Delta p \equiv p_H - p_L > 0$. There is no private benefit when working. The private benefit enjoyed by the borrower when shirking is either $b$ (with probability $\alpha$) or $B$ (with probability $1 - \alpha$). At the date of contracting, the borrower knows her private benefit, but the market (which is risk neutral and charges a 0 average rate of interest) does not know it. Assume that $p_L R + B < I$ (the project is always inefficient if the borrower shirks) and that

$$p_H\left(R - \frac{B}{\Delta p}\right) < I - A < p_H\left(R - \frac{b}{\Delta p}\right) \qquad (1)$$

and

$$[\alpha p_H + (1 - \alpha)p_L]\left[R - \frac{b}{\Delta p}\right] < I - A. \qquad (2)$$

(i) Interpret conditions (1) and (2) and show that there is no lending in equilibrium.

(ii) Suppose now that the borrower can at cost $r(x) = rx$ (which is paid from the cash endowment $A$) purchase a signal with quality $x \in [0, 1]$. (This quality can be interpreted as the reputation or the number of rating agencies that the borrower contracts with.) With probability $x$, the signal reveals the borrower’s type ($b$ or $B$) perfectly; with probability $1 - x$, the signal reveals nothing. The financial market observes both the quality $x$ of the signal chosen by the borrower and the outcome of the signal (full or no information). The borrower then offers a contract that gives the borrower $R_b$ and the lenders $R - R_b$ in the case of success (so, a contract is the choice of an $R_b \in [0, R]$). The timing is summarized in Figure 6.5.

*Figure 6.5*

| Step 1 | Step 2 | Step 3 |
|---|---|---|
| Borrower chooses quality of signal $x$ (this quality is observed by the capital market). | Borrower’s type revealed with probability $x$. Nothing revealed with probability $1 - x$. | Borrower goes to the capital market. |

Look for a pure strategy, *separating* equilibrium, that is, an equilibrium in which the two types pick different signal qualities.⁷⁹

- Argue that the bad borrower (borrower $B$) does not purchase a signal in a separating equilibrium.
- Argue that the good borrower (borrower $b$) borrows under the same conditions regardless of the signal’s realization, in a separating equilibrium.
- Show that the good borrower chooses signal quality $x \in (0, 1)$ given by
  $$A = x(A - rx) + (1 - x)\left[p_L\left(R - \frac{I - A + rx}{p_H}\right) + B\right].$$
- Show that this separating equilibrium exists only if $r$ is “not too large.”

> 79. One will assume that if the signal reveals the borrower’s type, the investors put probability 1 on this type, even when they put weight 0 on the corresponding type after observing the quality of the signal.

---

### 10. Maturity structure
**Source:** Tirole, Ch. 6, Exercise 6.10, p. 279 (PDF 292) · Answer in book: yes, p. 600

At date 0 the entrepreneur has cash on hand *A* and needs to finance an investment of fixed size $I$. At date 1, a deterministic income $r$ accrues; a liquidity shock must be met in order for the firm to continue. Liquidation yields nothing. The probability of success in the case of continuation depends on a date-1 effort: for a good borrower, this probability is $p_H$ or $p_L$ depending on whether she behaves (no private benefit) or misbehaves (private benefit $B$); similarly, for a bad borrower, it is $q_H$ or $q_L$. We assume that

$$p_H - p_L = q_H - q_L = \Delta p,$$

and so the incentive compatibility constraint in the case of continuation is the same for both types of borrower:

$$(p_H - p_L)R_b = (q_H - q_L)R_b = (\Delta p)R_b \geqslant B,$$

where $R_b$ is the borrower’s reward in the case of success.

The borrower knows at the date of contracting whether she is a “$p$-type” or a “$q$-type.” Let

$$\rho_0^G \equiv p_H\left(R - \frac{B}{\Delta p}\right) \quad \text{and} \quad \rho_0^B = q_H\left(R - \frac{B}{\Delta p}\right)$$

denote the date-1 pledgeable incomes for the good and bad types.

The liquidity shock is deterministic and equal to $\rho$. Information is asymmetric at date 0, but the capital market learns the borrower’s type perfectly at date 1, before the liquidity shock has to be met. Assume that

$$\rho_0^G > \rho > \rho_0^B.$$

Suppose further that under symmetric information only the good borrower is creditworthy (provided that she is incentivized to behave).

Assume that $r < I - A < r + [\rho_0^G - \rho]$. Show that the good borrower can costlessly signal her type.

#### Context needed to solve it

*From Tirole §6.3, Application 6 "Short-Term Maturities", pp. 254–255 (PDF 267–268) — the model of which the exercise is a variant (there the liquidity shock is random; in the exercise it is deterministic and the asymmetry is about the success probabilities). It defines $R$ and the preferences the statement leaves implicit:*

Let us consider the following variant of the model of debt maturities set up in Section 5.2. At date 0 the entrepreneur has a project of fixed size $I$, has wealth $A$, and must borrow $I - A$. At date 1, the investment yields a deterministic and verifiable short-term (date-1) profit $r > 0$. With probability $\lambda$, continuation requires reinvesting $\rho$ (the liquidation value is equal to 0); with probability $1 - \lambda$, continuation requires no reinvestment.⁵¹

In the case of continuation, the firm at date 2 yields $R$ in the case of success and 0 in the case of failure. The probability of success is $p_H$ in the case of good behavior and $p_L = p_H - \Delta p$ in the case of misbehavior (which yields private benefit $B$). Moral hazard is introduced in order to create an entrepreneurial rent from continuation, or, equivalently, a cost for the entrepreneur associated with early termination. Put differently, moral hazard introduces a friction in the date-1 refinancing market. Let

$$\rho_1 \equiv p_H R \quad \text{and} \quad \rho_0 \equiv p_H\left(R - \frac{B}{\Delta p}\right)$$

denote the continuation NPV and pledgeable income, respectively.

[…] the borrower can use retentions $(r - d)$ together with what can be raised in the capital market $(\rho_0)$ to meet shock $\rho$.

> 51. As usual, the entrepreneur is risk neutral and protected by limited liability; and the investors are risk neutral and demand a 0 rate of return.

*Figure 6.1 (timeline, left to right):* Date 0: Entrepreneur has wealth $A$ and fixed-size investment project $I - A$. → Date 1: Short-run income $r$. Reinvestment need $\rho$ (prob. $\lambda$) or 0 (prob. $1 - \lambda$). → (if reinvestment) Moral hazard ($p = p_H$ or $p_L$). → Outcome: success ($R$) or failure (0).

---

### 11. Myers–Majluf: whose interest does management serve?
**Source:** Amaro de Matos, Ch. 3, Exercise 3.2.6 #4, p. 95 (PDF 113) · Answer in book: yes, p. 260

Instead of Assumption 3.2.6, assume that the management acts in the interest of all shareholders. How would that affect the investment decision of the management? If management acts in the interest of the new shareholders, what is the optimal equity issuance rule?

#### Context needed to solve it

*From Amaro de Matos §3.2, p. 78 (PDF 96):*

**Assumption 3.2.1.** *Managers have better information about the value of the firm than other agents in the economy.*

*From Amaro de Matos §3.2.3 (Signals Conditioned by Investment Opportunities), pp. 86–88 (PDF 104–106):*

To see how all these conclusions are derived, the model must be formalized. Let $I$ be the required investment and $S$ denote the *slack* of the firm (i.e., large holdings of cash or marketable securities) or the ability to issue default-risk-free debt.

If $S \geq I$, it will not be necessary to issue any equity at all in order to finance the investment. The only interesting case happens when $S < I$, where the required amount of equity to be issued is $E = I - S$.

As opposed to the other models previously discussed, this is a three-date model with three distinct times—say, time 0, time 1, and time 2. Let us introduce the following notation. At time 0, the possible value of the assets of the firm at time 1 is described by a random variable $\widetilde{A}$. Similarly, let $\widetilde{B}$ denote the possible net present value of the investment opportunity at time 1.

At time 0, the information is symmetric. All the agents, managers and market, have the same information—namely, the distributions of $\widetilde{A}$ and $\widetilde{B}$ and the value of $S$.

At time 1, the asymmetry of information between managers and outsider investors is specified. Assumption 3.2.1 takes the form

**Assumption 3.2.5.** *At time 1, the management knows the realizations of $\widetilde{A}$ and $\widetilde{B}$, denoted respectively by $a$ and $b$, which are unknown to the outsider investors. Negative values of $a$ and $b$ are ruled out.*

At this stage, the only thing that the outsiders know is that the amount of equity to be issued is $E = \max[0, I - S]$. Also, at time 1, let $P$ be the market value of the shares of old shareholders if the stock is not issued and $P'$ be the price of the same shares if it is issued. At time 2, finally, all the information is disclosed.

Let $V^\circ$ be the value of the firm for the old shareholders. If the management, knowing the values of $a$ and $b$, decides not to issue equity, then the company is still owned by the same old shareholders with assets of value $a$ and slack $S$. Thus

$$V^\circ = a + S.$$

If, on the other hand, knowing the value of $a$ and $b$, the management decides to issue equity $E$, then the ownership of the company is shared between the old and new shareholders. The total value of the company will include the issued equity $E$ and the net present value of the investment opportunity apart from the assets of value $a$ and slack $S$. But the old shareholders will have only a proportion $P'/(P' + E)$ of all of this. Thus, in this case

$$V^\circ = \frac{P'}{P' + E}(E + S + a + b).$$

To explain the decision of the managers, the following assumption is required:

**Assumption 3.2.6.** *The management acts in the best interest of the old shareholders. Moreover, old shareholders are assumed to be passive—that is, they do not adjust their portfolios in response to the issue–invest decision of the firm.*

If that is so, the decision to issue new equity is taken only if the old shareholders are better off in such case—that is, only if

$$\frac{P'}{P' + E}(E + S + a + b) \geq a + S.$$

This inequality may be rewritten as

$$b \geq -E + \frac{E}{P'}(S + a) \qquad (3.20)$$

and should naturally be restricted by Assumption 3.2.5 to the region $a \geq 0$, $b \geq 0$.

Hence, inequality (3.20) divides the domain of the joint probability distribution of $\widetilde{A}$ and $\widetilde{B}$ into two disjoint regions identified in Figure 3.1: a region $M'$ in which all pairs $(a, b)$ satisfy the inequality and the firm issues new equity and invests in the new project, and a region $M$ in which no pair $(a, b)$ satisfies the inequality and there is no investment. In the first region, the amount of equity issued is $E = I - S$, whereas in the second, it is zero.

*Figure 3.1 (The Regions of Investment and No-Investment Decisions According to Myers and Majluf’s Model):* horizontal axis $a$, vertical axis $b$, both starting at 0. An upward-sloping straight line labelled $b = -E + \frac{E}{P'}(S + a)$ starts on the horizontal axis at a positive value of $a$ (where $b = 0$). The area above/left of the line is labelled “region $M'$”; the area below/right of the line is labelled “region $M$”.

It is simple to see that the price $P$ for the shares when $(a, b) \in M$ is greater than the price $P'$ when $(a, b) \in M'$. The equilibrium prices should be given by

$$P = S + E(\widetilde{A} \mid M) \qquad (3.21)$$

and

$$P' = S + E(\widetilde{A} + \widetilde{B} \mid M').$$

For any $(a, b) \in M$, the inequality (3.20) is not satisfied and hence

$$b < -E + \frac{E}{P'}(S + a) \quad \text{or} \quad a > P'(1 + b/E) - S.$$

Since $b/E \geq 0$ from Assumption 3.2.5, it follows that for any $(a, b) \in M$, $a > P' - S$. Thus $E(\widetilde{A} \mid M) > P' - S$ and (3.21) gives directly $P > P'$.


## Tier 3 — Really hard

### 12. Pecking order with variable investment
**Source:** Tirole, Ch. 6, Exercise 6.8, p. 278 (PDF 291) · Answer in book: yes, p. 599

Consider the privately-known-prospects model with risk neutrality and variable investment. For investment $I$, the realized income is either $R^S I$ (in the case of success) or $R^F I$ (in the case of failure), where $R^S > R^F \geqslant 0$. A good borrower has probability $p_H$ of success when working and $p_L$ when shirking; similarly, a bad borrower has probability $q_H$ of success when working and $q_L$ when shirking, where $p_H - p_L = \Delta p = q_H - q_L$, for simplicity. The entrepreneur’s private benefit is 0 when working and $BI$ when shirking. The entrepreneur is risk neutral and protected by limited liability; the investors are risk neutral and demand a rate of return equal to 0.

(i) Let $\tilde{U}_b^{SI}$ denote the bad borrower’s gross utility under symmetric information.⁸⁰ Consider the problem of maximizing the good borrower’s utility subject to the investors’ breaking even on that borrower, to the mimicking constraint that the good borrower’s terms not be preferred by the bad borrower to her symmetric-information terms, and to the no-shirking constraint. Let $\{R_b^S, R_b^F\}$ denote the (nonnegative) rewards of the good borrower in the cases of success and failure. Write the separating program.

(ii) Show that $R_b^F = 0$.

(iii) (Only if you have read the supplementary section.) Show that the separating outcome is the only perfect Bayesian equilibrium of the issuance game if and only if $\alpha \leqslant \alpha^*$ for some threshold $\alpha^*$.

> 80. This utility was derived in Section 3.4.2. It is equal to
> $$\left[1 + \frac{q_H R - 1}{1 - q_H(R - B/\Delta p)}\right]A$$
> if $q_H R \geqslant 1$, and to $A$ otherwise.

#### Context needed to solve it

*From Tirole §6.2 (privately-known-prospects model), p. 241 (PDF 254):*

*Privately-known-prospects model.* A borrower/entrepreneur has no funds ($A = 0$) to finance a project costing $I$. The project yields $R$ in the case of success and 0 in the case of failure. The borrower and the lenders are risk neutral, and the borrower is protected by limited liability. The interest rate in the economy is normalized at 0.

The borrower can be one of two types. A good borrower has a probability of success equal to $p$. A bad borrower has a probability of success $q$. […]

The borrower has private information about her type. The capital market, which is competitive and demands an expected rate of return equal to 0, puts probabilities $\alpha$ and $1 - \alpha$ on the borrower being a good or a bad type, respectively. Under asymmetric information, the capital market does not know whether it faces a “$p$-borrower” (a good borrower) or a “$q$-borrower” (a bad borrower). […]

*From Tirole §3.4.1–3.4.2 (the continuous-investment model, where footnote 80’s formula is derived), pp. 127–128 (PDF 140–141):*

**3.4.1 The Continuous-Investment Model.** The continuous-investment model of this section is the polar opposite of the fixed-investment one. The fixed-investment model depicts a situation in which returns are sharply decreasing beyond some investment level. In contrast, we now assume that there are constant returns to scale in the investment technology. An investment $I \in [0, \infty)$ yields income $RI$, proportional to $I$, in the case of success, and 0 in the case of failure. The borrower’s private benefit from misbehaving is also taken to be proportional to investment. As before, the borrower has a choice between behaving, in which case she derives no private benefit and the probability of success is $p_H$, and misbehaving, that is, enjoying private benefit $BI$, and reducing the probability of success to $p_L = p_H - \Delta p < p_H$. […]

The borrower initially has cash $A$, and must therefore borrow $I - A$ to finance a project of size $I$. A loan agreement specifies that the lenders (who as before are assumed to make no profit) and the borrower receive 0 each in the case of failure, and $R_l$ and $R_b$, respectively, in the case of success, where $R_l + R_b = RI$.

As in Section 3.2, we assume that investment has positive NPV (net present value), here per unit of investment, if the borrower behaves,

$$p_H R > 1, \qquad (3.7)$$

but negative NPV otherwise,

$$1 > p_L R + B, \qquad (3.8)$$

so that unless one can control the agency problem the investment cannot be funded. We also make an assumption that guarantees that the equilibrium investment is finite:

$$p_H R < 1 + \frac{p_H B}{\Delta p}. \qquad (3.9)$$

[…] Finally, we keep assuming that the capital market is competitive. […]

**3.4.2 The Lenders’ Credit Analysis.** Following the steps of Section 3.2, the incentive compatibility and the breakeven conditions are

$$(\Delta p) R_b \geqslant BI \qquad (\text{IC}_b)$$

and

$$p_H(RI - R_b) \geqslant I - A. \qquad (\text{IR}_l)$$

In equilibrium, competitive lenders make no profit on the contract that is most advantageous for the borrower; the borrower’s net utility is therefore equal to the social surplus brought about by the investment:

$$U_b = (p_H R - 1)I. \qquad (3.10)$$

From (3.10) it is optimal for the borrower to invest as much as possible. The upper bound on investment and in turn her borrowing capacity (“outside financing capacity” or “debt capacity”) are determined by constraints (IC$_b$) and (IR$_l$). Substituting (IC$_b$) into (IR$_l$), we obtain

$$I \leqslant kA, \qquad (3.11)$$

where

$$k = \frac{1}{1 - p_H(R - B/\Delta p)} > 1. \qquad (3.12)$$

[…] Another important concept […] is the shadow value $v$ of equity (here cash). The entrepreneur derives gross utility $v > 1$ from one more unit of equity. Letting $U_b^g \equiv A + U_b$ denote the borrower’s gross utility, and using (3.10) and (3.11), we have

$$U_b^g \equiv vA, \qquad (3.14)$$

where the shadow value of equity is

$$v = \frac{p_H B/\Delta p}{1 - p_H(R - B/\Delta p)} > 1. \qquad (3.15)$$

*From Tirole, Supplementary Section §6.4 (Contract Design by an Informed Party: An Introduction), pp. 264–268 (PDF 277–281) — the “issuance game,” the separating program and the uniqueness threshold $\alpha^*$ used in part (iii):*

A borrower who attempts to raise funds from lenders has private information about some characteristic (private benefit, value of assets in place, prospects of the firm, value of collateral) that affects the lenders’ payoff. The borrower may have type $b$ or $\tilde{b}$. While the borrower knows her type, the lenders only know that this type is $b$ with probability $\alpha$ and $\tilde{b}$ with probability $1 - \alpha$.

*Figure 6.4 (timeline, left to right):* Borrower offers a contract → Investors accept/refuse → Borrower picks action(s).

Let us, abstractly, denote the contractual terms faced by the borrower by $c$. Let $U_b(c)$ and $\tilde{U}_b(c)$ denote the two types’ net utilities for arbitrary contractual terms $c$.⁶⁸ Let $U_l(c)$ and $\tilde{U}_l(c)$ denote the investors’ expected profit when contractual terms are $c$ and the borrower turns out to have type $b$ and $\tilde{b}$, respectively.

*Example (privately-known-prospects).* In Section 6.2, the borrower had possible types $b = p$ and $\tilde{b} = q$. The contractual terms $c$ were just the borrower’s reward $R_b^S$ in the case of success. More generally, they also contain the probability of investment, $x$, her reward in the case of failure, $R_b^F$, and in the absence of investment, $R_b^0$, even though the latter in equilibrium can be taken to be equal to 1, 0, and 0, respectively (see Section 6.5). We have

$$U_b(c) = x[pR_b^S + (1 - p)R_b^F] + (1 - x)R_b^0,$$
$$\tilde{U}_b(c) = x[qR_b^S + (1 - q)R_b^F] + (1 - x)R_b^0,$$
$$U_l(c) = x[p(R - R_b^S) - (1 - p)R_b^F] - (1 - x)R_b^0,$$
$$\tilde{U}_l(c) = x[q(R - R_b^S) - (1 - q)R_b^F] - (1 - x)R_b^0.$$

[…] Figure 6.4 describes the timing of the *issuance game*. As earlier, we assume that the borrower designs the issue and offers the associated claims to a competitive capital market. Investors purchase the claims if and only if they expect a nonnegative profit. Lastly, the borrower chooses some action(s).

A few clarifications are in order. First, we allow for post-contracting actions by the borrower in order to accommodate situations in which the borrower can waste resources (as in Chapters 3–5). Second, we said that investors subscribe “if and only if they expect a nonnegative profit.” The expectation should be taken relative to the updated beliefs, that is, the investors’ beliefs after they observe the contract offer and thus possibly learn something about the borrower. Third, we will analyze the perfect Bayesian equilibrium (or equilibria) of the issuance game.⁷⁰ Fourth, a “contract” can in principle be anything that the borrower sees fit to design. However, for the purpose of the analysis, it can be shown that there is no loss of generality in assuming that the borrower offers an “option contract” $(c, \tilde{c})$, that is, as many contractual terms as there are possible types. […] It can further be shown that there is no loss of generality in assuming that the option contract is “incentive compatible,” that is, that type $b$ prefers contractual terms $c$ to $\tilde{c}$ and type $\tilde{b}$ prefers $\tilde{c}$ to $c$ […].

[…] Let an *allocation* be a pair of (possibly identical) type-contingent contractual terms $(c, \tilde{c})$. That is, it defines contractual terms $c$ for type $b$ and $\tilde{c}$ for type $\tilde{b}$. (Note that an option contract defines an allocation.)

*Definition.* An allocation $(c, \tilde{c})$ is *incentive compatible* if type $b$ prefers $c$ to $\tilde{c}$ and type $\tilde{b}$ prefers $\tilde{c}$ to $c$:

$$U_b(c) \geqslant U_b(\tilde{c}) \quad \text{and} \quad \tilde{U}_b(\tilde{c}) \geqslant \tilde{U}_b(c).$$

[…]

*Definition.* An incentive-compatible allocation $(c, \tilde{c})$ is *profitable type-by-type* if

$$U_l(c) \geqslant 0 \quad \text{and} \quad \tilde{U}_l(\tilde{c}) \geqslant 0.$$

*Definition.* An incentive-compatible allocation $(c, \tilde{c})$ is *profitable in expectation* (relative to the prior beliefs) if

$$\alpha U_l(c) + (1 - \alpha)\tilde{U}_l(\tilde{c}) \geqslant 0.$$

An incentive-compatible allocation $(c, \tilde{c})$ that is profitable in expectation is *interim efficient* if it is Pareto-optimal for the two types of borrower in the set of incentive-compatible, profitable-in-expectation allocations.

[…] *Definition.* Utility $U_b(c_0)$ for borrower type $b$ is the *low-information-intensity optimum* for that type if $c_0$ maximizes type $b$’s utility in the set of incentive-compatible, profitable-type-by-type allocations. That is, it is (part of) the solution to the following program.

*Program I (type $b$):*

$$\max_{\{c, \tilde{c}\}} U_b(c) \quad \text{s.t.} \quad U_b(c) \geqslant U_b(\tilde{c}), \quad \tilde{U}_b(\tilde{c}) \geqslant \tilde{U}_b(c), \quad U_l(c) \geqslant 0, \quad \tilde{U}_l(\tilde{c}) \geqslant 0.$$

The low-information-intensity optimum $\tilde{c}_0$ for type $\tilde{b}$ is defined similarly (Program I (type $\tilde{b}$)).

The payoff pair $(U_b(c_0), U_b(\tilde{c}_0))$ is called the *low-information-intensity optimum*. (By abuse of terminology, we will sometimes call the allocation $(c_0, \tilde{c}_0)$ itself the low-information-intensity optimum.) […]

**Lemma 6.1.** *The borrower can guarantee herself her low-information-intensity optimum ($U_b(c_0)$ if she has type $b$, and $\tilde{U}_b(\tilde{c}_0)$ if she has type $\tilde{b}$).*

[…]

**Proposition 6.1.**

(a) *The issuance game has a unique perfect Bayesian equilibrium if the low-information-intensity optimum is interim efficient (relative to prior beliefs $(\alpha, 1 - \alpha)$). The borrower then obtains her low-information-intensity optimum ($U_b(c_0)$ for type $b$, $\tilde{U}_b(\tilde{c}_0)$ for type $\tilde{b}$).*

(b) *If the low-information-intensity optimum is not interim efficient, then the set of equilibrium payoffs for the two types of borrowers is the set of payoffs that result from an incentive-compatible, profitable-in-expectation allocation and (weakly) Pareto-dominate the low-information-intensity optimum.*

[…] Let $\tilde{c}^{SI}$ denote the *symmetric information* contractual terms for the bad borrower. It solves

$$\max_{\{\tilde{c}\}} \tilde{U}_b(\tilde{c}) \quad \text{s.t.} \quad \tilde{U}_l(\tilde{c}) \geqslant 0.$$

**Assumption 6.4 (weak monotonic profit).** *Investors make a nonnegative profit if the contractual terms are those of the bad borrower under symmetric information and the borrower is a good one:*

$$U_l(\tilde{c}^{SI}) \geqslant 0.$$

This assumption is in general satisfied when both types are creditworthy under symmetric information (and it is satisfied in all of our illustrations). It is always satisfied when the bad borrower is not creditworthy under symmetric information: in that case, $\tilde{c}^{SI}$ is the absence of funding and thus $U_l(\tilde{c}^{SI}) = 0$.

*Definition.* The *separating allocation* is the allocation $c^*$ for the good borrower and the symmetric-information contractual terms $\tilde{c}^{SI}$ for the bad borrower, where $c^*$ maximizes the good borrower’s payoff subject to the investors breaking even for the good borrower and to the bad borrower not preferring $c^*$ to $\tilde{c}^{SI}$:

$$\max_{\{c\}} U_b(c) \quad \text{s.t.} \quad U_l(c) \geqslant 0, \quad \tilde{U}_b(c) \leqslant \tilde{U}_b(\tilde{c}^{SI}).$$

Note that the separating allocation is profitable type-by-type.

**Lemma 6.2.** *Under the weak monotonic-profit assumption, the separating allocation is the low-information-intensity optimum.*

*Proof.* First, note that the bad borrower’s symmetric-information program has the same objective function and fewer constraints than her low-information-intensity optimum program, Program I (type $\tilde{b}$). Hence,

$$\tilde{U}_b^{SI} \equiv \tilde{U}_b(\tilde{c}^{SI}) \geqslant \tilde{U}_b(\tilde{c}_0).$$

[…]

**Lemma 6.3.** *Under the weak monotonic-profit assumption, there exists a threshold level $\alpha^*$ for prior beliefs such that the low-information-intensity optimum (that is, the separating allocation under the weak monotonic-profit assumption) is interim efficient if and only if $\alpha \leqslant \alpha^*$.*

> 68. So, for example, if the borrower has initial cash $A$, and has quasi-linear preferences, the net utility is equal to the gross utility minus $A$.
>
> 70. Very roughly speaking, a perfect Bayesian equilibrium of a game is a set of strategies and beliefs such that at any stage of the game players act optimally given their beliefs at that stage (the equilibrium is “perfect”) and beliefs are updated by the players according to Bayes’ rule using equilibrium strategies and observed actions (the updating is Bayesian). […] Here investors are assumed to update their beliefs about the borrower’s type using the borrower’s equilibrium type-contingent contract offer and the actual contract offer. The previous condition, that they subscribe if and only if they expect a nonnegative profit given their updated beliefs, is an optimization requirement.

---

### 13. Information sharing among lenders
**Source:** Tirole, Ch. 6, Exercise 6.7, pp. 276–278 (PDF 289) · Answer in book: yes, p. 599

**Exercise 6.7 (endogenous communication among lenders).** Padilla and Pagano (1997) and others have observed that information sharing about creditworthiness is widespread among lenders (banks, suppliers, etc.). For example, Dun & Bradstreet Information Services, one of the leading rating agencies, collects information from thousands of banks. Similarly, over 600,000 suppliers communicate information about delays and defaults by their customers; and credit bureaux centralize information about the consumer credit markets.

Padilla and Pagano (see also Pagano and Jappelli (1993) and the references therein) argue that information sharing has both costs and benefits for the banks. By sharing information, they reduce their differentiation and compete more with each other. But this competition protects their borrowers' investment and therefore enhances opportunities for lending. In a sense, the "tax rate" (the markup that banks can charge borrowers) decreases but the "tax base" (the creditworthiness of borrowers) expands. This exercise builds on the Padilla–Pagano model.

There are two periods ($t = 1, 2$). The discount factor between the two periods is $\delta$. A risk-neutral borrower protected by limited liability has no cash on hand ($A = 0$). Each period, the borrower has a project with investment cost $I$. The project delivers at the end of the period $R$ or 0. There is no moral hazard. The probability of success is $p$ if the entrepreneur is talented (which has probability $\alpha$), and $q$ if she is not (which has probability $1 - \alpha$). We will assume that the market rate of interest in the economy is 0, that the lenders are risk neutral, and that only the good type is creditworthy:

$$pR > I > qR.$$

The date-1 and date-2 projects (if financed) are correlated and yield the same profit (they both succeed or both fail).

There are $n$ towns. Each town has one bank and one borrower. The "local bank" has local expertise and thereby learns the local borrower's type; the other banks, the "foreign banks," learn nothing (and therefore have beliefs $\alpha$ that the entrepreneur is talented) at date 1. At date 2, the foreign banks learn

- only whether the borrower was financed at date 1, if there is no information sharing among banks;
- whether the borrower was financed at date 1 and whether she repaid (i.e., whether she was successful), if there is information sharing about riskiness.

In other words, information sharing is feasible on hard data (repayments), but not on soft data (assessment of ability).

Padilla and Pagano add two twists to the model. First, banks decide *ex ante* whether they will communicate information about default and they make this decision public. Second, the borrower's type may be endogenous (in which it refers more to an investment in the projects or industry than in "pure talent"): at increasing and convex cost $C(\alpha)$ $\{C' > 0$, $C'' > 0$, $C(0) = 0$, $C'(0) = 0$, $C'(1) = \infty\}$, the borrower develops a $p$ project with probability $\alpha$ and a $q$ project with probability $1 - \alpha$. $C$ can be viewed as an investment cost and represents a nonmonetary cost borne by the borrower.

Contracts between banks and borrowers are *short-term* contracts. These contracts just specify a payment $R_b$ for the borrower in the case of success during the period (and 0 in the case of failure). Furthermore, in each period, banks simultaneously make take-it-or-leave-it offers to borrowers. And at date 2, the incumbent bank (the bank that has lent at date 1) makes its offer after the other banks.

The timing is summarized in Figure 6.6.

Figure 6.6 (timeline, left to right; p. 277, PDF 290)

| Date 1 | | | | | Date 2 | | |
|---|---|---|---|---|---|---|---|
| The banks decide whether to share information about default. | The borrower chooses $\alpha$. | The borrower's type ($p$ or $q$) is realized. | Banks offer contracts to borrowers. | Outcomes ($R$ or 0) and repayments. | Banks share information (if they agreed to do so). | Banks offer contracts to borrowers. | Outcomes ($R$ or 0) and repayments. |

(i) Suppose first that the probability $\alpha$ of being a $p$-type is exogenous (there is no borrower investment), that $[\alpha p + (1 - \alpha)q]R - I + \delta(\alpha p + (1 - \alpha)q)(R - I) < 0$, and that $qR - I + \delta q(R - I) < 0$. Show that the banks prefer not to share information.

(ii) Next, suppose that the borrower chooses $\alpha$. Assuming that the two assumptions made in (i) still hold in the relevant range of $\alpha$s (for example, $\alpha \in [0, \bar\alpha]$, where $\bar\alpha$ satisfies the conditions), show that the banks choose to share information.

---

### 14. Leland–Pyle with mean-variance preferences
**Source:** Amaro de Matos, Ch. 3, Exercise 3.2.6 #2, p. 95 (PDF 113) · Answer in book: no (p. 260 only cites page 377 of Leland and Pyle 1977)

In the context of Leland and Pyle (1977), suppose that the expected utility of the manager is given by $E[U(W_1)] = G[E(W_1) - \frac{b}{2}\sigma^2_{W_1}]$, where $G$ is an increasing function, $\sigma^2_{W_1}$ is the variance of the wealth At time 1, and the risk adjustment parameter $\lambda$ is given by $\lambda = \frac{E[M] - (1 + r)V_M}{\sigma^2_M}\operatorname{cov}(\varepsilon, M)$. In this case, under what conditions does the level of debt increase with the proportion $\alpha$ of the equity owned by the managers?

#### Context needed to solve it

*From Amaro de Matos §3.2, p. 78 (PDF 96):*

**Assumption 3.2.1.** *Managers have better information about the value of the firm than other agents in the economy.*

*From Amaro de Matos §3.2.2 "When Managers Are Also Investors", pp. 82–85 (PDF 100–103):*

Leland and Pyle (1977) developed a model in the same signaling context as Ross, in which risk averse managers are also investors in the firm. Consider entrepreneurs starting a project with a random return $X = \overline{X} + \epsilon$, with $E(\epsilon) = 0$, needing a capital investment $K$. Here, these entrepreneurs, who are going to manage the project, are the only individuals who know the expected return $\overline{X} = E(X)$. At time 0 they sell a fraction $(1 - \alpha)$ of the project and retain a fraction $\alpha$. The uninformed investors use this proportion as a signal of the value of the firm. Underlying this idea is, clearly, Assumption 3.2.1. As the management better knows the value of the firm, the fact that it holds a reasonable part of the equity is a good signal, whereas no participation will naturally be considered as a bad signal. As the managers are risk averse, they would like to diversify but cannot, since they have to hold on to their shares. That is their cost of signaling, and that is why the signal is credible. Managers of good projects are then easily identified with this procedure because their claim on the firm is worth more. That is why they can afford to signal in that way and hold onto a greater portion of the shares.

In this model, Assumption 3.2.1 that managers have superior information takes the simple form

**Assumption 3.2.4.** *Only the management knows the value of the expected return $X$.*

Uninformed investors will have to *infer* in equilibrium the expected return through a function of $\alpha$, say, $X(\alpha)$. Consequently, the *perceived* value of the firm, say, a function $V(\alpha)$, will also depend on $\alpha$. As in Ross's model, Leland and Pyle work in a two-time framework. As in equation (3.8), the perceived value of the firm will here be given by

$$V(\alpha) = \frac{X(\alpha) - \lambda}{1 + r}, \qquad (3.15)$$

where $\lambda$ is a risk adjustment parameter and $r$ is the risk-free interest rate.

At time 0, managers have their initial wealth $W_\circ$. Additionally they may issue risk-free debt in the amount of $B$ and sell a fraction $(1 - \alpha)$ of the perceived value of the project. The value of such a fraction is worth $(1 - \alpha)[V(\alpha) - B]$ at time 0, since debt must be paid from the proceeds of the project. Thus, entrepreneurs initially have

$$W_\circ + B + (1 - \alpha)[V(\alpha) - B].$$

This amount is assumed to be invested in three different assets, namely the project, the market portfolio, and a risk-free asset. The decision variables will be the proportion $\alpha$ of the equity of the firm held by the entrepreneurs and the proportion $\beta$ of the market portfolio held. The rest of their wealth (say, $Y$) will be invested in a risk-free asset. The optimal way to make this allocation is constrained by

$$W_\circ + B + (1 - \alpha)[V(\alpha) - B] = K + Y + \beta V_M,$$

where $V_M$ is taken as the value of the market portfolio. This equation is the *budget constraint* faced by the management when deciding how to allocate its wealth. Using equation (3.15) it follows that

$$Y = W_\circ + B - K - \beta V_M + \frac{1 - \alpha}{1 + r}[X(\alpha) - \lambda - (1 + r)B]. \qquad (3.16)$$

The objective of the managers is to maximize the expected utility of their random wealth at the end of the process (i.e., at time 1). If the return on the market portfolio is denoted by $\widetilde{M}$, the wealth of the management at that time is the random variable

$$\widetilde{W}_1 = \alpha[X - B(1 + r)] + \beta\widetilde{M} + (1 + r)Y.$$

Substituting the value of $Y$ by the expression in (3.16) (that is, incorporating in the random wealth the budget constraint with respect to which the utility maximization must be subject), it follows that

$$\widetilde{W}_1 = \alpha[\overline{X} + \epsilon - X(\alpha) + \lambda] + \beta[\widetilde{M} - (1 + r)V_M] + (W_\circ - K)(1 + r) + (X(\alpha) - \lambda).$$

Assuming that the management has a utility function $U$, its problem becomes

$$\max_{(\alpha, \beta) \in [0,1] \times [0,1]} E[U(\widetilde{W}_1)], \qquad (3.17)$$

for which there will be a solution $\alpha^* \equiv \alpha^*(\overline{X})$ and $\beta^* \equiv \beta^*(\overline{X})$. As in other signaling models, in equilibrium the values of $\alpha^*$ and $\beta^*$ must reveal the true expected return, that is to say, the equilibrium condition

$$\overline{X}[\alpha^*(\overline{X})] = \overline{X}$$

must be imposed on the solution of the problem. There are two necessary first-order conditions to be satisfied in order to solve (3.17): one with respect to $\alpha$ and the other with respect to $\beta$. Denoting by $X(\alpha)_\alpha$ the derivative $dX(\alpha)/d\alpha$, the first-order condition reads

$$(1 - \alpha)X(\alpha)_\alpha = -\frac{E[U'(\widetilde{W}_1)(\epsilon + \lambda)]}{E[U'(\widetilde{W}_1)]}, \qquad (3.18)$$

and the second is

$$E\{U'(\widetilde{W}_1)[\widetilde{M} - (1 + r)V_M]\} = 0. \qquad (3.19)$$

Solving (3.19) for $\beta$ and substituting this value of $\beta$ into (3.18), one gets a differential equation for $X(\alpha)$ whose solution does not depend explicitly on $\beta$ and is uniquely defined up to a constant of integration.

The following two important results are proved by Leland and Pyle:

**Proposition 3.2.1 (Leland and Pyle, 1977).** *$X(\alpha)$ is strictly increasing in $\alpha$ if and only if the management demand for equity is normal.*¹⁵

**Proposition 3.2.2 (Leland and Pyle, 1977).** *In equilibrium signaling, managers with normal demand have a value of $\alpha$ higher than the proportion they would invest if they could costlessly communicate the true value of $\overline{X}$.*

This last result may be seen as a welfare cost result. In fact, the cost of signaling reflected in the overparticipation of the management in the equity of the company may be used as a criterion to choose the constant of integration defining $X(\alpha)$ as the solution of the differential equation previously described. The constant will be chosen so as to minimize this signaling cost.

The relevant issue here is how these results relate to the debt policy followed by the firms. All other factors being fixed, including the amount invested by the management in equity, in most cases the level of debt increases with the proportion $\alpha$ of the equity owned by managers. From Proposition 3.2.1, it follows that $X(\alpha)$ increases with debt; therefore equation (3.15) implies that the perceived value $V(\alpha)$ increases with the debt level $B$, just as in Ross's model. […]

*From Amaro de Matos, Notes to Chapter 3, note 15, p. 280 (PDF 298):*

15. The demand for an asset is said to be normal if, in a portfolio choice situation without signaling, the demand is a decreasing function of price.

---

### 15. Assets in place and the negative stock-price reaction with a continuum of types
**Source:** Tirole, Ch. 6, Exercise 6.5, p. 275 (PDF 288) · Answer in book: yes, p. 597

Consider the privately-known-prospects model of Application 2 in Section 6.2.2, but with a continuum of types. The entrepreneur already owns a project, which with probability $p$ yields profit $R$ and probability $1 - p$ profit 0. The probability $p$ is private information of the borrower. From the point of view of the investors, $p$ is drawn from cumulative distribution $F(p)$ with continuous density $f(p) > 0$ on some interval $[\underline{p}, \bar{p}]$. Assume that the distribution has monotone hazard rates:

$$\frac{f(p)}{F(p)} \quad \text{is decreasing in } p$$

and

$$\frac{f(p)}{1 - F(p)} \quad \text{is increasing in } p.$$

(This assumption, which is satisfied by most usual distributions, is known to imply that the truncated means $m^-(p)$ and $m^+(p)$ have slope less than 1:

$$0 < (m^-(p))' \equiv \frac{d}{dp}[E(\tilde{p} \mid \tilde{p} \leqslant p)] \leqslant 1$$

and

$$0 < (m^+(p))' \equiv \frac{d}{dp}[E(\tilde{p} \mid \tilde{p} \geqslant p)] \leqslant 1$$

(see, for example, An 1998).)

The model is otherwise as in Section 6.2.2. A seasoned offering may be motivated by a profitable deepening investment: at cost $I$, the probability of success can be raised by an amount $\tau$ such that

$$\tau R > I$$

(of course, we need to assume that $\bar{p} + \tau \leqslant 1$). The entrepreneur has no cash on hand, is risk neutral, and is protected by limited liability. The investors are risk neutral and demand a rate of return equal to 0.

(i) Show that in any equilibrium, only types $p \leqslant p^*$, for some cutoff $p^*$, raise funds and finance the deepening investment.

(ii) Show that $p^* > \underline{p}$ and that if $p^* < \bar{p}$, then

$$\frac{\tau R}{I} = \frac{p^* + \tau}{m^-(p^*) + \tau}.$$

Show that if the benefits from investment are “not too large,” in that

$$\frac{\tau R}{I} < \frac{\bar{p} + \tau}{E[p] + \tau},$$

then indeed $p^* < \bar{p}$.

Show that if there are multiple equilibria, the one with the highest cutoff $p^*$ Pareto-dominates (is better for all types than) the other equilibria.

(iii) Is there a negative stock price reaction upon announcement of an equity issue?

(iv) Focusing on an interior Pareto-dominant equilibrium, show that, when $\tau$ increases, the volume of equity issues increases.

#### Context needed to solve it

*From Tirole §6.2 (privately-known-prospects model), p. 241 (PDF 254):*

*Privately-known-prospects model.* A borrower/entrepreneur has no funds ($A = 0$) to finance a project costing $I$. The project yields $R$ in the case of success and 0 in the case of failure. The borrower and the lenders are risk neutral, and the borrower is protected by limited liability. The interest rate in the economy is normalized at 0.

The borrower can be one of two types. A good borrower has a probability of success equal to $p$. A bad borrower has a probability of success $q$. Assume that $p > q$ and that $pR > I$ (at least the good type is creditworthy). […]

The borrower has private information about her type. The capital market, which is competitive and demands an expected rate of return equal to 0, puts probabilities $\alpha$ and $1 - \alpha$ on the borrower being a good or a bad type, respectively. Under asymmetric information, the capital market does not know whether it faces a “$p$-borrower” (a good borrower) or a “$q$-borrower” (a bad borrower). Let

$$m \equiv \alpha p + (1 - \alpha) q$$

denote the investors’ prior probability of success.

*From Tirole §6.2.2, Application 2: Assets in Place, the Negative Stock Price Reaction, and the Going-Public Decision, pp. 244–245 (PDF 257–258):*

Let us next suppose that the entrepreneur already owns a project that, without further investment, will succeed with probability $p$ or $q$, yielding profit $R$. As before, the entrepreneur knows the probability of success while the investors put probability $\alpha$ on $p$ and $(1 - \alpha)$ on $q$. Thus, in the absence of further information (and so the investors’ expectation of the probability of success is $m$), the assets in place are undervalued (respectively, overvalued) if the true probability of success is $p$ (respectively, $q$).

For computational simplicity, we will assume that the entrepreneur initially owns all shares. But nothing is altered if she owns only a fraction of the shares. By “stock price reaction upon the announcement of an equity issue,” we mean the difference between the total value of shares (whoever owns them) before and after the announcement. This notion corresponds to the approach taken by event studies in empirical work.

An equity offering may be motivated by a profitable “deepening investment” (more generally, the key feature is that one cannot contract on the cash flow generated by this investment separately from that generated by assets in place: the incomes generated by the two are intertwined or fungible²²). At cost $I$, the probability of success can be raised by an amount $\tau$ such that

$$\tau R > I.$$

That is, investing is efficient for both types of borrowers. Note that we assume for the moment that the increase in profitability is uniform across types: the probability of success becomes $p + \tau$ for a good borrower and $q + \tau$ for a bad one.

The entrepreneur, however, has no cash on hand. Accordingly, the full amount $I$ must be raised from investors. The entrepreneur must therefore issue new shares, thereby reducing the fraction of shares she owns.

A key insight is that relinquishing shares to investors is relatively less costly to the borrower with overvalued assets in place (the bad borrower) than to the borrower with undervalued assets in place (the good borrower). Thus, if the good borrower conducts an equity offering, so does the bad one.

Let us therefore investigate the possibility of an (efficient) pooling equilibrium. The entrepreneur must offer a stake $R_l$ in success to the investors such that

$$[\alpha(p + \tau) + (1 - \alpha)(q + \tau)]R_l = I \iff (m + \tau)R_l = I,$$

where, as earlier, $m \equiv \alpha p + (1 - \alpha)q$ is the prior mean probability of success. There exists a unique $R_l$, $0 < R_l < R$, satisfying this condition.

The good borrower, though, can guarantee herself $pR$ by not diluting her stake.²³ Thus, she is willing to issue new shares only if

$$(p + \tau)(R - R_l) \geqslant pR \iff \tau R \geqslant \frac{p + \tau}{m + \tau} I. \qquad (6.1)$$

[…] We are thus led to consider two situations:

*Pooling equilibrium.* If condition (6.1) holds, then both types conduct an equity offering.²⁴ If the accrual of this deepening investment is anticipated,²⁵ the total value of shares *before and after* the seasoned equity offering is

$$(m + \tau)R - I.$$

There is no stock price reaction to the offering, which is perfectly anticipated and uninformative.

*Separating equilibrium.* More interestingly, suppose that condition (6.1) is violated. The good borrower then does not raise funds. The bad borrower still does, but under market conditions that are not as favorable as in a pooling equilibrium. Because the investors know that the equity offering reveals overvalued assets, they demand a higher stake $R_l^B > R_l$ such that

$$(q + \tau)R_l^B = I.$$

The good borrower does not want to raise funds because

$$(p + \tau)(R - R_l^B) < pR \iff \tau R < \frac{p + \tau}{q + \tau} I, \qquad (6.2)$$

which holds if condition (6.1) is violated.

The announcement of a seasoned equity offering then leads to a *negative stock price reaction*. The preannouncement total value of shares is²⁶

$$V_0 = \alpha[pR] + (1 - \alpha)[(q + \tau)R - I].$$

After the announcement, it becomes

$$V_1 = (q + \tau)R - I.$$

Hence,

$$V_0 > V_1 \iff pR > (q + \tau)R - I.$$

But we know that

$$pR > (p + \tau)\left(R - \frac{I}{q + \tau}\right),$$

and so *a fortiori* $V_0 > V_1$.

> 22. Otherwise, it would be optimal for the good borrower to engage in project finance so as to avoid having to cross-subsidize the bad one.
>
> 23. That this “reservation utility” depends on the borrower’s type is the essential difference with the barebones model. Here, in the jargon of incentive theory, “reservation utilities are type-contingent.” […]
>
> 24. This pooling equilibrium is not unique whenever $(p + \tau)I/(m + \tau) \leqslant \tau R \leqslant (p + \tau)I/(q + \tau)$; indeed, if investors believe that an equity offering comes from a bad borrower and $\tau R \leqslant (p + \tau)I/(q + \tau)$, then the good type indeed prefers not to raise funds. However, the pooling equilibrium is the *Pareto-dominant* equilibrium (it is the best equilibrium for both the good and the bad borrower), and so we will focus on it. Note also that if condition (6.1) holds, then the bad borrower definitely prefers to raise funds since the analogous condition for her is $\tau R \geqslant \frac{q + \tau}{m + \tau} I$, which is always satisfied.
>
> 25. Otherwise, the news of the existence of an investment opportunity by itself raises the value of shares.
>
> 26. As in the previous footnote, note that we assume that the investment opportunity is perfectly anticipated by the capital market. Otherwise, the issue of new securities could convey good news about the firm’s opportunity set and the concomitant boost in share price might dominate the effect unveiled here.

## Original exercises (no book exercise exists)

None of the six course books has an exercise on the Stiglitz–Weiss model (lecture block 3.6) or on collateral as a separating signal (block 3.7). The four exercises below are original, written for this list with the user's agreement (2026-11-12). They use the notation of Prof. Ricca's slides and have no book answer; the worked solutions are sections 16–19 of the solutions files.

### 16. Stiglitz–Weiss with two types: the lender's return is not monotone in the rate (Easy)
**Origin:** original exercise on Stiglitz–Weiss (1981) credit rationing with mean-preserving spreads, built on Prof. Ricca's Topic 3 slides 47–55 (Aula/Topic_3.pdf) and Tirole §3.1 Introduction, p. 113 (PDF 126), and §6.1 Introduction, footnote 5, p. 240 (PDF 253) · Answer: in the solutions file

A lender finances projects that cost $I = 100$ each. Borrowers have no money of their own and there are two types, which the lender cannot tell apart. A low-risk (safe) borrower's project yields $R_L = 150$ with probability $p_L = 0.8$ and 0 otherwise. A high-risk (risky) borrower's project yields $R_H = 300$ with probability $p_H = 0.4$ and 0 otherwise. A share $\alpha = 0.75$ of the borrowers is low-risk. Borrowers and the lender are risk neutral. The lender offers only a standard debt contract: the borrower receives $I$ and repays $(1 + r)I$ if the project succeeds and nothing if it fails (limited liability; a failed project is worth 0). A borrower applies for a loan if and only if her expected payoff is non-negative.

(a) Show that both projects have the same expected return $\bar R$ and compute it. Compute the variance of each project's return. Show that the high-risk return is a mean-preserving spread of the low-risk return, i.e. that it can be obtained by adding to each realisation of the low-risk return a random variable with zero mean conditional on that realisation.

(b) Write each type's expected payoff from borrowing at rate $r$ as a function of $r$, and evaluate both at $r = 20\%$. Which type is hurt more by a rise in $r$, and why?

(c) Compute the rate $r^*$ above which the low-risk borrowers stop applying and the rate $r_{max}$ above which nobody applies. Who applies for $r \le r^*$, for $r^* < r \le r_{max}$ and for $r > r_{max}$?

(d) Let $\rho(r)$ be the lender's expected gross return per unit lent (expected repayment divided by $I$). Write $\rho(r)$ for $r \le r^*$ and for $r^* < r \le r_{max}$. Evaluate it at $r = 20\%$, $r = r^*$, $r = 60\%$, $r = 100\%$ and $r = r_{max}$. Compute the drop in $\rho$ when $r$ crosses $r^*$ and show that it equals $\alpha(p_L - p_H)(1 + r^*)$. Is $\rho$ monotone in $r$?

(e) Find the rate $\tilde r > r^*$ at which the lender's return first gets back to $\rho(r^*)$. Explain why a lender that faces more applicants than it can fund at $r^*$ would never raise its rate to any value in $(r^*, \tilde r)$, and why this makes the supply of loans "backward-bending".

(f) Suppose instead that the lender finances the project with equity: it takes a share $s$ of the project's return, in both success and failure. Find the share $s$ that gives the lender the same expected gross return per unit lent as the debt contract at $r^*$. Which types apply, and what is each type's expected payoff? Explain why the adverse selection of parts (c)–(e) disappears.

#### Context needed to solve it

*From Prof. Ricca's Topic 3 slides 47–55 (block 3.6, Stiglitz and Weiss 1981):*

- Notion of risk: mean-preserving spreads. Projects have the same mean; a mean-preserving spread of a random variable $X$ is obtained by adding a zero-mean random variable to each possible realisation of $X$ (slide 47).
- Asymmetric information and adverse selection may make the supply curve backward-bending at high interest rates: the pool of borrowers gets worse when rates rise, because the payoff in the default state does not depend on the rate, so a rise in the rate hurts the borrowers who default more often less (slide 48). Supply and demand may then not intersect, and demand can exceed supply at the prevailing rate: credit rationing.
- Two-type example (slides 50–54). Low risk: $R_L$ with probability $p_L$, 0 otherwise; high risk: $R_H$ with probability $p_H$, 0 otherwise; $p_L > p_H$ and $p_L R_L = p_H R_H = \bar R$ (the high-risk project is a mean-preserving spread of the low-risk one). Borrowers and lenders are risk neutral; types are private information; the project requires $I$. At rate $r$ the expected payoffs are $p_L[R_L - (1 + r)I] = \bar R - p_L(1 + r)I$ and $p_H[R_H - (1 + r)I] = \bar R - p_H(1 + r)I$.
- $r_{max}$ solves $\bar R - p_H(1 + r_{max})I = 0$, i.e. $r_{max} = \bar R/(p_H I) - 1$; $r^*$ solves $\bar R - p_L(1 + r^*)I = 0$, i.e. $r^* = \bar R/(p_L I) - 1$. For $r < r^*$ both types apply; for $r^* < r < r_{max}$ only high-risk borrowers apply.
- With $\alpha$ the proportion of low-risk types, the lender's expected payoff is $m(1 + r)$ with $m = \alpha p_L + (1 - \alpha)p_H$ when $r < r^*$, and $p_H(1 + r)$ when $r^* < r < r_{max}$. The expected return drops sharply around $r^*$ as the good types leave the market; it is not a monotonic function of the rate (slides 53–54).

*From Tirole §6.1 Introduction, footnote 5, p. 240 (PDF 253):* "Stiglitz and Weiss assume that lenders can offer only debt contracts, and show that the repayment probability decreases with the rate of interest offered by lenders, and that the loan market is characterized by credit rationing. However, the assumptions of the model predict that investors should instead offer equity contracts, in which case there would be no adverse selection (all firms have the same mean income) and no credit rationing (Hart 1985)."

### 17. Why raising the rate does not clear the loan market (Exam level)
**Origin:** original exercise on Stiglitz–Weiss (1981) credit rationing in a competitive loan market, built on Prof. Ricca's Topic 3 slides 47–55 (Aula/Topic_3.pdf) and Tirole §3.1 Introduction, p. 113 (PDF 126) · Answer: in the solutions file

There are $N = 1{,}000$ borrowers. Each needs $I = 100$ for a project and has no money of her own. A share $\alpha = 0.75$ of them is low-risk: the project yields $R_L = 130$ with probability $p_L = 0.9$ and 0 otherwise. The rest are high-risk: the project yields $R_H = 234$ with probability $p_H = 0.5$ and 0 otherwise. Types are private information. Banks are competitive and risk neutral, offer only standard debt contracts (repay $(1 + r)I$ on success, nothing on failure), make zero profit and pass to depositors the expected gross return per unit lent, $\rho$. Depositors supply funds

$$L^s(\rho) = \max\{0,\ 1{,}000{,}000\,(\rho - 0.96)\}.$$

A borrower applies if her expected payoff is non-negative (an indifferent borrower applies). When applicants exceed funds, the banks choose the borrowers who get a loan at random among the applicants.

(a) Compute $\bar R$, the rates $r^*$ (above which the low-risk borrowers stop applying) and $r_{max}$ (above which nobody applies), the banks' expected gross return $\rho(r)$ on each interval, $\rho^* \equiv \rho(r^*)$, and the rate $\tilde r > r^*$ at which $\rho$ is back to $\rho^*$.

(b) Compute loan demand and the supply of funds at $r = r^*$. How many applicants are turned down, and how many of them are low-risk and high-risk?

(c) One bank, facing excess demand, raises its rate to $r = 40\%$. Who applies at that rate, what is $\rho(40\%)$, and how much would depositors supply if all banks charged $40\%$? Explain why raising the rate does not clear the market.

(d) Show that no rate $r \le r^*$ equates supply and demand. Find the rate $r_W \in (r^*, r_{max}]$ at which supply equals demand, and the return $\rho(r_W)$. Show that $r_W$ is not an equilibrium: a bank that offers $r^*$ instead can pay its depositors more and still find borrowers. Conclude what the market interest rate is and whether there is credit rationing.

(e) Comparative statics; change one parameter at a time and keep the others at their initial values.
  (i) The share of low-risk borrowers rises to $\alpha = 0.9$. Compute $\rho^*$ and $L^s(\rho^*)$. Is there still rationing? If not, find the market-clearing rate.
  (ii) The high-risk project becomes riskier with the same mean: $p_H = 0.4$, $R_H = 292.5$ ($\alpha = 0.75$). Compute $r^*$, $r_{max}$, $\rho^*$, $L^s(\rho^*)$, the share of applicants turned down, the drop in $\rho$ at $r^*$, and check whether the rate that clears the market among high-risk borrowers only is an equilibrium.

(f) Go back to the initial parameters and the outcome of (b) and (d). A bank offers loans only to applicants who were turned down at $r^*$, at a rate $r' \in (\tilde r, r_{max}]$. Who accepts, and what is the bank's expected gross return? What will competition among such banks do to $r'$? Which borrowers remain without credit, and why can no rate above $r^*$ serve them?

#### Context needed to solve it

*From Prof. Ricca's Topic 3 slides 47–55 (block 3.6, Stiglitz and Weiss 1981):* same model as exercise 16, restated here.

- Mean-preserving spreads: $p_L > p_H$ and $p_L R_L = p_H R_H = \bar R$; risk-neutral borrowers and lenders; types are private information; investment $I$. At rate $r$ the expected payoffs are $\bar R - p_L(1 + r)I$ (low risk) and $\bar R - p_H(1 + r)I$ (high risk), so a rise in $r$ hurts the high-risk borrowers less (slide 51).
- $r_{max} = \bar R/(p_H I) - 1$ (neither type applies when $r > r_{max}$); $r^* = \bar R/(p_L I) - 1$ (only high-risk borrowers apply when $r^* < r < r_{max}$; both types apply when $r < r^*$) (slide 52).
- Lender's expected payoff per unit: $m(1 + r)$, $m = \alpha p_L + (1 - \alpha)p_H$, for $r < r^*$; $p_H(1 + r)$ for $r^* < r < r_{max}$; it drops sharply around $r^*$ and is not monotone in $r$ (slides 53–54).
- The pool of borrowers gets worse when rates rise; the supply curve can be backward-bending at high rates; supply and demand may not intersect, so demand can exceed supply at the prevailing rate: credit rationing (slides 47–48).

*From Tirole §3.1 Introduction, p. 113 (PDF 126):* "Why are lenders not willing to raise interest rates if the demand for loans exceeds their supply at the prevailing rates? […] The adverse selection explanation is that, in a situation where lenders cannot directly tell good and bad borrowers apart, higher interest rates tend to attract low-quality borrowers; for, low-quality borrowers are more likely to default on their loan and therefore are less affected by a rise in the interest rate than high-quality borrowers. Lenders may then want to keep interest rates low in order to face a better sample of borrowers."

### 18. Collateral as a separating signal (Exam level)
**Origin:** original exercise on costly collateral as a signal (Bester 1985), built on Prof. Ricca's Topic 3 slides 56–67 (Aula/Topic_3.pdf) and Tirole §6.3, Application 5, pp. 251–253 (PDF 264–266) · Answer: in the solutions file

An entrepreneur needs $I = 60$ for a project that yields $R = 120$ if it succeeds and 0 if it fails. She has no cash, but she owns an illiquid asset worth 60 to her that she can pledge as collateral: collateral worth $C$ to her is worth only $\delta C$ to a lender, with $\delta = 0.5$. A good type succeeds with probability $p = 0.9$, a bad type with probability $q = 0.6$; the share of good types is $\alpha = 0.5$. Everybody is risk neutral, the riskless rate is 0, and lenders are competitive (zero expected profit). A contract $\{R_u, C\}$ says that the lender receives $R_u$ if the project succeeds and seizes the collateral $C$ if it fails; the entrepreneur keeps $R - R_u$ on success and loses $C$ on failure.

(a) Symmetric information. Compute each type's zero-profit repayment with no collateral, $R_u^G$ and $R_u^B$, and each type's utility. Then let the good type pledge $C = 20$: compute her zero-profit repayment and her utility, and show that her utility falls by $(1 - p)(1 - \delta)C$. Why is $C = 0$ optimal under symmetric information?

(b) Asymmetric information without collateral. Compute the prior $m$ and the pooling repayment $R_u = I/m$, and each type's utility. Show that if the good type asked for her symmetric-information contract $\{I/p, 0\}$, the bad type would mimic her.

(c) Separating equilibrium. In it the bad type pledges no collateral and repays $R_u^B = I/q$. The good type chooses $\{\tilde R, \tilde C\}$ to maximise her utility subject to the no-mimicking condition of the bad type and the lender's break-even condition. Write the program, explain why both constraints bind, and solve for $C_G$ and $R_u^G$ (give the general formulas and the numbers). Verify both constraints numerically and check that the good type can afford the collateral.

(d) Compute the good type's utility in the separating equilibrium and the expected deadweight cost of collateral, $(1 - p)(1 - \delta)C_G$. Compare it with her utility in (a) and in (b). Which regime does the good type prefer, and by how much?

(e) Check that neither type wants the other type's contract in the separating equilibrium. Explain why collateral can separate the types here (which type finds it more costly, and why).

#### Context needed to solve it

*From Prof. Ricca's Topic 3 slides 56–67 (block 3.7, signalling with costly collateral):*

- To be a successful separating mechanism, the cost of the signalling device has to differ sufficiently among the types (slide 56).
- Projects require $I$ and yield $R$ on success and 0 otherwise; the good type succeeds with probability $p$, the bad type with $q$; the share of good types is $\alpha$ and the prior is $m = \alpha p + (1 - \alpha)q$; both types have positive NPV, $pR > I$, $qR > I$ (slide 57).
- Borrowers have no cash on hand but can pledge an illiquid asset as collateral. Assets worth $C$ in the hands of borrowers are worth only $\delta C$ in the lenders' hands, $0 < \delta < 1$; collateral is inefficient: $(1 - \delta)C$ is lost in case of default (slide 58). (Tirole writes $\beta$ for $\delta$.)
- Symmetric information: with collateral $C$ the good type's zero-profit repayment satisfies $pR_u + (1 - p)\delta C = I$, i.e. $R_u = I/p - (1 - p)\delta C/p$, and her utility is $p(R - R_u) + (1 - p)(-C) = pR - I - (1 - p)(1 - \delta)C$, so the best choice is $C = 0$; same for the bad type (slides 59–60).
- Asymmetric information without collateral: both types repay $R_u = I/m > I/p = R_u^G$ (slide 61).
- Separating equilibrium: good type $\{R_u^G, C_G\}$, bad type $\{R_u^B, C_B\}$; lenders infer the type from the contract. The bad type must not want to mimic, so $C_B = 0$ and $R_u^B = I/q$. The good type's contract $\{\tilde R, \tilde C\}$ solves
  $$\max_{\tilde R, \tilde C}\ p(R - \tilde R) + (1 - p)(-\tilde C)$$
  subject to $q(R - \tilde R) + (1 - q)(-\tilde C) \le qR - I$ (no-mimicking) and $p\tilde R + (1 - p)\delta\tilde C \ge I$ (lender's break-even) (slides 62–65).
- Both constraints bind at the solution (slide 66). Signalling is worth it for the good type when the adverse-selection cost is large: $p(R - R_u^G) + (1 - p)(-C_G) \ge p(R - I/m)$ (slide 67).

*From Tirole §6.3, Application 5 "Costly Collateral Pledging", pp. 251–253 (PDF 264–266):* the same program written with the borrower's reward $R_b = R - R_u$; Assumption 6.1, $0 < qR - I < pR - I$; the borrower has "a sizeable amount of assets" to pledge; signalling works because pledging collateral is relatively more costly for a bad borrower, while a higher reward in success is valued more by a good one (the sorting condition).

### 19. When does signalling with collateral pay? (Really hard)
**Origin:** original exercise on costly collateral as a signal (Bester 1985): separating versus pooling and comparative statics, built on Prof. Ricca's Topic 3 slides 56–67 (Aula/Topic_3.pdf) and Tirole §6.3, Application 5, pp. 251–253 (PDF 264–266) · Answer: in the solutions file

Same model as exercise 18 (restated in the context below) with $I = 50$, $R = 100$, $p = 0.8$, $q = 0.7$ and, unless stated otherwise, $\delta = 0.2$. The entrepreneur owns illiquid assets worth 50 to her. The share of good types $\alpha$ varies across parts.

(a) Compute the good type's least-cost separating contract $\{R_u^G, C_G\}$ (both constraints binding), check both constraints, and compute her utility $U^{sep}$ and the expected deadweight cost $(1 - p)(1 - \delta)C_G$. Does $U^{sep}$ depend on $\alpha$?

(b) For $\alpha = 0.3$ and for $\alpha = 0.6$, compute $m$, the pooling repayment $I/m$ and the good type's pooling utility $U^{pool} = p(R - I/m)$. In which case does she prefer to signal?

(c) Show, for general parameters, that $U^{sep} \ge U^{pool}$ if and only if
$$\alpha\,p\,(1 - p)(1 - \delta) \le (1 - \alpha)(p - q),$$
and write the threshold $\hat\alpha$ below which the good type prefers to signal. Compute $\hat\alpha$ and check that at $\hat\alpha$ the two utilities coincide.

(d) Comparative statics in $\delta$. Show that $C_G$ increases with $\delta$ while the expected deadweight cost $(1 - p)(1 - \delta)C_G$ decreases with $\delta$; evaluate both derivatives at $\delta = 0.2$. Compute $C_G$, $R_u^G$, the deadweight cost and $U^{sep}$ for $\delta = 0$ and $\delta = 0.6$, and the limits as $\delta \to 1$. For $\alpha = 0.6$, find the threshold $\hat\delta$ above which the good type prefers to signal, and check it with the numbers for $\delta = 0.6$.

(e) Comparative statics in $q$ ($\delta = 0.2$). Show that $C_G$ falls as $q$ rises toward $p$, and compute $C_G$ and the deadweight cost for $q = 0.6$ and $q = 0.75$. Interpret.

(f) Welfare at $\alpha = 0.3$. Compute total expected surplus per borrower (both types together) under pooling and under separation, the bad type's utility in each, and the surplus lost to separation. Which outcome is efficient, and why does the good type still choose to signal?

#### Context needed to solve it

*From Prof. Ricca's Topic 3 slides 56–67 (block 3.7, signalling with costly collateral):* the model of exercise 18, restated.

- Project: cost $I$, return $R$ on success, 0 on failure; good type succeeds with probability $p$, bad type with $q < p$; share of good types $\alpha$, prior $m = \alpha p + (1 - \alpha)q$; $pR > I$ and $qR > I$; no cash on hand; risk neutrality, riskless rate 0, competitive lenders (slide 57).
- Collateral worth $C$ to the borrower is worth $\delta C$ to the lender, $0 < \delta < 1$ (Tirole: $\beta$, $0 \le \beta < 1$); $(1 - \delta)C$ is lost in default (slide 58). Under symmetric information the good type's utility with collateral is $pR - I - (1 - p)(1 - \delta)C$, so $C = 0$ (slides 59–60).
- Pooling without collateral: $R_u = I/m$, good type's utility $p(R - I/m)$ (slides 61, 67).
- Separating: bad type $C_B = 0$, $R_u^B = I/q$, utility $qR - I$. Good type: $\max_{\tilde R, \tilde C} p(R - \tilde R) - (1 - p)\tilde C$ subject to $q(R - \tilde R) - (1 - q)\tilde C \le qR - I$ and $p\tilde R + (1 - p)\delta\tilde C \ge I$; both bind (slides 63–66), giving
  $$R_u^G = \frac{(1 - q) - \delta(1 - p)}{p(1 - q) - \delta q(1 - p)}\,I, \qquad C_G = \frac{I}{1 + \dfrac{q(1 - p)(1 - \delta)}{p - q}}.$$
- If the adverse-selection cost is very large (large share of bad borrowers $1 - \alpha$, or large distance between $p$ and $q$), the good type is better off with the possibility of signalling: $p(R - R_u^G) + (1 - p)(-C_G) \ge p(R - I/m)$ (slide 67).

*From Tirole §6.3, Application 5, p. 253 (PDF 266):* "The good borrower must pledge more collateral when collateral pledging becomes cheaper for the borrower ($\partial C^*/\partial\beta > 0$)" and "the stronger the asymmetry of information ($\partial C^*/\partial q < 0$) […] $C^*$ tends to 0 […] when $q$ tends to $p$, as we would expect."
