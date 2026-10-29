---
tags: [exercise-list, ricca-r6, liquidity-risk-management]
date: 2026-10-24
---

# Exercise list R6 — Liquidity and risk management

Ricca topic 6 (syllabus reading: Tirole Ch. 5): liquidity shocks and the liquidity–scale tradeoff, credit lines and loan commitments, liquidity hoarding and the pricing of liquid assets, free cash flow and debt maturity, and corporate hedging. 15 exercises ordered easy → really hard, copied verbatim from the course books for personal study; pages are printed (PDF in brackets). Links: [[Map/exercises-index|exercise index]] · [[rules/05_liquidez|rules]].

## References
| # | Tier | Book | Ch. | Exercise | Printed p. | Answer in book | Trains |
|---|---|---|---|---|---|---|---|
| 1 | Easy | Ross | 19 | CQ 19.1 | 690 (714) | no | Why too much cash worries shareholders |
| 2 | Easy | Ross | 19 | CQ 19.10 | 690 (714) | no | Excess cash and agency problems (free cash flow) |
| 3 | Easy | Grinblatt–Titman | 21 | 21.1 | 771 (784) | no | Why hedging rises with firm size |
| 4 | Easy | Grinblatt–Titman | 21 | 21.7 | 771 (784) | no | Why partial hedging can be optimal |
| 5 | Easy | Berk | 20 | 20.6 | 613 (644) | no | Cash buffer versus short-term borrowing |
| 6 | Exam | Tirole | 5 | 5.1 | 229 (242) | yes, p. 591 | Loan commitment in a long-term contract; renegotiation proofness |
| 7 | Exam | Tirole | 5 | 5.2 | 229 (242) | yes, p. 591 | Credit line as protection against predation and date-0 moral hazard |
| 8 | Exam | Tirole | 5 | 5.5 | 231 (244) | yes, p. 592 | Liquidity hoarding and the liquidity premium on Treasury bonds |
| 9 | Exam | Tirole | 5 | 5.11 | 234 (247) | yes, p. 595 | Hedging via debt indexed to output prices |
| 10 | Exam | Tirole | 5 | 5.7 | 232 (245) | yes, p. 593 | Balance-sheet strength and debt maturity (free cash flow) |
| 11 | Exam | Tirole | 5 | 5.9 | 233 (246) | yes, p. 594 | Uncoordinated lending and short-term bias in maturity |
| 12 | Really hard | Grinblatt–Titman | 22 | 22.12 | 816 (829) | no | Two-factor hedge with zero cash outlay |
| 13 | Really hard | Tirole | 5 | 5.6 | 231 (244) | yes, p. 593 | Continuous effort with a continuum of liquidity shocks |
| 14 | Really hard | Tirole | 5 | 5.10 | 234 (247) | yes, p. 595 | Optimal cutoff for a deepening investment; credit line vs. returning to market |
| 15 | Really hard | Tirole | 5 | 5.8 | 232 (245) | yes, p. 593 | Multistage investment with news about prospects; cutoff rules |

## Tier 1 — Easy

### 1. Can a firm hold too much cash?
**Source:** Ross, Ch. 19, Exercise CQ 19.1 (Revisão de conceitos e questões instigantes 1), p. 690 (PDF 714) · Answer in book: no

Administração de caixa [OA3] É possível que uma empresa tenha muito caixa? Por que os acionistas se importariam se uma empresa acumulasse grandes quantidades de caixa?

---

### 2. Excess cash and agency problems
**Source:** Ross, Ch. 19, Exercise CQ 19.10 (Revisão de conceitos e questões instigantes 10), p. 690 (PDF 714) · Answer in book: no

Problemas de agência [OA3] Às vezes, afirma-se que o caixa excedente retido por uma empresa pode agravar os problemas de agência (discutidos no Capítulo 1) e, de modo geral, reduzir os incentivos para a maximização do valor para o acionista. Como você analisaria essa questão?

---

### 3. Small firms hedge less
**Source:** Grinblatt–Titman, Ch. 21, Exercise 21.1, p. 771 (PDF 784) · Answer in book: no

