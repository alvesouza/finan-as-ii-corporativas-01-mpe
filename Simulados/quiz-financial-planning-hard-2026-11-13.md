---
quiz: "Financial planning and forecasting — hard conceptual quiz"
tags:
  pfs: "Percent-of-sales pro forma, EFN and the plug"
  cap: "Capacity, idle capacity and the timing of expansion"
  grow: "Internal and sustainable growth, growth vs. value"
  val: "Valuing an expansion from forecast free cash flows"
---

## pfs

Q: A pro forma forecast uses external financing required (EFN) as the plug, assumes the whole EFN is borrowed, and charges interest on end-of-period debt. Why is the forecast circular, and what does ignoring the circularity do to the EFN estimate?
- Interest on new debt is a financing flow, not an operating cost, so it is kept out of the retained-earnings line; the loop is only apparent and EFN is the same whether or not it is solved.
- New debt raises interest, and the extra interest cuts taxes by more than it cuts net income; ignoring the loop leaves out this tax saving and so overstates EFN, which errs on the safe side.
- EFN sets new debt, new debt sets interest, interest sets net income and so retained earnings, which set EFN; ignoring the loop leaves out interest on the new debt and so understates EFN.
- EFN depends on the payout ratio, and the payout ratio depends on EFN through the dividend policy; the loop is broken by fixing dividends, after which interest has no effect on EFN.
<!-- YW5zOjI= -->
> Higher borrowing means more interest, lower net income, lower retained earnings and therefore a larger EFN, which again means more borrowing. The loop converges (each round adds only after-tax interest on the increment), so it is solved by iteration or algebraically. Skipping it omits the after-tax interest on the new debt and slightly understates the need. Taxes soften the effect (the shield is $\tau$ times the extra interest) but never reverse it.
> Ref: Higgins 13e Ch. 3 §3.1.2 (p. 86) and §3.3 (pp. 89–92); Berk *Fundamentals* Ch. 18 §18.2 (pp. 537–540, interest held fixed in the first pass)
> Similar: Lista R2c, Ex. 12 (R&E Supplies, circular interest); Lista R2c, Ex. 8 (two-pass pro forma)

Q: A toy maker sells most of its output in the last quarter. Its annual pro forma for next year, built from year-end balance sheets, shows zero external financing required. What does this tell its treasurer about borrowing needs during the year?
- Little: year-end balances miss the mid-year build-up of inventory and receivables, so peak needs can be large even with a zero annual EFN; a monthly cash budget must size the seasonal line.
- That no borrowing will be needed: the annual pro forma integrates every flow in the year, so any intra-year deficit would already appear in the year-end balance of cash or of external financing.
- That borrowing will be needed only if sales fall short of the forecast, since a zero EFN means that planned cash receipts and planned payments match in every single month of the forecast year.
- That the firm should borrow long-term now to cover the season, because a zero EFN at year end implies that short-term debt would have to be rolled over at the trough of the seasonal cycle.
<!-- YW5zOjA= -->
> A pro forma is a snapshot at the forecast date. For a seasonal firm the need peaks when inventory and receivables are largest, well before year end, and unwinds as collections come in, so an annual EFN of zero is compatible with a large mid-year deficit. Only a forecast at the frequency of the cycle (a cash budget, or quarterly pro formas as for Toys-4-Kids) reveals the peak.
> Ref: Higgins 13e Ch. 3 §3.1.3 (p. 86), §3.6 (p. 96), §3.7 (p. 100); Berk *Fundamentals* Ch. 20 §20.1 (p. 593)
> Similar: Lista R2c, Ex. 2 (Higgins 3.4c); Lista R5b, Ex. 15 (Toys-4-Kids quarterly forecast)

