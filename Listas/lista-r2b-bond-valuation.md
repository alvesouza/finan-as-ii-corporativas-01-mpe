---
tags: [exercise-list, ricca-r2b, bond-valuation, zero-coupon, yield-to-maturity, term-structure, credit-spread, cost-of-debt]
date: 2026-11-12
---

# Exercise list R2b — Bond valuation, the term structure and the cost of debt

Ricca Topic 2A, blocks 2A.1 (present value with spot rates: a Treasury coupon bond priced off the zero-coupon curve) and 2A.10 ($r_D$ is neither the coupon nor the yield: with default risk the promised yield exceeds the expected return), with the syllabus reading Berk Ch. 6. The list covers zero-coupon and coupon bonds, yield to maturity, spot rates and the term structure, why bond prices change (time and interest-rate risk), callable bonds, and corporate bonds (ratings, credit spreads, promised yield vs. expected return). 15 real exercises ordered easy → really hard, copied verbatim from the course books for personal study; pages are printed, with the PDF page in brackets. None of them appears in another list.

**Uncovered subtopic (rule `exercise-lists#4`).** No course book has a *numerical* exercise on the slide model $D = [F(1-p) + Cp]/(1+r_D)$, where a physical default probability $p$ and a recovery $C$ give the expected return $r_D$ below the promised yield $y$ (searched: Berk Ch. 6 and Ch. 13 problems, Ross Cap. 7 and Cap. 14, Higgins Ch. 5 and 7, Grinblatt–Titman Ch. 2, 7, 10 and 13, Tirole, Amaro de Matos). The closest are Exercise 5 (Berk, conceptual) and Exercise 15 (Grinblatt–Titman, a defaultable bond priced with risk-neutral probabilities, where the promised yield is twice the expected return). No original exercise was written: whether to add one is the user's call. Links: [[Map/exercises-index|exercise index]] · [[rules/02_valuation|rules]].

| Topic block | Exercises |
|---|---|
| Zero-coupon bonds, their yields and the yield curve | 1, 13 |
| Coupon bonds: price, yield to maturity, coupon rate | 3, 9, 12 |
| Spot rates and the term structure (pricing a coupon bond with zero-coupon yields) | 8, 13 |
| Why bond prices change: time, interest-rate risk, holding-period return | 2, 7, 11 |
| Embedded options: callable bonds | 4, 14 |
| Corporate bonds: ratings, credit spreads, promised yield vs. expected return | 5, 6, 10, 15 |

## References

