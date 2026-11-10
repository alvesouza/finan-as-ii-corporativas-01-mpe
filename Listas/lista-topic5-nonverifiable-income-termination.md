---
tags: [exercise-list, lecture-topic5, nonverifiable-income, strategic-default, termination, debt-structure]
date: 2026-11-10
---

# Exercise list — Topic 5: Nonverifiable income, strategic default, the threat of termination, and debt structure

One list for Prof. Ricca's Topic 5 lecture (`Aula/Topic_5.pdf`, mapped in [[Map/lectures-index|lectures-index]]): income the lender cannot verify, strategic versus liquidity default, the termination threat that makes repayment credible, and — from the book sections the lecture's model comes from (Amaro de Matos §5.1–5.2, Tirole §3.8 and §7.1.2) — renegotiation, the number of creditors and debt maturity. 13 real exercises ordered easy → really hard, copied verbatim from the course books for personal study; pages are printed, with the PDF page in brackets. The course books have fewer than 15 exercises on this material, and **none on the sovereign-debt model** (Eaton–Gersovitz, Arellano; slides 13–29). Blocks 3, 8, 9, 10 and 13 are taken unchanged from lists R6 and R7; the others are new; all pass `tools/check_lists.py`. Links: [[Map/exercises-index|exercise index]] · [[rules/04_agencia_estrutura_governanca|rules]] · [[Listas/lista-r7-lectures-3-5|R7]] · [[Listas/lista-r6-liquidity-risk-management|R6]].

| Lecture block or book complement | Exercises |
|---|---|
| 5.1 Nonverifiable income, control in default | 1 |
| 5.2 Threat of termination (continuation probability, liquidation) | 3, 6, 7 |
| Renegotiation and bankruptcy design (slide 12; Amaro de Matos §5.1) | 4, 13 |
| One vs. many creditors (Amaro de Matos §5.2.2) | 10 |
| Debt maturity (Amaro de Matos §5.2.3, Diamond 1991; Tirole Ch. 5) | 2, 5, 8, 9, 11, 12 |

## References

| # | Tier | Book | Ch. | Exercise | Printed p. (PDF) | Answer in book | Trains | From |
|---|---|---|---|---|---|---|---|---|
| 1 | Easy | Grinblatt & Titman 2e | Ch. 16 | 16.10 | 593 (606) | no | Shift of control to creditors in bankruptcy: how debt holders' and equity holders' preferences differ and how decisions change | new |
| 2 | Easy | Amaro de Matos | Ch. 5 | 5.2.5 #3 | 148 (166) | yes, p. 268 | Diamond (1991): pricing one-period debt, face value $r_1$ from the lenders' expected return over upgrade and downgrade states | new |
| 3 | Exam | Amaro de Matos | Ch. 5 | 5.2.5 #1 | 148 (166) | yes, p. 267 | Comparative statics of the optimal liquidation probability $\beta_\circ$ in (5.8) with respect to $q$ | R7 ex. 13 |
| 4 | Exam | Amaro de Matos | Ch. 5 | 5.1.6 #3 | 134 (152) | yes, p. 266 | Aghion–Bolton entrepreneur control with $t_s < \hat t$: renegotiation toward $a_b$ in $\theta_b$ raises the entrepreneur's expected payoff | new |
| 5 | Exam | Amaro de Matos | Ch. 5 | 5.2.5 #5 | 148 (166) | no (p. 268 only cites example 1 of Diamond 1991, pp. 716–717) | Diamond (1991) numerical case without liquidation: face values, downgrade probability, payoffs under short- vs. long-term debt | new |
| 6 | Exam | Tirole | Ch. 7 | 7.7 | 325 (338) | yes, pp. 603–604 | Bolton–Scharfstein predation deterrence with general rewards: generalized (PD) and (IC), $r_b^S = 0$, $R_b^{SS} \geqslant R_b^{FS}$ | new |
| 7 | Exam | Tirole | Ch. 3 | 3.14 | 149–150 (162) | yes, pp. 577–578 | Privately observed signal and liquidation: truth-telling constraint raises the financing threshold by $\underline{\gamma}B/[(\Delta p)(\Delta\gamma)]$ | new |
| 8 | Exam | Tirole | Ch. 5 | 5.7 | 232 (245) | yes, p. 593 | Balance-sheet strength and debt maturity (free cash flow) | R6 ex. 10 |
| 9 | Exam | Tirole | Ch. 5 | 5.9 | 233 (246) | yes, p. 594 | Uncoordinated lending and short-term bias in maturity | R6 ex. 11 |
| 10 | Really hard | Amaro de Matos | Ch. 5 | 5.2.5 #2 | 148 (166) | no (p. 268 only cites Bolton and Scharfstein 1996, pp. 10–13) | Number of creditors: higher payoff $y - S$ in strategic default, lower $\overline{L}_\circ$ in liquidity default | R7 ex. 15 |
| 11 | Really hard | Amaro de Matos | Ch. 5 | 5.2.5 #4 | 148 (166) | no (p. 268 only cites the appendix of Diamond 1991, pp. 732–733) | Diamond (1991): proving that $(q^dX + f^dC)/R \le L$ makes the good entrepreneur prefer the liquidating debt structure | new |
| 12 | Really hard | Amaro de Matos | Ch. 5 | 5.2.5 #6 (with #5 as Part 0) | 148 (166) | no (p. 268 only cites examples 2 and 3 of Diamond 1991, pp. 717–719) | Diamond (1991) with control rents: liquidation after a downgrade, preference for long-term debt, reversal at $f = 3/4$ | new |
| 13 | Really hard | Tirole | Ch. 4 | 4.9 | 190–191 (203) | yes, p. 586 | Optimal continuation cutoff $r^*$ as short-term debt; why a borrower-friendly court hurts the borrower | R7 ex. 18 |

## Tier 1 — Easy

### 1. Control passing to creditors
**Source:** Grinblatt & Titman, Ch. 16, Exercise 16.10, p. 593 (PDF 606) · Answer in book: no

16.10. In the event of bankruptcy, the control of a firm passes from the equity holders to the debt holders. Describe differences in the preferences of the equity holders and debt holders and how decisions following bankruptcy proceedings are likely to change.

---

### 2. Duration of debt: proving (5.11)
**Source:** Amaro de Matos, Ch. 5, Exercise 5.2.5 #3, p. 148 (PDF 166) · Answer in book: yes, p. 268

3. Prove equation (5.11).

#### Context needed to solve it

*From Amaro de Matos §5.2.3 "The Choice of the Duration", pp. 139–141 (PDF 157–159):*

A model developed by Diamond (1991, 1993) illustrates in a very simple way the differences between short-term and long-term debt financing. The model is based on information asymmetry and credit rating.

Regaining the notation of Aghion and Bolton, consider an entrepreneur with a two-period project who needs funds for an initial investment $K = 1$. The project may be of one of two types: good or bad. At time $t = 2$ a good project has a payoff $X > 0$, whereas a bad project pays that amount with a probability $\pi$, and pays zero with probability $1 - \pi$. Let $\theta$ denote the type of project, $\theta_g$ referring to a good project and $\theta_b$ referring to a bad project. The quality of the project is known to the entrepreneur but not to the investor. Given a project, as of date $t = 0$ the investor assigns a probability $f$ that $\theta = \theta_g$. This probability is referred to as a *credit rating* and reflects the lender's information about the project. It follows that, as of time 0, the probability $q$ that a borrower pays the loan at date $t = 2$ is given by

$$q \equiv f + \pi(1 - f) = \pi + f(1 - \pi). \qquad (5.9)$$

At time $t = 1$ information about the project becomes available to the investor. This new information is not verifiable, so it makes no sense to write contracts contingent upon that information, since they cannot be enforced. However, the investors update their beliefs about the quality of the project and the credit rating will be either upgraded or downgraded.

Under this revision of the credit rating, let $f^u$ denote the probability that $\theta = \theta_g$ given an upgrade and let $f^d$ denote the probability that $\theta = \theta_g$ given a downgrade. In that case, the probability that an entrepreneur who receives a downgrade repays at time $t = 2$ is

$$q^d = \pi + f^d(1 - \pi) > f^d. \qquad (5.10)$$

Moreover, it is here assumed that

$$f^d < f < f^u,$$

meaning that the probability that the project is good is greater given an upgrade than given a downgrade. Furthermore, the simplifying assumption $f^u = 1$ is also made. Thus, given an upgrade at date $t = 1$, it is certain that the project is good. However, it is not certain that all projects of good quality are upgraded. There is room for one such project to be downgraded. Let $e$ denote the probability of such an event.

All projects are also assumed to produce a nonassignable control rent $C$ if the management has control at time $t = 2$. Also, if at time $t = 1$ the manager defaults on short-term debt, lenders then have the right to remove the management from control, selling the assets for a liquidation value $L < K = 1$. All projects may be liquidated at that point in time, under those conditions. If the project is liquidated, the entrepreneur is prevented from consumption of his/her present or future cash flows and control rents. In this case, an optimal contract is a debt contract enforced by the right to liquidate the project if the debt is not repaid in full.

Just as in the case of the borrowers, lenders are assumed be risk neutral. Moreover, lenders have alternative investments at $t = 0$ that provide a return $R$ at $t = 2$. The condition $L < X/R$ ensures that a good project yields a higher return when not liquidated.

A project may be financed with either long-term or short-term debt. In the context of this model, long-term debt refers to a contract issued at $t = 0$ with no refinancing at date $t = 1$ and maturing at $t = 2$. If one such instrument provides $K = 1$ at time $t = 0$ with face value $\rho \le X$, the lender expects to receive at maturity $\rho[\pi + f(1 - \pi)] = R^2$. Notice that if $\rho > X$, a borrower with credit rating $f$ will not be able to provide the lender with the required rate of return $R^2$. Now, if the project is upgraded at time $t = 1$, the market value of the debt contract at that point in time becomes $V_l^u = \rho/R$. Similarly, if the project is downgraded, the market value of debt at time $t = 1$ becomes $V_l^d = q^d\rho/R$.

Short-term debt, on the other hand, is debt financed at $t = 0$ with face value $r_1$ and maturity at time $t = 1$. If short-term borrowers are upgraded at $t = 1$, their debt contract at that point in time is worth $V_s^u = r_1$ and they may refinance their project by issuing a new short-term debt contract with maturity at $t = 2$ and face value $r_1 R$ that will be paid with certainty and guarantees a return of $R$ per unit invested by the lender. If short-term borrowers are downgraded, however, in principle they may refinance their debt with a new short-term contract only if $q^d X/R > r_1$, since $X$ is the maximum that a borrower can pay at $t = 2$. If that is the case, at $t = 1$ the market value of the short-term debt issued at $t = 0$ would be $V_s^d = r_1$ if the borrower pays, possibly through the refinancement mechanism. But what happens if $q^d X/R < r_1$? In that case there is still room for a refinancement provided that the liquidation value $L$ is less than the expected value to the lender from a refinancement, $q^d X/R$. Under a downgrading, the time $t = 1$ value of the short-term debt is thus

$$V_s^d = \min\left[r_1, \max(L, q^d X/R)\right].$$

The face value of short-term debt is established such as to provide the lenders with an expected return of $R$ per period. It then follows that

$$r_1 = \frac{R - [1 - (1 - e)f]V_s^d}{(1 - e)f}. \qquad (5.11)$$


## Tier 2 — Exam level

### 3. Threat of termination: continuation probability
**Source:** Amaro de Matos, Ch. 5, Exercise 5.2.5 #1, p. 148 (PDF 166) · Answer in book: yes, p. 267

1. Show that in the optimal debt contract, the probability $\beta_\circ$ defined in (5.8) decreases as $q$ increases as stated in the text.

#### Context needed to solve it

*From Amaro de Matos §5.2.1 "Extending the Model", pp. 134–137 (PDF 152–155):*

As before, all the agents are risk neutral and the risk-free rate is assumed to be zero. The time schedule refers to a two-period model and is characterized as follows: At time $t = 0$ an amount $K$ is invested in the project. The entrepreneur, as before, is assumed to have no initial wealth. In this specification of the model, the state of nature is characterized by the cash flow at $t = 1$. It may be $\theta_g = x$ with probability $q$ and $\theta_b = 0$ with probability $1 - q$. The cash flow is observable for both the investor and the entrepreneur, but not for any third party, and is thus not verifiable. Therefore, as before, a contract between the investor and the entrepreneur is incomplete.