Small firms currently hedge less than large firms. Why is this? Do you expect smaller firms to start hedging more in the future? Explain.

---

### 4. Partial hedging by oil firms
**Source:** Grinblatt–Titman, Ch. 21, Exercise 21.7, p. 771 (PDF 784) · Answer in book: no

Oil firms hedge only part of their exposure to oil price movements. Why might that be a good idea?

---

### 5. Entering the year with a cash buffer
**Source:** Berk, Ch. 20, Exercise 20.6 (with the shared table for Problems 3–7), p. 613 (PDF 644) · Answer in book: no

The following table includes quarterly working capital levels for your firm for the next year. Use it to answer Problems 3–7.

| (\$000) Quarter | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Cash | \$100 | \$100 | \$100 | \$100 |
| Accounts Receivable | 200 | 100 | 100 | 600 |
| Inventory | 200 | 500 | 900 | 50 |
| Accounts Payable | 100 | 100 | 100 | 100 |

6. If you choose to enter the year with \$400 total in cash, what is your maximum short-term borrowing (see MyFinanceLab for the data in Excel format)?

---

## Tier 2 — Exam level

### 6. Long-term contract and loan commitment
**Source:** Tirole, Ch. 5, Exercise 5.1, p. 229 (PDF 242) · Answer in book: yes, p. 591

Exercise 5.1 (long-term contract and loan commitment). Consider the two-project, two-period version of the fixed-investment model of Section 3.2 and a unit discount factor. Assume, say, that the borrower initially has no equity ($A = 0$). Show the following.

(i) If $p_H(p_HR-I)+(p_HR-I-p_HB/\Delta p) \geqslant 0$, then the optimal long-term contract specifies a loan commitment in which the second-period project is financed at least if the first-period project is successful. Show that if $p_H(p_HR-I)+(p_HR-I-p_HB/\Delta p) > 0$, then the optimal long-term contract specifies that the second-period project is implemented with probability 1 in the case of first-period success, and with probability $\xi \in (0,1)$ in the case of failure.

(ii) In question (i), look at how $\xi$ varies with various parameters.

(iii) Is the contract "renegotiation proof," that is, given the first-period outcome, would the parties want to modify the contract to their mutual advantage?

(iv) Investigate whether the long-term contract outcome can be implemented through a sequence of short-term contracts where the first-period contract specifies that the borrower receives $\bar A = I - p_H(R - B/\Delta p)$ with probability 1 in the case of success and with probability $\xi$ in the case of failure.

*Context: Tirole §3.2, pp. 115–125 (fixed-investment model); §5.2.3, pp. 205–206 (credit lines).*

---

### 7. Credit rationing, predation, and liquidity shocks
**Source:** Tirole, Ch. 5, Exercise 5.2, p. 229 (PDF 242) · Answer in book: yes, p. 591

Exercise 5.2 (credit rationing, predation, and liquidity shocks). (i) Consider the fixed-investment model. An entrepreneur has cash $A$ and can invest $I_1 > A$ in a project. The project's payoff is $R_1$ in the case of success and 0 otherwise. The entrepreneur can work, in which case her private benefit is 0 and the probability of success is $p_H$, or shirk, in which case her private benefit is $B_1$ and the probability of success $p_L$. The project has positive NPV ($p_HR_1 > I_1$), but will not be financed if the contract induces the entrepreneur to shirk. The (expected) rate of return demanded by investors is 0.

What is the threshold value of $A$ such that the project is financed?

In the following, let

$$\rho_0^1 \equiv p_H\left(R_1 - \frac{B_1}{\Delta p}\right).$$

The next three questions add a prior period, period 0, in which the entrepreneur's equity $A$ is determined. The discount factor between dates 0 and 1 is equal to 1.

(ii) In this question, the entrepreneur's date-1 (entire) equity is determined by her date-0 profit. This profit can take one of two values, $a$ or $A$, such that

$$a < I_1 - \rho_0^1 < A.$$

At date 0, the entrepreneur faces a competitor in the product market. The competitor can "prey" or "not prey." The entrepreneur's date-0 profit is $a$ in the case of predation and $A$ in the absence of predation. Preying reduces the competitor's profit at date 0, but by an amount smaller than the competitor's date-1 gain from the entrepreneur's date-1 project not being funded.

