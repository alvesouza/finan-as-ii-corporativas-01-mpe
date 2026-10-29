---
tags: [notes, lecture-01, accounting, market-value, leverage, enterprise-value, liquidity]
date: 2026-10-24
status: taught
source: "Aula/Topic1.pdf slides 22–31 (blocks 1.4–1.5); Berk 2e Ch. 2 §2.2–2.3, eqs. (2.3)–(2.5), Examples 2.1–2.2, pp. 29–32; Higgins 13e Ch. 1 'Market Value vs. Book Value', pp. 22–23, 25; Ross Fundamentos Cap. 3 Exemplo 3.1, p. 62; slides 24–25 Starbucks 27/12/2020"
---

# 1.4–1.5 · Book vs market equity, leverage ratios, enterprise value, liquidity ratios

> **Claim.** Book equity is a residual of historical costs. Market capitalization is a price on
> **future** cash flows, including those of assets the balance sheet never records. The two can
> differ in sign: Starbucks had book equity of **−7.9 bn USD** and a market cap of **122.6 bn USD**,
> and it was not insolvent. Leverage and value ratios therefore use **market** equity. **Enterprise
> value** prices the business alone: equity plus debt minus cash.

Prev: [[L01-02-balance-sheet-items]] · Next: [[L01-04-income-statement]] · Map: [[L01-00-map]]

**Notation.**

| Symbol | Meaning | Range |
|---|---|---|
| $E^{\text{book}}$, $E^{\text{mkt}}$ | book equity ($A-L$); market capitalization | book real, market $\ge0$ |
| $P$, $N$ | share price; common shares outstanding | $>0$ |
| $D$ | interest-bearing debt (short- and long-term, incl. current maturities), book value | $\ge0$ |
| $L$ | total liabilities | $\ge D$ |
| $C$ | cash and marketable securities | $\ge0$ |
| $EV$ | enterprise value | real |
| $CA$, $CL$, $\mathrm{Inv}$ | current assets, current liabilities, inventories | $\ge0$ |

---

## 1 · C — book equity and market capitalization (slide 22)

$$E^{\text{book}}=A-L \tag{3.1}$$

$$E^{\text{mkt}}=P\times N \tag{3.2}$$

Book equity is "an accounting measure of the net worth of the firm". Market capitalization is what
investors are willing to pay for the equity. Slide 22 sums up the difference: **market values are
forward-looking** (they reflect the expected discounted value of future payoffs to shareholders),
**book values are backward-looking**.

**Berk, Example 2.1 (p. 29).** Global has $N=3.6$ million shares at $P=10.00$. Substituting into
(3.2):

$$E^{\text{mkt}}=10.00\times3.6=36\ \text{million}$$

against $E^{\text{book}}=22.2$ million. **Higgins, Polaris (p. 25):** $E^{\text{mkt}}=95.28\times61.9=5{,}898$
million (rounded as printed), against a book value of 1,434 million. The ratio is
$5{,}898/1{,}434=4.11$.

---

## 2 · C — why book and market differ (slide 23)

| Driver | Mechanism | Source |
|---|---|---|
| Historical cost | assets are carried at cost less depreciation; the cost does not update for changes in the income the asset will generate | slide 23; Higgins pp. 22–23 |
| Little marking to market | only a few assets and liabilities trade actively | slide 23 |
| **Off-balance-sheet assets** | quality of employees and managers, future R&D, reputation, loyal customers | slide 23; Berk p. 29 |
| **Off-balance-sheet liabilities** | pending lawsuits (product-liability claims) | slide 23 |
| What equity buys | "equity investors buy shares for the future income they hope to receive, not for the value of the firm's assets" | Higgins p. 23 |

---

## 3 · C — worked example: Starbucks, 27/12/2020 (slides 24–25)

USD millions, as on slide 24:

| Assets | | Liabilities & shareholders' equity | |
|---|---|---|---|
| **Current assets** | **8,358** | **Current liabilities** | **7,884** |
| Cash and equivalents | 5,028 | Accounts payable | 1,051 |
| Accounts receivable, net | 888 | Accrued payroll and benefits | 685 |
| Inventories | 1,472 | Current portion of operating lease liability | 1,268 |
| Other | 970 | Short-term debt | 493 |
| | | Current portion of long-term debt | 750 |
| | | Stored value card liability and current portion of deferred revenue | 1,871 |
| | | Other | 1,767 |
| **Non-current assets** | **21,611** | **Non-current liabilities** | **29,989** |
| Property and equipment, net | 6,118 | Long-term debt | 14,674 |
| Operating lease, right-of-use asset | 8,199 | Operating lease liability | 7,755 |
| Goodwill | 3,707 | Other | 7,561 |
| Other | 3,587 | **Total liabilities** | **37,872** |
| | | **Shareholders' equity (deficit)** | **(7,904)** |
| **Total assets** | **29,968** | **Total liabilities & equity** | **29,968** |

**The identity, then the residual.** Substituting into (3.1):

$$E^{\text{book}}=29{,}968-37{,}872=-7{,}904\ \text{million}$$

(The line items are rounded: they sum to 7,885 and 29,990 against the printed subtotals of 7,884 and
29,989, a one-unit rounding difference.)

**Is Starbucks insolvent?** Slide 25: **no.** Book equity is −7.9 bn and the market capitalization
on 28 December 2020 was 122.6 bn:

$$E^{\text{mkt}}-E^{\text{book}}=122.6-(-7.9)=130.5\ \text{bn USD}$$

> **How does book equity go negative?** The statement of equity (note 04, eq. (4.9)) moves book
> equity by net income minus dividends, plus or minus issuance and **repurchases**. When cumulative
> payouts exceed paid-in capital plus retained earnings, the residual turns negative, while the
> brand, the customers and the store network that produce the cash stay off the balance sheet.
> Creditors lend against the **market** value of the assets: Berk (p. 29) notes that successful firms
> "are often able to borrow in excess of the book value of their assets". Amazon in June 2005
> had book equity of −64 million and a market value of equity over 15 billion (p. 29).

![Left: Starbucks 2020 book assets 30.0, total liabilities 37.9, book equity −7.9 and market capitalization 122.6, in USD billions. Right: a waterfall from market cap 122.6 plus interest-bearing debt 15.9 minus cash 5.0 to an enterprise value of 133.5, then plus lease liabilities 9.0 to 142.5](figures/L01-book-vs-market.png)

*Slides 24–25 (book items, market cap 122.6 bn) and eq. (3.6). Debt = short-term debt + current
portion of LTD + long-term debt = 15.9 bn; the lease column is a convention choice, not on the slide.*

The left panel shows the sign flip: the book claim of the owners is negative and the market's claim is
four times total book assets. The right panel builds enterprise value from the same balance sheet
(§7). Whether operating-lease liabilities count as debt changes EV by 9 bn, about 7%.

---

## 4 · U — intangible assets (slide 26)

