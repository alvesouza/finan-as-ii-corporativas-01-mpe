---
quiz: "Topic 2B — Taxes, bankruptcy costs and the static trade-off"
tags:
  tax: "Interest tax shield and valuation methods"
  dist: "Financial distress and the trade-off"
  pol: "Payout policy and bank capital"
---

## tax

Q: Interest is tax-deductible and dividends are not. Why is a levered firm worth more than an otherwise identical unlevered firm, and who captures the gain?
- Total payouts to investors rise by the tax saved on interest each period, so the claims are worth more by the PV of that saving, and it accrues to shareholders.
- Interest lowers the cost of equity directly because shareholders bear less risk, and the resulting gain in value is shared evenly by creditors and shareholders.
- Debt raises operating cash flows because lenders monitor the managers, and the gain accrues to the creditors through a lower interest rate on their loans.
- Debt lets the levered firm invest more, so its operating assets are worth more, and the gain accrues to the government through higher future tax receipts.
<!-- YW5zOjA= -->
> Each period the levered firm pays $(1-\tau)X + \tau r_D D$ to its investors, the extra $\tau r_D D$ being the interest tax shield, so $V_L = V_U + V_{ITS}$. Creditors are paid a fair return, so the gain goes to shareholders, as in the repurchase example where the share price rises by exactly $V_{ITS}$ per share.
> Ref: Topic 2B slides 2–8, 14–15; Ross *Fundamentos* Cap. 16 §16.4 (p. 551); Amaro de Matos Ch. 2 §2.1.3, Prop. 2.1.3 (p. 45)
> Similar: PS2 Ex. 2(c)

Q: When is the interest tax shield discounted at the unlevered cost of capital $r_U$ rather than at the cost of debt $r_D$?
- When the debt is risky, since the tax shield then disappears in default, and the expected return on the unlevered assets $r_U$ is the rate that prices default.
- When the debt level is fixed in perpetuity, since a constant amount of debt makes the shield as risky as the operating assets, whose return is $r_U$.
- When the firm keeps a target $D/E$, rebalancing continuously, so debt and the tax shield move with asset value and inherit the assets' risk.
- When the tax rate is expected to change, since tax-rate risk is systematic and the unlevered return $r_U$ is the only rate that can price it.
<!-- YW5zOjI= -->
> A fixed debt level gives a shield as safe as the debt: discount at $r_D$, so $V_{ITS} = \tau D$. With a constant target leverage ratio, debt scales with firm value, so the shield is as risky as the assets: $r_{ITS} = r_U$. The second is the usual assumption behind the WACC.
> Ref: Topic 2B slides 10–13; Higgins 13e Ch. 8 App. 8.A.3 (p. 321)
> Similar: PS2 Ex. 2(c)–(e) (three debt policies)

Q: Why does the formula $FCF = EBIT(1-\tau) + \text{Dep} - \text{Capex} - \Delta NWC$ give the same cash flow for a levered firm and an identical unlevered one?
- The formula is applied after interest, and the interest paid to creditors has already been deducted from EBIT in the levered firm's income statement.
- It taxes EBIT as if the firm had no interest, so the tax saving from debt is left out of the cash flow and has to enter through the WACC or the APV.
- The tax saving from interest is exactly offset by the higher expected bankruptcy costs of the levered firm, so net of both effects the flows coincide.
- In the benchmark interest is not tax-deductible, so financing choices never alter cash flows and the formula needs no adjustment for any firm.
<!-- YW5zOjE= -->
> EBIT is before interest, and $\tau$ is applied to all of it, so the formula computes the tax an unlevered firm would pay. That is why it is called unlevered FCF: the debt subsidy is handled separately, by lowering the discount rate (after-tax WACC) or by adding $V_{ITS}$ (APV).
> Ref: Topic 2B slides 4, 16; Topic 2A slides 24–25
> Similar: Higgins 13e Ch. 7 §7.3.7 (financing costs enter via the discount rate, p. 267)