| # | Tier | Book | Ch. | Exercise | Printed p. (PDF) | Answer in book | Trains |
|---|---|---|---|---|---|---|---|
| 1 | Easy | Berk–DeMarzo–Harford, *Fundamentals* 2e | Ch. 6 | 6.4 | 172 (203) | no | Zero-coupon prices → yields; shape of the zero-coupon yield curve |
| 2 | Easy | Higgins (Koski–Higgins–Mitton) 13e | Ch. 5 | 5.5 | 188 (209) | yes, p. 410 | Holding-period return on a bond; why its price fell |
| 3 | Easy | Ross *Fundamentos* 9e | Cap. 7 | 7.6 | 232 (256) | no | Price of a seasoned semiannual coupon bond from its YTM (annuity factor) |
| 4 | Easy | Higgins (Koski–Higgins–Mitton) 13e | Ch. 5 | 5.4 | 188 (209) | no | A call provision raises the yield investors demand |
| 5 | Easy | Berk–DeMarzo–Harford, *Fundamentals* 2e | Ch. 6 | Critical Thinking 8 | 172 (203) | no | Promised yield vs. expected return on a corporate bond (block 2A.10) |
| 6 | Exam | Berk–DeMarzo–Harford, *Fundamentals* 2e | Ch. 6 | 6.24 | 174 (205) | no | One-year zero prices by rating; credit spreads and why they rise as ratings fall |
| 7 | Exam | Berk–DeMarzo–Harford, *Fundamentals* 2e | Ch. 6 | 6.16–6.18 | 173 (204) | no | Price path over time at a constant yield: accrual and the coupon drop |
| 8 | Exam | Berk–DeMarzo–Harford, *Fundamentals* 2e | Ch. 6 | 6.10 | 173 (204) | no | Pricing a coupon bond with spot rates (block 2A.1) |
| 9 | Exam | Ross *Fundamentos* 9e | Cap. 7 | 7.19 | 233 (257) | no | Yield of existing debt = coupon for a new issue at par (cost of debt, not the old coupon) |
| 10 | Exam | Berk–DeMarzo–Harford, *Fundamentals* 2e | Ch. 6 | 6.26 | 175 (206) | no | Rating → yield → price → issue size; inverting a price to an implied rating; junk status |
| 11 | Exam | Berk–DeMarzo–Harford, *Fundamentals* 2e | Ch. 6 | 6.21–6.22 | 174 (205) | no | Interest-rate sensitivity across maturity and coupon (duration intuition) |
| 12 | Really hard | Ross *Fundamentos* 9e | Cap. 7 | 7.31 (DESAFIO) | 234 (258) | no | Bond with deferred, stepped coupons: deferred annuities vs. a zero |
| 13 | Really hard | Grinblatt & Titman 2e | Ch. 10 | 10A.3 | 369 (382) | no | Bootstrapping spot and annuity yields from par yields |
| 14 | Really hard | Ross *Fundamentos* 9e | Cap. 7 | 7.32 (DESAFIO) | 234 (258) | no | Implied value of a call option by replicating the callable bond's coupon with two noncallable bonds |
| 15 | Really hard | Grinblatt & Titman 2e | Ch. 7 | 7.3 | 254 (267) | no | Defaultable bond on a binomial tree: price, promised yield vs. risk-free expected return |

## Tier 1 — Easy

### 1. Zero-coupon prices and the yield curve
**Source:** Berk, Ch. 6, Exercise 6.4, p. 172 (PDF 203) · Answer in book: no

The following table summarizes prices of various default-free zero-coupon bonds (expressed as a percentage of face value):

| Maturity (years) | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Price (per \$100 face value) | \$95.51 | \$91.05 | \$86.38 | \$81.65 | \$76.51 |

a. Compute the yield to maturity for each bond.

b. Plot the zero-coupon yield curve (for the first five years).

c. Is the yield curve upward sloping, downward sloping, or flat?

---

### 2. Holding-period return on a bond
**Source:** Higgins (Koski–Higgins–Mitton), Ch. 5, Exercise 5.5, p. 188 (PDF 209) · Answer in book: yes, p. 410

The return an investor earns on a bond over a period of time is known as the holding period return, defined as interest income plus or minus the change in the bond's price, all divided by the beginning bond price.

a. What is the holding period return on a bond with a par value of \$1,000 and a coupon rate of 6 percent if its price at the beginning of the year was \$1,050 and its price at the end was \$940? Assume interest is paid annually.

b. Can you give two reasons the price of the bond might have fallen over the year?

---

### 3. Price of a seasoned semiannual bond
**Source:** Ross, Cap. 7, Exercise 7.6, p. 232 (PDF 256) · Answer in book: no

6\. Preços de títulos de dívida [OA2] A Companhia Pereira emitiu títulos de 11 anos há um ano, com taxa de cupom de 6,9%. Os pagamentos são semestrais. Se o YTM sobre esses títulos for de 7,4%, qual é o seu preço corrente?

#### Context needed to solve it

*From Ross §7.1 "Valores e retornos dos títulos de dívida", p. 195 (PDF 219) — the bond value formula:*

Com base em nossos exemplos, agora podemos escrever a expressão geral do valor de um título de dívida. Se um título tem (1) um valor de face (F) pago no vencimento; (2) um cupom (C) pago por período; (3) t períodos até o vencimento; e (4) um retorno de r por período, seu valor é:

