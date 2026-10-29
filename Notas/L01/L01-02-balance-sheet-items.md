---
tags: [notes, lecture-01, accounting, balance-sheet, working-capital]
date: 2026-10-24
status: taught
source: "Aula/Topic1.pdf slides 15–21 (block 1.3); Berk 2e Ch. 2 §2.2, eq. (2.2), pp. 27–28; Higgins 13e Ch. 1 pp. 9–10, 13 (depreciation example); slide 21 GPA balance sheet 31/12/2020"
---

# 1.3 · Balance-sheet items: current vs non-current, depreciation, net working capital

> **Claim.** The balance sheet sorts assets and liabilities by **horizon**: within one year, or
> beyond. Fixed assets enter at cost and are written down by depreciation, an accounting
> allocation that **moves no cash**. Current assets minus current liabilities is **net working
> capital**, the short-term cushion. The GPA example shows NWC can be negative because
> **suppliers finance the firm**.

Prev: [[L01-01-balance-sheet-view]] · Next: [[L01-03-book-vs-market-leverage]] · Map: [[L01-00-map]]

**Notation.**

| Symbol | Meaning | Range |
|---|---|---|
| $CA$, $CL$ | current assets, current liabilities | $\ge0$ |
| $NWC$ | net working capital, $CA-CL$ | real |
| $K_0$ | acquisition cost of a fixed asset | $>0$ |
| $S_v$ | salvage value at the end of its life | $0\le S_v\le K_0$ |
| $n$ | productive life, years | $n\ge1$ |
| $\mathrm{Dep}_k$, $BV_k$ | depreciation in year $k$, book value at the end of year $k$ | $\ge0$ |

---

## 1 · C — current assets (slide 15)

**Current assets** can be converted into cash **within one year** (slide 15; Berk §2.2, p. 27):

| Item | What it is |
|---|---|
| Cash and marketable securities | short-term, liquid, low-risk investments: money-market funds, government debt, bank deposits |
| Accounts receivable | owed by customers who bought on credit |
| Inventories | raw materials, work in progress, finished goods |

---

## 2 · C — non-current assets, goodwill and depreciation (slide 16)

**Non-current ("long-term") assets:** fixed assets such as property, plant and equipment, and
**goodwill**. Slide 16 defines goodwill as the difference between the price of an acquisition and the
*fair value* of what was acquired. Fair value is "the accountant's estimate of the potential value
of an asset, not necessarily equal to book value":

$$\text{Goodwill}=\text{price paid for the target}-\text{fair value of its identifiable net assets} \tag{2.1}$$

**Depreciation.** Fixed assets wear out; the accountant writes down their book value by an amount
called depreciation. Two facts carry through the whole lecture (slide 16):

> **Depreciation is not a cash expense.** The cash left the firm when the asset was bought.
> **Book value of an asset = acquisition cost − accumulated depreciation.**

With straight-line depreciation (one of the methods of slide 35; note 04 §3):

$$\mathrm{Dep}_k=\frac{K_0-S_v}{n}\quad(k=1,\dots,n) \tag{2.2}$$

$$BV_k=K_0-\sum_{j=1}^{k}\mathrm{Dep}_j \tag{2.3}$$

**Worked example (Higgins 13e, p. 13).** A facility costs $K_0=50$ million, has a 10-year life, and,
we add for the arithmetic, no salvage value. Substituting $K_0=50$, $S_v=0$, $n=10$ into (2.2):

$$\mathrm{Dep}_k=\frac{50-0}{10}=5\ \text{million per year}$$

Substituting into (2.3) at the end of year 3:

$$BV_3=50-(5+5+5)=35\ \text{million}$$

| End of year $k$ | 0 | 1 | 3 | 5 | 10 |
|---|---|---|---|---|---|
| $BV_k$ (millions) | 50 | 45 | 35 | 25 | 0 |
| Cash paid in year $k$ | 50 | 0 | 0 | 0 | 0 |