Q: A project will be financed with a fixed loan repaid on a set schedule, so its debt-to-equity ratio will drift over time. Which valuation method is more convenient, and why?
- WACC, because one after-tax WACC already averages the changing $D/E$, so discounting unlevered FCF at it gives the right value under any debt schedule.
- WACC, because the APV needs a forecast of the unlevered cost of capital for every period, while the WACC needs only the leverage ratio at the start.
- APV, because the WACC cannot handle growing cash flows, while the APV discounts every cash flow at the risk-free rate whatever the leverage is.
- APV, because it values unlevered FCF at $r_U$ and adds the PV of the tax shields from the known loan schedule; the WACC needs a constant $D/E$.
<!-- YW5zOjM= -->
> The two methods coincide when $D/E$ is constant. When the debt schedule is known instead, the APV is the natural tool: $V_L = V_U + V_{ITS}$, with the shield computed from the actual interest payments. A single WACC would have to be recomputed period by period.
> Ref: Topic 2B slides 19–32; Higgins 13e Ch. 8 App. 8.A.3 (p. 321)
> Similar: PS2 Ex. 2(e) (fixed perpetual debt)

## dist

Q: Which of the following is an indirect cost of financial distress rather than a direct one?
- Lawyers' and administrators' fees paid during a court-supervised reorganisation, which arise only once the firm has formally entered bankruptcy.
- Assets sold at fire-sale prices in liquidation because specialised buyers are scarce, a loss the firm suffers only when it is actually liquidated.
- Customers paying less for a durable product, and skilled workers leaving, as the producer's default risk rises, even before any bankruptcy filing.
- Time that managers and creditors spend negotiating claims in the bankruptcy court, which pulls their effort away from running the business.
<!-- YW5zOjI= -->
> Direct costs are incurred in the liquidation or reorganisation itself: legal fees, management time, fire sales. Indirect costs arise from the prospect of distress: car prices fall with the maker's CDS spread (Hortaçsu et al., 2013), applications and talent drain away (Brown and Matsa, 2016; Baghai et al., 2021), plus debt overhang and risk-shifting.
> Ref: Topic 2B slides 36–40; Ross *Fundamentos* Cap. 16 §16.5 (p. 556); Higgins 13e Ch. 6 §6.2.3 (p. 208)
> Similar: Ross *Fundamentos* Cap. 16 problems (pp. 575–579)

Q: Creditors are competitive and price debt correctly, and a default would cost a fraction of the realised cash flow in legal fees. Who bears this expected cost at the time the debt is issued?
- The shareholders: creditors anticipate the loss and demand a higher face value, so the expected cost is subtracted from the value of equity at issuance.
- The creditors: legal fees are paid out of the assets they seize in default, so the cost falls on them and the value of equity is left unaffected.
- The lawyers: bankruptcy fees are a transfer to them, so neither creditors nor shareholders are worse off in expectation at the date of issuance.
- Both equally: creditors lose in default and shareholders lose the tax shield, so the expected cost is split in half whatever the face value of debt.
<!-- YW5zOjA= -->
> Competitive lenders break even in expectation, so they raise the promised repayment until the expected loss is covered. The deadweight cost lowers the total value of the firm, and the owners, who choose the capital structure, bear it ex ante.
> Ref: Topic 2B slides 36, 41–45
> Similar: PS2 Ex. 3(c)

Q: In the static trade-off model, how does the optimal face value of debt $K^*$ respond to a higher corporate tax rate $\tau$ and to a higher fixed bankruptcy cost $C$?
- It falls with $\tau$, since higher taxes cut after-tax cash flow and so default risk, and it rises with $C$, since a costlier default makes lenders more careful.
- It rises with both, since a higher $C$ raises the interest rate on debt, and a higher interest rate means a larger tax shield for each unit of debt.
- It responds to neither, since by MM the value of the firm does not depend on its capital structure, so no interior optimum for $K$ can exist.
- It rises with $\tau$, which raises the marginal tax benefit of debt, and falls with $C$, which raises the marginal expected cost of distress.
<!-- YW5zOjM= -->
> $V(K) = V_U$ + PV of tax savings $- C\,H(K)/(1+r_f)$, where $H(K)$ is the probability of default. $K^*$ sets the marginal tax benefit equal to the marginal expected bankruptcy cost, so it increases in $\tau$ and decreases in $C$. MM irrelevance no longer holds once taxes and distress costs are present.
> Ref: Topic 2B slides 41–45; Ross *Fundamentos* Cap. 16 §16.6 (p. 558); Amaro de Matos Ch. 2 §2.2.5 (p. 54)
> Similar: Amaro de Matos 2.2.7 exercises (p. 58)

