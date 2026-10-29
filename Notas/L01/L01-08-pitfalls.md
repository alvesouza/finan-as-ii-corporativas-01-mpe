---
tags: [notes, lecture-01, pitfalls, true-false, review]
date: 2026-10-24
status: taught
source: "Aula/Topic1.pdf slides 7–62; notes L01-01 to L01-06; original True/False items in the macro-1 style (rules/00_estilo_avaliacao.md)"
---

# Topic 1 · Pitfalls and a True/False self-test

Prev: [[L01-07-formulas]] · Next: [[L01-09-python]] · Map: [[L01-00-map]]

---

## Part I — the confusions this material produces

### 1 · Negative book equity is not insolvency
**Counterexample:** Starbucks, book equity −7,904 m and market cap 122.6 bn (slides 24–25). Book
equity is the residual (3.1) of historical costs and cumulative payouts (4.9). Solvency is about
whether the assets' **market** value covers the claims. → [[L01-03-book-vs-market-leverage]] §3.

### 2 · Profit is not cash
**Counterexample:** Berk's Global, positive net income and −0.4 m of operating cash flow (p. 44),
because receivables grew. Cash collected is $S-\Delta AR$ (4.1). → [[L01-06-cash-flows-fcf]] §1.

### 3 · "Depreciation is a source of cash"
Adding depreciation back in (6.1) only **undoes** a non-cash charge. **Minimal counterexample:** with
$\tau=0$, doubling depreciation lowers NI by the same amount it raises the add-back, so CFO does not
move. Depreciation's only cash effect runs through taxes: each unit of depreciation saves $\tau$ in
tax, which is why $\mathrm{EBIT}(1-\tau)+\text{Dep}$ in (6.6) rises with Dep when $\tau>0$.

### 4 · Which "D/E"?
The slide divides **total liabilities** by equity (3.4). Berk divides **interest-bearing debt**
(p. 30). Starbucks' market ratio is 0.309 on the first and 0.130 on the second. Net debt subtracts cash
as well (3.5). State the definition, and say book or market. → [[L01-03-book-vs-market-leverage]] §6.

### 5 · EV is not "market cap + total liabilities"
(3.6) adds **debt** and subtracts **cash**. Operating liabilities such as payables are part of the
business, so they stay out. Leases are a convention choice: Starbucks' EV is 133.5 bn without them and
142.5 bn with them. → §7.

### 6 · A higher ROE is not better performance
Three failures (Higgins pp. 54–57). **Timing:** an equity-funded project lowers ROE before it pays.
**Risk:** Take-a-Risk's 30% is worse than Never-Dare's 20%. **Value:** ROE is on **book** equity
(Polaris 28.9% vs a 7.0% earnings yield). → [[L01-05-ratios-dupont-roic]] §7.

### 7 · Leverage raises ROE only with a positive spread, and always raises its risk
By (5.20), ROE rises with $D/E$ iff $\mathrm{ROIC}>r_D(1-\tau)$. **Counterexample:** slide 50's firm at
$r_D=16\%$ has ROE −14.4%. Even with a positive spread, (5.22) multiplies ROE's volatility by $1+D/E$.
→ §8–9.

### 8 · ROA "measures operations"
ROA has net income, which is after interest, in the numerator, so it **falls with any debt** (5.21):
Company A shows 1.8% against B's 7.2% with identical operations. Only ROIC (5.16) is financing-neutral.
→ §8.

### 9 · DuPont's factors are independent levers
Raising leverage raises interest and **lowers the net margin** in (5.14) (Berk p. 38, fn. 7). The
identity is exact, but it says nothing about causation. → §6, §9.

### 10 · FCF uses actual taxes
(6.6) charges tax on **EBIT**, as if there were no debt. Actual taxes are lower by $\tau\cdot\text{Int}$,
so the claims together receive $FCF+\tau\,\text{Int}$ (6.11). Mixing in actual taxes and then also
using an after-tax WACC counts the tax shield **twice**. → [[L01-06-cash-flows-fcf]] §7.

### 11 · Interest belongs in FCF
Interest is a payment **to a claimant**, so it is excluded from FCF, as are dividends. Subtracting it
gives a cash flow to equity, and FCFE also needs net borrowing (6.7). Discounting FCF − interest at a
firm-wide rate mixes the two valuations of §8.

### 12 · Every current item is in ΔNWC
Short-term **debt** and current maturities are financing. Working-capital investment nets only
**non-interest-bearing** current liabilities (slide 60; Berk p. 28). Securities bought for cash
management, such as GM's AFS lines, are not capex either. → §4, §6.

### 13 · A better current ratio means more liquidity
Paying current liabilities with cash **raises** a ratio above 1 and **lowers** one below 1 (Ross
Exemplo 3.1, p. 62). Negative NWC can also be a business model (GPA, supplier finance).
→ [[L01-03-book-vs-market-leverage]] §8, [[L01-02-balance-sheet-items]] §6.

### 14 · Positive net income means owners are compensated
Net income charges nothing for equity. Polaris's 414 m becomes 271 m of economic earnings at a 10%
cost of equity (5.6). → [[L01-05-ratios-dupont-roic]] §3.

### 15 · A high P/E means overvalued
P/E rises with growth, falls with risk, and moves with leverage (slide 51). It signals overvaluation
only **relative to comparable peers**, and even then only "could". Depressed earnings inflate it
(Polaris above 45 in 2017). → §10.

---

## Part II — True/False self-test (original items)

*Scoring as in `macro-1`: $\max\{0,\text{correct}-\text{wrong}/2\}$; blanks do not count.*

