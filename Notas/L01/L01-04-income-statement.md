---
tags: [notes, lecture-01, accounting, income-statement, accrual, operating-leverage]
date: 2026-10-24
status: taught
source: "Aula/Topic1.pdf slides 32–39 (block 1.6); Higgins 13e Ch. 1 'Accrual Accounting' and 'Depreciation', pp. 12–13; Berk 2e Ch. 2 §2.4, eq. (2.8), p. 34, and §2.6, eq. (2.20), p. 44; slide 39 GM income statement 31/12/2020"
---

# 1.6 · The income statement: accrual, matching, depreciation, from sales to net income

> **Claim.** The income statement measures **profit over a period**, and profit is an
> **allocation**, not a count of cash. Revenue is booked when the sale is made, costs when goods
> and services are bought, and a fixed asset's cost is spread over its life. The lines from sales to
> net income show **who is paid in what order**: suppliers and workers, then lenders (interest), then
> the state (taxes), then owners. A cost structure heavy in fixed costs makes operating income move
> **more than proportionally** with sales.

Prev: [[L01-03-book-vs-market-leverage]] · Next: [[L01-05-ratios-dupont-roic]] · Map: [[L01-00-map]]

**Notation.**

| Symbol | Meaning | Range |
|---|---|---|
| $S$ | sales (revenue) of the period | $\ge0$ |
| $\mathrm{COGS}$ | cost of goods sold (cost of sales) | $\ge0$ |
| $\mathrm{OpEx}$ | other operating expenses (SG&A, R&D, depreciation) | $\ge0$ |
| $\mathrm{NOI}$ | nonoperating income | real |
| $\mathrm{Int}$, $T$ | interest expense, income taxes | $\ge0$ |
| $v$, $F$ | variable-cost share of sales, fixed costs (§4) | $0\le v<1$, $F\ge0$ |
| $\Delta AR$ | increase in accounts receivable over the period | real |
| $\mathrm{Div}$ | dividends paid | $\ge0$ |

---

## 1 · C — what the income statement measures (slide 32)

The income statement (P&L) "attempts to measure the profits the firm generates during a period of
time": it lists revenues and expenses. **Revenues increase book equity, expenses reduce it**
(slide 32). Through net income it is the flow that links two balance sheets (§5).

---

## 2 · C — the accrual and matching principles (slides 32–33)

**Accrual principle:** revenue is recognized at the time of the sale, not when the customer pays;
expenses when goods and services are bought, not when suppliers are paid. **Matching principle:**
revenues and expenses are recorded in the period in which the transaction occurs (slide 32).

The slide-33 table:

| Event | Cash flow? | Revenue / expense? |
|---|---|---|
| A customer buys and pays in cash | Yes | Yes |
| A customer pays the bill for an earlier purchase | Yes | No |
| A customer buys and agrees to pay later | No | Yes |

The gap between the two columns is the change in receivables:

$$\text{cash collected from customers}=S-\Delta AR \tag{4.1}$$

**Higgins, Polaris 2020 (pp. 12–13).** Revenue 7,108 million; receivables rose by 67 million.
Substituting into (4.1):

$$\text{cash collected}=7{,}108-67=7{,}041\ \text{million}$$

"The other 67 million still awaits collection."

---

## 3 · C — depreciation: spreading capex over the asset's life (slides 34–35)

Charging a fixed asset's full cost in the year of purchase would make profit "too low in the year
of the investment, and too high in the other productive years" (slide 34). Spreading the cost as
depreciation **matches** the asset's cost to the revenue it helps produce.

**Higgins's facility (p. 13), with eq. (2.2) of note 02:** cost 50 million, 10-year life,
straight line, no salvage value, so 5 million a year. The two treatments of the same outlay, years 1
to 3 (the purchase is booked in year 1 under expensing):

| Year | 1 | 2 | 3 | … | 10 | Sum over 10 years |
|---|---|---|---|---|---|---|
| Expense if charged at once | 50 | 0 | 0 | … | 0 | 50 |
| Depreciation (straight line) | 5 | 5 | 5 | … | 5 | 50 |
| Cash outflow | 50 | 0 | 0 | … | 0 | 50 |

> **Both treatments expense 50 in total and neither changes the cash row.** Depreciation changes
> **when** profit falls, not **whether** cash leaves. "Depreciation is not a cash expense; the cash
> outlay only occurs at the time of the investment" (slide 34). Its one cash consequence runs through
> taxes, since depreciation is deductible (note 06 §6, note 08 pitfall 3).

How much to depreciate requires three estimates: productive life, salvage value, and the method,
straight line or accelerated (slide 35; Higgins p. 13). Also by the matching principle, **an
increase in inventory is not an expense**: goods are expensed (as COGS) when sold (slide 35).

---

## 4 · C — the lines of the income statement and operating leverage (slides 36–37)

From sales to net income, one subtraction per line:

$$\text{Gross profit}=S-\mathrm{COGS} \tag{4.2}$$

$$\text{Operating income}=\text{Gross profit}-\mathrm{OpEx} \tag{4.3}$$

$$\mathrm{EBIT}=\text{Operating income}+\mathrm{NOI} \tag{4.4}$$

$$\text{Net income}=\mathrm{EBIT}-\mathrm{Int}-T \tag{4.5}$$

> **EBIT is income "before it is split among debtholders, equityholders, and the tax authorities"**
> (slide 37). Net income is the owners' residual. Apart from issuance or payout, it is what makes
> book equity grow (§5).

**Operating leverage.** Slide 36: most COGS is **variable** (moves with sales), most other operating
expenses are **fixed**, and "companies with a high proportion of fixed costs are more vulnerable to
sale declines". To see why, write COGS $=vS$ and $\mathrm{OpEx}=F$ in (4.2)–(4.3):