The manager is assumed to have the ability to divert cash flow without the control of the investor. In that case a zero payoff would be declared at $t = 1$ when the actual payoff was $x$. If the declared cash flow at $t = 1$ is $x$, the contract states a payment of $R_x$ to the creditholder and, with probability $\beta_x$, the right of the creditholder to liquidate a part of the assets that is worth $L_x$. If the cash flow is null, the values are, respectively, $R_\circ$, $\beta_\circ$, and $L_\circ$.

Notice that taking $\beta_x = 0$, $\beta_\circ = 1$, and $L_x = L_\circ$, being equal to the value of the assets of the project at time $t = 1$, this reduces to a usual debt contract with face value $R_x < x$ and one-period maturity. The issue in designing a contract is to find the optimal values for the preceding parameters. Therefore, it is possible in this simple setting to analyze the conditions under which a debt contract would result as optimal.

In the second period, two things may happen. Either the manager continues the project or the project is liquidated, in the sense that it is separated from the manager. If the manager's activity continues, the cash flow at time $t = 2$ is $y$. In the case of no liquidation, the project thus has a net present value of $qx + y - K$.

The expected return to the firm is then written as

$$\pi_f = q[x - R_x + (1 - \beta_x)y] + (1 - q)[-R_\circ + (1 - \beta_\circ)y]. \qquad (5.3)$$

On the other hand, the investor expects to get

$$\pi_i = q[R_x + \beta_x L_x] + (1 - q)[R_\circ + \beta_\circ L_\circ] - K. \qquad (5.4)$$

Suppose for a moment that at time $t = 1$ the cash flow is $x$. The expected return to the firm would then be $x - R_x + (1 - \beta_x)y$, decomposed as follows: The cash flow $x$ goes to the entrepreneur, who has to pay $R_x$ to the investor. With probability $\beta_x$ the project is liquidated at date $t = 1$, leading to a continuation value of zero, and with probability $1 - \beta_x$ the project continues until time $t = 2$, generating a cash flow $y$ at that point. If, however, the manager hides from the outer investor the cash flow $x$, then only $R_\circ$ will be paid at time $t = 1$, and liquidation occurs with probability $\beta_\circ$, leaving to the firm a possible payoff $S$, not necessarily zero, as before. This happens because the liquidation value $L_\circ$ does not correspond to the true value of the assets in that state of nature. In that case the expected return to the firm is $x - R_\circ + \beta_\circ S + (1 - \beta_\circ)y$.

For the manager to be induced to pay the due $R_x$ when the cash flow is $x$, one must therefore impose

$$x - R_x + (1 - \beta_x)y \geq x - R_\circ + \beta_\circ S + (1 - \beta_\circ)y. \qquad (5.5)$$

Noticing that $R_\circ = \beta_x = 0$ is optimal in the sense that these values maximize the profit to the firm and facilitates the verification of (5.5), the preceding inequality reads

$$R_x \leq \beta_\circ(y - S).$$

Among all these possible values for $R_x$ that ensure a trustworthy behavior from the manager of the project, any investor would maximize its expected return by choosing the greatest value. Thus, at the optimum, this restriction is binding. Substituting the optimal values of the parameters in expression (5.4) for the expected result of the investor, one gets

$$\pi_i = \beta_\circ[q(y - S) + (1 - q)L_\circ] - K. \qquad (5.6)$$

Using the optimal values of the parameters, namely those minimizing the profit to the investor, in the profit of the firm (5.3), it follows that

$$\pi_f = (qx + y - K) - (1 - q)\beta_\circ(y - L_\circ). \qquad (5.7)$$

This result can be interpreted as the net present value of the project in the absence of liquidation minus a cost due to contract incompleteness.

For the profit in (5.6) to be positive, ensuring the minimum condition of feasibility of the contract, one must have

$$1 \geq \beta_\circ \geq \frac{K}{q(y - S) + (1 - q)L_\circ},$$

where the first inequality comes from the fact that $\beta_\circ$ is a probability and the second inequality comes from the condition $\pi_i \geq 0$. Notice that $\pi_f$ is decreasing in $\beta_\circ$ whereas $\pi_i$ is monotonically increasing in that parameter. Maximizing the expected return to the firm conditioned to a positive expected return to the investor defines the optimal value of $\beta_\circ$ as the lowest possible. Thus

$$\beta_\circ = \frac{K}{q(y - S) + (1 - q)L_\circ}.$$

Both $S$ and $L_\circ$ (and thus also $\beta_\circ$) are still to be specified. There is no need to specify $L_x$, since the main feature of the optimal contract just described is that there is no liquidation in the good state. Liquidation occurs only, if at all, in the case of a poor performance. In order to understand what determines $S$ and $L_\circ$ some additional assumptions are required.

It is assumed that the entrepreneur is not able to continue managing the project in the case of bankruptcy after a zero cash flow. This is the case of a *liquidity default*. In that case, the creditor may sell the position to a third party who obtains at $t = 2$ a cash flow $\alpha y$, with $\alpha \in [0, 1]$, meaning that the incoming manager cannot get better results out of the assets than the manager who left the firm.

In the case of bankruptcy after a nonzero cash flow, the original manager will negotiate the buyback of the firm with the creditholder, sharing the second-period return $y$. In that situation, $S = y/2$. This is the case of a *strategic default*.

It is also assumed that, in the case of liquidity default, the buyer of the assets incurs an informational cost $c \in [0, \bar c]$. This cost is modeled as a uniformly distributed random variable. Therefore, by a negotiating process similar to the preceding, the remaining value of the assets, $\alpha y$, is equally divided between the creditor and the buyer. The buyer then negotiates only if $c \leq \alpha y/2$. Thus, assuming that $\alpha y/2 \leq \bar c$, the probability that this happens is

$$\Pr\left(c \leq \frac{\alpha y}{2}\right) = \frac{\alpha y}{2\bar c}.$$

Therefore, the expected value of the liquidation payoff in the case of a zero cash flow at $t = 1$ is

$$L_\circ = \frac{\alpha^2 y^2}{4\bar c},$$

and the optimal $\beta_\circ$ reads

$$\beta_\circ = \frac{K}{q\frac{y}{2} + (1 - q)\frac{\alpha^2 y^2}{4\bar c}}. \qquad (5.8)$$

It follows³ that the optimal value of $\beta_\circ$ decreases as $q$ increases. Thus, the probability of liquidation of assets decreases as the probability of positive cash flow increases. Thus, the inefficiency due to contract incompleteness, expressed in (5.7) as $(1 - q)\beta_\circ(y - L_\circ)$, is lower for higher $q$, or, in other words, with lower risk of bankruptcy.

*From Amaro de Matos, Notes to Chapter Five, note 3:*

3. This is left as an exercise.

---

### 4. Entrepreneur control and renegotiation
**Source:** Amaro de Matos, Ch. 5, Exercise 5.1.6 #3, p. 134 (PDF 152) · Answer in book: yes, p. 266

3. Under entrepreneur control, show that the renegotiation of the contract whenever $t_s < \hat t$ for $s = 0, 1$ leads to an increase in the expected payoff of the entrepreneur.

#### Context needed to solve it

*From Amaro de Matos §5.1.1 "The Model", pp. 127–129 (PDF 145–147):*

The relationship between incomplete financial contracts and the allocation of control in a firm may be discussed within a simple analytical context, as in the paper of Aghion and Bolton (1992). This section discusses their model, where a bilateral contract is considered between an entrepreneur having no initial wealth and an investor who has the resources to invest the amount $K$ at $t = 0$. This is a model with three points in time characterizing the following dynamic setting:

At $t = 1$, the state of nature $\theta$ is revealed. This state may be either good ($\theta_g$) with probability $q$ or bad ($\theta_b$) with probability $1 - q$. Finally, at $t = 2$, the result of the investment is obtained, expressed as a rate of return $r$. After the realization of the state of nature at $t = 1$ and before the maturity of the contract at $t = 2$, an action $a$ is undertaken by one of the agents, either the investor or the entrepreneur. The decision about who takes the action is to be contracted at $t = 0$. The agent who chooses the action is said to be the one who owns the project or who retains control.

The action $a$ and the state of nature $\theta$ are determining elements of the stochastic return $r$. An action is said to be optimal if it maximizes the expected wealth conditional to a given state of nature. Let $a_g$ denote the optimal action under the state of nature $\theta_g$ and let $a_b$ denote the optimal action under the state of nature $\theta_b$.

The model follows the idea of Grossman and Hart (1986) that incomplete contracts are characterized by the fact that the state of nature is impossible or very costly to describe ex-ante and, therefore, the ex-ante contract cannot be contingent on the state $\theta$. Unlike Grossman and Hart (1986), however, it is assumed here that at $t = 1$ there is a publicly verifiable signal $s \in \{0, 1\}$ that is correlated with the state of nature $\theta$ and that the contract may be contingent on $s$. One then defines the two conditional probabilities

$$\beta_g = \text{Prob}(s = 1 \mid \theta = \theta_g) > 1/2$$
$$\beta_b = \text{Prob}(s = 1 \mid \theta = \theta_b) < 1/2.$$

Note that $\beta_g = 1$ and $\beta_b = 0$ imply that the public signal $s$ is a perfect proxy for $\theta$. In other words, one may infer $\theta$ directly from the observable signal $s$, and thus the contract is no longer incomplete. For a contract to be incomplete, either $\beta_g$ is at a certain distance from 1 or $\beta_b$ is away from zero, or both situations occur. One may then use the sum of these two distances, namely,

$$d = |\beta_g - 1| + \beta_b, \qquad (5.1)$$

as a measure of the degree of incompleteness of the contract.

The entrepreneur (E) and the investor (I) are assumed to be risk neutral in income and to have utility functions given, respectively, by

$$U_E(r, a) = g(r) + l(a, \theta)$$
$$U_I(r, a) = r - g(r),$$

where $l(a, \theta)$ is part of the total payoff of the entrepreneur that, although depending on the action undertaken and on the state of nature, is nonmonetary and not observable by third parties. Therefore, this term is taken as reflecting the *private benefits* for the entrepreneur.

It is also assumed that the stochastic return at $t = 2$ may take only two values: $r = 1$ or $r = 0$. As described previously, the stochastic return depends on both the state of nature $\theta$ and on the undertaken action $a$. Define $y^i_j$ as

$$y^i_j = E\left[r \mid \theta = \theta_i;\ a = a_j\right].$$

In other words, $y^i_j$ is the expected rate of return given that the state of nature is $\theta_i$ and the action undertaken is $a_j$. Under the same state of nature and action, let the private benefit to the entrepreneur be denoted by $l^i_j$. Then, for the project to be feasible from the point of view of the investor, one must have a positive net present value for the project,

$$q y^g_g + (1 - q) y^b_b > K.$$

Also, the optimality of $a_g$ and $a_b$ is assumed to be expressed as

$$y^g_g + l^g_g > y^g_b + l^g_b$$
$$y^b_b + l^b_b > y^b_g + l^b_g.$$

Finally, it is assumed that the entrepreneur is compensated with a positive monetary transfer schedule $g(r) = t(s, r)$, which is a function of the first-time-period public signal, revealing information about the state of nature and also the function of the return of the project at the end of the second period. Given that $r$ can take only the values 0 and 1, with no loss of generality, this implies that the schedule $t(s, r)$ is composed of a fixed part and a variable part, proportional to $r$:

$$t(s, r) = t_s r + t'_s \geq 0, \qquad (5.2)$$

where $t_s$ and $t'_s$ are constants. All residual returns go to the investor. Hence, if each one of the agents could choose the action to be taken maximizing his/her utilitiy, then the entrepreneur would maximize $t_s y^i_j + t'_s + l^i_j$ and the investor would maximize $(1 - t_s) y^i_j - t'_s$. The problem to be discussed within this model is the following: How does the structure presented induce the agents to settle an ex-ante agreement on who should decide which action should be taken after the state of nature is revealed? Is there room for renegotiation of the contract once the state of the world is revealed, but before the action is undertaken?