Q: Three analysts forecast next year's external financing for the same firm from the same assumptions: one builds a pro forma balance sheet, one a cash-flow forecast of sources and uses, and one a cash budget of receipts and disbursements. How should their estimates of the annual funding need compare?
- The cash-flow forecast gives a higher number, since it counts every use of cash, while the pro forma balance sheet nets spontaneous liabilities against assets and so hides part of the need.
- The cash budget gives the lowest number, since it tracks actual receipts and disbursements, while the two accrual-based methods count non-cash items such as depreciation as needs.
- The pro forma balance sheet gives the highest number, since it adds the plug to equity, while the other two methods treat the external financing as an outflow that offsets the deficit.
- They coincide for the year as a whole, since the three are different presentations of the same assumptions; a gap between them signals inconsistent inputs, not a property of a method.
<!-- YW5zOjM= -->
> Every change in a balance-sheet account is a source or a use of cash, and a cash budget is the same flows grouped by receipt and payment. With identical assumptions the three must give the same annual need; they differ in what they show (balance-sheet structure, sources and uses, timing within the year), not in the answer. A gap is a bookkeeping error.
> Ref: Higgins 13e Ch. 3 §3.5–3.7 (pp. 95–100)
> Similar: Lista R2c, Ex. 2 (Higgins 3.4b, true or false); Lista R2c, Ex. 5

## cap

Q: A firm's fixed assets currently run below full capacity, while its current assets and payables scale with sales. How does this idle capacity shape the relation between sales growth $g$ and external financing required?
- It lowers the intercept but not the slope: a fixed share of plant is idle for good, so required financing is a straight line in growth that sits below the full-capacity line at every growth rate.
- It creates a kink: until sales reach full capacity only net working capital needs funding, so financing rises slowly with growth; past that point new plant is needed and the slope steepens.
- It has no effect: idle plant is already on the balance sheet and already financed, and the percent-of-sales ratios use existing book values, so the forecast comes out identical either way.
- It steepens the line from the start: idle plant must first be brought back into service, which takes extra inventory and receivables per unit of sales before any new plant is bought.
<!-- YW5zOjE= -->
> With sales at a fraction $c$ of capacity, sales can grow by $1/c - 1$ with no new fixed assets. Below that rate only current assets net of spontaneous liabilities grow with sales; above it, fixed assets must grow with the sales in excess of full-capacity sales, so EFN is piecewise linear in $g$ with a steeper second segment. Idle capacity lowers EFN, but not uniformly.
> Ref: Ross *Fundamentos* Cap. 4 §4.3, "Uma situação alternativa" (p. 104)
> Similar: Lista R2c, Ex. 11 (Turismo da Onça at 80% capacity, 4.26); Lista R2c, Ex. 14

Q: A firm's plant will hit capacity in two years. An expansion built now has positive NPV, and building it one year from now would serve demand just as well. Which rule tells management when to build?
- Build now only if its NPV exceeds the present value today of the NPV of building next year; a positive NPV now is not by itself enough, as delay defers the outlay and keeps the option open.
- Build now, since any project with positive NPV should be accepted at once; delay only postpones the value created, and a dollar of NPV received next year is worth less than a dollar received today.
- Build when the plant hits capacity, since building earlier ties up capital that earns nothing and building later loses sales; the timing follows from the capacity forecast and needs no valuation.
- Build next year, since delay always raises value: the outlay is discounted for one more year while the sales gained from the expansion stay the same, so the later date dominates by construction.
<!-- YW5zOjA= -->
> Building now and building next year are mutually exclusive projects, so the rule is to pick the date with the highest NPV measured today. A positive NPV now is necessary but not sufficient; delay saves the time value of the outlay (and may resolve uncertainty) but can cost sales or margin if capacity binds earlier than planned. Neither "now" nor "later" wins by construction.
> Ref: Berk *Fundamentals* Ch. 18 §18.3 (p. 542) and §18.5 (p. 551, optimal timing and the option to delay); Topic 2A slides 28–38 (NPV rule, mutually exclusive projects)
> Similar: Lista R2c, Ex. 15 (KMS expansion delayed to 2012; the closest book exercise, none covers timing directly)

## grow