**1.** A firm whose total liabilities exceed its total book assets must have negative book equity.
**T.** Book equity is defined as the residual $A-L$ (3.1). If $L>A$ the residual is negative by
construction, as in Starbucks (126% of assets in liabilities). Nothing says the firm's market value is
negative.

**2.** $A=L+E$ holds in market value only if the firm has no debt.
**F.** (1.8) follows from linear pricing and the exhaustive split (1.6), for **any** split of the
cash flow. Debt changes who receives each state's cash, not the sum, as long as the split leaves the
cash flow itself unchanged.

**3.** Buying a machine for cash changes total assets but not book equity.
**F.** It changes the **composition** of assets (cash down, PP&E up by the same amount). Total assets,
liabilities and equity are all unchanged. Only later depreciation reduces equity, through net
income.

**4.** Straight-line depreciation lowers the firm's cash in every year of the asset's life.
**F.** The cash leaves once, at purchase (slide 34). Depreciation allocates that outlay over time
(note 02 §2). Its only cash effect is the tax it saves when $\tau>0$.

**5.** A firm can report positive net income and negative cash flow from operations in the same year.
**T.** Receivable or inventory build-ups are subtracted in (6.1). Berk's Global did exactly this
(p. 44).

**6.** Under the accrual principle, a customer paying an old invoice raises revenue in the period of payment.
**F.** Slide 33, row 2: cash flow yes, revenue no. The revenue was booked at the sale.

**7.** With all of cost of sales variable and all SG&A fixed, GM's 2020 operating income would fall about 20.6% after a 10% fall in sales.
**T.** By (4.8) the elasticity is $1+7{,}038/6{,}634=2.061$, and $2.061\times10\%=20.6\%$; the direct
computation in note 04 §4 gives −20.61%.

**8.** Market-to-book above 1 means the firm's accountants overstated its liabilities.
**F.** It means the market values the equity above its historical-cost residual. Forward-looking value
and off-balance-sheet assets (slide 23) explain it, with no accounting error required.

**9.** For a firm with large cash balances, net debt is a better leverage measure than gross debt.
**T.** Slide 29: cash can repay debt on short notice, so it acts as negative debt.

**10.** Enterprise value equals market capitalization plus total liabilities.
**F.** (3.6) adds **debt** and subtracts **cash**. Operating liabilities such as payables and accruals
stay out because they belong to the business being valued.

**11.** If two firms have the same ROE, they have the same net profit margin.
**F.** DuPont (5.14) has three factors. Google (14.8%) and Chevron (14.4%) reach similar ROEs with
margins of 21.6% and 9.7% (slide 48).

**12.** Holding ROIC, $r_D$ and $\tau$ fixed, ROE is a linear function of the book debt-equity ratio.
**T.** (5.20) is affine in $D/E$ with intercept ROIC and slope $\mathrm{ROIC}-r_D(1-\tau)$.

**13.** Raising leverage always raises ROE.
**F.** Only if the spread is positive. At $r_D(1-\tau)>\mathrm{ROIC}$ leverage lowers ROE; slide 50's
firm at $r_D=16\%$ gets −14.4%.

**14.** In slide 50's example, ROA rates Company A's operations below Company B's even though they are identical.
**T.** ROA is 1.8% vs 7.2% because A's net income is after interest (5.21). Only ROIC (7.2% for both)
is financing-neutral.

**15.** With $D/E=9$, a one-point fall in ROIC lowers ROE by nine points.
**F.** By ten: by (5.20), $\partial\mathrm{ROE}/\partial\mathrm{ROIC}=1+D/E=10$ (5.22).

**16.** Positive accounting net income implies that shareholders earned at least their required return.
**F.** Net income charges no cost for equity (slide 42). Economic earnings (5.6) can be negative while
NI is positive.

**17.** Free cash flow to the firm subtracts interest expense because interest is a cash outflow.
**F.** Interest is a payment to a claimant. FCF (6.6) is measured before any payment to claimants
and taxes EBIT as if the firm were all-equity.

**18.** FCFE can exceed FCF.
**T.** By (6.7), when net borrowing exceeds after-tax interest. GM 2020: FCF 13,290 and FCFE 18,574
(note 06 §6).

**19.** With corporate taxes, the cash flow to debtholders plus FCFE equals unlevered FCF exactly.
**F.** They sum to $FCF+\tau\,\text{Int}$ (6.11). Ross's Brasil S/A: $24+63=87=63.22+23.78$.

**20.** An increase in accounts payable raises cash flow from operations, holding everything else fixed.
**T.** Purchases expensed (or put in inventory) but not yet paid: the sign is $+$ in (6.1).

**21.** Diluted EPS can never exceed basic EPS when options and convertibles are counted in the denominator as on slide 40.
**T.** With the slide's definition (5.2), the numerator is the same NI and the denominator is at least
$N$, so for positive NI the diluted figure is weakly smaller. (Accounting standards refine this with
the convertible's interest and anti-dilution rules, which are not on the slides.)

**22.** A higher P/E than industry peers proves the stock is overvalued.
**F.** Slide 51 says it "could indicate" overvaluation. Higher growth, lower risk, or a different
capital structure can all justify it.

---

## Links

- Every pitfall points to its note; equations in [[L01-07-formulas]].
- More practice in the same style: [[../../Simulados/quiz-topic1-accounting-2026-10-24|Topic 1 quiz]]
  (tags `bs`, `is`, `cf`); [Lista R1](../../Listas/lista-r1-accounting-capital-structure.md) Ex. 5
  (Higgins 2.3, p. 71, true/false on ratios); grading style [[../../rules/00_estilo_avaliacao|rules/00]].