*From Amaro de Matos §5.1.2 "Entrepreneur Control", pp. 129–131 (PDF 147–149):*

In this section, the case where the entrepreneur has full control is studied. This means that the entrepreneur chooses the action $a$. The action will therefore be chosen so as to maximize the entrepreneur's reward and will be given by

$$a^E(\theta_i, s) = \arg\max_{a_j}\left\{t_s y^i_j + t'_s + l^i_j\right\},$$

for $i = g, b$ and $j = g, b$. In order to describe the nature of the different contracts that may arise in this context, we say that a contract is *efficient* if the action chosen is the optimal action for the realized state of nature. Also, we say that a contract is *feasible* if the investor expects to obtain at least as much as the amount invested, $K$.

First, consider the case where the private benefits ($l$) satisfy the inequalities $l^g_g > l^g_b$ and $l^b_b > l^b_g$. In that case, it is said that the private benefits ($l$) are comonotonic¹ with the total revenues ($y + l$). It is fairly simple to show that, in this situation, a contract with a schedule $t(s, r)$ given by a constant $t$, independent of the signal perceived and of the return obtained, is efficient. Under the assumption of comonotonic private benefits,

$$t + l^g_g > t + l^g_b$$
$$t + l^b_b > t + l^b_g,$$

thus ensuring that the revelation of a good state ($i = g$) implies $a^E = a_g$ and the revelation of a bad state ($i = b$) implies $a^E = a_b$. In other words, the optimal choice of the entrepreneur coincides with the optimal choice for the project and one may say that entrepreneur control is efficient.

In this case, for the contract also to be feasible, the constant fee schedule $t \geq 0$ must be chosen such that $q y^g_g + (1 - q) y^b_b - t = K$. One such constant always exists given the assumption $q y^g_g + (1 - q) y^b_b > K$ and it follows

**Proposition 5.1.1 (Aghion and Bolton).** *If $l^g_g > l^g_b$ and $l^b_b > l^b_g$, then entrepreneur control is always efficient and feasible.*

A different treatment is required when the assumptions of the preceding result are not satisfied. Without loss of generality, assume that in state $\theta_b$ the inequality $l^b_b < l^b_g$ holds.

Under such a condition and depending on the fee schedule designed (namely, on $t_s$), the action chosen by the entrepreneur in certain states may not be the one that maximizes the value of the project. Therefore, there is room for renegotiation of the contract, in order to guarantee that there are no ex-post inefficiencies. It is also clear that all the gains from renegotiation revert to the entrepreneur.

Since the issue of renegotiating or not depends on the design of the fee schedule, one first looks for sufficient conditions that guarantee the absence of renegotiation and feasibility of the contract. In this case one would like the contract to induce the entrepreneur to choose action $a_b$ in state $\theta_b$. In other words, the fee schedule and the private benefits to the entrepreneur should relate as

$$t_s y^b_b + l^b_b \geq t_s y^b_g + l^b_g$$

or $t_s \geq (l^b_g - l^b_b)/(y^b_b - y^b_g)$. Let this lower bound be denoted by

$$\hat t \equiv \frac{l^b_g - l^b_b}{y^b_b - y^b_g}.$$

For the contract with $t_s = \hat t$ to be feasible, then it is required that the expected payoff to the investor be greater than $K$ or, denoting by $\pi_1$ the expected payoff,

$$\pi_1 \equiv q(1 - \hat t) y^g_g + (1 - q)(1 - \hat t) y^b_b \geq K.$$

This case is feasible only if $K$ is low enough as compared to the expected payoff (that is what the preceding condition means) and/or the fee schedule is high enough (that is the meaning of $t_s \geq \hat t$), transferring to the entrepreneur a relatively high part of the monetary proceedings of the project.

Consider now the case where $t_s < \hat t$ for $s = 0, 1$. In order to maximize the ex-ante expected payoff, the investor will only accept a contract with $t_s = 0$ whatever signal is observed. The schedule $t(r, s)$ in this contract becomes a simple fixed fee. This fact, together with the assumption that $l^b_b < l^b_g$, implies that the entrepreneur will always choose $a_g$, independently of the state of nature. Then, the ex-ante expected return to the investor is given by

$$\pi_2 = q y^g_g + (1 - q) y^b_g.$$

For the contract to be feasible, one requires that $\pi_2 \geq K$. In this situation, and given that $y^b_b > y^b_g$, there is an incentive to renegotiate. The investor is willing to pay up to $q y^g_g + (1 - q) y^b_b - \pi_2$ for the entrepreneur to choose action $a_b$ in state $\theta_b$. It turns out that this is an interesting offer to the entrepreneur who in this way increases its expected payoff. All the bargaining power being on the side of the entrepreneur, the ex-ante expected payoff to the investor remains $\pi_2$ after the renegotiation.

*From Amaro de Matos, Notes to Chapter Five, note 1, p. 281 (PDF 299):*

1. Take $\gamma$ and $\delta$ as the expected values conditioned on $\theta$ and $a$ of two random variables. If $\gamma^g_g > \gamma^g_b$ and $\gamma^b_b > \gamma^b_g$, then $\delta$ is said to be comonotonic with $\gamma$ if $\delta^g_g > \delta^g_b$ and $\delta^b_b > \delta^b_g$.

---

### 5. Diamond (1991): short- vs. long-term debt, no liquidation case
**Source:** Amaro de Matos, Ch. 5, Exercise 5.2.5 #5, p. 148 (PDF 166) · Answer in book: no (p. 268 only cites example 1 of Diamond 1991, pp. 716–717)

5. This exercise illustrates the case of Lemma 5.2.1 in the model of Diamond (1991). Take $L = R = 1$, $\pi = \frac{1}{2}$, $X = 1\frac{3}{4}$, $C = 0$, $f = \frac{1}{2}$, and $f^d = \frac{1}{3}$.

(a) What are the face values of a short-term and a long-term debt contract?

(b) Show that in this example there will be no liquidation.

(c) What is the payoff of a good project financed with long-term debt?

(d) What is the probability that a good project receives a downgrade at $t = 1$?

(e) What is the payoff of a good project financed with short-term debt?

#### Context needed to solve it

*From Amaro de Matos §5.2.3 "The Choice of the Duration", pp. 139–141 (PDF 157–159):*

A model developed by Diamond (1991, 1993) illustrates in a very simple way the differences between short-term and long-term debt financing. The model is based on information asymmetry and credit rating.

Regaining the notation of Aghion and Bolton, consider an entrepreneur with a two-period project who needs funds for an initial investment $K = 1$. The project may be of one of two types: good or bad. At time $t = 2$ a good project has a payoff $X > 0$, whereas a bad project pays that amount with a probability $\pi$, and pays zero with probability $1 - \pi$. Let $\theta$ denote the type of project, $\theta_g$ referring to a good project and $\theta_b$ referring to a bad project. The quality of the project is known to the entrepreneur but not to the investor. Given a project, as of date $t = 0$ the investor assigns a probability $f$ that $\theta = \theta_g$. This probability is referred to as a *credit rating* and reflects the lender's information about the project. It follows that, as of time 0, the probability $q$ that a borrower pays the loan at date $t = 2$ is given by

$$q \equiv f + \pi(1 - f) = \pi + f(1 - \pi). \qquad (5.9)$$

At time $t = 1$ information about the project becomes available to the investor. This new information is not verifiable, so it makes no sense to write contracts contingent upon that information, since they cannot be enforced. However, the investors update their beliefs about the quality of the project and the credit rating will be either upgraded or downgraded.

Under this revision of the credit rating, let $f^u$ denote the probability that $\theta = \theta_g$ given an upgrade and let $f^d$ denote the probability that $\theta = \theta_g$ given a downgrade. In that case, the probability that an entrepreneur who receives a downgrade repays at time $t = 2$ is

$$q^d = \pi + f^d(1 - \pi) > f^d. \qquad (5.10)$$

Moreover, it is here assumed that

$$f^d < f < f^u,$$

meaning that the probability that the project is good is greater given an upgrade than given a downgrade. Furthermore, the simplifying assumption $f^u = 1$ is also made. Thus, given an upgrade at date $t = 1$, it is certain that the project is good. However, it is not certain that all projects of good quality are upgraded. There is room for one such project to be downgraded. Let $e$ denote the probability of such an event.

All projects are also assumed to produce a nonassignable control rent $C$ if the management has control at time $t = 2$. Also, if at time $t = 1$ the manager defaults on short-term debt, lenders then have the right to remove the management from control, selling the assets for a liquidation value $L < K = 1$. All projects may be liquidated at that point in time, under those conditions. If the project is liquidated, the entrepreneur is prevented from consumption of his/her present or future cash flows and control rents. In this case, an optimal contract is a debt contract enforced by the right to liquidate the project if the debt is not repaid in full.

Just as in the case of the borrowers, lenders are assumed be risk neutral. Moreover, lenders have alternative investments at $t = 0$ that provide a return $R$ at $t = 2$. The condition $L < X/R$ ensures that a good project yields a higher return when not liquidated.

A project may be financed with either long-term or short-term debt. In the context of this model, long-term debt refers to a contract issued at $t = 0$ with no refinancing at date $t = 1$ and maturing at $t = 2$. If one such instrument provides $K = 1$ at time $t = 0$ with face value $\rho \le X$, the lender expects to receive at maturity $\rho[\pi + f(1 - \pi)] = R^2$. Notice that if $\rho > X$, a borrower with credit rating $f$ will not be able to provide the lender with the required rate of return $R^2$. Now, if the project is upgraded at time $t = 1$, the market value of the debt contract at that point in time becomes $V_l^u = \rho/R$. Similarly, if the project is downgraded, the market value of debt at time $t = 1$ becomes $V_l^d = q^d\rho/R$.

Short-term debt, on the other hand, is debt financed at $t = 0$ with face value $r_1$ and maturity at time $t = 1$. If short-term borrowers are upgraded at $t = 1$, their debt contract at that point in time is worth $V_s^u = r_1$ and they may refinance their project by issuing a new short-term debt contract with maturity at $t = 2$ and face value $r_1 R$ that will be paid with certainty and guarantees a return of $R$ per unit invested by the lender. If short-term borrowers are downgraded, however, in principle they may refinance their debt with a new short-term contract only if $q^d X/R > r_1$, since $X$ is the maximum that a borrower can pay at $t = 2$. If that is the case, at $t = 1$ the market value of the short-term debt issued at $t = 0$ would be $V_s^d = r_1$ if the borrower pays, possibly through the refinancement mechanism. But what happens if $q^d X/R < r_1$? In that case there is still room for a refinancement provided that the liquidation value $L$ is less than the expected value to the lender from a refinancement, $q^d X/R$. Under a downgrading, the time $t = 1$ value of the short-term debt is thus

$$V_s^d = \min\left[r_1, \max(L, q^d X/R)\right].$$

The face value of short-term debt is established such as to provide the lenders with an expected return of $R$ per period. It then follows that

$$r_1 = \frac{R - [1 - (1 - e)f]V_s^d}{(1 - e)f}. \qquad (5.11)$$

*From Amaro de Matos §5.2.3, pp. 141–142 (PDF 159–160):*

Given this model, the point is to characterize under what conditions short-term or long-term maturities will be offered. The maturity preferred by the entrepreneurs of good projects will be the only one offered to all borrowers. This happens because if any other maturity is offered, it reveals a project of bad quality and lenders will not be willing to finance it.

The following result implies that, in the absence of liquidation given a downgrade, the entrepreneurs of good projects prefer short-term debt:

**Lemma 5.2.1 (Diamond, 1991).** *Comparing two debt contracts issued at $t = 0$, neither of which involves liquidation on a downgrade at $t = 1$, the one with the higher value at that point in time given a downgrade, $V^d$, is preferred by the entrepreneurs of good projects.*

*Proof.* The expected payoff to the entrepreneurs of good projects from debt not yielding liquidation is

$$e\left(X + C - \frac{RV^d}{q^d}\right) + (1 - e)(X + C - r_1 R).$$

Using expression (5.11) this payoff is rewritten as

$$X + C - \frac{R^2}{f} + RV^d e\left(\frac{1}{f^d} - \frac{1}{q^d}\right).$$

Given (5.10) this expression for the payoff is clearly an increasing function of $V^d$. ■

---

### 6. Optimal contracts in the Bolton–Scharfstein model
**Source:** Tirole, Ch. 7, Exercise 7.7, p. 325 (PDF 338) · Answer in book: yes, pp. 603–604

**Exercise 7.7 (optimal contracts in the Bolton–Scharfstein model).** Redo the Bolton and Scharfstein analysis of Section 7.1.2, allowing for fully general contracts: the entrepreneur receives $r_b^S$ in the case of date-0 success but no refinancing, $R_b^{SS}$ in the cases of date-0 and date-1 success, and $R_b^{FS}$ in the cases of date-1 success and date-0 failure (with $R_b^{SS}, R_b^{FS} \geqslant B/\Delta p$). (Under risk neutrality, there is no point rewarding failures unless it serves to deter predation. Hence, the exception $R_b^{FS}$.) Generalize the conditions (PD) and (IC) and show that $r_b^S = 0$ and that $R_b^{SS} \geqslant R_b^{FS}$ ($\geqslant B/\Delta p$).

#### Context needed to solve it

*From Tirole §7.1.1.1 "Basics: Profit Destruction and Benchmarking Effects", p. 284 (PDF 297):*

The model is the basic, fixed-investment model of Section 3.2 except for the twist that a firm's profit depends on how successful the other firm is. Namely, while a firm makes no profit if it fails to develop the new technology, its profit when its succeeds in developing it depends on whether it faces a competitor, that is, whether the other firm also succeeds. Thus the firm's profit is as follows:

$$\text{profit} = \begin{cases} M & \text{if it is the only firm to succeed,} \\ D & \text{if both firms succeed,} \\ 0 & \text{if it fails,} \end{cases}$$

where

$$M \geqslant D \geqslant 0 \quad \text{and} \quad p_H M > I.$$

Here, $M$ stands for "monopoly profit" and $D$ for "duopoly profit." […]

The familiar agency cost affects the development process. Each entrepreneur succeeds with probability $p_H$ if she behaves (in which case she receives no private benefit) and with probability $p_L = p_H - \Delta p$ if she misbehaves (and thereby receives private benefit $B$), where $\Delta p > 0$.

Each entrepreneur needs to raise $I - A$ in order to finance her project, where $I$ is the investment cost and $A$ her initial net worth.

*From Tirole §7.1.2.1 "Financial Muscle and Predation", p. 290 (PDF 303):*

*Simple-minded long-purse story: short-term financing arrangements.* There are two dates, $t = 0, 1$. There is no discounting between the two periods.

Consider a duopoly. Firms $i = 1, 2$ are identical in all respects except the amount of wealth they have access to in order to finance investments. Firm 1 (the predator, the financially strong firm) has a large amount of wealth and never needs to go to the capital market to finance investment. Firm 2 (the prey, the financially weak firm) has just enough wealth to finance the date-0 investment.¹⁶

[…] The second period, date 1, is described exactly as in Section 7.1.1: for each firm, the investment cost is $I$. Entrepreneurs then engage in moral hazard. The probability of success of the date-1 project is $p_H$ if the entrepreneur behaves and $p_L = p_H - \Delta p$ if she misbehaves (in which case she obtains private benefit $B$). A firm's date-1 profit is $M$ if it alone succeeded, $D$ if both firms succeeded, and 0 otherwise. […]

¹⁶ Alternatively, one could assume that it is able to secure financing for the date-0 investment, where the loan is to be repaid from date-0 profits: that is, there is no long-term financing arrangement.

*From Tirole §7.1.2.1, "Strategic security design (Bolton and Scharfstein)", pp. 292–293 (PDF 305–306):*

Let us now investigate these points in more detail. To do so, we need to build upon the simple-minded model by explicitly describing the date-0 actions and by allowing for long-term financing. To simplify the analysis, let us assume that

- $p_H = 1$;
- furthermore, date 0 is identical to date 1 except for the private benefit from misbehaving—the latter is equal to $B_0$ at date 0 and $B$ at date 1;¹⁹
- the financially strong firm's act of predation in a given period²⁰ results in 0 profits (failure) for both firms in that period;
- investors in the financially weak firm observe only that firm's profit at date 0.²¹

As earlier, the financially strong firm is self-financed. The financially weak firm signs a long-term agreement with its investors that specifies:²²

- the probabilities $z^S$ and $z^F$ of refinancing (date-1 investment) in the case of date-0 success (i.e., profit $D$) or failure (i.e., profit 0), respectively;
- a reward $R_b^i$ in the case of date-1 success (which assumes a date-1 reinvestment in the first place), where $i \in \{S, F\}$ indexes the date-0 outcome—for all $i$, $R_b^i$ must satisfy the date-1 incentive constraint $(\Delta p)R_b^i \geqslant B$.²³

The timing is summarized in Figure 7.5.

Figure 7.5 (timeline, left to right; p. 293, PDF 306)

| Date 0: step 1 | Date 0: step 2 | Date 0: step 3 | Date 1: step 4 | Date 1: step 5 | Date 1: step 6 |
|---|---|---|---|---|---|
| Financially weak firm signs initial contract. Financing of investment $I$. Choice of $z^S$, $z^F$, and $R_b^i$. | Date-0 efforts. Probability of success: $p_H = 1$ for high effort or $p_L$ for low effort (private benefit $B_0$) if no predation; 0 if predation. Strong firm preys? | Profits: $D$ if successful and no predation, 0 otherwise. | Reinvestment $I$ by weak firm? | Date-1 effort(s). Probability of success: $p_H = 1$ for high effort, or $p_L$ for low effort (private benefit $B$). | Date-1 profit(s). |

Let us make the following assumptions.

**Assumption 7.1.** *Positive-NPV investment even under duopoly in the absence of predation:*

$$D - I > 0.$$

(Recall: the probability of success in the case of good behavior is here equal to 1.)

**Assumption 7.2.** *Dearth of pledgeable income in the case of continuation:*²⁴

$$\left(D - \frac{B}{\Delta p}\right) - I < 0.$$

Preventing predation by firm 1 at date 0 benefits firm 2 in two ways. First, its date-0 income is increased by $D$, the duopoly profit. Second, it may avoid credit rationing, which from Assumption 7.2 is a threat, and from Assumption 7.1 undesirable.

*Predation deterrence constraint.* To avoid predation firm 2 must choose its financial contract so that firm 1's date-0 cost of predation, $D$, exceed its date-1 gain from monopolization. To compute the latter, note that it is not in firm 1's interest to prey in the last period. Hence, preventing refinancing by firm 2 raises firm 1's profit from $D$ to $M$. And the probability that firm 2 receives refinancing falls from $z^S$ in the absence of predation to $z^F$ under predation (recall that the probability of refinancing is $z^S$ if firm 2's date-0 profit is $D$ and $z^F$ if it is equal to 0). The predation deterrence constraint is therefore