Slide 26 (Visual Capitalist; "Tangible Assets vs. Intangible Assets for S&P 500 Companies,
1975–2018") stacks tangible and intangible value. The intangible share, computed from the chart's
own labels:

| Year | Total | Intangible | Intangible share |
|---|---|---|---|
| 1975 | 715 bn | 122 bn | $122/715=17.1\%$ |
| 1985 | 1.5 tn | 482 bn | $0.482/1.5=32.1\%$ |
| 1995 | 4.59 tn | 3.12 tn | $3.12/4.59=68.0\%$ |
| 2005 | 11.6 tn | 9.28 tn | $9.28/11.6=80.0\%$ |
| 2018 | 25.03 tn | 21.03 tn | $21.03/25.03=84.0\%$ |

> **Tangibles are "easy to value, thick and efficient secondary markets, insurable". Intangibles are
> "difficult to value, thin and inefficient secondary markets, difficult to insure"** (slide 26
> legend). The same properties that keep intangibles off the balance sheet make them poor collateral.
> This is the reason "redeployable assets" support high leverage in Tirole's stylized facts
> ([[../../rules/01_introducao_fatos|rules/01]]).

---

## 5 · C — the market-to-book ratio (slide 27)

$$\text{Market-to-book}=\frac{E^{\text{mkt}}}{E^{\text{book}}} \tag{3.3}$$

This is Berk's (2.3), p. 30. **Growth stocks** have a high market-to-book ratio; **value stocks** a low
one (slide 27). Berk's 2010 figures (p. 30): AmeriServ Financial 0.52, Citigroup 0.82, financial
services about 1, large U.S. firms close to 3, technology about 6, Amazon over 11.

**Starbucks.** Substituting into (3.3): $122{,}600/(-7{,}904)=-15.5$. **A negative ratio carries no
information about growth.** The ratio is meaningful only when $E^{\text{book}}>0$.

---

## 6 · C — the debt-equity ratio, book and market (slides 28–29)

The slide's definition (slide 28):

$$\frac{D}{E}\Big|_{\text{slide}}=\frac{L}{E} \tag{3.4}$$

Berk's (2.4) (p. 30) uses **interest-bearing debt** in the numerator ("short- and long-term debt,
including current maturities"). Either can be computed with book or market equity. **Always state
which definition you use.**

| Firm | Numerator | Book $E$ | Market $E$ | Book ratio | Market ratio |
|---|---|---|---|---|---|
| Global 2010 (Berk p. 31) | $D=5.5+113.2=118.7$ | 22.2 | 36 | $118.7/22.2=5.3$ | $118.7/36=3.3$ |
| Starbucks 2020 | $L=37{,}872$ | −7,904 | 122,600 | $-4.79$ (meaningless) | $37{,}872/122{,}600=0.309$ |
| Starbucks 2020 | $D=493+750+14{,}674=15{,}917$ | −7,904 | 122,600 | $-2.01$ (meaningless) | $15{,}917/122{,}600=0.130$ |
| GPA 2020 | $L=36{,}488$ | 16,807 | — | $36{,}488/16{,}807=2.171$ | — |

> **The market ratio "is more informative about the firm's leverage and capacity to meet future debt
> payments"** (slide 28). Even firms with negative book equity may carry a lot of debt because they
> are expected to be profitable, which makes the market ratio "particularly useful for assessing the
> leverage of high-growth and start-up firms". Berk (p. 31, fn. 3) adds that the book value of debt is
> used as a proxy for its market value because the two are usually close (slide 29 says the same).

**Net debt** treats cash as negative debt, "used on short notice to repay debts" (slide 29):

$$\text{Net debt}=D-C \tag{3.5}$$

The slide writes "liabilities less cash"; with interest-bearing debt, Starbucks:
$15{,}917-5{,}028=10{,}889$ million. GPA, using borrowings only: $(2{,}309+6{,}842)-8{,}711=9{,}151-8{,}711=440$
million BRL. Net debt is the better measure for firms with large cash balances.

---

## 7 · C — enterprise value (slide 30)

$$EV=E^{\text{mkt}}+D-C \tag{3.6}$$

This is Berk's (2.5), p. 31. **Derivation as a takeover cost** (slide 30's question: "how much cash
does an investor need to be the single owner of all the assets?"). The buyer pays three amounts:

$$\text{buy all the equity}: +E^{\text{mkt}}$$
$$\text{pay off the debt}: +D$$
$$\text{receive the firm's cash}: -C$$

Summing the three gives (3.6): what is bought is the business assets, net of the cash that comes with
them.

**Worked cases.**

Berk, Global (p. 31). Substituting $E^{\text{mkt}}=36$, $D=118.7$, $C=23.2$ into (3.6):

$$EV=36+118.7-23.2=131.5\ \text{million}$$

Berk, Example 2.2, Heinz, April 2010 (p. 32). The market cap, then book equity from the
market-to-book ratio (3.3), then debt from the book D/E:

$$E^{\text{mkt}}=46.15\times316.2\text{ m}=14.59\text{ bn}$$
$$E^{\text{book}}=14.59/7.99=1.83\text{ bn}$$
$$D=1.83\times2.64=4.83\text{ bn}$$
$$EV=14.59+4.83-0.5623=18.858\text{ bn}$$

Starbucks, from slides 24–25. Substituting $E^{\text{mkt}}=122{,}600$, $D=15{,}917$, $C=5{,}028$:

$$EV=122{,}600+15{,}917-5{,}028=133{,}489\ \text{million USD}$$

Counting the operating-lease liabilities ($1{,}268+7{,}755=9{,}023$) as debt gives
$133{,}489+9{,}023=142{,}512$. Both are in the figure of §3.

> **EV values the business; market cap values one claim on it.** EV is what FCF forecasts value
> (slide 61, note 06 §8). Because it nets out financing, EV multiples (EV/EBITDA, Berk pp. 39–40)
> are comparable across firms with different leverage, and P/E is not (note 05 §10).

---

## 8 · C — current and quick ratios (slide 31)

$$\text{Current ratio}=\frac{CA}{CL} \tag{3.7}$$

$$\text{Quick ratio (acid test)}=\frac{CA-\mathrm{Inv}}{CL} \tag{3.8}$$

Both measure the ability to meet short-term obligations; "some debt covenants require the current
ratio to be above a certain value" (slide 31).

| Firm | Current ratio (3.7) | Quick ratio (3.8) |
|---|---|---|
| GPA 2020 | $17{,}641/18{,}483=0.954$ | $(17{,}641-6{,}536)/18{,}483=11{,}105/18{,}483=0.601$ |
| Starbucks 2020 | $8{,}358/7{,}884=1.060$ | $(8{,}358-1{,}472)/7{,}884=6{,}886/7{,}884=0.873$ |

**Ross, Exemplo 3.1 (p. 62): paying current liabilities with cash pushes the ratio away from 1.**
Start from $CA=4$, $CL=2$ and use 1 of cash to pay 1 of current liabilities:

$$\frac{4-1}{2-1}=3>2$$

Start instead from $CA=2$, $CL=4$:

$$\frac{2-1}{4-1}=\frac13<\frac12$$

> **A ratio is not a level of liquidity.** The same transaction raises a healthy firm's current ratio
> and lowers a stressed firm's. Buying inventory for cash leaves (3.7) unchanged but lowers (3.8)
> (Ross p. 62).

---

## Links

- Prev / next: [[L01-02-balance-sheet-items]] · [[L01-04-income-statement]].
- Market equity in returns ratios: [[L01-05-ratios-dupont-roic]] §7 (the value problem), §10 (P/E).
- EV and FCF: [[L01-06-cash-flows-fcf]] §8. Market-value $D/E$ as the input of unlevering betas
  and MM II: [[../L02/L02-00-map|L02]] blocks 2A.2, 2A.9.
- Rules: [[../../rules/01_introducao_fatos|rules/01]] (Tirole Ch. 2 stylized facts on leverage);
  [[../../rules/02_valuation|rules/02]] (valuation).
- Practice: [Lista R1](../../Listas/lista-r1-accounting-capital-structure.md) Ex. 4 (Berk 2.8, p. 53:
  market cap, market-to-book, D/E, EV), Ex. 5 (Higgins 2.3, p. 71: ratio identities), Ex. 6
  (Berk 2.21, p. 55: book vs market leverage); quiz
  [[../../Simulados/quiz-topic1-accounting-2026-10-24|Topic 1 quiz]] tag `bs`.
- Books: Berk 2e §2.2–2.3 (pp. 29–33); Higgins 13e Ch. 1 pp. 22–25; Ross *Fundamentos* Cap. 3
  §3.3 (pp. 60–64).