$$\text{Operating income}=S-vS-F=(1-v)S-F \tag{4.6}$$

A change $\Delta S$ in sales, with $v$ and $F$ fixed, changes (4.6) by

$$\Delta\,\text{Operating income}=(1-v)\,\Delta S \tag{4.7}$$

Divide the percentage change in operating income by the percentage change in sales:

$$\frac{\Delta\text{OI}/\text{OI}}{\Delta S/S}=\frac{(1-v)\Delta S/\text{OI}}{\Delta S/S}=\frac{(1-v)S}{\text{OI}}$$

Substitute $(1-v)S=\text{OI}+F$ from (4.6):

$$\frac{\Delta\text{OI}/\text{OI}}{\Delta S/S}=\frac{\text{OI}+F}{\text{OI}}=1+\frac{F}{\text{OI}} \tag{4.8}$$

> **The elasticity of operating income to sales exceeds 1 by the ratio of fixed costs to operating
> income.** With $F=0$ the elasticity is 1. A firm whose fixed costs are large relative to its
> operating income sees its profit swing by a multiple of its sales.

**On GM's numbers (slide 39, §6), with the slide's own heuristic** (all of cost of sales variable, all
of SG&A fixed): $F=7{,}038$, $\text{OI}=6{,}634$. Substituting into (4.8):

$$1+\frac{7{,}038}{6{,}634}=1+1.0609=2.061$$

A 10% fall in sales cuts gross profit from 13,672 to $0.9\times13{,}672=12{,}304.8$. Operating income
falls to

$$12{,}304.8-7{,}038=5{,}266.8$$

which is a change of

$$\frac{5{,}266.8-6{,}634}{6{,}634}=-20.61\%=2.061\times(-10\%)$$

---

## 5 · C — the statement of equity (slide 38)

$$E^{\text{book}}=\text{paid-in capital}+\text{retained earnings}$$

$$E^{\text{book}}_{\text{end}}=E^{\text{book}}_{\text{begin}}+\text{NI}-\mathrm{Div}\pm\text{other changes} \tag{4.9}$$

"Other changes" are equity issuance, treasury-share transactions (repurchases) and stock-based
compensation (slide 38). With no other changes, retained earnings grow by NI − Div, Berk's (2.20)
(p. 44). **Berk's Global, 2010 (p. 44):** NI 2 million, dividends 1 million, so retained earnings
rise by $2-1=1$ million, a payout ratio of $1/2=50\%$ (Berk (2.21)).

> **(4.9) explains Starbucks' negative book equity (note 03 §3):** large repurchases enter
> "other changes" with a minus sign, and nothing in (4.9) requires the residual to stay positive.

---

## 6 · C — worked example: GM, income statement 2020 (slide 39)

USD millions, as on slide 39, with each subtotal recomputed:

| Line | Value | Check |
|---|---|---|
| Net sales automotive | 108,673 | |
| Net sales Financial | 13,812 | |
| **Net sales** | **122,485** | $108{,}673+13{,}812=122{,}485$ |
| Automotive and other cost of sales | 97,539 | |
| GM financial interest, operating and other expenses | 11,274 | |
| **Cost of sales** | **108,813** | $97{,}539+11{,}274=108{,}813$ |
| **Gross profit** (4.2) | **13,672** | $122{,}485-108{,}813=13{,}672$ |
| Automotive and other SG&A | 7,038 | |
| **Operating income** (4.3) | **6,634** | $13{,}672-7{,}038=6{,}634$ |
| Nonoperating income | 2,559 | |
| **EBIT** (4.4) | **9,193** | $6{,}634+2{,}559=9{,}193$ |
| Interest expense | 1,098 | |
| **Pre-tax income** | **8,095** | $9{,}193-1{,}098=8{,}095$ |
| Taxes | 1,774 | |
| **Net income** (4.5) | **6,321** | $8{,}095-1{,}774=6{,}321$ |

**Effective tax rate** (used for GM's free cash flow in note 06 §6):

$$\tau=\frac{1{,}774}{8{,}095}=0.21915$$

> **Read the cost-of-sales line carefully.** GM Financial's **interest** sits inside cost of sales
> (11,274, "GM financial interest, operating and other expenses"). For a captive finance arm,
> borrowing is part of operations, so the "interest expense" line (1,098) is only the automotive
> side's. Ratios that separate operating from financing items (EBIT margin, coverage, ROIC, FCF) are
> blurred for firms with a finance subsidiary.

---

## Links

- Prev / next: [[L01-03-book-vs-market-leverage]] · [[L01-05-ratios-dupont-roic]] (margins,
  EBITDA and coverage on these GM numbers, §2 and §5).
- Depreciation and accruals in cash flow: [[L01-06-cash-flows-fcf]] §2; book value of an asset:
  [[L01-02-balance-sheet-items]] §2.
- Forward: taxable income and the interest tax shield in [[../L03/L03-00-map|L03]] (block 2B.1).
- Practice: [Lista R1](../../Listas/lista-r1-accounting-capital-structure.md) Ex. 2 (Berk 2.12, p. 54:
  margins), Ex. 3 (Berk 2.31, p. 57: depreciation, earnings vs cash), Ex. 15 (Ross 2.25–2.26,
  pp. 50–51: two years of statements); quiz
  [[../../Simulados/quiz-topic1-accounting-2026-10-24|Topic 1 quiz]] tag `is`.
- Books: Higgins 13e Ch. 1 "The Income Statement", "Accrual Accounting", "Depreciation"
  (pp. 11–13); Berk 2e §2.4 (pp. 33–34); Ross *Fundamentos* Cap. 2 §2.2 (p. 30).