$$D \geqslant (z^S - z^F)(M - D). \qquad (\text{PD})$$

To deter predation, the weak firm's contract must make the continuation decision relatively insensitive to that firm's date-0 profit performance. Note that (PD) can be rewritten as

$$\frac{D}{M - D} \geqslant z^S - z^F. \qquad (\text{PD}')$$

Suppose that competition between the two firms reduces industry profit:

$$M \geqslant 2D.$$

The left-hand side of (PD′) can then take any value between 0 (extreme, Bertrand competition) and 1 (perfect tacit collusion or noncompeting goods). In the latter case, (PD′) really does not constrain the financial contract and there is little incentive to prey. By contrast, with Bertrand competition, predation can only be deterred by a performance-insensitive continuation rule (on the other hand, remaining in the market is also unattractive for firm 2).

*Weak firm's date-0 incentive constraint.* The weak firm's contract must also induce its entrepreneur to behave. Here, the entrepreneur's compensation is delayed. She receives $R_b^i$ if there is reinvestment and firm 2 has profit $D$ in the last period. Let

$$\mathcal{R}_b^S \equiv z^S R_b^S \quad \text{and} \quad \mathcal{R}_b^F \equiv z^F R_b^F$$

denote the expected continuation payoffs for the entrepreneur in the cases of date-0 success and failure, respectively. By misbehaving at date 0, the entrepreneur receives private benefit $B_0$, but reduces the probability of date-0 success by $\Delta p$ (provided that the rival does not prey, i.e., if constraint (PD) is satisfied).

Hence, the incentive constraint is

$$\mathcal{R}_b^S - \mathcal{R}_b^F \geqslant \frac{B_0}{\Delta p}. \qquad (\text{IC})$$

(a) *The no-predation benchmark.* Suppose, first, that the predator is unable to prey and so constraint (PD) is irrelevant. Let $U_b(z^S)$ denote the NPV:

$$U_b(z^S) \equiv D - I + z^S(D - I).$$

From Assumption 7.1, it increases in $z^S$.

The investors' breakeven constraint can be written as

$$U_b(z^S) - \mathcal{R}_b^S + A \geqslant 0. \qquad (\text{IR}_l)$$

Finally, the entrepreneur's incentive compatibility constraint is

$$\mathcal{R}_b^S - \mathcal{R}_b^F \geqslant \frac{B_0}{\Delta p}. \qquad (\text{IC})$$

[…]

*From Tirole §7.1.2.1, p. 294 (PDF 307):*

(b) *Reintroducing the predation-deterrence constraint.* The best, predation-deterring financial contract is now obtained by maximizing firm 2's NPV subject to the predation-deterrence constraint (PD), the breakeven constraint (IR$_l$), and the incentive-compatibility (IC) constraint.

If the solution in the no-predation benchmark case satisfied (PD), then it is also the solution when predation if feasible. So, we will assume that (PD) is not satisfied by the benchmark solution. […]

*Footnotes 19–24, p. 292 (PDF 305):*

¹⁹ We will later assume that $B_0 < B$. This distinction between $B_0$ and $B$ allows us to shorten the analysis by ensuring that date-0 incentives can be provided through the continuation policy. See below.

²⁰ Predation can, of course, occur at date 0 only. The predator can only lose by preying at date 1 because there is no future at that date.

²¹ The important assumption is that a court cannot ascertain whether the absence of date-0 profit for firm 2 is due to a predatory act or to moral hazard (lack of luck is not a possible third explanation because we assumed that $p_H = 1$). […]

²² Exercise 7.7 shows that there is only a slight loss of generality in considering this class of contracts, and that the results are not qualitatively affected by our focus on this class.

²³ Note that if $(\Delta p)R_b^i < B$, then there is always renegotiation to an $R_b^i \geqslant B/\Delta p$ as long as $p_H(R - B/\Delta p) > p_L R$. But even in the absence of renegotiation, the analysis generalizes.

²⁴ Given that rent $p_H(B/\Delta p) = B/\Delta p$ must be given to the entrepreneurs, investors would not finance firm 2 at date 1 in the absence of retained earnings and long-term contracting obligations.

---

### 7. Liquidation incentives with a private signal
**Source:** Tirole, Ch. 3, Exercise 3.14, pp. 149–150 (PDF 162) · Answer in book: yes, pp. 577–578

**Exercise 3.14 (liquidation incentives).** This exercise extends the fixed-investment model of Section 3.2 by adding a signal on the profitability of the project that (a) accrues after effort has been chosen, and (b) is privately observed. (The following model is used as a building block in a broader context by Dessi (2005).)

An entrepreneur has cash $A$ and wants to invest $I > A$ into a project. The project yields $R$ (success) or 0 (failure) at the end. An intermediate signal reveals the probability $\gamma$ that the project will succeed, with $\gamma = \bar\gamma$ or $\underline{\gamma}$ ($\bar\gamma = \underline{\gamma} + \Delta\gamma$ and $\Delta\gamma > 0$). The probability, $p$, that $\gamma = \bar\gamma$ depends on the entrepreneur's effort. If the entrepreneur behaves, then $p = p_H$ and the entrepreneur receives no private benefit. If the entrepreneur misbehaves, then $p = p_L$ and the entrepreneur receives private benefit $B$. Investors and entrepreneur are risk neutral and the latter is protected by limited liability. The competitive rate of return is equal to 0.

Introduce further an option to liquidate after the signal is realized but before the final profit accrues. Liquidation yields $L$, and $L$ is entirely pledgeable to investors.

One will assume that

$$\bar\gamma R > L > \underline{\gamma} R,$$

so that it is efficient to liquidate if and only if the signal is bad; and that

$$p_H \bar\gamma R + (1 - p_H)L > I$$

(which will imply that the NPV is positive).

Figure 3.11 summarizes the timing.

Figure 3.11 (timeline, left to right; p. 150, PDF 163)

| Step 1 | Step 2 | Step 3 | Step 4 |
|---|---|---|---|
| The entrepreneur borrows $I - A$ and invests in a project with cost $I$. | The entrepreneur behaves ($\Pr(\gamma = \bar\gamma) = p_H$; no private benefit), or misbehaves ($\Pr(\gamma = \bar\gamma) = p_L$; private benefit $B$). | State of the world $\gamma = \bar\gamma$ or $\underline{\gamma}$ realized. | Continuation: success ($R$) with probability $\gamma$, failure (0) with probability $1 - \gamma$. Or liquidation (yields $L$). |

(i) Suppose first that $\gamma$ is verifiable. Argue that the entrepreneur should be rewarded solely as a function of the realization of $\gamma$. What is the pledgeable income? Show that the project is financed if and only if $A \geqslant \bar A$, where

$$p_H\left(\bar\gamma R - \frac{B}{\Delta p}\right) + (1 - p_H)L = I - \bar A.$$

(ii) Suppose now that $\gamma$ is observed only by the entrepreneur. This implies that the entrepreneur must be induced to tell the truth about $\gamma$. Without loss of generality, consider an incentive scheme in which the entrepreneur receives $R_b$ in the case she announces $\gamma = \bar\gamma$ (and therefore the project continues) *and* the final profit is $R$, $L_b$ if she announces $\gamma = \underline{\gamma}$ (and therefore the project is liquidated), and 0 otherwise.

Show that the project is funded if and only if

$$A \geqslant \bar A + \underline{\gamma}\,\frac{B}{(\Delta p)(\Delta\gamma)}.$$

#### Context needed to solve it

*From Tirole §3.2.1 "The Fixed-Investment Model", pp. 115–116 (PDF 128–129):*

Variants of the following entrepreneurial model will be used in the following: an entrepreneur (also called the "insider" or the "borrower," "she") has a project. This project requires a fixed investment $I$. The entrepreneur initially has "assets" ("cash on hand" or "net worth") $A < I$. For the moment we interpret these assets as being cash or liquid securities that can be used toward covering the cost of investment. […] The entrepreneur's cash can either be invested in the project or used for consumption. To implement the project the entrepreneur must borrow $I - A$ from lenders. […]

*Project.* If undertaken, the project either succeeds, that is, yields verifiable income $R > 0$, or fails, that is, yields no income. The probability of success is denoted by $p$. The project is subject to moral hazard. The entrepreneur can "behave" ("work," "exert effort," "take no private benefit") or "misbehave" ("shirk," "take a private benefit") […].

Behaving yields probability $p = p_H$ of success and no private benefit to the entrepreneur, and misbehaving results in probability $p = p_L < p_H$ of success and private benefit $B > 0$ (measured in units of account) to the entrepreneur. In the "effort interpretation," $B$ can also be interpreted as a disutility of effort saved by the entrepreneur when shirking. Let $\Delta p \equiv p_H - p_L$.

*Preferences and the loan agreement.* Both the borrower and the potential lenders (or "investors") are risk neutral. For notational simplicity, there is no time preference; the rate of return expected by investors (which is also the riskless rate, due to risk neutrality) is taken to be 0. The borrower is protected by limited liability, and so her income cannot take negative values.

Lenders behave competitively in the sense that the loan, if any, makes zero profit. […]

Let us turn to the loan contract. A contract first stipulates whether the project is financed. If so, it further specifies how the profit is shared between the lenders and the borrower. The borrower's limited liability will imply that both sides receive 0 in the case of failure […]. In the case of success, the two parties share the profit $R$; $R_b$ goes to the borrower and $R_l$ to the lenders. To sum up, we posit an incentive scheme for the entrepreneur of the following form: $R_b$ in the case of success, 0 in the case of failure.

[…] We summarize the timing in Figure 3.1.

Figure 3.1 (timeline, left to right): Loan agreement (sharing rule) → Investment → Moral hazard → Outcome.

We assume that the project is viable only in the absence of moral hazard. That is, the project has positive NPV if the entrepreneur behaves,

$$p_H R - I > 0, \qquad (3.1)$$

but negative NPV, even if one includes the borrower's private benefit, if she does not,

$$p_L R - I + B < 0. \qquad (3.2)$$

*From Tirole §3.2.2 "The Lenders' Credit Analysis", pp. 116–117 (PDF 129–130):*

[…] the borrower will therefore behave if the following "incentive compatibility constraint" is satisfied:

$$p_H R_b \geqslant p_L R_b + B \quad \text{or} \quad (\Delta p) R_b \geqslant B. \qquad (\text{IC}_b)$$

From this incentive compatibility constraint we infer that the highest income in the case of success that can be pledged to the lenders without jeopardizing the borrower's incentives is

$$R - \frac{B}{\Delta p}.$$

The *(expected) pledgeable income* is then

$$\mathcal{P} = p_H\left(R - \frac{B}{\Delta p}\right).$$

Because the lenders must break even in order to be willing to finance the project, a necessary condition for the borrower to receive a loan is that the expected pledgeable income exceed the lenders' initial outlay:

$$\mathcal{P} \equiv p_H\left(R - \frac{B}{\Delta p}\right) \geqslant I - A, \qquad (\text{IR}_l)$$

[…] Thus a necessary condition for financing to be arranged is

$$A \geqslant \bar A = p_H \frac{B}{\Delta p} - (p_H R - I). \qquad (3.3)$$

To make things interesting, we will assume that

$$\bar A > 0 \iff p_H R - I < p_H \frac{B}{\Delta p}, \qquad (3.4)$$

otherwise even a borrower with no wealth of her own would be able to obtain credit. […]

Thus, *the borrower must have enough assets in order to be granted a loan.* Note that, if $A < \bar A$, the project has positive NPV and yet is not funded. […] There is *credit rationing*. […]

Conversely, if $A \geqslant \bar A$, the entrepreneur is able to secure financing, and so condition (3.3) is both a necessary and a sufficient condition for financing. The entrepreneur offers claim $R_l$ to competitive investors so as not to leave them with a surplus:

$$p_H R_l = I - A.$$

Her stake,

$$R_b = R - R_l = R - \frac{I - A}{p_H} \geqslant R - \frac{I - \bar A}{p_H} = \frac{B}{\Delta p}, \qquad (3.5)$$

then induces her to behave.

[…] Using the breakeven condition for the lenders ($p_H R_l = I - A$), the borrower obtains net utility or payoff (where "net" means that we subtract the consumption utility, $A$, that the entrepreneur would get by not undertaking the project):

$$U_b = \begin{cases} 0 & \text{if } A < \bar A, \\ p_H R_b - A = p_H(R - R_l) - A = p_H R - I & \text{if } A \geqslant \bar A. \end{cases} \qquad (3.6)$$

As could have been expected from the zero-profit condition for the lenders, *the borrower receives the entire social surplus or net present value if the project is funded.*

So, the borrower's utility jumps up at $A = \bar A$. […]

---

### 8. Decreasing returns to scale and debt maturity
**Source:** Tirole, Ch. 5, Exercise 5.7, p. 232 (PDF 245) · Answer in book: yes, p. 593

Exercise 5.7 (decreasing returns to scale). Extend the treatment of Section 5.6.1 to the case of decreasing returns to scale: the payoff in the case of continuation and success is $R(I)$, with $R(0) = 0$, $R' > 0$, $R'' < 0$, $R'(0) = \infty$, and $R'(\infty) = 0$. The rest is unchanged (the short-term income is $rI$, the reinvestment need is $\rho I$, and the private benefit is $BI$).

(i) What are the first-order conditions yielding the optimal investment level $I$ and cutoff $\rho^*$?

(ii) Assuming that $r > \rho^*$, and that $(R(I)/I - R'(I))$ is increasing in $I$ (a condition satisfied, for example, by $R(I)$ quadratic), derive the impact of the strength of the balance sheet as measured, say, by $A$ on debt maturity.

#### Context needed to solve it

*From Tirole §5.3.2 "Continuum of Liquidity Shocks", pp. 209–210 (PDF 222–223):*

After the (endogenous size) investment $I$ is sunk at date 0 and before the borrower works on the project, some exogenous shock occurs at date 1 that determines a per-unit-of-investment level $\rho \in [0, \infty)$ of "cost overruns." That is, a cash infusion equal to $\rho I$ is needed in order for the project to continue. If $\rho I$ is not invested, the project is abandoned altogether and thus yields no income. As in Section 5.2, the fraction $\rho$ is *a priori* distributed according to the continuous distribution $F(\rho)$ on $[0, \infty)$, with density $f(\rho)$. (As we already observed, the model of Section 3.4 is therefore a special case, with $F$ being a spike at $\rho = 0$.)

Regardless of the required amount of the cash infusion, the project, if pursued, is still a project of size $I$, in that the income in the case of success is $RI$ and the borrower's private benefit from misbehaving is $BI$. One cannot increase the size of the project after the initial stage.

The timing is summarized in Figure 5.4.

Figure 5.4 (timing, transcribed): **Date 0** — Loan agreement; Investment $I$. **Date 1** — Need for cash infusion $\rho I$ realized; then either Disbursement → Moral hazard, or No disbursement → Project is abandoned. **Date 2** — Outcome.

[…] It is easy to show that it is optimal to have a "cutoff rule" for infusing cash. There exists an optimal threshold $\rho^*$ such that one should continue if and only if

$$\rho \leqslant \rho^*. \qquad (5.2)$$

The incentive constraint in the case of continuation is the same as in the absence of a liquidity shock (see Section 3.4):

$$(\Delta p)R_b \geqslant BI. \qquad (\text{IC}_b)$$

The breakeven condition is slightly altered by the presence of liquidity shocks:

$$F(\rho^*)[p_H(RI - R_b)] \geqslant I - A + \int_0^{\rho^*}\rho If(\rho)\,\mathrm{d}\rho. \qquad (\text{IR}_l)$$

That is, the lenders receive a return only if the project is pursued, which has probability $F(\rho^*)$. The left-hand side of (IR$_l$) is the expected pledgeable income. Furthermore, there is a new term, representing the expected outlay on overruns, on the right-hand side. From these two constraints, we deduce the borrowing capacity (or, more precisely, the maximum investment that allows the lenders to break even):

$$I = k(\rho^*)A,$$

where

$$k(\rho^*) = \frac{1}{1 + \int_0^{\rho^*}\rho f(\rho)\,\mathrm{d}\rho - F(\rho^*)[p_HR - p_HB/\Delta p]} = \frac{1}{1 + \int_0^{\rho^*}\rho f(\rho)\,\mathrm{d}\rho - F(\rho^*)\rho_0} \qquad (5.3)$$

involves a straightforward modification relative to the no-liquidity-shock multiplier $k$. […] Note that the borrower's borrowing capacity is maximal when the threshold $\rho^*$ is equal to the expected per-unit pledgeable income $\rho_0 \equiv p_H(R - B/\Delta p)$.

Given that the competitive lenders make no profits, the borrower's net utility is as usual the social surplus brought about by the project, namely,

$$U_b = m(\rho^*)I = m(\rho^*)k(\rho^*)A, \qquad (5.4)$$

where

$$m(\rho^*) \equiv F(\rho^*)p_HR - 1 - \int_0^{\rho^*}\rho f(\rho)\,\mathrm{d}\rho$$

is the margin per unit of investment.

[…] Next, we observe that *this optimal threshold lies between the expected per-unit-of-investment pledgeable income and income*:

$$\rho_0 = p_H\left(R - \frac{B}{\Delta p}\right) < \rho^* < \rho_1 = p_HR. \qquad (5.8)$$

*From Tirole §5.6.1 "Optimal Claim Maturity", p. 226 (PDF 239):*

Let us return to the continuous-investment, continuous-shock version of Section 5.3.2, but with a short-term income (the analysis is not really new and is therefore only sketched): see Figure 5.10. Because the short-term income $rI$ is fully pledgeable to the lenders, everything is *as if* the unit investment cost were equal to $1 - r$ instead of 1. The lenders' breakeven condition, that is, the equality between expected revenue and expected investment cost, becomes

$$rI + F(\rho^*)\rho_0I = I - A + \left[\int_0^{\rho^*}\rho f(\rho)\,\mathrm{d}\rho\right]I$$

and so

$$k(\rho^*) = \frac{1}{1 + \int_0^{\rho^*}\rho f(\rho)\,\mathrm{d}\rho - [r + F(\rho^*)\rho_0]}. \qquad (5.3'')$$

The margin (expected profit of the firm per unit of investment) becomes

$$m(\rho^*) = [r + F(\rho^*)\rho_1] - \left[1 + \int_0^{\rho^*}\rho f(\rho)\,\mathrm{d}\rho\right]. \qquad (5.4'')$$

And thus the borrower's (gross) utility becomes

$$U_b = m(\rho^*)k(\rho^*)A = \frac{\rho_1 - c(\rho^*)}{c(\rho^*) - \rho_0}A,$$

where the expected unit cost of effective investment, $c(\rho^*)$, is given by

$$c(\rho^*) = \frac{1 - r + \int_0^{\rho^*}\rho f(\rho)\,\mathrm{d}\rho}{F(\rho^*)}. \qquad (5.5'')$$

So the optimal threshold is given by

$$\int_0^{\rho^*}F(\rho)\,\mathrm{d}\rho = 1 - r \qquad (5.6'')$$

and the borrower's utility by

$$U_b = \frac{\rho_1 - \rho^*}{\rho^* - \rho_0}A. \qquad (5.7'')$$

Figure 5.10 (timing, transcribed): **Date 0** — Loan agreement. Investment $I$. **Date 1** — Accrual of short-term income $rI$. Realization $\rho I$ of investment need. Then either Disbursement → Moral hazard, or No disbursement → Project is abandoned. **Date 2** — Date-2 income ($RI$ or 0).

It is important to note that *the short-term income, even though it is deterministic and fully pledgeable, is not equivalent to an increase in the borrower's cash on hand $A$.* Such an increase in equity would result in a larger investment (as is the case here), but not in a modification of the continuation rule. By contrast, condition (5.6$''$) shows that the larger the short-term profit, the lower the optimal threshold $\rho^*$. […]

(a) *Liquidity management.* Let us now turn to the implementation of the optimum and thus to the claim maturity. To this purpose we make the following assumption. (Footnote 57: Of course, it must also be the case that $\rho^* > \rho_0$ (otherwise, the borrower's borrowing capacity and utility would be infinite in this constant-returns-to-scale model). Because $\mathrm{d}\rho^*/\mathrm{d}r < -1$, we must thus also assume that $r$ is not "too large.")

*Free-cash-flow assumption:* $r > \rho^*$. Under the free-cash-flow assumption, and given that the entrepreneur cannot steal the intermediate income, the entrepreneur would reinvest excessively if she were not asked to pay out money to investors at date 1. Namely, she would reinvest as long as $\rho \leqslant r$.

To obtain the optimal amount of reinvestment, an amount $P_1 \equiv (r - \rho^*)I$ must be pumped out of the firm, and the entrepreneur must be denied the right to dilute initial investors.

---

### 9. The priority game: uncoordinated lending and short-term bias
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


## Tier 3 — Really hard

### 10. One vs. two creditors: strategic and liquidity default
**Source:** Amaro de Matos, Ch. 5, Exercise 5.2.5 #2, p. 148 (PDF 166) · Answer in book: no (p. 268 only cites pages 10–13 of Bolton and Scharfstein 1996)

Show that two creditors are paid more in the case of strategic default than one creditor, but are paid less in the case of liquidity default.

#### Context needed to solve it

*From Amaro de Matos §5.2.1 "Extending the Model", pp. 134–137 (PDF 152–155):*

As before, all the agents are risk neutral and the risk-free rate is assumed to be zero. The time schedule refers to a two-period model and is characterized as follows: At time $t = 0$ an amount $K$ is invested in the project. The entrepreneur, as before, is assumed to have no initial wealth. In this specification of the model, the state of nature is characterized by the cash flow at $t = 1$. It may be $\theta_g = x$ with probability $q$ and $\theta_b = 0$ with probability $1 - q$. The cash flow is observable for both the investor and the entrepreneur, but not for any third party, and is thus not verifiable. Therefore, as before, a contract between the investor and the entrepreneur is incomplete.

The manager is assumed to have the ability to divert cash flow without the control of the investor. In that case a zero payoff would be declared at $t = 1$ when the actual payoff was $x$. If the declared cash flow at $t = 1$ is $x$, the contract states a payment of $R_x$ to the creditholder and, with probability $\beta_x$, the right of the creditholder to liquidate a part of the assets that is worth $L_x$. If the cash flow is null, the values are, respectively, $R_\circ$, $\beta_\circ$, and $L_\circ$.

Notice that taking $\beta_x = 0$, $\beta_\circ = 1$, and $L_x = L_\circ$, being equal to the value of the assets of the project at time $t = 1$, this reduces to a usual debt contract with face value $R_x < x$ and one-period maturity. The issue in designing a contract is to find the optimal values for the preceding parameters. Therefore, it is possible in this simple setting to analyze the conditions under which a debt contract would result as optimal.

In the second period, two things may happen. Either the manager continues the project or the project is liquidated, in the sense that it is separated from the manager. If the manager's activity continues, the cash flow at time $t = 2$ is $y$. In the case of no liquidation, the project thus has a net present value of $qx + y - K$.

The expected return to the firm is then written as

$$\pi_f = q[x - R_x + (1 - \beta_x)y] + (1 - q)[-R_\circ + (1 - \beta_\circ)y]. \qquad (5.3)$$

On the other hand, the investor expects to get

$$\pi_i = q[R_x + \beta_x L_x] + (1 - q)[R_\circ + \beta_\circ L_\circ] - K. \qquad (5.4)$$

Suppose for a moment that at time $t = 1$ the cash flow is $x$. The expected return to the firm would then be $x - R_x + (1 - \beta_x)y$, decomposed as follows: The cash flow $x$ goes to the entrepreneur, who has to pay $R_x$ to the investor. With probability $\beta_x$ the project is liquidated at date $t = 1$, leading to a continuation value of zero, and with probability $1 - \beta_x$ the project continues until time $t = 2$, generating a cash flow $y$ at that point. If, however, the manager hides from the outer investor the cash flow $x$, then only $R_\circ$ will be paid at time $t = 1$, and liquidation occurs with probability $\beta_\circ$, leaving to the firm a possible payoff $S$, not necessarily zero, as before. This happens because the liquidation value $L_\circ$ does not correspond to the true value of the assets in that state of nature. In that case the expected return to the firm is $x - R_\circ + \beta_\circ S + (1 - \beta_\circ)y$.

For the manager to be induced to pay the due $R_x$ when the cash flow is $x$, one must therefore impose

$$x - R_x + (1 - \beta_x)y \geq x - R_\circ + \beta_\circ S + (1 - \beta_\circ)y. \qquad (5.5)$$

Noticing that $R_\circ = \beta_x = 0$ is optimal in the sense that these values maximize the profit to the firm and facilitates the verification of (5.5), the preceding inequality reads

$$R_x \leq \beta_\circ(y - S).$$

Among all these possible values for $R_x$ that ensure a trustworthy behavior from the manager of the project, any investor would maximize its expected return by choosing the greatest value. Thus, at the optimum, this restriction is binding. Substituting the optimal values of the parameters in expression (5.4) for the expected result of the investor, one gets

$$\pi_i = \beta_\circ[q(y - S) + (1 - q)L_\circ] - K. \qquad (5.6)$$

Using the optimal values of the parameters, namely those minimizing the profit to the investor, in the profit of the firm (5.3), it follows that

$$\pi_f = (qx + y - K) - (1 - q)\beta_\circ(y - L_\circ). \qquad (5.7)$$

This result can be interpreted as the net present value of the project in the absence of liquidation minus a cost due to contract incompleteness.

For the profit in (5.6) to be positive, ensuring the minimum condition of feasibility of the contract, one must have

$$1 \geq \beta_\circ \geq \frac{K}{q(y - S) + (1 - q)L_\circ},$$

where the first inequality comes from the fact that $\beta_\circ$ is a probability and the second inequality comes from the condition $\pi_i \geq 0$. Notice that $\pi_f$ is decreasing in $\beta_\circ$ whereas $\pi_i$ is monotonically increasing in that parameter. Maximizing the expected return to the firm conditioned to a positive expected return to the investor defines the optimal value of $\beta_\circ$ as the lowest possible. Thus

$$\beta_\circ = \frac{K}{q(y - S) + (1 - q)L_\circ}.$$

Both $S$ and $L_\circ$ (and thus also $\beta_\circ$) are still to be specified. There is no need to specify $L_x$, since the main feature of the optimal contract just described is that there is no liquidation in the good state. Liquidation occurs only, if at all, in the case of a poor performance. In order to understand what determines $S$ and $L_\circ$ some additional assumptions are required.

It is assumed that the entrepreneur is not able to continue managing the project in the case of bankruptcy after a zero cash flow. This is the case of a *liquidity default*. In that case, the creditor may sell the position to a third party who obtains at $t = 2$ a cash flow $\alpha y$, with $\alpha \in [0, 1]$, meaning that the incoming manager cannot get better results out of the assets than the manager who left the firm.

In the case of bankruptcy after a nonzero cash flow, the original manager will negotiate the buyback of the firm with the creditholder, sharing the second-period return $y$. In that situation, $S = y/2$. This is the case of a *strategic default*.

It is also assumed that, in the case of liquidity default, the buyer of the assets incurs an informational cost $c \in [0, \bar c]$. This cost is modeled as a uniformly distributed random variable. Therefore, by a negotiating process similar to the preceding, the remaining value of the assets, $\alpha y$, is equally divided between the creditor and the buyer. The buyer then negotiates only if $c \leq \alpha y/2$. Thus, assuming that $\alpha y/2 \leq \bar c$, the probability that this happens is

$$\Pr\left(c \leq \frac{\alpha y}{2}\right) = \frac{\alpha y}{2\bar c}.$$

Therefore, the expected value of the liquidation payoff in the case of a zero cash flow at $t = 1$ is

$$L_\circ = \frac{\alpha^2 y^2}{4\bar c},$$

and the optimal $\beta_\circ$ reads

$$\beta_\circ = \frac{K}{q\frac{y}{2} + (1 - q)\frac{\alpha^2 y^2}{4\bar c}}. \qquad (5.8)$$

[…]

*From Amaro de Matos §5.2.2 "The Case of Many Creditholders", pp. 137–138 (PDF 155–156):*

Bolton and Scharfstein (1996) bring to this discussion a related issue: The crucial element is the number, nature, and type of creditors—in other words, whether credit is private or public, whether it is granted by banks or obtained by issuing bonds in the marketplace, and also the nature of the governance structure among the creditors.

In this setting assume that at time $t = 0$ the amount $K$ is invested to acquire the assets $A$ and $B$. These are the assets that constitute the investment project. If there are two creditors, assume that each of the assets $A$ and $B$ provides collateral for each of them. Denoting by $y^A$ and $y^B$ the cash flows for assets $A$ and $B$, as managed separately, one defines $\Delta = y - y^A - y^B$, which is assumed to be positive. This means that the cash flow generated by both assets is assumed to be greater than the sum of the cash flow generated by each of the assets individually. It is then possible to show that the expected value of liquidation at time $t = 1$ is given by

$$\overline{L}_\circ = \frac{\alpha^2 y^2}{4\bar c} - \frac{\alpha^2 \Delta^2}{36\bar c} < \frac{\alpha^2 y^2}{4\bar c} = L_\circ.$$

In other words, in the case of two creditors, the expected value of liquidation when there is a zero cash flow at $t = 1$ is lower than the value expected with only one creditor. Moreover, in the state with probability $q$,

$$S = \frac{y}{2} - \frac{\Delta}{6},$$

leading to an optimal value of $\beta_\circ$ with a denominator given by

$$q\left(\frac{y}{2} - \frac{\Delta}{6}\right) + (1 - q)\left(\frac{\alpha^2 y^2}{4\bar c} - \frac{\alpha^2 \Delta^2}{36\bar c}\right),$$

which can be greater or less than the similar value found before with only one creditor. […]

---

### 11. When the good entrepreneur prefers liquidating debt
**Source:** Amaro de Matos, Ch. 5, Exercise 5.2.5 #4, p. 148 (PDF 166) · Answer in book: no (p. 268 only cites the appendix of Diamond 1991, pp. 732–733)

4. Prove that inequality (5.12) provides a sufficient condition for the good entrepreneur to prefer the debt structure that leads to liquidation under the conditions of the lemma to which it refers.

#### Context needed to solve it

*From Amaro de Matos §5.2.3 "The Choice of the Duration", pp. 139–141 (PDF 157–159):*

A model developed by Diamond (1991, 1993) illustrates in a very simple way the differences between short-term and long-term debt financing. The model is based on information asymmetry and credit rating.

Regaining the notation of Aghion and Bolton, consider an entrepreneur with a two-period project who needs funds for an initial investment $K = 1$. The project may be of one of two types: good or bad. At time $t = 2$ a good project has a payoff $X > 0$, whereas a bad project pays that amount with a probability $\pi$, and pays zero with probability $1 - \pi$. Let $\theta$ denote the type of project, $\theta_g$ referring to a good project and $\theta_b$ referring to a bad project. The quality of the project is known to the entrepreneur but not to the investor. Given a project, as of date $t = 0$ the investor assigns a probability $f$ that $\theta = \theta_g$. This probability is referred to as a *credit rating* and reflects the lender's information about the project. It follows that, as of time 0, the probability $q$ that a borrower pays the loan at date $t = 2$ is given by

$$q \equiv f + \pi(1 - f) = \pi + f(1 - \pi). \qquad (5.9)$$

At time $t = 1$ information about the project becomes available to the investor. This new information is not verifiable, so it makes no sense to write contracts contingent upon that information, since they cannot be enforced. However, the investors update their beliefs about the quality of the project and the credit rating will be either upgraded or downgraded.

Under this revision of the credit rating, let $f^u$ denote the probability that $\theta = \theta_g$ given an upgrade and let $f^d$ denote the probability that $\theta = \theta_g$ given a downgrade. In that case, the probability that an entrepreneur who receives a downgrade repays at time $t = 2$ is

$$q^d = \pi + f^d(1 - \pi) > f^d. \qquad (5.10)$$

Moreover, it is here assumed that

$$f^d < f < f^u,$$

meaning that the probability that the project is good is greater given an upgrade than given a downgrade. Furthermore, the simplifying assumption $f^u = 1$ is also made. Thus, given an upgrade at date $t = 1$, it is certain that the project is good. However, it is not certain that all projects of good quality are upgraded. There is room for one such project to be downgraded. Let $e$ denote the probability of such an event.

All projects are also assumed to produce a nonassignable control rent $C$ if the management has control at time $t = 2$. Also, if at time $t = 1$ the manager defaults on short-term debt, lenders then have the right to remove the management from control, selling the assets for a liquidation value $L < K = 1$. All projects may be liquidated at that point in time, under those conditions. If the project is liquidated, the entrepreneur is prevented from consumption of his/her present or future cash flows and control rents. In this case, an optimal contract is a debt contract enforced by the right to liquidate the project if the debt is not repaid in full.

Just as in the case of the borrowers, lenders are assumed be risk neutral. Moreover, lenders have alternative investments at $t = 0$ that provide a return $R$ at $t = 2$. The condition $L < X/R$ ensures that a good project yields a higher return when not liquidated.

A project may be financed with either long-term or short-term debt. In the context of this model, long-term debt refers to a contract issued at $t = 0$ with no refinancing at date $t = 1$ and maturing at $t = 2$. If one such instrument provides $K = 1$ at time $t = 0$ with face value $\rho \le X$, the lender expects to receive at maturity $\rho[\pi + f(1 - \pi)] = R^2$. Notice that if $\rho > X$, a borrower with credit rating $f$ will not be able to provide the lender with the required rate of return $R^2$. Now, if the project is upgraded at time $t = 1$, the market value of the debt contract at that point in time becomes $V_l^u = \rho/R$. Similarly, if the project is downgraded, the market value of debt at time $t = 1$ becomes $V_l^d = q^d\rho/R$.

Short-term debt, on the other hand, is debt financed at $t = 0$ with face value $r_1$ and maturity at time $t = 1$. If short-term borrowers are upgraded at $t = 1$, their debt contract at that point in time is worth $V_s^u = r_1$ and they may refinance their project by issuing a new short-term debt contract with maturity at $t = 2$ and face value $r_1 R$ that will be paid with certainty and guarantees a return of $R$ per unit invested by the lender. If short-term borrowers are downgraded, however, in principle they may refinance their debt with a new short-term contract only if $q^d X/R > r_1$, since $X$ is the maximum that a borrower can pay at $t = 2$. If that is the case, at $t = 1$ the market value of the short-term debt issued at $t = 0$ would be $V_s^d = r_1$ if the borrower pays, possibly through the refinancement mechanism. But what happens if $q^d X/R < r_1$? In that case there is still room for a refinancement provided that the liquidation value $L$ is less than the expected value to the lender from a refinancement, $q^d X/R$. Under a downgrading, the time $t = 1$ value of the short-term debt is thus

$$V_s^d = \min\left[r_1, \max(L, q^d X/R)\right].$$

The face value of short-term debt is established such as to provide the lenders with an expected return of $R$ per period. It then follows that

$$r_1 = \frac{R - [1 - (1 - e)f]V_s^d}{(1 - e)f}. \qquad (5.11)$$

*From Amaro de Matos §5.2.3, pp. 141–142 (PDF 159–160):*

Given this model, the point is to characterize under what conditions short-term or long-term maturities will be offered. The maturity preferred by the entrepreneurs of good projects will be the only one offered to all borrowers. This happens because if any other maturity is offered, it reveals a project of bad quality and lenders will not be willing to finance it.

The following result implies that, in the absence of liquidation given a downgrade, the entrepreneurs of good projects prefer short-term debt:

**Lemma 5.2.1 (Diamond, 1991).** *Comparing two debt contracts issued at $t = 0$, neither of which involves liquidation on a downgrade at $t = 1$, the one with the higher value at that point in time given a downgrade, $V^d$, is preferred by the entrepreneurs of good projects.*

*Proof.* The expected payoff to the entrepreneurs of good projects from debt not yielding liquidation is

$$e\left(X + C - \frac{RV^d}{q^d}\right) + (1 - e)(X + C - r_1 R).$$

Using expression (5.11) this payoff is rewritten as

$$X + C - \frac{R^2}{f} + RV^d e\left(\frac{1}{f^d} - \frac{1}{q^d}\right).$$

Given (5.10) this expression for the payoff is clearly an increasing function of $V^d$. ■

*From Amaro de Matos §5.2.3, p. 142 (PDF 160):*

This implies that when there is no liquidation after a downgrade, short-term debt is preferred. The idea behind this result is simple. If there is no risk of liquidation, in order to reduce their expected financing costs, borrowers of the good type, who are less likely than average to be downgraded, prefer to extract larger payments from those who are downgraded. However, if there is the possibility of liquidation, the increase in the payment extracted from those who get a downgrade incorporates, for the good entrepreneurs, the risk of losing control rents. In that case the following result characterizes the trade-off incurred:

**Lemma 5.2.2 (Diamond, 1991).** *Consider a debt structure that does not imply liquidation and leads to a value of debt $V^d$, given a downgrade. Compare it with an alternative structure that implies liquidation. Entrepreneurs of good projects prefer the latter if and only if the control rent $C < \widehat C$, where the upper bound is given by*

$$\widehat C = \frac{LR}{f^d} - X - RV^d\left(\frac{1}{f^d} - \frac{1}{q^d}\right) > 0.$$

It follows that a sufficient condition for the good entrepreneur to prefer liquidation is that $C = 0$, representing the absence of control rents. It is also sufficient for the good entrepreneur to prefer liquidation if that state does not provide sufficiently high control rents $C$ to the entrepreneur compared to the proceeds $L$ to the investor or

$$\frac{q^d X + f^d C}{R} \le L. \qquad (5.12)$$

---

### 12. Diamond (1991): liquidation after a downgrade
**Source:** Amaro de Matos, Ch. 5, Exercise 5.2.5 #6, p. 148 (PDF 166) · Answer in book: no (p. 268 only cites examples 2 and 3 of Diamond 1991, pp. 717–719)

6. This exercise illustrates the case of Lemma 5.2.2 in the model of Diamond (1991). Keep everything from the previous exercise except that here $X = 1.4$ and $C = 0.35$. Show that in this case, if the project is financed with short-term debt, it will be liquidated in the case of a downgrade at $t = 1$. Show also that this leads the entrepreneur of a good project to prefer long-term to short-term debt. Finally, show that this conclusion is reversed if the initial credit rating is $f = \frac{3}{4}$ instead of the initial $\frac{1}{2}$.

#### Context needed to solve it

**Part 0.** *From Amaro de Matos, Ch. 5, Exercise 5.2.5 #5, p. 148 (PDF 166) — "the previous exercise":*

5. This exercise illustrates the case of Lemma 5.2.1 in the model of Diamond (1991). Take $L = R = 1$, $\pi = \frac{1}{2}$, $X = 1\frac{3}{4}$, $C = 0$, $f = \frac{1}{2}$, and $f^d = \frac{1}{3}$.

(a) What are the face values of a short-term and a long-term debt contract?

(b) Show that in this example there will be no liquidation.

(c) What is the payoff of a good project financed with long-term debt?

(d) What is the probability that a good project receives a downgrade at $t = 1$?

(e) What is the payoff of a good project financed with short-term debt?

*From Amaro de Matos §5.2.3 "The Choice of the Duration", pp. 139–141 (PDF 157–159):*

A model developed by Diamond (1991, 1993) illustrates in a very simple way the differences between short-term and long-term debt financing. The model is based on information asymmetry and credit rating.

Regaining the notation of Aghion and Bolton, consider an entrepreneur with a two-period project who needs funds for an initial investment $K = 1$. The project may be of one of two types: good or bad. At time $t = 2$ a good project has a payoff $X > 0$, whereas a bad project pays that amount with a probability $\pi$, and pays zero with probability $1 - \pi$. Let $\theta$ denote the type of project, $\theta_g$ referring to a good project and $\theta_b$ referring to a bad project. The quality of the project is known to the entrepreneur but not to the investor. Given a project, as of date $t = 0$ the investor assigns a probability $f$ that $\theta = \theta_g$. This probability is referred to as a *credit rating* and reflects the lender's information about the project. It follows that, as of time 0, the probability $q$ that a borrower pays the loan at date $t = 2$ is given by

$$q \equiv f + \pi(1 - f) = \pi + f(1 - \pi). \qquad (5.9)$$

At time $t = 1$ information about the project becomes available to the investor. This new information is not verifiable, so it makes no sense to write contracts contingent upon that information, since they cannot be enforced. However, the investors update their beliefs about the quality of the project and the credit rating will be either upgraded or downgraded.

Under this revision of the credit rating, let $f^u$ denote the probability that $\theta = \theta_g$ given an upgrade and let $f^d$ denote the probability that $\theta = \theta_g$ given a downgrade. In that case, the probability that an entrepreneur who receives a downgrade repays at time $t = 2$ is

$$q^d = \pi + f^d(1 - \pi) > f^d. \qquad (5.10)$$

Moreover, it is here assumed that

$$f^d < f < f^u,$$

meaning that the probability that the project is good is greater given an upgrade than given a downgrade. Furthermore, the simplifying assumption $f^u = 1$ is also made. Thus, given an upgrade at date $t = 1$, it is certain that the project is good. However, it is not certain that all projects of good quality are upgraded. There is room for one such project to be downgraded. Let $e$ denote the probability of such an event.

All projects are also assumed to produce a nonassignable control rent $C$ if the management has control at time $t = 2$. Also, if at time $t = 1$ the manager defaults on short-term debt, lenders then have the right to remove the management from control, selling the assets for a liquidation value $L < K = 1$. All projects may be liquidated at that point in time, under those conditions. If the project is liquidated, the entrepreneur is prevented from consumption of his/her present or future cash flows and control rents. In this case, an optimal contract is a debt contract enforced by the right to liquidate the project if the debt is not repaid in full.

Just as in the case of the borrowers, lenders are assumed be risk neutral. Moreover, lenders have alternative investments at $t = 0$ that provide a return $R$ at $t = 2$. The condition $L < X/R$ ensures that a good project yields a higher return when not liquidated.

A project may be financed with either long-term or short-term debt. In the context of this model, long-term debt refers to a contract issued at $t = 0$ with no refinancing at date $t = 1$ and maturing at $t = 2$. If one such instrument provides $K = 1$ at time $t = 0$ with face value $\rho \le X$, the lender expects to receive at maturity $\rho[\pi + f(1 - \pi)] = R^2$. Notice that if $\rho > X$, a borrower with credit rating $f$ will not be able to provide the lender with the required rate of return $R^2$. Now, if the project is upgraded at time $t = 1$, the market value of the debt contract at that point in time becomes $V_l^u = \rho/R$. Similarly, if the project is downgraded, the market value of debt at time $t = 1$ becomes $V_l^d = q^d\rho/R$.

Short-term debt, on the other hand, is debt financed at $t = 0$ with face value $r_1$ and maturity at time $t = 1$. If short-term borrowers are upgraded at $t = 1$, their debt contract at that point in time is worth $V_s^u = r_1$ and they may refinance their project by issuing a new short-term debt contract with maturity at $t = 2$ and face value $r_1 R$ that will be paid with certainty and guarantees a return of $R$ per unit invested by the lender. If short-term borrowers are downgraded, however, in principle they may refinance their debt with a new short-term contract only if $q^d X/R > r_1$, since $X$ is the maximum that a borrower can pay at $t = 2$. If that is the case, at $t = 1$ the market value of the short-term debt issued at $t = 0$ would be $V_s^d = r_1$ if the borrower pays, possibly through the refinancement mechanism. But what happens if $q^d X/R < r_1$? In that case there is still room for a refinancement provided that the liquidation value $L$ is less than the expected value to the lender from a refinancement, $q^d X/R$. Under a downgrading, the time $t = 1$ value of the short-term debt is thus

$$V_s^d = \min\left[r_1, \max(L, q^d X/R)\right].$$

The face value of short-term debt is established such as to provide the lenders with an expected return of $R$ per period. It then follows that

$$r_1 = \frac{R - [1 - (1 - e)f]V_s^d}{(1 - e)f}. \qquad (5.11)$$

*From Amaro de Matos §5.2.3, pp. 141–142 (PDF 159–160):*

Given this model, the point is to characterize under what conditions short-term or long-term maturities will be offered. The maturity preferred by the entrepreneurs of good projects will be the only one offered to all borrowers. This happens because if any other maturity is offered, it reveals a project of bad quality and lenders will not be willing to finance it.

The following result implies that, in the absence of liquidation given a downgrade, the entrepreneurs of good projects prefer short-term debt:

**Lemma 5.2.1 (Diamond, 1991).** *Comparing two debt contracts issued at $t = 0$, neither of which involves liquidation on a downgrade at $t = 1$, the one with the higher value at that point in time given a downgrade, $V^d$, is preferred by the entrepreneurs of good projects.*

*Proof.* The expected payoff to the entrepreneurs of good projects from debt not yielding liquidation is

$$e\left(X + C - \frac{RV^d}{q^d}\right) + (1 - e)(X + C - r_1 R).$$

Using expression (5.11) this payoff is rewritten as

$$X + C - \frac{R^2}{f} + RV^d e\left(\frac{1}{f^d} - \frac{1}{q^d}\right).$$

Given (5.10) this expression for the payoff is clearly an increasing function of $V^d$. ■

*From Amaro de Matos §5.2.3, p. 142 (PDF 160):*

This implies that when there is no liquidation after a downgrade, short-term debt is preferred. The idea behind this result is simple. If there is no risk of liquidation, in order to reduce their expected financing costs, borrowers of the good type, who are less likely than average to be downgraded, prefer to extract larger payments from those who are downgraded. However, if there is the possibility of liquidation, the increase in the payment extracted from those who get a downgrade incorporates, for the good entrepreneurs, the risk of losing control rents. In that case the following result characterizes the trade-off incurred:

**Lemma 5.2.2 (Diamond, 1991).** *Consider a debt structure that does not imply liquidation and leads to a value of debt $V^d$, given a downgrade. Compare it with an alternative structure that implies liquidation. Entrepreneurs of good projects prefer the latter if and only if the control rent $C < \widehat C$, where the upper bound is given by*

$$\widehat C = \frac{LR}{f^d} - X - RV^d\left(\frac{1}{f^d} - \frac{1}{q^d}\right) > 0.$$

It follows that a sufficient condition for the good entrepreneur to prefer liquidation is that $C = 0$, representing the absence of control rents. It is also sufficient for the good entrepreneur to prefer liquidation if that state does not provide sufficiently high control rents $C$ to the entrepreneur compared to the proceeds $L$ to the investor or

$$\frac{q^d X + f^d C}{R} \le L. \qquad (5.12)$$

*Omitted: Proposition 5.2.1 (p. 142, PDF 160), which gives the credit-rating bound above which good entrepreneurs prefer short-term debt; applied to these numbers it states the exercise's conclusion.*

---

### 13. A borrower-friendly bankruptcy court
**Source:** Tirole, Ch. 4, Exercise 4.9, pp. 190–191 (PDF 203) · Answer in book: yes, p. 586

**Exercise 4.9 (borrower-friendly bankruptcy court).** Consider the timing described in Figure 4.7.

Figure 4.7 (timeline, left to right; p. 191, PDF 204)

| Date 0 | Date 1 | | Date 2 |
|---|---|---|---|
| Investment, contract. Entrepreneur has cash $A$, must borrow $I - A$. | Short-term profit realized. Liquidate → Liquidation value $L$ (known); or Continue → | Moral hazard: Effort decision (high or low). | Final profit: Success (profit $R$) or failure (profit 0)? |

The project, if financed, yields random and verifiable short-term profit $r \in [0, \bar r]$ (with a continuous density and *ex ante* mean $E[r]$). After $r$ is realized and cashed in, the firm either liquidates (sells its assets), yielding some known liquidation value $L > 0$, or continues. Note that (the random) $r$ and (the deterministic) $L$ are not subject to moral hazard. If the firm continues, its prospects improve with $r$ (so $r$ is "good news" about the future). Namely, the probability of success is $p_H(r)$ if the entrepreneur works between dates 1 and 2 and $p_L(r)$ if the entrepreneur shirks. Assume that $p_H' > 0$, $p_L' > 0$, and

$$p_H(r) - p_L(r) \equiv \Delta p$$

is independent of $r$ (so shirking reduces the probability of success by a fixed amount independent of prospects). As usual, one will want to induce the entrepreneur to work if continuation obtains. It is convenient to use the notation

$$\rho_1(r) \equiv p_H(r)R \quad \text{and} \quad \rho_0(r) \equiv p_H(r)\left[R - \frac{B}{\Delta p}\right].$$

Investors are competitive and demand an expected rate of return equal to 0. Assume

$$\rho_1(r) > L \quad \text{for all } r \qquad (1)$$

and

$$E[r] + L > I - A > E[r + \rho_0(r)]. \qquad (2)$$

(i) Argue informally that, in the optimal contract for the borrower, the short-term profit and the liquidation value (if the firm is liquidated) ought to be given to investors.

Argue that, in the case of continuation, $R_b = B/\Delta p$. (If you are unable to show why, take this fact for granted in the rest of the question.)

Interpret conditions (1) and (2).

(ii) Write the borrower's optimization program.

Assume (without loss of generality) that the firm continues if and only if $r \geqslant r^*$ for some $r^* \in (0, r)$. Exhibit the equation defining $r^*$.

(iii) Argue that this optimal contract can be implemented using, inter alia, a short-term debt contract at level $d = r^*$. Interpret "liquidation" as a "bankruptcy."

How does short-term debt vary with the borrower's initial equity? Explain.

(iv) Suppose that, when the decision to liquidate is taken, the firm must go to a bankruptcy court. The judge mechanically splits the bankruptcy proceeds $L$ equally between investors and the borrower.

Define $\hat r$ by

$$\rho_0(\hat r) \equiv \tfrac{1}{2}L.$$

Assume first that

$$r^* > \hat r$$

(where $r^*$ is the value found in question (ii)).

Show that the borrower-friendly court actually prevents the borrower from having access to financing. (Note: a diagram may help.)

(v) Continuing on question (iv), show that when

$$r^* < \hat r,$$

the borrower-friendly court either prevents financing or increases the probability of bankruptcy, and in all cases hurts the borrower and not the lenders.

#### Context needed to solve it

The statement defines its own model; "as usual" refers to the fixed-investment model's moral-hazard setup (private benefit $B$, limited liability, incentive constraint), copied here.

*From Tirole §3.2.1 "The Fixed-Investment Model", pp. 115–116 (PDF 128–129):*

Variants of the following entrepreneurial model will be used in the following: an entrepreneur (also called the "insider" or the "borrower," "she") has a project. This project requires a fixed investment $I$. The entrepreneur initially has "assets" ("cash on hand" or "net worth") $A < I$. For the moment we interpret these assets as being cash or liquid securities that can be used toward covering the cost of investment. […] The entrepreneur's cash can either be invested in the project or used for consumption. To implement the project the entrepreneur must borrow $I - A$ from lenders. […]

*Project.* If undertaken, the project either succeeds, that is, yields verifiable income $R > 0$, or fails, that is, yields no income. The probability of success is denoted by $p$. The project is subject to moral hazard. The entrepreneur can "behave" ("work," "exert effort," "take no private benefit") or "misbehave" ("shirk," "take a private benefit") […].

Behaving yields probability $p = p_H$ of success and no private benefit to the entrepreneur, and misbehaving results in probability $p = p_L < p_H$ of success and private benefit $B > 0$ (measured in units of account) to the entrepreneur. In the "effort interpretation," $B$ can also be interpreted as a disutility of effort saved by the entrepreneur when shirking. Let $\Delta p \equiv p_H - p_L$.

*Preferences and the loan agreement.* Both the borrower and the potential lenders (or "investors") are risk neutral. For notational simplicity, there is no time preference; the rate of return expected by investors (which is also the riskless rate, due to risk neutrality) is taken to be 0. The borrower is protected by limited liability, and so her income cannot take negative values.

Lenders behave competitively in the sense that the loan, if any, makes zero profit. […]

Let us turn to the loan contract. A contract first stipulates whether the project is financed. If so, it further specifies how the profit is shared between the lenders and the borrower. The borrower's limited liability will imply that both sides receive 0 in the case of failure […]. In the case of success, the two parties share the profit $R$; $R_b$ goes to the borrower and $R_l$ to the lenders. To sum up, we posit an incentive scheme for the entrepreneur of the following form: $R_b$ in the case of success, 0 in the case of failure.

*From Tirole §3.2.2 "The Lenders' Credit Analysis", pp. 116–117 (PDF 129–130):*

[…] the borrower will therefore behave if the following "incentive compatibility constraint" is satisfied:

$$p_H R_b \geqslant p_L R_b + B \quad \text{or} \quad (\Delta p) R_b \geqslant B. \qquad (\text{IC}_b)$$

From this incentive compatibility constraint we infer that the highest income in the case of success that can be pledged to the lenders without jeopardizing the borrower's incentives is

$$R - \frac{B}{\Delta p}.$$

The *(expected) pledgeable income* is then

$$\mathcal{P} = p_H\left(R - \frac{B}{\Delta p}\right).$$