$$\text{Valor do título de dívida} = C \times [1 - 1/(1+r)^t]/r + F/(1+r)^t$$

*From Ross Example 7.1 "Cupons semestrais", p. 195 (PDF 219):*

Os títulos de dívida (bonds) emitidos nos Estados Unidos normalmente fazem pagamentos de cupom duas vezes ao ano. Assim, se um bond comum tiver uma taxa de cupom de 14%, o seu titular terá um total de \$140 por ano, mas esses \$140 virão em dois pagamentos de \$70 cada um. […] Os retornos desses títulos são cotados em taxa nominal anual; a taxa cotada é igual à taxa efetiva do período multiplicada pelo número de períodos. Nesse caso, com um retorno cotado a 16% e pagamentos semestrais, o verdadeiro retorno é de 8% a cada seis meses.

*Face value:* the statement gives none; Ross's bond examples and problems use a face value of \$1.000 (e.g. Problems 7.1–7.2 on p. 229), and the answer is given per \$1.000 of face value.

---

### 4. Callable vs. noncallable bonds
**Source:** Higgins (Koski–Higgins–Mitton), Ch. 5, Exercise 5.4, p. 188 (PDF 209) · Answer in book: no

Two 20-year bonds are identical in all respects except that one allows the issuer to call the bond in return for \$1,000 cash at any time after five years, while the other contains no call provisions. Will the yield to maturity on the two bonds differ? If so, which will be higher? Why?

---

### 5. Expected return vs. yield on a corporate bond
**Source:** Berk, Ch. 6, Critical Thinking question 8, p. 172 (PDF 203) · Answer in book: no

Explain why the expected return of a corporate bond does not equal its yield to maturity.

---

## Tier 2 — Exam level

### 6. Credit spreads on one-year zeros
**Source:** Berk, Ch. 6, Exercise 6.24, p. 174 (PDF 205) · Answer in book: no

The following table summarizes the yields to maturity on several one-year, zero-coupon securities:

| Security | Yield (%) |
|---|---|
| Treasury | 3.1 |
| AAA corporate | 3.2 |
| BBB corporate | 4.2 |
| B corporate | 4.9 |

a. What is the price (expressed as a percentage of the face value) of a one-year, zero-coupon corporate bond with an AAA rating?

b. What is the credit spread on AAA-rated corporate bonds?

c. What is the credit spread on B-rated corporate bonds?

d. How does the credit spread change with the bond rating? Why?

---

### 7. A bond's price over time at a constant yield
**Source:** Berk, Ch. 6, Exercises 6.16–6.18 (shared setup), p. 173 (PDF 204) · Answer in book: no

Suppose that General Motors Acceptance Corporation issued a bond with ten years until maturity, a face value of \$1000, and a coupon rate of 7% (annual payments). The yield to maturity on this bond when it was issued was 6%. Use this information for Problems 16–18.

**16.** What was the price of this bond when it was issued?

**17.** Assuming the yield to maturity remains constant, what is the price of the bond immediately before it makes its first coupon payment?

**18.** Assuming the yield to maturity remains constant, what is the price of the bond immediately after it makes its first coupon payment?

---

### 8. Pricing a coupon bond with spot rates
**Source:** Berk, Ch. 6, Exercise 6.10, p. 173 (PDF 204) · Answer in book: no

Assume the current Treasury yield curve shows that the spot rates for 6 months, 1 year, and $1\tfrac{1}{2}$ years are 1%, 1.1%, and 1.3%, all quoted as semiannually compounded APRs. What is the price of a \$1000 par, 4% coupon bond maturing in $1\tfrac{1}{2}$ years (the next coupon is exactly 6 months from now)?

#### Context needed to solve it

*From Berk Ch. 6, Appendix B "The Yield Curve and the Law of One Price", p. 179 (PDF 210) — Eq. 6.4:*

[…] the price of a coupon bond must equal the present value of its coupon payments and face value discounted at the competitive market interest rates (see Eq. 5.7 in Chapter 5):