Q: With perpetual safe debt, $V_L = V_U + \tau D$ suggests that firm value rises with every unit of debt. Why is 100% debt not optimal in the lecture's framework?
- The formula assumes risk-neutral investors, and once investors are risk averse the shield is worth less than $\tau D$, falling to zero at high leverage.
- The formula assumes safe debt; as debt grows, default becomes likely, the tax savings are lost in default, and expected distress costs rise.
- Tax authorities cap the deductibility of interest at a share of EBIT, so beyond that cap any additional debt has no tax effect on firm value.
- MM II says the cost of equity rises with leverage, which exactly cancels the tax shield, so the firm is indifferent across all levels of debt.
<!-- YW5zOjE= -->
> $\tau D$ is the value of a riskless shield on riskless debt. With risky debt the shield is paid only in solvent states and default carries deadweight costs, so $V_L = V_U + V_{ITS} - PV(\text{distress costs})$ has an interior maximum. MM II reprices equity but does not cancel the tax gain.
> Ref: Topic 2B slides 33–35, 45; Higgins 13e Ch. 6 §6.2.2–6.2.3 (p. 208)
> Similar: Higgins 13e Ch. 6 problems (p. 230)

## pol

Q: Critics of tighter bank capital rules argue: "higher equity requirements hurt bank shareholders because they lower the return on equity." Why does the lecture's framework reject this claim?
- Lower leverage lowers ROE but also the risk of equity, so the required return falls too; in the frictionless benchmark shareholder value is unchanged.
- Bank ROE does not depend on leverage, because bank assets are financed by deposits, which do not count as debt in the DuPont identity used for banks.
- Higher equity requirements actually raise ROE, because better-capitalised banks borrow at lower rates, which raises net income by more than equity.
- Shareholders care only about dividends, not ROE, and by dividend irrelevance the payouts are unaffected by how much equity the regulator requires.
<!-- YW5zOjA= -->
> This is MM II applied to banks (Admati et al., 2013): ROE moves with leverage, but so does the required return on equity, so a lower ROE is not a loss of value. The one private cost that survives is the lost tax shield — a transfer from taxpayers, not a social cost — set against the social benefit of fewer bank failures.
> Ref: Topic 2B slides 46–47; Topic 1 slides 47–49 (DuPont)
> Similar: PS2 Ex. 4(c)–(d) (EPS and P/E after a leverage change)

Q: With its investment plan held fixed, a firm raises its dividend and pays for it by issuing new shares at a fair price. Why is the total value of the firm unchanged?
- The higher dividend raises the share price by the same amount, so existing owners collect the dividend twice while new shareholders lose it once.
- Issuing shares is costly, and the issuance cost exactly offsets the tax advantage of paying out cash, which leaves the value of the firm where it was.
- Value is the discounted stream of cash flow minus investment, and selling new shares at a fair price is a zero-NPV exchange that only redistributes it.
- Dividends are paid out of retained earnings, which are already excluded from the firm's market value under the accounting identity for equity.
<!-- YW5zOjI= -->
> From sources = uses each period, $V_t = E\sum_i \beta^i (X_{t+i} - I_{t+i})$: dividends drop out once investment is fixed. New shareholders pay what their shares are worth, so a higher payout financed by issuance is a repackaging, not a change in value. The result extends to debt-financed payouts and to risk-averse investors.
> Ref: Topic 2B slides 48–51; Ross *Fundamentos* Cap. 17 §17.2 (p. 587); Amaro de Matos Ch. 4 §4.1 (p. 100)
> Similar: PS2 Ex. 1(f) (debt-financed dividend)