Q: Analyst 1 computes a firm's sustainable growth rate as $ROE \cdot b$ with ROE on beginning-of-period equity; analyst 2 uses $ROE\,b/(1 - ROE\,b)$ with ROE on end-of-period equity, where $b$ is the retention ratio. How do their answers compare?
- Analyst 2 always reports more, since the factor $1/(1-ROE\,b)$ compounds growth within the year, which the simpler product $ROE \cdot b$ ignores, so the two agree only when $b = 0$.
- Analyst 1 always reports more, since beginning equity is smaller than end-of-period equity, so $ROE \cdot b$ is inflated relative to $ROE\,b/(1-ROE\,b)$ whenever earnings are retained.
- They coincide, since end-of-period equity is beginning equity plus retained earnings, and putting this into $ROE\,b/(1-ROE\,b)$ gives back exactly $ROE \cdot b$ on beginning equity.
- They coincide only roughly, since $ROE\,b/(1-ROE\,b)$ is a first-order expansion of $ROE \cdot b$ that is accurate for low ROE and drifts apart as ROE or retention rises.
<!-- YW5zOjI= -->
> Let $NI$ be net income and $E_0$, $E_1 = E_0 + b\,NI$ the beginning and ending equity. With $ROE = NI/E_1$, $1 - ROE\,b = E_0/E_1$, so $ROE\,b/(1-ROE\,b) = b\,NI/E_0$: the same number. The two formulas differ only in which equity defines ROE; the same holds for the internal growth rate with ROA.
> Ref: Ross *Fundamentos* Cap. 4 §4.4 (p. 109), Tabela 4.9 (p. 111) and "Uma observação sobre os cálculos da taxa de crescimento sustentável" (p. 112); Higgins 13e Ch. 4 §4.1.1 (pp. 112–114)
> Similar: Lista R2c, Ex. 13 (Ross 4.33); Lista R2c, Ex. 4