$$P = PV(\text{Bond Cash Flows}) = \frac{CPN}{1+YTM_1} + \frac{CPN}{(1+YTM_2)^2} + \cdots + \frac{CPN + FV}{(1+YTM_n)^n} \qquad (6.4)$$

where $CPN$ is the bond coupon payment, $YTM_n$ is the yield to maturity of a zero-coupon bond that matures at the same time as the $n$th coupon payment, and $FV$ is the face value of the bond.

---

### 9. Coupon rate for a new issue sold at par
**Source:** Ross, Cap. 7, Exercise 7.19, p. 233 (PDF 257) · Answer in book: no

19\. Retornos de títulos de dívida [OA2] A Gomes & Cia. quer emitir novas obrigações de 20 anos para alguns projetos de expansão extremamente necessários. A empresa, no momento, tem obrigações vendidas por \$930, com cupom de 8%, que fazem pagamentos semestrais e têm vencimento em 20 anos. Qual taxa de cupom deve ser definida pela empresa para seus novos títulos de dívida se ela quiser que sejam vendidos ao par?

#### Context needed to solve it

*From Ross §7.1, p. 195 (PDF 219) — the bond value formula, with face value $F$, coupon $C$ per period, $t$ periods to maturity and return $r$ per period:*

$$\text{Valor do título de dívida} = C \times [1 - 1/(1+r)^t]/r + F/(1+r)^t$$

*From Ross Example 7.1, p. 195 (PDF 219):* Os retornos desses títulos são cotados em taxa nominal anual; a taxa cotada é igual à taxa efetiva do período multiplicada pelo número de períodos.

---

### 10. Ratings, prices and issue size
**Source:** Berk, Ch. 6, Exercise 6.26, p. 175 (PDF 206) · Answer in book: no

HMK Enterprises would like to raise \$10 million to invest in capital expenditures. The company plans to issue five-year bonds with a face value of \$1000 and a coupon rate of 6.5% (annual payments). The following table summarizes the yield to maturity for five-year (annual-pay) coupon corporate bonds of various ratings:

| Rating | AAA | AA | A | BBB | BB |
|---|---|---|---|---|---|
| YTM | 6.20% | 6.30% | 6.50% | 6.90% | 7.50% |

a. Assuming the bonds will be rated AA, what will the price of the bonds be?

b. How much of the total principal amount of these bonds must HMK issue to raise \$10 million today, assuming the bonds are AA rated? (Because HMK cannot issue a fraction of a bond, assume that all fractions are rounded to the nearest whole number.)

c. What must the rating of the bonds be for them to sell at par?

d. Suppose that when the bonds are issued, the price of each bond is \$959.54. What is the likely rating of the bonds? Are they junk bonds?

#### Context needed to solve it

*From Berk §6.5 "Corporate Bonds", "Bond Ratings", p. 166 (PDF 197):*

Bonds in the top four categories are often referred to as investment-grade bonds because of their low default risk. Bonds in the bottom five categories are often called speculative bonds, junk bonds, or high-yield bonds because their likelihood of default is high and so they promise higher yields.

*Table 6.6, p. 167 (PDF 198), rating classes (Moody's / Standard & Poor's):* Investment Grade Debt — Aaa/AAA, Aa/AA, A/A, Baa/BBB; Speculative Bonds ("Junk Bonds") — Ba/BB, B/B, Caa/CCC, Ca/CC, C/C, D.

---

### 11. Interest-rate sensitivity: maturity and coupon
**Source:** Berk, Ch. 6, Exercises 6.21–6.22 (shared table), p. 174 (PDF 205) · Answer in book: no

Consider the following bonds for Questions 21 and 22:

| Bond | Coupon Rate (annual payments) | Maturity (years) |
|---|---|---|
| A | 0% | 15 |
| B | 0% | 10 |
| C | 4% | 15 |
| D | 8% | 10 |

