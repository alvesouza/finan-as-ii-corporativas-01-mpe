---
tags: [exercise-list, ricca-r3, mm-taxes-tradeoff]
date: 2026-10-24
---

# Exercise list R3 — A frictionless benchmark, taxes, distress and static trade-off theory

Ricca topic 3: complete markets and arbitrage, MM I (homemade leverage, risky debt), MM II and the WACC, the interest tax shield, APV vs. WACC, personal taxes (Miller), bankruptcy costs and the static trade-off, payout irrelevance, and the bank capital debate. 18 exercises. Exercises 1–15 run from easy to really hard and are copied verbatim from the course books for personal study; pages are printed page numbers (PDF page in brackets). Exercises 16–18 (easy → really hard) are **original exercises**, not book exercises: they cover the bank capital debate (Admati et al. 2013, "bank equity is not socially expensive", Prof. Ricca's Topic 2B slides 46–47), which has no exercise in any of the six course books. The user agreed on 2026-11-12 to original exercises for this topic; each one opens with an `**Origin:**` line instead of a `**Source:**` line, and its answer is in the solutions file. Links: [[Map/exercises-index|exercise index]] · [[rules/03_benchmark_mm|rules]].

## References
| # | Tier | Book | Ch. | Exercise | Printed p. | Answer in book | Trains |
|---|---|---|---|---|---|---|---|
| 1 | 1 Easy | Berk | 16 | 16.1 | 490 (PDF 521) | no | MM with safe debt: value of unlevered and levered equity of a two-outcome project |
| 2 | 1 Easy | Berk | 17 | 17.7 | 528 (PDF 559) | no | Dividend vs. repurchase in a perfect market: ex-dividend and post-repurchase prices |
| 3 | 1 Easy | Ross | 16 | 16.14 | 578 (PDF 602) | no (selected answers in the web-only Apêndice C) | MM I with corporate taxes: $V_L = V_U + T_C D$ for perpetual debt |
| 4 | 1 Easy | Higgins | 8 | 8.23 | 333 (PDF 354) | yes, p. 425 | APV = base-case NPV + PV of interest tax shields on constant debt |
| 5 | 1 Easy | Berk | 16 | 16.5 | 491 (PDF 522) | no | MM II with rising $r_D$; why the highest expected equity return is not the goal |
| 6 | 2 Exam | Berk | 16 | 16.11 | 492 (PDF 523) | no | PV of tax shields on amortising debt discounted at $r_D$ |
| 7 | 2 Exam | Ross | 16 | 16.18 | 578 (PDF 602) | no (selected answers in the web-only Apêndice C) | MM I by arbitrage: homemade leverage between a levered and an unlevered twin |
| 8 | 2 Exam | Berk | 16 | 16.22 | 494 (PDF 525) | no | Trade-off: share price with tax shield, implied PV of financial distress costs |
| 9 | 2 Exam | Grinblatt | 13 | 13.15–13.16 | 494 (PDF 507) | no | $r_E$ and after-tax WACC with riskless perpetual debt; WACC after a debt-for-equity swap (Hamada) |
| 10 | 2 Exam | Grinblatt | 16 | 16.2 | 591–592 (PDF 604) | no | Static trade-off in two states: tax saving per dollar of debt vs. a fixed bankruptcy cost |
| 11 | 2 Exam | Grinblatt | 14 | 14.2–14.3 | 526–527 (PDF 539) | no | Risky debt in a binomial market, equal-seniority new debt, undoing leverage, MM still holds |
| 12 | 3 Really hard | Berk | 16 | 16.18* | 493 (PDF 524) | no | Leveraged recap with taxes: market-value balance sheets, price at announcement, shares repurchased |
| 13 | 3 Really hard | Ross | 16 | 16.19 (DESAFIO) | 578 (PDF 602) | no (selected answers in the web-only Apêndice C) | Derive the MM adjusted cost of capital $R_U[1 - T_C(D/V)]$ |
| 14 | 3 Really hard | Amaro de Matos | 2 | 2.2.7 #1 | 58 (PDF 76) | yes, p. 255 | Proof of Miller's gain from leverage with corporate and personal taxes |
| 15 | 3 Really hard | Amaro de Matos | 2 | 2.1.5 #3–#4 | 48 (PDF 66) | yes, pp. 252–254 | MM I with perpetual debt (with and without taxes) and its breakdown with unequal borrowing/lending rates |
| 16 | 1 Easy | Original | — | — | Topic 2B slides 46–47; Topic 2A slides 97–102 | no (solutions file) | Bank capital without taxes: ROE and its risk at 4% and 20% equity, MM II, constant WACC; Statements 1 and 2 |
| 17 | 2 Exam | Original | — | — | Topic 2B slides 7–18, 47 | no (solutions file) | Bank capital with corporate taxes: lost interest tax shield, after-tax WACC, private cost vs. transfer from taxpayers; Statement 3 |
| 18 | 3 Really hard | Original | — | — | Topic 2B slides 44–47 | no (solutions file) | Failure externality: socially optimal capital ratio, the bank's private choice, how the fallacies bias the requirement |

## Tier 1 — Easy

### 1. Two-outcome project financed with equity or safe debt
**Source:** Berk, Ch. 16, Exercise 16.1, p. 490 (PDF 521) · Answer in book: no

Consider a project with free cash flows in one year of \$130,000 or \$180,000, with each outcome being equally likely. The initial investment required for the project is \$100,000, and the project's cost of capital is 20%. The risk-free interest rate is 10%.

a. What is the NPV of this project?

b. Suppose that to raise the funds for the initial investment, the project is sold to investors as an all-equity firm. The equity holders will receive the cash flows of the project in one year. How much money can be raised in this way—that is, what is the initial market value of the unlevered equity?

c. Suppose the initial \$100,000 is instead raised by borrowing at the risk-free interest rate. What are the cash flows of the levered equity, and what is its initial value according to MM?

#### Context needed to solve it

*From Berk Ch. 16, Problems, section "Capital Structure in Perfect Capital Markets" (instruction that heads this problem section), p. 490 (PDF 521):*

For problems in this section assume no taxes or distress costs.

---

### 2. One-time dividend or repurchase in a perfect market
**Source:** Berk, Ch. 17, Exercise 17.7, p. 528 (PDF 559) · Answer in book: no

Natsam Corporation has \$250 million of excess cash. The firm has no debt and 500 million shares outstanding with a current market price of \$15 per share. Natsam's board has decided to pay out this cash as a one-time dividend.

a. What is the ex-dividend price of a share in a perfect capital market?

b. If the board instead decided to use the cash to do a one-time share repurchase, in a perfect capital market, what is the price of the shares once the repurchase is complete?

c. In a perfect capital market, which policy in part (a) or (b) makes investors in the firm better off?

---

### 3. MM I with corporate taxes
**Source:** Ross, Cap. 16, Exercise 16.14, p. 578 (PDF 602) · Answer in book: no (selected answers in the web-only Apêndice C)

A Frederico & Co. espera um Lajir de \$92.000 por ano para sempre. A empresa pode tomar empréstimos a 9%. Atualmente, a Frederico não tem dívida, e o custo do capital próprio é 15%. Se a alíquota tributária for 35%, qual será o valor da empresa? Qual será o valor se a empresa tomar empréstimos de \$60.000 e usar a receita para recomprar ações?

---

### 4. APV with constant debt
**Source:** Higgins, Ch. 8, Exercise 8.23, p. 333 (PDF 354) · Answer in book: yes, p. 425

You are valuing a project for Gila Corp. using the APV method. You already found the net present value of free cash flows from the project (discounted at the appropriate cost of equity) to be \$500,000. The only important side effect of financing is the present value of interest tax shields. The project will be partially financed by a constant \$1 million in debt over the life of the project, which is three years. Gila's tax rate is 40 percent, and the current interest rate applicable for the project's debt is 8 percent (assume this rate is also appropriate for discounting the interest tax shields). Assuming tax shields are realized at the end of each year, what is the APV of the project?

---

### 5. MM II with a rising cost of debt
**Source:** Berk, Ch. 16, Exercise 16.5, p. 491 (PDF 522) · Answer in book: no

Hardmon Enterprises is currently an all-equity firm with an expected return of 12%. It is considering borrowing money to buy back some of its existing shares, thus increasing its leverage.

a. Suppose Hardmon borrows to the point that its debt-equity ratio is 0.50. With this amount of debt, the debt cost of capital is 6%. What will the expected return of equity be after this transaction?

b. Suppose instead Hardmon borrows to the point that its debt-equity ratio is 1.50. With this amount of debt, Hardmon's debt will be much riskier. As a result, the debt cost of capital will be 8%. What will the expected return of equity be in this case?

c. A senior manager argues that it is in the best interest of the shareholders to choose the capital structure that leads to the highest expected return for the stock. How would you respond to this argument?

#### Context needed to solve it

*From Berk Ch. 16, Problems, section "Capital Structure in Perfect Capital Markets" (instruction that heads this problem section), p. 490 (PDF 521):*

For problems in this section assume no taxes or distress costs.

---

## Tier 2 — Exam level

### 6. Tax shields on amortising debt
**Source:** Berk, Ch. 16, Exercise 16.11, p. 492 (PDF 523) · Answer in book: no

Your firm currently has \$100 million in debt outstanding with a 10% interest rate. The terms of the loan require the firm to repay \$25 million of the balance each year. Suppose that the marginal corporate tax rate is 40%, and that the interest tax shields have the same risk as the loan. What is the present value of the interest tax shields from this debt?

---

### 7. Homemade leverage between twin firms
**Source:** Ross, Cap. 16, Exercise 16.18, p. 578 (PDF 602) · Answer in book: no (selected answers in the web-only Apêndice C)

As companhias Weber e Cavaleiro são idênticas em todos os aspectos, exceto que a Weber não é alavancada. As informações financeiras das duas empresas são mostradas no quadro a seguir. Todos os grupos de lucros são perpetuidades, e nenhuma das empresas paga impostos. As duas empresas distribuem imediatamente todos os lucros disponíveis aos acionistas.

| | Weber | Cavaleiro |
|---|---|---|
| Lucro operacional projetado | \$400.000 | \$400.000 |
| Juros sobre a dívida ao fim do ano | — | \$72.000 |
| Valor de mercado do capital próprio | \$2.500.000 | \$1.632.000 |
| Valor de mercado da dívida | — | \$1.200.000 |

a. Um investidor que pode tomar emprestado a 6% ao ano deseja comprar 5% do capital da Cavaleiro. Ele poderia aumentar seu retorno comprando 5% do capital da Weber se tomar emprestado de tal forma que os custos líquidos das estratégias sejam iguais?

b. Dadas as duas estratégias de investimentos de (a), qual será a estratégia escolhida pelos investidores? Quando esse processo terminará?

---

### 8. Announcement effect of a debt-financed repurchase with distress costs
**Source:** Berk, Ch. 16, Exercise 16.22, p. 494 (PDF 525) · Answer in book: no

Hawar International is a shipping firm with a current share price of \$5.50 and 10 million shares outstanding. Suppose that Hawar announces plans to lower its corporate taxes by borrowing \$20 million and repurchasing shares, that Hawar pays a corporate tax rate of 30%, and that shareholders expect the change in debt to be permanent.

a. If the only imperfection is corporate taxes, what will the share price be after this announcement?

b. Suppose the only imperfections are corporate taxes and financial distress costs. If the share price rises to \$5.75 after this announcement, what is the PV of financial distress costs Hawar will incur as the result of this new debt?

---

### 9. After-tax WACC with riskless perpetual debt, then a debt-for-equity exchange
**Source:** Grinblatt & Titman, Ch. 13, Exercises 13.15 and 13.16, p. 494 (PDF 507) · Answer in book: no

**[13.15]** The Akron Company consists of \$50 million in perpetual riskless debt and \$50 million in equity. The current market value of its assets is \$100 million and the beta of its equity return is 1.2. Assume the risk-free rate is 8 percent, the expected return of the market portfolio is 13 percent per year, and the CAPM is true. Compute the expected return of Akron's equity and its WACC assuming a 40 percent corporate tax rate.

**[13.16]** Akron, from the last example, is considering an exchange offer where half of Akron's outstanding debt (\$25 million) is retired. The purchase of this debt would be financed by issuing \$25 million in equity to the debt holders of Akron. Assuming debt policy that is consistent with the Hamada model, what will Akron's new WACC be after the exchange offer?

#### Context needed to solve it

*From Grinblatt & Titman Ch. 13, Eq. (13.8), p. 476 (PDF 489):*

$$\text{WACC} = w_E \bar r_E + w_D (1 - T_c) \bar r_D \qquad (13.8)$$

where

- WACC = weighted average cost of capital
- $w_E = \dfrac{E}{D + E}$ = market value of equity over market value of all financing
- $w_D = \dfrac{D}{D + E}$ = market value of debt over market value of all financing
- $T_c$ = marginal corporate tax rate if interest is fully tax deductible (or, more generally, the debt financing subsidy in percentage terms)

The costs of the financing components are

- $\bar r_E$ = the expected return on equity to investors
- $\bar r_D$ = the expected return on debt to investors

*From Grinblatt & Titman Ch. 13, Exhibit 13.1 and "Static Perpetual Risk-Free Debt", pp. 464–465 (PDF 477–478):*

Exhibit 13.1 — Balance Sheet for a Firm with Leverage When Debt Interest Is Corporate Tax Deductible

| Assets | | Liabilities and Equity | |
|---|---|---|---|
| Debt Tax Shield ($TX$) | $T_c D$ | Debt | $D$ |
| Unlevered Assets ($UA$) | $D + E - T_c D$ | Equity | $E$ |

Viewing the assets of the firm with value $A$ as a portfolio of unlevered assets with value $UA$ and debt tax shields with value $TX$ implies that the beta (or expected return) of the assets is the portfolio-weighted average of the betas (or expected returns) of the unlevered assets and debt tax shields; that is

$$\beta_A = \left(\frac{UA}{D + E}\right)\beta_{UA} + \left(\frac{TX}{D + E}\right)\beta_{TX} \qquad (13.1a)$$

and

$$\bar r_A = \left(\frac{UA}{D + E}\right)\bar r_{UA} + \left(\frac{TX}{D + E}\right)\bar r_{TX} \qquad (13.1b)$$

where $\beta_{UA}$ = beta risk of the unlevered assets, $\beta_{TX}$ = beta risk of the debt tax shield, $\bar r_{UA}$ = expected return of the unlevered assets, $\bar r_{TX}$ = expected return of the debt tax shield.

**Static Perpetual Risk-Free Debt.** Let $T_c$ denote the effective corporate tax rate. Exhibit 13.1 has the firm's debt tax shield expressed as

$$TX = T_c D \qquad (13.2)$$

and thus

$$UA = D + E - T_c D \qquad (13.3)$$

The values for $TX$ and $UA$ both in Exhibit 13.1 and in equations (13.2) and (13.3) are developed in a model by Hamada (1972). If the firm issues default-free perpetual debt (that is, debt that never matures) with aggregate face amount of $D$ and interest payments equal to the risk-free rate, each interest payment of $D r_f$ saves $T_c D r_f$ in taxes in the year it is paid. The present value of the tax savings from the interest payments […] is

$$T_c D = \frac{T_c D r_f}{r_f}$$

The same present value is also achieved when the risk-free rate changes over time and the firm rolls over one-period risk-free debt.

The Hamada model assumes that the tax shield is riskless and thus, each period's tax deduction arising from an interest payment should be discounted back to date 0 at the risk-free rate. This implies that the beta of the debt tax shield in the Hamada model is zero. Using this observation, and substituting equations (13.2) and (13.3) into equation (13.1a) yields

$$\beta_A = \left[\frac{D + E - T_c D}{D + E}\right]\beta_{UA} \qquad (13.4)$$

[…] The key assumptions that lead to this result are: (1) The debt is perpetual; in other words, it is either a perpetuity or consists of rolled over short-term debt positions. (2) The debt is default-free and pays the risk-free rate. (3) The face value of the debt and the tax rate do not change over time. The third assumption distinguishes the Hamada model from other models that will be discussed later in this chapter.

**Equity Betas and Asset Betas.** Equity betas are also affected by taxes. Chapter 11 indicated that (assuming risk-free debt) the equity beta is

$$\beta_E = \left(1 + \frac{D}{E}\right)\beta_A \qquad (13.5)$$

[…] With a little simplification, this equation, which is based on the Hamada model, becomes

$$\beta_E = \left[1 + (1 - T_c)\frac{D}{E}\right]\beta_{UA} \qquad (13.6)$$

*From Grinblatt & Titman Ch. 13, Eq. (13.11), p. 481 (PDF 494):*

$$\text{WACC} = \bar r_A - \left(\frac{D}{D + E}\right) T_c\, \bar r_D \qquad (13.11)$$

*From Grinblatt & Titman Ch. 13, "The Adjusted Cost of Capital Formula", p. 482 (PDF 495):*

In the Hamada model, with static perpetual debt, both debt and its tax shield are risk-free, implying $\bar r_D = r_f$, $\beta_{TX} = 0$, and $TX = T_c D$. In this case, the portfolio-weighted average of the expected returns of the unlevered assets and the debt tax shield, given in equation (13.1b), simplifies to

$$\bar r_A = \left(1 - \frac{T_c D}{D + E}\right)\bar r_{UA} + \frac{T_c D}{D + E}\bar r_D$$

If we substitute this equation into equation (13.11), equation (13.11) reduces to Modigliani and Miller's (1963) adjusted cost of capital formula, which gives the firm's WACC as a function of its debt to value ratio:

$$\text{WACC} = \bar r_{UA}\left[1 - T_c \frac{D}{D + E}\right]$$

---

### 10. Taxes vs. bankruptcy costs in two states
**Source:** Grinblatt & Titman, Ch. 16, Exercise 16.2, p. 591 (PDF 604) · Answer in book: no

Nigel decides he can make zippers at night for one period and will have cash flows next period of \$210 if the economy is favorable, and \$66 if the economy is unfavorable. One-third of these proceeds must be paid out in taxes if the firm is all equity financed; however, because of the tax advantage of debt, Nigel saves \$0.05 in taxes for every \$1.00 of debt financing that he uses. Assume investors are risk neutral, the riskless rate is 10 percent per period, and the probability of each state is .5. Also assume that if Nigel's firm goes bankrupt and debt holders take over, the legal fees and other bankruptcy costs total \$20.

a. If Nigel organizes his firm as all equity, what will it be worth?

b. Suppose Nigel's firm sold a zero-coupon bond worth \$44 at maturity next period. How much would the firm receive for the debt?

c. With the debt level above, how much would the equity be worth?

d. How much would the firm be worth?

e. Would the firm be worth more if it had a debt obligation of \$70 next period?

---

### 11. Risky debt in a binomial market and new debt of equal seniority
**Source:** Grinblatt & Titman, Ch. 14, Exercise 14.3 (with Exercise 14.2, on which it builds, as part 0), pp. 526–527 (PDF 539) · Answer in book: no

**[14.2]** Consider a single period binomial setting where the riskless interest rate is zero, and there are no taxes. A firm consists of a machine that will produce cash flows of \$210 if the economy is good and \$80 if the economy is bad. The good and bad states occur with equal risk-neutral probability. Initially, the firm has 100 shares outstanding and debt with a face value of \$50 due at the end of the period. What is the share price of the firm?

**[14.3]** Suppose the firm in exercise 14.2 unexpectedly announces that it will issue additional debt, with the same seniority as existing debt and a face value of \$50. The firm will use the entire proceeds to repurchase some of the outstanding shares.

a. What is the market price of the new debt?

b. Just after the announcement, what will the price of a share jump to?

c. Show how a shareholder with 20 percent of the shares outstanding is better off as a result of this transaction when he or she undoes the leverage change.

d. Show how the Modigliani-Miller Theorem still holds.

---

## Tier 3 — Really hard

### 12. Leveraged recapitalisation with corporate taxes
**Source:** Berk, Ch. 16, Exercise 16.18 (starred), p. 493 (PDF 524) · Answer in book: no

Kurz Manufacturing is currently an all-equity firm with 20 million shares outstanding and a stock price of \$7.50 per share. Although investors currently expect Kurz to remain an all-equity firm, Kurz plans to announce that it will borrow \$50 million and use the funds to repurchase shares. Kurz will pay interest only on this debt, and it has no further plans to increase or decrease the amount of debt. Kurz is subject to a 40% corporate tax rate.

a. What is the market value of Kurz's existing assets before the announcement?

b. What is the market value of Kurz's assets (including any tax shields) just after the debt is issued, but before the shares are repurchased?

c. What is Kurz's share price just before the share repurchase? How many shares will Kurz repurchase?

d. What are Kurz's market value balance sheet and share price after the share repurchase?

---

### 13. Derive the MM adjusted cost of capital
**Source:** Ross, Cap. 16, Exercise 16.19 (DESAFIO), p. 578 (PDF 602) · Answer in book: no (selected answers in the web-only Apêndice C)

Em um mundo com impostos apenas sobre lucros da pessoa jurídica, mostre que o CMPC pode ser escrito como $\text{CMPC} = R_U \times [1 - T_C(D/V)]$.

#### Context needed to solve it

*From Ross Cap. 16, "Impostos e Proposição I de M&M" and "Impostos, o CMPC e a Proposição II", p. 553 (PDF 577):*

Suponhamos que o custo de capital da empresa U seja de 10%. Chamaremos isso de **custo não alavancado de capital** e usaremos o símbolo $R_U$ para representá-lo. Podemos imaginar o $R_U$ como o custo de capital que uma empresa teria se não tivesse dívida. […] O valor da empresa não alavancada ($V_U$) é simplesmente:

$$V_U = \frac{\text{Lajir} \times (1 - T_C)}{R_U}$$

O valor da empresa alavancada ($V_L$) é:

$$V_L = V_U + T_C \times D$$

[…] No Capítulo 14, vimos que, após considerarmos o efeito dos impostos, o CMPC é:

$$\text{CMPC} = (E/V) \times R_E + (D/V) \times R_D \times (1 - T_C)$$

Para calcular esse CMPC, precisamos saber qual é o custo do capital próprio. A Proposição II de M&M com impostos da pessoa jurídica afirma que o custo do capital próprio é:

$$R_E = R_U + (R_U - R_D) \times (D/E) \times (1 - T_C) \qquad [16.4]$$

*From Ross Cap. 16, Tabela 16.6 "Resumo de Modigliani e Miller", part II, p. 555 (PDF 579):*

II. O caso com impostos sobre lucros da pessoa jurídica

A. Proposição I com impostos: o valor da empresa alavancada ($V_L$) é igual ao valor da empresa não alavancada ($V_U$) mais o valor presente do benefício fiscal dos juros:

$$V_L = V_U + T_C \times D$$

onde $T_C$ é a alíquota de impostos da pessoa jurídica, e $D$ é o montante da dívida.

B. Proposição II com impostos: o custo do capital próprio ($R_E$) é:

$$R_E = R_U + (R_U - R_D) \times (D/E) \times (1 - T_C)$$

onde $R_U$ é o custo não alavancado de capital, isto é, o custo de capital da empresa caso não haja dívida.

---

### 14. Miller's gain from leverage with personal taxes
**Source:** Amaro de Matos, Ch. 2, Exercise 2.2.7 #1, p. 58 (PDF 76) · Answer in book: yes, p. 255

Show that in the presence of personal income tax and corporate income tax, the gain from leverage to stockholders is given by the expression

$$G_L = \left[1 - \frac{(1-\tau_c)(1-\tau_s)}{1-\tau_b}\right] B$$

where $B$ denotes the market value of the debt in the leveraged firm.

#### Context needed to solve it

*From Amaro de Matos §2.2 "Personal and Corporate Taxation" and §2.2.1 "Demand for Bonds", p. 49 (PDF 67):*

On the basis of Miller's argument, there is the underlying assumption that taxes are differentiated. Consider here that besides the tax on corporate profits under which interest payments are deductible, hereby denoted by $\tau_c$, there are also personal income taxes denoted by $\tau_b$ and $\tau_s$ that are applicable, respectively, to bonds and to shares. […]

To study the demand for bonds, consider the existence of two types of bonds: fully tax-exempt bonds, with equilibrium rate of return $r_\circ$, and the other bonds, which are not tax-exempt and have a required rate of return $r_b$. The after-tax rate of return on these latter bonds is $(1 - \tau_b) r_b$. There is demand for the nonexempt bonds provided that this after-tax rate of return is greater than $r_\circ$. This means that

$$r_b \ge \frac{r_\circ}{1 - \tau_b}.$$

Consider a firm that raises equity at a cost of capital before taxes denoted by $\rho$. If this equity is within the same class of risk as the tax-exempt bonds, with rate of return $r_\circ$ as just described, one would require the same rate of return for the equity after paying the taxes due. Thus

$$r_\circ = (1 - \tau_s)(1 - \tau_c)\rho.$$

*From Amaro de Matos §2.2.3 "The Equilibrium", p. 52 (PDF 70):*

[…] To see why, notice that to raise a certain amount $K$ of capital, one can issue either debt or equity. In the first case, the stockholders pay back $r_b(1 - \tau_c)K$, whereas in the second, they pay $\rho(1 - \tau_c)K$. But since in equilibrium $r_b^* = \rho$, there is no relative advantage in one form of raising capital with respect to the other.

Alternatively, the relative advantage of leverage for stockholders, $G_L$, is written as

$$G_L = [\rho(1 - \tau_c) - r_b^*(1 - \tau_c)]K = \left[1 - \frac{(1 - \tau_s)(1 - \tau_c)}{1 - \tau_b(B^*)}\right]\frac{r_\circ K}{(1 - \tau_s)}.$$

---

### 15. MM I with perpetual debt, and when borrowing and lending rates differ
**Source:** Amaro de Matos, Ch. 2, Exercises 2.1.5 #3 and #4, p. 48 (PDF 66) · Answer in book: yes, pp. 252–254

**[2.1.5 #3]** Modigliani and Miller (1958) developed their theory under some different assumptions. They assumed that debt had an infinite life and that each period the firm had to pay interest on debt equal to $rD$. Moreover, firms could deduct the interest on debt in computing taxable profits. The return to the stockholders is defined as the time average of an infinite stream of payoffs and given by $X$. How would you obtain proposition MM1 with and without taxes?

**[2.1.5 #4]** In the context of the previous exercise, suppose that an individual in the economy faces a borrowing interest rate $\bar r$ and a lending interest rate $\underline{r}$ such that $\bar r > r > \underline{r}$, where $r$ is the corporate interest rate. What happens to MM1?

#### Context needed to solve it

*From Amaro de Matos §2.1.1 "The Irrelevancy Statement", pp. 40–42 (PDF 58–60) — MM1 without taxes:*

Assume that a firm starts at time $t = 0$ and has payoffs $\Gamma_j(t)$ in state $j$ at any point in time $t$, with $j = 1, 2, \dots k(t)$ denoting the possible states of nature at time $t$.

In the setting to be considered here, it is assumed that markets do not allow for arbitrage opportunities and also that markets are perfect, in the sense that there are no frictions of any type, taxes included. Also, there are two ways to finance the firm: either through equity only or through equity together with debt. When debt is issued, the firm is said to be *levered*; otherwise it is *unlevered*.

Equityholders and debtholders have different claims on the final payoff of the firm. Debtholders, also known as *bondholders* or *creditors*, buy a debt contract issued by the firm giving them the claim to a face value $F$ at time $T$. If at that point in time the state of nature is such that $\Gamma_j(T)$ is less than $F$, the firm is said to go *bankrupt*, in which case the creditholder will receive $\Gamma_j(T)$, if positive. Let $V_j(T)$ denote the positive part of $\Gamma_j(T)$, or $V_j(T) \equiv [\Gamma_j(T)]^+$. […] The payoff to a debt instrument in the $j$-th state of nature is thus

$$B_j(T) = \min\{F, V_j(T)\}.$$

If $K$ is the number of possible states of nature at time $T$, then, under the absence of arbitrage opportunities, there exists a strictly positive vector $\psi \in R^K$ such that the present value of the debt is

$$B = \sum_{j=1}^{K} \psi_j B_j(T).$$

Notice that, if there is no state leading to bankruptcy, $B_j(T) = F$ and the preceding expression implies that

$$B = F \sum_{j=1}^{K} \psi_j \Rightarrow B = \frac{F}{R}. \qquad (2.1)$$

[…] In other words, the payoff to equityholders in state $j$ is

$$S_j(T) = [\Gamma_j(T) - \min\{F, V_j(T)\}]^+ = V_j(T) - \min\{F, V_j(T)\} = \max[0, V_j(T) - F], \qquad (2.2)$$

implying that

$$V_j(T) = S_j(T) + B_j(T).$$

The present value of the equity is thus

$$S = \sum_{j=1}^{K} \psi_j S_j(T).$$

In this setting, it is clear that the value of the unlevered firm $V_u$ is equal to the value $V_l$ of a levered firm since

$$V_l = S + B = \sum_{j=1}^{K} \psi_j [B_j(T) + S_j(T)] = \sum_{j=1}^{K} \psi_j V_j(T) = V_u$$

This result is known as the first proposition of Modigliani and Miller and may be stated as

**Proposition 2.1.1 (MM1).** *The market value of any firm is independent of its capital structure*

$$V_l = V_u. \qquad (2.3)$$

*From Amaro de Matos §2.1.3 "The MM Propositions with Taxes", pp. 44–45 (PDF 62–63) — MM1 with taxes:*

[…] In this section it is assumed that firms pay taxes at a rate $\tau \in [0, 1]$.

Consider the case of a levered firm. In that case, let $T$ be the point in time where both taxes and the creditholders are paid. In case of bankruptcy, no taxes are paid; otherwise, the firm pays $\tau[V_j(T) - F]$. In other words, in any case the taxes are calculated in state $j$ as

$$\theta_j^\tau(T) = \tau[V_j(T) - F]^+.$$

[…] The debtholders will receive in state $j$

$$B_j(T) = \min\{F, [V_j(T) - \theta_j^\tau(T)]^+\} = \min\{F, V_j(T)\},$$

exactly the same payoff as without taxes. The equityholders are left in state $j$ with

$$S_j^\tau(T) = V_j(T) - B_j(T) - \theta_j^\tau(T). \qquad (2.5)$$

[…] Given the payoffs in the presence of taxes, the value of the unlevered firm is

$$V_u^\tau = (1 - \tau)\sum_{j=1}^{K} \psi_j V_j(T).$$

In the case of the levered firm, the firm generates for equity and debtholders the value

$$V_l^\tau = \sum_{j=1}^{K} \psi_j [S_j^\tau(T) + B_j(T)].$$

[…] In other words,

$$V_l^\tau = (1 - \tau)\sum_{j=1}^{K} \psi_j V_j(T) + \tau \sum_{j=1}^{K} \psi_j B_j(T) = V_u^\tau + \tau B.$$

This result is known as the proposition of Modigliani and Miller under taxes and is summarized as

**Proposition 2.1.3.** *Under the absence of arbitrage opportunities and in the presence of taxes, the value of the firm increases linearly with the level of debt as*

$$V_l^\tau = V_u^\tau + \tau B. \qquad (2.7)$$

*From Amaro de Matos §1.2.5 "Beta Values", p. 26 (PDF 44) — the symbol $R$ in (2.1):*

[…] The return on the preceding portfolio will be denoted by $R$ and is given by $R = 1 + r$. Such a portfolio is risk-free by construction and, as one would expect, for each unit invested at time 0 it gives back $(1 + r)$ units at $t = 1$.

---

## Original exercises (no book exercise exists)

None of the six course books has an exercise on the bank capital debate of Topic 2B, block 2B.8 (slides 46–47). The three exercises below are original, written with the user's agreement (2026-11-12), and are numbered after the book exercises. They go from easy (16) to really hard (18). Answers: `Listas/lista-r3-mm-taxes-tradeoff-solutions.pdf`, sections 16–18.

### 16. Bank capital without taxes: does more equity lower ROE and raise funding costs?
**Origin:** original exercise on the bank capital debate (Statements 1 and 2) and MM I/II without taxes, built on Prof. Ricca's Topic 2B slides 46–47 (Aula/Topic2B.pdf) and Topic 2A slides 89 and 97–102 (Aula/Topic2A.pdf) · Answer: in the solutions file

A bank holds loans with a market value of $A = 100$ (\$ billion) at $t = 0$. One year later the loans pay $A(1 + \tilde r_A)$, where the return on assets $\tilde r_A$ is $9\%$ in a good state and $3\%$ in a bad state, each with probability $\tfrac12$. The loans are fairly priced: their required (expected) return is $r_A = 6\%$. The bank funds the loans with deposits $D$ and equity $E$, $D + E = A$. Deposits pay the risk-free rate $r_D = r_f = 4\%$ and are repaid at $t = 1$ before shareholders receive anything. There are no taxes, no bankruptcy costs and no other frictions, and investors can borrow and lend at $r_f$. The equity ratio is $e = E/A$, and the bank's return on equity is

$$ROE = \frac{(\text{payoff to shareholders at } t = 1) - E}{E}.$$

The regulator considers raising the minimum equity ratio from $e = 4\%$ to $e = 20\%$; the bank keeps the same loans.

a. For $e = 4\%$ and $e = 20\%$, find $E$, $D$ and the amount owed to depositors at $t = 1$, and show that deposits are repaid in full in both states, so they are indeed risk-free.

b. For each equity ratio, compute the payoff to shareholders and the ROE in each state, the expected ROE $\mathbb{E}[ROE]$, and the standard deviation $\sigma(ROE)$. Compute also the ratio $(\mathbb{E}[ROE] - r_f)/\sigma(ROE)$ at each equity ratio.

c. Use MM II to compute the required return on equity $r_E$ at each equity ratio, compare it with the expected ROE of part (b), and compute the weighted average cost of capital $r_{WACC} = e\,r_E + (1 - e)\,r_D$ at each ratio. Does the higher requirement change the value of the bank?

d. A shareholder who liked the ROE of the $e = 4\%$ bank holds shares of the bank after it moves to $e = 20\%$. Per \$1 of her own money, how much of the $20\%$ bank's equity must she buy and how much must she borrow at $r_f$ to receive exactly the ROE of the $e = 4\%$ bank in each state? Verify state by state.

e. Statement 1 (slide 47): "Increased equity requirements will hurt bank shareholders since it would lower the banks' return on equity (ROE)." True or false? Justify with your answers to (b)–(d).

f. Statement 2 (slide 47): "Increased equity requirements increase the funding costs for banks because they must use more equity, which has a higher required return." A bank executive supports it with this computation: "At $e = 4\%$ our equity costs $r_E^{4\%}$ (the value you found in (c)) and our deposits $4\%$; at $20\%$ equity our funding cost becomes $0.20\,r_E^{4\%} + 0.80 \times 4\%$, against $6\%$ today." Compute the executive's number, find the error, and say whether Statement 2 is true or false.

#### Context needed to solve it

*From Prof. Ricca's Topic 2B slide 46 (Aula/Topic2B.pdf):*

Admati et al. (2013): no! Bank equity is not socially expensive. They use many of the arguments discussed in this lecture. They call for larger capital requirements, that is, less leverage in the banking industry.

*From Prof. Ricca's Topic 2A slides 98–99 and 101–102 (Aula/Topic2A.pdf) — MM I and MM II:*

MM I implies that the market value of the firm, $V$, or equivalently, the market value of the assets of the firm, $A$, is independent of the choices of $D$ and $E$. As the expected return on assets is defined by $A = \mathbb{E}[\tilde C_A]/(1 + r_A)$ and $A$ and $\tilde C_A$, the cash flows generated by the assets, are independent of $D$ and $E$, $r_A$ is independent of $D$ and $E$. Recall the identity

$$r_A = \frac{E}{E + D}\,r_E + \frac{D}{E + D}\,r_D.$$

Rearranging, we have that

$$r_E = r_A + \frac{D}{E}\,(r_A - r_D).$$

As $r_A$ is fixed (independent of $E$ and $D$) and $r_A > r_D$, $r_E$ increases with $D/E$, the market debt to equity ratio. For small values of $D$, that is, when debt is risk-free, $r_D$ is fixed and equal to $r_f$, and $r_E$ is linear in $D/E$. […] We refer to $r_A$ as the weighted average cost of capital, $r_{WACC}$. MM I implies that $r_{WACC}$ does not depend on how the firm finances its assets (on the choices of $D$ and $E$). […] Conservation of value principle: With perfect capital markets, financial transactions neither add nor destroy value, but instead represent a repackaging of risk (and therefore return).

*From Prof. Ricca's Topic 2A slide 89 (Aula/Topic2A.pdf) — homemade leverage:*

The arbitrageur can "lever up" firm 2 by borrowing on individual accounts (homemade leverage). Absence of arbitrage implies that $V_1 = V_2$.

---

### 17. Bank capital with corporate taxes: the lost interest tax shield
**Origin:** original exercise on the bank capital debate (Statement 3) and MM I with corporate taxes, built on Prof. Ricca's Topic 2B slides 7–18 and 47 (Aula/Topic2B.pdf) · Answer: in the solutions file

A bank's assets generate a perpetual expected pre-tax cash flow of $X = 7.5$ (\$ billion per year). The corporate tax rate is $\tau = 20\%$, so the all-equity (unlevered) bank would pay $\tau X$ in taxes every year and its owners would receive $(1 - \tau)X = 6$ per year. The unlevered cost of capital is $r_U = 6\%$, so the unlevered bank is worth $V_U = (1 - \tau)X/r_U = 100$. The bank's debt is perpetual, risk-free and kept at a constant amount $D$; it pays $r_D = 4\%$, and interest is deductible from taxable income. The bank always has enough income to use the deduction in full. There are no bankruptcy costs and no other frictions. The equity ratio is measured at market value, $e = E/V_L$ with $V_L = D + E$ the value of the levered bank. The regulator raises the minimum equity ratio from $e = 5\%$ to $e = 20\%$; the bank keeps the same assets.

a. For $e = 5\%$ and $e = 20\%$, find $V_L$, $D$, $E$ and the value of the interest tax shield $V_{ITS}$. (Use $D = (1 - e)V_L$ together with MM I with taxes.)

b. The bank moves from $e = 5\%$ to $e = 20\%$ by issuing new shares at a fair price and using all the proceeds to retire debt at its market value. How much debt is retired? Compute the annual interest tax saving $\tau r_D D$ at each ratio, the value lost by the bank's existing shareholders, and that loss as a fraction of their equity before the change.

c. Compute the after-tax WACC at each ratio with the constant-debt formula, and check that discounting the unlevered after-tax cash flow $(1 - \tau)X$ at it gives $V_L$. Derive the required return on equity $r_E$ at each ratio from the market-value balance sheet with $r_{ITS} = r_D$, and check that $\frac{E}{V_L}\,r_E + \frac{D}{V_L}\,r_D(1 - \tau)$ equals the after-tax WACC.

d. The government collects $\tau(X - r_D D)$ per year from the bank. The part $\tau X$ is as risky as the assets (discount it at $r_U$); the part $\tau r_D D$ is risk-free (discount it at $r_D$). Compute the present value $G$ of the government's tax claim at each ratio, and the total $V_L + G$. Who gains what the existing shareholders lose in (b)?

e. Statement 3 (slide 47): "Increased equity requirements increase the funding costs for banks because they reduce the ability of banks to benefit from the tax shield associated with interest payments on debt." Is it true for the bank's shareholders? Is the lost tax shield a cost for society as a whole? Explain why this argument does not show that equity is socially expensive.

#### Context needed to solve it

*From Prof. Ricca's Topic 2B slides 7–8 (Aula/Topic2B.pdf) — MM I with corporate taxes:*

Relative to an identical unlevered firm, the levered firm can pay out $\tau r_f D$ more to its investors in each period. Assuming perpetuity

$$V_{ITS} = \frac{\tau r_f D}{r_f} = \tau D.$$

(MM I with corporate taxes) The value of a levered firm equals that of an unlevered firm plus the present value of the interest tax shield

$$V_L = V_U + V_{ITS}.$$

If investors cannot get an equivalent tax break on homemade leverage, they are willing to pay a premium for levered firms. All the tax benefits from leverage accrue to the shareholders.

*From Prof. Ricca's Topic 2B slides 9–11 (Aula/Topic2B.pdf) — market-value balance sheet with taxes:*

Assets of the levered firm: $V_U$ (market value of the unlevered firm's assets, return $r_U$) and $V_{ITS}$ (return $r_{ITS}$); claims: debt $D$ (return $r_D$) and equity $E$ (return $r_E$); $V_L = V_U + V_{ITS} = D + E$. From the balance sheet, we have the identity

$$\frac{D}{D + E}\,r_D + \frac{E}{D + E}\,r_E = \frac{V_U}{V_U + V_{ITS}}\,r_U + \frac{V_{ITS}}{V_U + V_{ITS}}\,r_{ITS}.$$

$r_{ITS} = r_D$ if the firm maintains a constant market value debt amount in perpetuity. In this case, $V_{ITS} = \tau D r_D / r_D = \tau D$.

*From Prof. Ricca's Topic 2B slides 16 and 18 (Aula/Topic2B.pdf) — after-tax WACC:*

With tax-deductible interest, the effective return on debt is $r_D(1 - \tau)$. The after-tax WACC is

$$r_{WACC} = \frac{E}{E + D}\,r_E + \frac{D}{E + D}\,r_D(1 - \tau).$$

If we discount the unlevered free cash flows with the after-tax WACC, we obtain the correct value of the levered firm. Constant debt level:

$$r_{WACC} = \Bigl(1 - \tau\,\frac{D}{D + E}\Bigr)\,r_U.$$

---

### 18. The failure externality and the socially optimal capital ratio
**Origin:** original exercise on the bank capital debate (failure externality) and the static trade-off, built on Prof. Ricca's Topic 2B slides 44–47 (Aula/Topic2B.pdf) · Answer: in the solutions file

Measure everything per \$1 of bank assets per year. The bank's equity ratio is $e \in [0, 1]$ and its deposits are $1 - e$. Each year the assets suffer a loss rate $\ell \ge 0$ (loss as a fraction of assets) that is exponentially distributed with mean $\theta = 0.01$:

$$\Pr(\ell > x) = \exp(-x/\theta), \qquad x \ge 0.$$

The bank fails when the loss exceeds its equity, $\ell > e$. A failure imposes on the rest of the economy (the deposit insurer and taxpayers, and the disruption of credit to borrowers) a social loss of $\kappa = 0.50$ per \$1 of the bank's assets. The bank's shareholders bear none of it: they have limited liability, and deposits are fully insured at a flat premium, so the deposit rate does not depend on $e$. Deposits also give depositors liquidity services worth $\lambda = 0.005$ per \$1 of deposits per year; this is a genuine social benefit of deposit funding, and the bank captures all of it through fees. Each \$1 of deposits also saves the bank $s = \tau r_D = 0.20 \times 4\% = 0.008$ of taxes per year. Apart from these features, MM holds: the higher required return on equity at low $e$ only compensates shareholders for the higher risk of their claim, and the tax saving is paid by the government.

a. Find the annual failure probability $p(e)$ and the expected annual social cost of failure $F(e) = \kappa\,p(e)$ at $e = 4\%$ and at $e = 20\%$.

b. Explain why society's annual cost of the funding mix, per \$1 of assets and up to a constant, is

$$S(e) = \lambda e + \kappa \exp(-e/\theta),$$

and why neither the equity premium nor the tax saving $s$ appears in it. Derive the first-order condition, check the second-order condition, and find the socially optimal equity ratio $e^*$ in closed form and numerically. What is the annual failure probability at $e^*$? Compute $S(4\%)$, $S(e^*)$ and $S(20\%)$.

c. Per \$1 of assets per year, the bank's shareholders bear the private cost $(\lambda + s)\,e$ of using equity (fees and tax savings forgone on the deposits it replaces) and none of the failure cost. Which equity ratio does the bank choose if it is unregulated, and which if the regulatory minimum is $\underline e = 4\%$? For a move from $4\%$ to $e^*$, compute the private cost to the shareholders and the social gain $S(4\%) - S(e^*)$.

d. A planner who believes two of the slide-47 statements computes a different "optimal" ratio. (i) Counting the lost tax saving as a social cost, she uses $\lambda + s$ in place of $\lambda$. (ii) Believing that equity is costly because of its higher required return, she uses the gap of $10$ percentage points between a $14\%$ required return on equity and a $4\%$ deposit rate, $0.10$ per \$1 of equity per year, in place of $\lambda$. Find the ratio each calculation gives and compare it with $e^*$.

e. Derive $\partial e^*/\partial\kappa$, $\partial e^*/\partial\lambda$ and $\partial e^*/\partial\theta$, and sign them at the given parameter values. By how much does $e^*$ rise if the social loss of a failure $\kappa$ doubles?

#### Context needed to solve it

*From Prof. Ricca's Topic 2B slide 47 (Aula/Topic2B.pdf):*

[…] negative externality because the increase in leverage raises the probability of a bank failure, weakening the financial system and imposing losses on the broader economy.

*From Prof. Ricca's Topic 2B slides 44–45 (Aula/Topic2B.pdf) — the static trade-off this exercise transposes from the firm to society:*

An increase in $K$ has two effects. It increases the value of the tax shield […] But it increases the expected bankruptcy cost $C$: $C\,H(K)$. The optimal debt level $K^*$ is such that the marginal benefit of debt equals the marginal expected bankruptcy costs. […] With bankruptcy costs, $V_L = V_U + V_{ITS} - PV(\text{bankruptcy costs})$.

*Results of MM without and with taxes (Topic 2A slides 98–102; Topic 2B slides 7–8), restated:*

Without taxes, a change in leverage leaves $r_{WACC} = r_A$ and the value of the assets unchanged: the higher required return on equity at higher leverage, $r_E = r_A + \frac{D}{E}(r_A - r_D)$, is compensation for risk, not a cost to anyone. With corporate taxes, $V_L = V_U + \tau D$ for constant perpetual debt; the gain $\tau D$ is paid by the government, whose tax claim falls by the same amount, so the total value of the claims on the assets (shareholders, debtholders and government) does not depend on $D$.