Q: A percent-of-sales pro forma lets payables grow with sales but holds interest expense fixed. With no new debt or equity, its EFN is zero at some growth rate $g_0$. How does $g_0$ compare with the textbook internal growth rate $ROA\,b/(1-ROA\,b)$, where $b$ is the retention ratio?
- It is lower, since fixed interest is a drag that the formula ignores: as sales grow, interest absorbs part of the extra profit, so retained earnings cover less of the growth in assets.
- It is higher, for two reasons the formula ignores: payables fund part of the growth in assets, and fixed interest makes the net margin rise with sales, so retained earnings outpace sales.
- It is the same, since the formula is derived from that very model by setting EFN to zero; any gap in practice comes from rounding the return on assets and the retention ratio.
- It is higher, but only because payables finance part of the growth in assets; interest is fixed, so it does not change with sales and cannot move the growth rate at which EFN is zero.
<!-- YW5zOjE= -->
> The formula is the root of $A\,g = m S_0 (1+g) b$: all assets scale, no spontaneous liabilities, constant net margin $m$. Payables that grow with sales cut the assets to be financed; a fixed interest bill makes the margin rise with sales. Both raise the zero-EFN growth rate, and the fixed cost matters precisely because it does not scale.
> Ref: Ross *Fundamentos* Cap. 4 §4.4 (pp. 106–111)
> Similar: Lista R2c, Ex. 14 (Ross 4.28–4.29: why the model's rates differ from the formulas); Lista R2c, Ex. 13

Q: A firm grows exactly at its sustainable growth rate, financing the growth with retained earnings and new debt at a constant debt-to-equity ratio and issuing no shares. Does this growth create value for its shareholders?
- Yes: since no shares are issued, existing owners are not diluted, and growth financed internally adds the retained earnings to book equity, which raises the value of each share.
- Yes: the sustainable growth rate equals ROE times retention, and a positive ROE means each retained unit earns a positive return, so reinvestment at that rate has a positive NPV.
- No: growing at the sustainable rate forces leverage up year after year, so the gain from growth is offset by the higher cost of equity that the extra debt brings about under MM II.
- Not necessarily: the sustainable rate says only what growth the policy can fund; growth adds value only if new investment beats its cost of capital and destroys value otherwise.
<!-- YW5zOjM= -->
> The sustainable growth rate is a feasibility benchmark (growth with no new equity and constant leverage), not a value criterion. A positive accounting ROE is not a positive NPV: value rises only if the return on new capital exceeds the rate investors require. Leverage is constant by construction, so the MM II story does not apply, and retaining earnings in bad projects destroys value with no dilution at all.
> Ref: Berk *Fundamentals* Ch. 18 §18.4, "Growth and Firm Value" (p. 547); Higgins 13e Ch. 4 §4.1.2 (p. 114) and §4.3 (p. 123); Topic 1 slides 40–51 (ROE pitfalls)
> Similar: Lista R2c, Ex. 9 (KMS vs. its SGR); Lista R2c, Ex. 10 (Under Armour)

## val

Q: An expansion is valued by APV: unlevered free cash flows over a five-year forecast, a continuation value equal to horizon EBITDA times the EBITDA multiple of comparable firms, and the present value of interest tax shields for the five forecast years only. The new debt stays outstanding for years after the horizon. Why are the later tax shields not added?
- The comparables' multiple comes from their enterprise values, which already capitalise their debt tax shields, so the continuation value is levered and adding later shields counts them twice.
- After the horizon the firm is assumed to sit at its long-run leverage, and at a stable leverage ratio MM irrelevance makes the tax shields worth nothing, so only the forecast-year shields carry value.
- EBITDA is measured before interest, so a value built on it contains no interest and hence no tax shield; the later shields are left out because they cannot be estimated without a debt forecast.
- Shields after the horizon are discounted at the cost of debt over many years, so their present value is negligible next to the continuation value, and dropping them is a harmless approximation.
<!-- YW5zOjA= -->
> Comparable firms' enterprise values are market values of levered firms, $V_U + V_{ITS}$. A multiple taken from them prices the shields a firm with that leverage enjoys, so the continuation value already includes post-horizon shields. Adding them again double counts. The third option confuses the measure (EBITDA is pre-interest) with the price (the multiple is levered).
> Ref: Berk *Fundamentals* Ch. 18 §18.5 (pp. 551–555, Eq. 18.7 and footnote 14); Topic 2B slides 7–9
> Similar: Lista R2c, Ex. 15 (Berk 18.21–18.22, EBITDA-multiple continuation value and APV)

Q: In an APV valuation, the forecast unlevered free cash flows and the continuation value are discounted at the firm's pretax WACC, while the interest tax shields on a planned bond issue are discounted at the bond's interest rate. What justifies the two rates?
- The pretax WACC is used because unlevered cash flows are measured before interest, and the bond rate because tax shields are a transfer from the government, whose promises are riskless at that rate.
- The pretax WACC already includes the tax benefit of the planned debt, and the bond rate is lower, so discounting the shields at it offsets the double count of the debt subsidy in the cash flows.
- Unlevered cash flows carry asset risk, priced by the pretax WACC; the shields come from a fixed debt schedule, so they are as risky as the debt; under a constant D/E they take the asset rate.
- The pretax WACC is used because the firm is not yet levered at the forecast date, and the bond rate because the shields arise after the bond is issued, when the firm's risk falls to that of its debt.
<!-- YW5zOjI= -->
> Under a constant leverage ratio the pretax WACC equals the unlevered cost $r_U$, the right rate for cash flows that exclude the debt subsidy. Shields on a predetermined debt schedule are known as long as the debt is serviced, so they carry the debt's risk and are discounted at $r_D$. Had the firm kept a target $D/E$, debt and shields would move with asset value and the shields would be discounted at $r_U$. The government's promise is not the point: the shield is only as safe as the debt behind it.
> Ref: Berk *Fundamentals* Ch. 18 §18.5 (pp. 553–554); Topic 2B slides 10–13 and 19–32
> Similar: Lista R2c, Ex. 15 (Berk 18.22); Lista R3, Ex. 4 and Ex. 6 (tax shields on constant and amortising debt)