**21.** What is the percentage change in the price of each bond if its yield to maturity falls from 6% to 5%?

**22.** Which of the bonds A–D is most sensitive to a 1% drop in interest rates from 6% to 5% and why? Which bond is least sensitive? Provide an intuition explanation for your answer.

#### Context needed to solve it

*Face value:* the statement gives none; Berk's problems in this section use \$1000 bonds (Problems 13–19), and percentage changes do not depend on the face value.

---

## Tier 3 — Really hard

### 12. A bond with deferred, stepped payments
**Source:** Ross, Cap. 7, Exercise 7.31 (DESAFIO), p. 234 (PDF 258) · Answer in book: no

31\. Avaliação de obrigações [OA2] A Corporação Pereira tem duas obrigações diferentes em circulação. O título M tem valor de face de \$20.000 e vencimento em 20 anos. Ele não faz pagamentos nos primeiros seis anos; em seguida, paga \$1.100 a cada seis meses durante os oito anos subsequentes; e, por último, paga \$1.400 a cada seis meses nos seis anos restantes. O título N também tem valor de face de \$20.000 e vencimento em 20 anos; ele não tem cupom. Se o retorno exigido de ambas as obrigações for de 7% capitalizados semestralmente, qual é o preço atual do título M? E do título N?

---

### 13. Spot and annuity yields from par yields
**Source:** Grinblatt & Titman, Ch. 10, Exercise 10A.3, p. 369 (PDF 382) · Answer in book: no

Compute spot yields and annuity yields for years 1, 2, 3, and 4 if par yields for years 1, 2, 3, and 4 are, respectively, 4.5 percent, 5 percent, 5.25 percent, and 5.25 percent. Assume annual compounding for all rates and annual payments for all bonds.

#### Context needed to solve it

*From Grinblatt & Titman Appendix 10A, §10A.1 "Term Structure Varieties", p. 363 (PDF 376):*

There are a variety of term structures. The par yield curve for the United States represents the yields and interpolated yields of on-the-run coupon-paying Treasury securities of various maturities (see Chapter 2). The annuity term structure represents the yields to maturity of riskless bonds with level payments. There also is the spot term structure, which represents the yields to maturity of zero-coupon bonds of various maturities.

*From §10A.2 "Spot Rates, Annuity Rates, and Par Rates", "Using Spot Yields to Compute Annuity Yields and Par Yields", p. 364 (PDF 377):*

Computing annuity yields from spot yields is relatively straightforward. The annuity yield for year $t$ is found by assuming a cash payment of a fixed amount for years $1, 2, \ldots, t$—for example, \$1 is paid at each of those years. This is like a portfolio of $t$ zero-coupon bonds, each with a \$1 face value. Using spot yields, compute the present value of each zero-coupon bond and sum up the $t$ present values. If the present value is $P$, find the internal rate of return for the cash flows: $-P, 1, 1, \ldots, 1$. This is the annuity yield-to-maturity for date $t$. Repeat this process for $t = 1$, $t = 2$, $t = 3, \ldots$, and $t = T$.

*From "Computing Spot Yields from Par Yields and Annuity Yields", pp. 366–367 (PDF 379–380):*

There are many ways to compute the spot yield curve from the par yield curve. Perhaps the easiest way to proceed is to move sequentially from the shortest maturity to the longest. With annual compounding and annual coupons, the par bond with the earliest maturity is a zero-coupon bond. The spot yield is identical to the par yield in this case. The two-year spot yield is computed from a long position in the two-year par bond and a short position in the one-year par bond. Because the one-year par bond is a zero-coupon bond, it is possible to form a portfolio that looks like a zero-coupon bond with two years' maturity by weighting the two par bonds properly. The yield of this properly weighted portfolio is the spot yield for two years' maturity. Given the one- and two-year spot rates, it is possible to form a portfolio consisting of a long position in a three-year par bond and short positions in one- and two-year zero-coupon bonds that look like a three-year zero coupon bond. The yield of this bond is the three-year spot rate. Proceed sequentially in this manner as far out into time as necessary.