- What happens if the entrepreneur waits until date 1 to go to the capital market?
- Can the entrepreneur avoid this outcome? You may want to think about a credit line from a bank. Would such a credit line be credible, that is, would it be renegotiated to the mutual advantage of the entrepreneur and his investors at the end of date 0?

(iii) Forget about the competitor, but keep the assumption that the entrepreneur's date-0 profit can take the same two values, $a$ and $A$. We now introduce a date-0 moral-hazard problem on the entrepreneur's side.

Assume that the entrepreneur's date-0 production involves an investment cost $I_0$ and that the entrepreneur initially has no cash. The entrepreneur can work or shirk at date 0. Working yields no private benefit and probability of profit $A$ equal to $q_H$ (and probability $1-q_H$ of obtaining profit $a$). Shirking yields private benefit $B_0$ to the entrepreneur, but reduces the probability of profit $A$ to $q_L = q_H - \Delta q$ ($0 < q_L < q_H < 1$). Assume that

$$I_1 + I_0 - (q_LA + (1-q_L)a) > \rho_0^1.$$

- Interpret this condition.

Consider the following class of long-term contracts between the entrepreneur and investors. "The date-1 project is financed with probability 1 if the date-0 profit is $A$ and with probability $x < 1$ if this profit is $a$. The entrepreneur receives $R_b = B_1/\Delta p$ if the date-1 project is financed *and* succeeds, and 0 otherwise." Assume that such contracts are not renegotiated.

- What is the optimal probability $x^*$? (Assume that $(\Delta q)p_HB_1 \geqslant (\Delta p)B_0$.)
- Assuming that $\rho_0^1 > I_1$, is the previous contract robust to (a mutually advantageous) renegotiation?

(iv) Show that the entrepreneur cannot raise sufficient funds at date 0 if renegotiation at the end of date 0 cannot be prevented, if $\rho_0^1 > I_1$, and if

$$I_0 + I_1 - (q_HA + (1-q_H)a) > \rho_0^1 - \left(\frac{q_HB_0}{\Delta q}\right).$$

*Context: Tirole §3.2.1, pp. 115–116 (fixed-investment model); §5.2.3, pp. 205–206 (credit lines).*

---

### 8. Liquidity needs and pricing of liquid assets
**Source:** Tirole, Ch. 5, Exercise 5.5, p. 231 (PDF 244) · Answer in book: yes, p. 592

Exercise 5.5 (liquidity needs and pricing of liquid assets). Consider the liquidity-needs model with a *fixed investment* and *two possible liquidity shocks*. The borrower has cash $A$ and wants to finance a fixed-size investment $I > A$ at date 0. At date 1, a cash infusion equal to $\rho$ is needed in order for the project to continue. If $\rho$ is not invested at date 1, the project stops and yields nothing. If $\rho$ is invested, the borrower chooses between working (no private benefit, probability of success $p_H$) and shirking (private benefit $B$, probability of success $p_L = p_H - \Delta p$). The project then yields, at date 2, $R$ in the case of success and 0 in the case of failure.

The liquidity shock is equal to $\rho_L$ with probability $(1-\lambda)$ and to $\rho_H$ with probability $\lambda$, where

$$\rho_L < \rho_0 < \rho_H < \rho_1,$$

where $\rho_1 \equiv p_HR$ and $\rho_0 \equiv p_H(R - B/\Delta p)$. Assume further that

$$\rho_0 - \rho_L > I - A. \tag{1}$$