> **The book value falls by 5 a year while the cash row is zero after year 0.** The 5 per year is an
> allocation of a past outlay to the years it serves (Higgins: "the allocation of past expenditures to
> future time periods to match revenues and expenses", p. 13). Note 04 §3 shows the income-statement
> side. Note 06 §2 shows why the cash-flow statement adds the 5 back.

---

## 3 · U — the rise in corporate cash (slide 17)

Slide 17 reproduces Figure 1 of Faulkender, Hankins and Petersen (2019), built from the Federal
Reserve Flow of Funds, Table L.102 (nonfinancial business): checking and savings accounts plus debt
securities held, 1994–2017. Read off the chart, aggregate corporate cash rises from under 1 trillion
dollars to roughly 4 trillion, and **faster than GDP**: the cash/GDP index goes from 100 (1994) to
about 160. The paper's title states the two candidate explanations: **precautionary savings** or
**foreign taxes**. Why firms hold liquidity at all is the liquidity topic of the syllabus
(rules/05).

---

## 4 · C — liabilities (slides 18–19)

**Current liabilities**, due within one year (slide 18):

| Item | What it is |
|---|---|
| Debt due next year | from short-term **and** long-term instruments (current portion of long-term debt) |
| Accounts payable | owed to suppliers for credit purchases |
| Accruals | salaries, taxes owed but not yet paid |
| Deferred (unearned) revenue | cash received for products not yet delivered |

**Non-current liabilities** extend beyond one year: debt payments not due within the next
accounting year (slide 19).

Berk (p. 28) adds a distinction that matters later. Notes payable and short-term debt come from
**financing** decisions; accounts payable and accruals come from **operating** decisions.
Free cash flow (note 06, eq. (6.6)) puts the operating liabilities in working capital and the financing
ones in debt.

---

## 5 · C — net working capital (slide 20)

$$NWC=CA-CL \tag{2.4}$$

This is Berk's (2.2), p. 28. It measures short-term financial health: firms with low NWC "might
not have enough resources to meet short-term obligations" (slide 20).

**Berk's Global Corporation, 2010 (p. 28).** Substituting $CA=57.0$, $CL=34.7$ into (2.4):

$$NWC=57.0-34.7=22.3\ \text{million}$$

---

## 6 · C — worked example: GPA, 31/12/2020 (slide 21)

BRL millions, as on the slide:

| Assets | | Liabilities & shareholders' equity | |
|---|---|---|---|
| **Current assets** | **17,641** | **Current liabilities** | **18,483** |
| Cash and equivalents | 8,711 | Trade payable, net | 11,424 |
| Trade receivable, net | 686 | Borrowings and financing | 2,309 |
| Inventories | 6,536 | Lease liabilities | 947 |
| Other | 1,708 | Financing of property and equipment | 100 |
| | | Other | 3,703 |
| **Non-current assets** | **35,654** | **Non-current liabilities** | **18,005** |
| Property and equipment, net | 19,888 | Borrowings and financing | 6,842 |
| Intangible | 6,164 | Lease liabilities | 7,427 |
| Other | 9,602 | Other | 3,736 |
| | | **Total liabilities** | **36,488** |
| | | **Shareholders' equity** | **16,807** |
| **Total assets** | **53,295** | **Total liabilities & equity** | **53,295** |

**Every subtotal checks.**

$$CA=8{,}711+686+6{,}536+1{,}708=17{,}641$$
$$NCA=19{,}888+6{,}164+9{,}602=35{,}654$$
$$A=17{,}641+35{,}654=53{,}295$$
$$CL=11{,}424+2{,}309+947+100+3{,}703=18{,}483$$
$$NCL=6{,}842+7{,}427+3{,}736=18{,}005$$
$$L=18{,}483+18{,}005=36{,}488$$
$$L+E=36{,}488+16{,}807=53{,}295=A\quad\checkmark\ (1.1)$$

**Net working capital**, substituting into (2.4):

$$NWC=17{,}641-18{,}483=-842\ \text{million BRL}$$

**Where the short-term money comes from.** Trade payables relative to current liabilities and to
total assets:

$$\frac{11{,}424}{18{,}483}=0.6181,\qquad \frac{11{,}424}{53{,}295}=0.2144$$

> **Suppliers fund 62% of GPA's current liabilities and 21% of its whole balance sheet**, against
> 2,309 of short-term borrowings. This is the slide's remark ("note the importance of suppliers in
> the provision of short-term financing"). A grocer sells for cash quickly and pays suppliers later,
> so **negative NWC is a feature of the business model, not a sign of distress**. Whether trade credit
> is cheap finance or a symptom of constraints is the subject of
> [Lista R5b](../../Listas/lista-r5b-trade-credit-working-capital.md).

![Common-size balance sheets of GPA and Starbucks, 2020: assets column (cash, receivables, inventories, other current, non-current) beside the liabilities-plus-equity column (trade payables, other current liabilities, non-current liabilities, equity), each as a percent of total assets; GPA's equity is 31.5% while Starbucks' equity is a negative 26.4% below the zero line](figures/L01-balance-sheets.png)

*Slides 21 and 24 as percentages of total assets; equation (1.1) is the dotted 100% line; Starbucks'
liabilities run past 100% and its equity hangs below zero.*

Both firms satisfy (1.1). GPA's two columns meet at 100% with equity on top. At Starbucks the
liabilities alone reach 126% of the assets, so book equity must be −26%: the identity forces a
negative residual. Payables are 21% of GPA's balance sheet and 3.5% of Starbucks'. Note 03 takes up
Starbucks.

---

## Links

- Prev / next: [[L01-01-balance-sheet-view]] · [[L01-03-book-vs-market-leverage]] (current and
  quick ratios on these same numbers, §8).
- Depreciation in the income statement: [[L01-04-income-statement]] §3; in the cash-flow statement:
  [[L01-06-cash-flows-fcf]] §2.
- NWC in free cash flow: [[L01-06-cash-flows-fcf]] eq. (6.6); NWC recouped at a project's end:
  [[../L02/L02-00-map|L02]] block 2A.3.
- Rules: [[../../rules/05_liquidez|rules/05]] (liquidity, why firms hold cash).
- Practice: [Lista R1](../../Listas/lista-r1-accounting-capital-structure.md) Ex. 1 (Higgins 1.4,
  p. 33), Ex. 14 (Higgins 2.11, p. 74, balance-sheet reconstruction); quiz
  [[../../Simulados/quiz-topic1-accounting-2026-10-24|Topic 1 quiz]] tag `bs`.
- Books: Berk 2e §2.2 (pp. 26–28); Higgins 13e Ch. 1 "The Balance Sheet" (pp. 9–10),
  "Depreciation" (p. 13).