*From Example 10A.2, p. 367 (PDF 380), the year-3 step with par yields 9%, 8%, 7% (two-year spot 7.96%):* To find the year 3 spot rate, strip the two \$7 coupons at years 1 and 2 from the par bond. This leaves a bond with a value of

$$\$100 - \frac{\$7}{1.09} - \frac{\$7}{(1.0796)^2} = \$87.5722$$

With a future payoff at year 3 in the amount of \$107, and no future cash flows at other dates, the stripped bond now has the payoff of a zero-coupon bond with a 3-year spot yield $r$ that solves

$$\$87.5722 = \frac{\$107}{(1+r)^3}$$

implying $r = 6.91$ percent.

---

### 14. The implied value of a call option
**Source:** Ross, Cap. 7, Exercise 7.32 (DESAFIO), p. 234 (PDF 258) · Answer in book: no

32\. Avaliação da opção de resgate antecipado [OA2] Considere a seguir os preços das três emissões do Tesouro em 15 de maio de 2007:

| | | | | | |
|---|---|---|---|---|---|
| 6,500 | 13 de maio | 106:10 | 106:12 | −13 | 5,28 |
| 8,250 | 13 de maio | 103:14 | 103:16 | − 3 | 5,24 |
| 12,000 | 13 de maio | 134:25 | 134:31 | −15 | 5,32 |

O título do meio é resgatável em fevereiro de 2008. Qual é o valor implícito da opção de resgate antecipado? (Dica: existe uma forma de combinar as duas emissões não resgatáveis para criar uma emissão que tenha o mesmo cupom do título resgatável?)

#### Context needed to solve it

*Table transcribed from the PDF image (the MD lost the layout); the book prints it without column headings. The columns follow the layout of the Treasury quotes in Figure 7.4, explained below. Editor's note (not in the book): "13 de maio" translates "May 13" of the English original, i.e. maturity in May 2013; what matters for the solution is that the three issues mature on the same date.*

*From Ross §7.5, "Relatórios de preços de títulos de dívida" (Treasury quotes, Figure 7.4), pp. 218–219 (PDF 242–243):*

A Figura 7.4 mostra uma parte das listagens diárias de notas e obrigações do Tesouro encontradas no site wsj.com. A entrada que começa com "2021 Nov 15" está destacada. Essa informação indica que aquele título vence em novembro de 2021. A coluna ao lado representa a taxa de cupom, que é de 8,000%. Todos os títulos do Tesouro norte-americano fazem pagamentos semestrais e têm valor de face de \$1.000, de modo que esse título pagará \$40 a cada seis meses até o vencimento.

As duas informações seguintes são os preços de oferta de compra e de venda. Em qualquer mercado de balcão ou em corretoras, o preço de oferta de compra (bid) representa aquilo que um corretor está disposto a pagar por um título, e o preço de oferta de venda (ask) é aquilo que um corretor está disposto a aceitar por ele. A diferença entre os dois é chamada de margem (ou spread) entre compra e venda e representa o lucro do corretor.

Por motivos históricos, os preços dos títulos emitidos pelo Tesouro norte-americano são cotados em 32 avos. Assim, o preço de oferta de venda do título de 8% de novembro de 2021, 136:29, na verdade, pode ser traduzido como 136 29/32, ou 136,90625% do valor de face. Com um valor de face de \$1.000, isso representa \$1.369,0625. Como os preços são cotados em 32 avos, a menor variação de preço possível é 1/32. Isso é chamado de tick size (tamanho da variação admitida).

O próximo número cotado é o preço de oferta de venda do dia anterior, medida em ticks (ou seja, em 32 avos), de modo que o preço de oferta de venda da emissão subiu em 5/32 de 1% ou 0,15625% do valor de face em relação ao dia anterior. O último número reportado é o retorno até o vencimento, com base no preço de oferta de venda.