There is a single liquid asset, Treasury bonds. A Treasury bond yields 1 unit of income for certain at date 1 (and none at dates 0 and 2). It is sold at date 0 at price $q \geqslant 1$. (The investors' rate of time preference is equal to 0.)

(i) Suppose that the firm has the choice between buying enough Treasury bonds to withstand the high liquidity shock and buying none. Show that it chooses to hoard liquidity if

$$(q-1)(\rho_H - \rho_0) \leqslant (1-\lambda)(\rho_0 - \rho_L) - \lambda(\rho_H - \rho_0) - I + A \tag{2}$$

and

$$(q-1)(\rho_H - \rho_0) \leqslant \lambda(\rho_1 - \rho_H). \tag{3}$$

(ii) Suppose that the economy is composed of a continuum, with mass 1, of identical firms with characteristics as described above. The liquidity shocks of the firms are perfectly correlated. There are $T$ Treasury bonds in the economy, with $T < \rho_H - \rho_0$. Show that when $\lambda$ is small, the liquidity premium $(q-1)$ commanded by Treasury bonds is proportional to the probability of a high liquidity shock. (Hint: show that either (2) or (3) must be binding, and use (1) to conclude that (3) is binding.)

(iii) Suppose that, in the economy considered in the previous subquestion, the government issues at date 0 not only the $T$ Treasury bonds, but also a security that yields at date 1 a payoff equal to 1 in the good state (the firms experience liquidity shock $\rho_L$) and 0 in the bad state (the firms experience liquidity shock $\rho_H$). What is the equilibrium date-0 price $q'$ of this new asset? (Prices of the Treasury bonds and of this new asset are market clearing prices.)

*Context: Tirole §5.2.1, pp. 201–204 (liquidity-needs model, fixed investment); §5.3.1, pp. 207–209 (two-shock case).*

---

### 9. Should debt contracts be indexed to output prices?
**Source:** Tirole, Ch. 5, Exercise 5.11, p. 234 (PDF 247) · Answer in book: yes, p. 595

Exercise 5.11 (should debt contracts be indexed to output prices?). This exercise returns to optimal corporate risk management when profits are positively serially correlated (see Section 5.4.2). The source of serial correlation is now a permanent shift in the market price of output, as summarized in Figure 5.15. The model is the fixed-investment model, except that the date-1 and date-2 incomes depend on an exogenous market price $P$, with mean $\bar P$, that is realized at date 1. The realizations of $P$ and $\rho$ are independent.

Figure 5.15 (timing, transcribed):

| Date 0 | Date 1 (if investment) | Date 1–2 (if reinvestment) | Date 2 |
|---|---|---|---|
| Entrepreneur has wealth $A$ and fixed-investment project costing $I > A$. | Short-term income $Pr > 0$. Reinvestment need $\rho$ (drawn from $F(\cdot)$). | Moral hazard ($p = p_H$ or $p_L$). | Success (profit $PR$) with probability $p$, failure (profit 0) with probability $1-p$. |

The rest of the model is otherwise the same as in Section 5.2. Following the steps of Section 5.4.2:

(i) Determine the optimal reinvestment policy $\rho^*(P)$.

(ii) Show that, accounting for seasoned offerings, the optimal debt is fully indexed debt:

$$d(P) = Pr - \ell_0,$$

where $\ell_0$ is a positive constant.

*Context: Tirole §5.2, pp. 201–207 (liquidity-needs model); §5.4.2, pp. 216–220 (incomplete hedging with serially correlated profits).*

---

### 10. Decreasing returns to scale and debt maturity
**Source:** Tirole, Ch. 5, Exercise 5.7, p. 232 (PDF 245) · Answer in book: yes, p. 593

Exercise 5.7 (decreasing returns to scale). Extend the treatment of Section 5.6.1 to the case of decreasing returns to scale: the payoff in the case of continuation and success is $R(I)$, with $R(0) = 0$, $R' > 0$, $R'' < 0$, $R'(0) = \infty$, and $R'(\infty) = 0$. The rest is unchanged (the short-term income is $rI$, the reinvestment need is $\rho I$, and the private benefit is $BI$).

(i) What are the first-order conditions yielding the optimal investment level $I$ and cutoff $\rho^*$?

(ii) Assuming that $r > \rho^*$, and that $(R(I)/I - R'(I))$ is increasing in $I$ (a condition satisfied, for example, by $R(I)$ quadratic), derive the impact of the strength of the balance sheet as measured, say, by $A$ on debt maturity.

*Context: Tirole §5.6.1, pp. 226–227 (free cash flow and optimal claim maturity).*

---

### 11. The priority game: uncoordinated lending and short-term bias
**Source:** Tirole, Ch. 5, Exercise 5.9, p. 233 (PDF 246) · Answer in book: yes, p. 594

Exercise 5.9 (the priority game: uncoordinated lending leads to a short-term bias). This chapter, like Chapters 3 and 4, has assumed that the firm's balance sheet is transparent. In particular, each investor has perfect knowledge of loans made by other lenders and of the firm's obligations to them.

This exercise argues that uncoordinated lending leads to financing that is too oriented to the short term. In a nutshell, lenders, by cashing out early, exert a negative externality on other lenders. Because this externality is not internalized, the resulting financial structure contains too much short-term debt.

We consider a three-period model: $t = 0, 1, 2$. The entrepreneur has no cash ($A = 0$), is risk neutral, and is protected by limited liability. At date 0, a fixed investment $I$ is made. The project yields a known return $r > 0$ at date 1, and an uncertain return ($R$ or 0) at date 2. Because the point is quite general and does not require credit constraints, we assume away moral hazard; or, equivalently, the private benefit from misbehaving is 0. The probability of a date 2 success is

$$p + \tau(I_1),$$

where $I_1$ is the date-1 deepening investment, equal to $r$ minus the level of short-term debt repaid to lenders and the date-1 payment to the entrepreneur (the firm does not return to the capital market at date 1), and $\tau$ is an increasing and concave function (with $\tau'(0) = \infty$). Assume that $\tau'(r)R < 1$.

We assume that the entrepreneur cannot engage in "fraud," that is, cannot fail to honor the short-term debt and, if the project succeeds at date 2, the long-term debt. By contrast, obligations to lenders, and in particular $I_1$, cannot be verified as the firm's balance sheet is opaque.

(i) Derive the first-best investment $I_1^*$. Show how this allocation can be implemented by a mixture of short- and long-term debt (note that in this model without moral hazard the structure of compensation for the entrepreneur exhibits a degree of indeterminacy).

(ii) Assume that $r - I_1^* < I$ (creditors must hold long-term debt). Suppose next that financing is not transparent. Start from the first-best solution, with a large number (a continuum of mass 1) of lenders, with the representative lender owning short-term claim $r_l$ and contingent long-term claim $R_l$ on the firm.

Show that the entrepreneur has an incentive to secretly collude with any lender to increase the latter's short-term claim in exchange for a smaller long-term claim.

Given the constraint that financing is provided by many lenders and that the latter do not observe each other's contracts, is the indeterminacy mentioned in question (i) resolved?

---

## Tier 3 — Really hard

### 12. Two-factor hedge with no cash outlay
**Source:** Grinblatt–Titman, Ch. 22, Exercise 22.12, p. 816 (PDF 829) · Answer in book: no

Consider a two-factor model, where the factors are interest rate movements and changes in the exchange rate. Your company has a future cash flow with factor betas of 2 on the interest rate factor and 5 on the exchange rate factor. You would like to eliminate your sensitivity to both of these factors by means of financial securities, but do not wish to use any of the company's cash to do this.

The following investment opportunities are available to you.

- You can purchase 30-year government bonds.
- You can enter into a 2-year interest rate swap agreement.
- You can invest in a foreign index fund.

The following factor equations, with the two factors being changes in interest rates and changes in exchange rates, correspond to the future values of the three investment opportunities, respectively.

$$
\begin{aligned}
\tilde C_1 &= 4 - 4\tilde F_{\text{int}} && \text{(per \$1 million invested)}\\
\tilde C_2 &= 6 - 2\tilde F_{\text{int}} + 6\tilde F_{\text{ex}} && \text{(per \$1 million invested)}\\
\tilde C_3 &= 3 - 3\tilde F_{\text{int}} - 2\tilde F_{\text{ex}} && \text{(per \$1 million invested)}
\end{aligned}
$$

Design a proper hedge against interest rate movements and exchange rates in this environment.

---

### 13. Continuous entrepreneurial effort and liquidity needs
**Source:** Tirole, Ch. 5, Exercise 5.6, p. 231 (PDF 244) · Answer in book: yes, p. 593

Exercise 5.6 (continuous entrepreneurial effort; liquidity needs). (i) An entrepreneur with initial cash $A$ and protected by limited liability wants to invest in a fixed-size project with investment cost $I > A$. After the investment is made, the entrepreneur chooses the probability $p$ of success ($0 \leqslant p \leqslant 1$); the disutility of effort is $g(p) = \frac{1}{2}p^2$. (The entrepreneur enjoys no private benefit in this model.) In question (i) only, the profit is $R = 2\sqrt{I - A}$ in the case of success and 0 in the case of failure. (We assume that $R < 1$ to avoid considering probabilities of success exceeding 1. $R$ takes an arbitrary value in question (ii).) As usual, the uninformed investors demand an expected rate of interest equal to 0 and everyone is risk neutral. Let $R_b$ denote the entrepreneur's reward in the case of success.

Solve for the optimal contract ($R_b$). Show that

$$R_b = \tfrac{1}{2}R.$$

(ii) Now introduce an intermediate liquidity shock $\rho$ (for a now arbitrary level $A$ of cash on hand). The cumulative distribution of $\rho$ is $F(\rho)$ on $[0, \infty)$ and the density $f(\rho)$. The effort decision is made *after* the value of $\rho$ is realized and, of course, *conditional* on the choice of continuing (incurring reinvestment cost $\rho$). *Suppose* that the entrepreneur's stake in the case of continuation ($R_b$) is independent of $\rho$. Write the investors' breakeven condition. Write the optimization program yielding ($R_b, \rho^*$), where $\rho^*$ is the cutoff liquidity shock.

*Context: Tirole §5.2.1, pp. 201–204 (liquidity shock and continuation cutoff).*

---

### 14. Liquidity and deepening investment
**Source:** Tirole, Ch. 5, Exercise 5.10, p. 234 (PDF 247) · Answer in book: yes, p. 595

Exercise 5.10 (liquidity and deepening investment). (i) Consider the fixed-investment model. The entrepreneur has cash $A$ and can invest $I > A$ in a project. The project's return in the case of success (respectively, failure) is $R$ (respectively, 0). The probability of success is $p_H$ if the entrepreneur behaves (she then gets no private benefit) and $p_L = p_H - \Delta p$ if she misbehaves (in which case she gets private benefit $B$). In this subquestion and in the subsequent extension, one will assume that the project is viable only if the incentive scheme induces the entrepreneur to behave. The entrepreneur and the capital market are risk neutral; the entrepreneur is protected by limited liability; and the market rate of interest is equal to 0.

Let

$$\rho_1 \equiv p_HR \quad \text{and} \quad \rho_0 \equiv p_H[R - B/\Delta p],$$

and assume $\rho_1 > I > \rho_0$.

What is the necessary and sufficient condition for the project to be financed?

(ii) Now add an intermediate stage, in which there is an option to make a deepening investment. This investment increases the probability of success to $p_H + \tau$ (in the case of good behavior) and $p_L + \tau$ (in the case of misbehavior).

If the deepening investment is not made, the probabilities of success remain $p_H$ and $p_L$, respectively. This deepening investment costs $\rho$, where $\rho$ is unknown *ex ante* and distributed according to distribution $F(\rho)$ and density $f(\rho)$ on $[0, \infty)$. The timing is summarized in Figure 5.14.

Figure 5.14 (timing, transcribed):

| Date 0 | Date 1 | Date 1–2 | Date 2 |
|---|---|---|---|
| Entrepreneur has wealth $A$ and fixed-size investment project $I$. | $\rho$ is realized. Reinvesting $\rho$ raises probabilities of success to $p_\cdot + \tau$. | Moral hazard. | Outcome ($R$ or 0). |

Let $\mu \equiv \tau/p_H$, $\hat\rho_1 \equiv \mu\rho_1$, and $\hat\rho_0 \equiv \mu\rho_0$.

Write the incentive compatibility constraint and (for a given cutoff $\rho^*$) the investors' breakeven condition.

(iii) What is the optimal cutoff $\rho^*$? (Hint: consider three cases, depending on whether

$$\rho_0[1 + \mu F(\hat\rho_k)] \lessgtr I - A + \int_0^{\hat\rho_k} \rho f(\rho)\,\mathrm{d}\rho,$$

with $k = 0, 1$.)

(iv) Should the firm content itself with returning to the capital market at date 1 in order to finance the deepening investment (if any)?

*Context: Tirole §3.2.1, pp. 115–116 (fixed-investment model); §5.2.1, pp. 201–204 (cutoff rule); §5.2.4, pp. 206–207 (reinvestment that raises growth prospects).*

---

### 15. Multistage investment with interim news about prospects
**Source:** Tirole, Ch. 5, Exercise 5.8, p. 232 (PDF 245) · Answer in book: yes, p. 593

Exercise 5.8 (multistage investment with interim accrual of information about prospects). In this chapter we have focused mostly on the case of shocks about the reinvestment need (cost overruns, say). Consider, instead, the case of news about the final profitability. In the two-outcome framework, news can accrue about either the probability of success or the payoff in the case of success. We consider both, in sequence. The investment is a multistage one: let

$$I = I_0 + I_1,$$

where $I_0$ is the date-0 investment and $I_1$ is the date-1 reinvestment. In contrast with $I_0$, $I_1$ is not incurred if the firm decides to stop. The timing is as in Figure 5.12.

Figure 5.12 (timing, transcribed): Date 0 — entrepreneur and investors contract, and sink $I_0$. Date 1 — news about date-2 prospect accrues (publicly); then either stop (no liquidation value) or invest $I_1$, followed by moral hazard. Date 2 — outcome: success ($R$) or failure (0).

| | Pr (success) | Private benefit |
|---|---|---|
| Behaves | $p_H + \tau$ | 0 |
| Misbehaves | $p_L + \tau$ | $B$ |

As usual, the entrepreneur has initial wealth $A$, is risk neutral, and protected by limited liability. Investors are risk neutral. The discount rate is equal to 0. If reinvestment cost $I_1$ is sunk at date 1, then the firm can continue. Misbehavior reduces the probability of success by $\Delta p$, but yields private benefit $B$ to the entrepreneur.

Assume

$$B < (\Delta p)R.$$

As announced, we consider two variants.

(a) *News about the probability of success.* $R$ is known at date 0, but the probability of success is $p_H + \tau$ in the case of good behavior and $p_L + \tau$ in the case of misbehavior, where $\tau$ is publicly learned at the beginning of date 1. The random variable $\tau$ is distributed according to the distribution function $F(\tau)$ with density $f(\tau)$ on $[\underline{\tau}, \bar\tau] = [-p_L, 1 - p_H]$ (to keep probabilities in the interval $[0, 1]$). Let $\tau^e$ denote the expectation of $\tau$.

(b) *News about the payoff in the case of success.* The probabilities of success are known: $p_H$ and $p_L$ (normalize: $\tau = 0$). By contrast, the profit $R$ in the case of success is drawn from distribution $G(R)$ with density $g(R)$ on $(0, \infty)$. (The profit in the case of failure is always equal to 0.)

(i) For each variant, show that there exist two thresholds, $A_0$ and $A_1$, $A_0 < A_1$, such that the first best prevails for $A \geqslant A_1$ and financing is secured if and only if $A \geqslant A_0$. Show that the continuation rules take the form of cutoffs, as described in Figure 5.13. Determine $\tau_0^*, \tau_1^*, R_0^*, R_1^*$.

Figure 5.13 (transcribed): panel (a) plots the cutoff $\tau^*$ against $A$ — equal to $\tau_0^*$ at $A_0$, decreasing until it reaches $\tau_1^*$ at $A_1$, and flat at $\tau_1^*$ beyond $A_1$; panel (b) plots the cutoff $R^*$ the same way, from $R_0^*$ at $A_0$ down to $R_1^*$ at $A_1$.

(ii) For each variant, assume that $A = A_0$. Let $y \equiv (p_H + \tau)R$ denote the expected income, and $\mathcal{R}(y)$ denote the entrepreneur's rent in the case of continuation. Show that (above the threshold $y^*$)

- $0 < \mathcal{R}'(y) < 1$ in variant (a);
- $\mathcal{R}$ is constant in variant (b).

*Context: Tirole §5.2.1, pp. 201–204 (continuation cutoffs).*