---

### 15. A defaultable bond on a binomial tree
**Source:** Grinblatt & Titman, Ch. 7, Exercise 7.3, p. 254 (PDF 267) · Answer in book: no

Value a risky corporate bond, assuming that the risk-free interest rate is 4 percent per period, where a period is defined as six months. The corporate bond has a face value of \$100 payable two periods from now and pays a 5 percent coupon per period; that is, interest payments of \$5 at the end of both the first period and the second period.

The corporate bond is a derivative of the assets of the issuing firm. Assume that the assets generate sufficient cash to pay off the promised coupon one period from now. In particular, the corporation has set aside a reserve fund of \$5/1.04 per bond to pay off the promised coupon of the bond one period from now. Two periods from now, there are three possible states. In one of those states, the assets of the firm are not worth much and the firm defaults, unable to generate a sufficient amount of cash. Only \$50 of the \$105 promised payment is made on the bond in this state.

The exhibit below describes the value of the firm's assets per bond (less the amount in the reserve fund maintained for the intermediate coupon) and the cash payoffs of the bond. The nonreserved assets of the firm are currently worth \$100 per bond. At the $U$ and $D$ nodes, the reserve fund has been depleted and the remaining assets of the firm per bond are worth \$120 and \$90, respectively, while they are worth \$300, \$110, and \$50, respectively, in the $UU$, $UD$, and $DD$ states two periods from now.

**Paths for the Value of the Firm's Assets Per Bond (Above the Node) Cash Payoffs of a Risky Bond (Below the Node) in a Two-Period Binomial Tree Diagram** (transcribed from the PDF image; the tree recombines at $UD$):

| Node | Date | Reached from | Firm's assets per bond (above the node) | Bond cash payoff (below the node) |
|---|---|---|---|---|
| 0 | 0 | — | \$100 | — |
| $U$ | 1 | 0 (up) | \$120 | \$5 |
| $D$ | 1 | 0 (down) | \$90 | \$5 |
| $UU$ | 2 | $U$ (up) | \$300 | \$105 |
| $UD$ | 2 | $U$ (down) or $D$ (up) | \$110 | \$105 |
| $DD$ | 2 | $D$ (down) | \$50 | \$50 |

#### Context needed to solve it

*From Grinblatt & Titman §7 "Risk-Neutral Valuation of Derivatives: The Wall Street Approach", pp. 240–241 (PDF 253–254):*

The risk-neutral valuation method is a three-step procedure for valuing derivatives.

1. Identify risk-neutral probabilities that are consistent with investors being risk neutral, given the current value of the underlying asset and its possible future values. Risk-neutral probabilities are a set of weights applied to the future values of the underlying asset along each path. The expected future asset value generated by these probabilities, when discounted at the risk-free rate, equals the current value of the underlying asset.
2. Multiply each risk-neutral probability by the corresponding future value for the derivative and sum the products together.
3. Discount the sum of the products in step 2 (the probability-weighted average of the derivative's possible future values) at the risk-free rate. This simply means that we divide the result in step 2 by the sum of 1 plus the risk-free rate.

[…] Note from Example 7.8 that .87 is the risk-neutral probability, not the actual probability, of the good state occurring, which remains unspecified.

*From "A General Formula for Risk-Neutral Probabilities", p. 242 (PDF 255):*

One determines risk-neutral probabilities from the returns of the underlying asset at each of the binomial outcomes, and not by the likelihood of each binomial outcome. The risk-neutral probabilities, $\pi$, are those probabilities that make the "expected" return of an asset equal the risk-free rate. That is, $\pi$ must solve

$$\pi u + (1-\pi) d = 1 + r_f$$

where $r_f$ = risk-free rate, $u$ = 1 + per period rate of return of the underlying asset at the up node, $d$ = 1 + per period rate of return of the underlying asset at the down node. When rearranged, this says

$$\pi = \frac{1 + r_f - d}{u - d} \qquad (7.4)$$
