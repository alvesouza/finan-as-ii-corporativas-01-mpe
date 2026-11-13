---
quiz: "Topic 2B — Taxes, distress, payout and bank capital (hard conceptual)"
tags:
  its: "Tax shield, WACC under debt policies, APV"
  ptax: "Personal taxes and the 100%-debt puzzle"
  dist: "Distress costs and the static trade-off"
  pol: "Payout irrelevance and the bank capital debate"
---

## its

Q: A firm whose unlevered free cash flows grow at rate $g$ keeps a target debt-to-value ratio. If it rebalances debt once a year, $V_{ITS} = \frac{\tau r_D D}{r_U - g}\cdot\frac{1+r_U}{1+r_D}$; if it rebalances continuously, $V_{ITS} = \frac{\tau r_D D}{r_U - g}$. Here $\tau$ is the tax rate, $D$ current debt, $r_D$ the cost of debt and $r_U$ the unlevered cost of capital. What explains the factor $(1+r_U)/(1+r_D)$?
- With annual rebalancing, each year's debt is fixed a year ahead, so each shield is known one period before it is paid: it is discounted at $r_D$ over that last period and at $r_U$ before it.
- With annual rebalancing, debt sits above target for part of each year, so the firm collects extra shields between rebalancing dates, a gain that grows with the gap between $r_U$ and $r_D$.
- With annual rebalancing, the shield is paid in arrears, so its value must be compounded forward one period at $r_U$ and discounted back one period at $r_D$ to reach the end-of-year date.
- With annual rebalancing, the firm bears default risk only once a year, so its debt is safer and all its shields are discounted at $r_D$ forever, while continuous rebalancing uses $r_U$ forever.
<!-- YW5zOjA= -->
> When debt is reset once a year to a fraction of firm value, the interest paid at $t+1$ is set by the debt chosen at $t$: from $t$ on it is as safe as the debt, while before $t$ it moves with firm value. Each shield therefore carries asset risk until one period before payment and debt risk in the last period, which multiplies the continuous-rebalancing value by $(1+r_U)/(1+r_D) > 1$. The firm does not gain extra shields; the same shields are less risky.
> Ref: Topic 2B slides 12–13 and 18 (DeMarzo 2005; Stanton and Seasholes 2005); Higgins 13e Ch. 8 App. 8.A.3 (p. 321)
> Similar: Lista R3, Ex. 9 (Hamada vs. other debt policies); PS2 Ex. 2(c)–(e)

Q: A no-growth firm with perpetual unlevered cash flows can follow two debt policies with the same current debt-to-value ratio $D/V$: a fixed perpetual debt level, giving $r_{WACC} = (1 - \tau D/V)\,r_U$, or a continuously rebalanced target ratio, giving $r_{WACC} = r_U - \tau r_D D/V$, with $r_D < r_U$. Why does the fixed-debt policy give the lower WACC?
- Fixed debt is serviced at face value rather than at market value, so the deductible interest is larger for the same leverage, and the larger deduction shows up as a lower WACC at every debt-to-value ratio.
- Under a target ratio the shields are discounted at the cost of equity, which exceeds the asset return, so they are worth less, and the WACC falls by less than under a fixed perpetual debt level.
- Under fixed debt the formula holds only for the first year, after which leverage changes; the larger reduction averages the subsidy of all future years into a single discount rate for today.
- Fixed debt makes the shields as safe as the debt, so each unit of debt creates a more valuable subsidy than shields that move with firm value; a more valuable subsidy lowers the discount rate by more.
<!-- YW5zOjM= -->
> With fixed debt, $V_{ITS} = \tau D$ (shields at $r_D$); with a rebalanced ratio, $V_{ITS} = \tau r_D D/r_U$ (shields at $r_U$), which is smaller. The WACC folds the subsidy into the discount rate, so the more valuable subsidy cuts the rate by $\tau r_U D/V$ instead of $\tau r_D D/V$. The cost of equity never discounts the shields, and with no growth a fixed debt level keeps $D/V$ steady in expectation.
> Ref: Topic 2B slides 10–13, 16–18 and 54–61 (WACC derivation); Ross *Fundamentos* Cap. 16 §16.4 (p. 551)
> Similar: Lista R3, Ex. 13 (derive $R_U[1 - T_C(D/V)]$); Lista R3, Ex. 9

Q: A firm's debt is risky: its market value is well below the promised repayment, and its expected return $r_D$ far exceeds the coupon rate. When the interest tax shield enters the WACC, which rate on debt determines it?
- The expected return on the debt, since it is the investors' required return and so the true economic cost of borrowing, which is what the tax code lets the firm deduct from its taxable income.
- The expected coupon divided by the debt's market value, since deductions follow the interest actually paid; the after-tax cost of debt is the expected return minus tax times that ratio.
- The yield to maturity, since once default is priced it equals the expected return on risky debt, and the tax code deducts interest at the market yield rather than at the coupon on the bond.
- The risk-free rate, since the tax authority pays the shield whatever happens to the firm, so the shield is riskless and its rate cannot depend on the default risk of the debt that creates it.
<!-- YW5zOjE= -->
> Expected return on risky debt includes expected principal losses, which are not deductible; only interest paid is. With coupon rate $\bar r_D = E[C_{t+1}]/D_t$, the after-tax cost of debt is $r_D - \tau \bar r_D$, not $r_D(1-\tau)$. The yield overstates $r_D$ when default is possible, and the shield is lost exactly in the states where the firm cannot pay.
> Ref: Topic 2B slides 62–63 (appendix, comment on $r_D$); Topic 2A slides 103–105 ($r_D$ is not the coupon or the yield)
> Similar: Lista R3, Ex. 10 (risky zero-coupon debt and taxes); Lista R3, Ex. 11

## ptax

Q: With a corporate tax rate $\tau_c$, a personal tax rate $\tau_s$ on equity income and $\tau_b$ on interest income, Miller's gain from leverage is $G_L = \left[1 - \frac{(1-\tau_c)(1-\tau_s)}{1-\tau_b}\right]B$, where $B$ is the market value of debt. Under which condition does debt add no value although interest is deductible at the corporate level?
- When $\tau_s = \tau_b$: if equity income and interest income are taxed alike at the personal level, investors are indifferent between the two claims, so the firm cannot gain by changing the mix.
- When $\tau_b = 0$: bondholders then pay no personal tax, so competition among them drives the pre-tax bond rate down to the after-tax equity return and removes any gain from issuing debt.
- When $(1-\tau_c)(1-\tau_s) = 1-\tau_b$: a unit of pre-tax income paid as equity leaves investors as much after all taxes as a unit paid as interest, so the corporate deduction is undone.
- When $\tau_c = \tau_b$: the corporate deduction on interest is then recaptured one for one by the personal tax on interest, whatever the tax rate on equity income turns out to be.
<!-- YW5zOjI= -->
> Income routed as interest is taxed once, at $\tau_b$; routed as equity it is taxed at $\tau_c$ and then $\tau_s$. Debt is neutral when the two after-tax amounts match. With $\tau_s = \tau_b$ the gain is $\tau_c B$, the MM result; with $\tau_b = 0$ it is largest; $\tau_c = \tau_b$ gives $G_L = 0$ only if $\tau_s = 0$ as well. In Miller's equilibrium the marginal investor's rates satisfy the neutrality condition, so leverage is irrelevant for any single firm.
> Ref: Amaro de Matos Ch. 2 §2.2.1–2.2.3 (pp. 49–53, Miller 1977); Topic 2B slide 5 (differential tax treatment of interest and dividends)
> Similar: Lista R3, Ex. 14 (Amaro de Matos 2.2.7 #1, proof of $G_L$)

Q: In the static trade-off model, cash flow $X$ has density $h$ and c.d.f. $H$ on $[\underline X, \bar X]$, the face value of debt is $K$, interest is deductible only when the firm is solvent, investors are risk-neutral with rate $r_f$, and default costs a fixed amount $C$. Suppose $C = 0$. Which face value maximises firm value, and why?
- $K = \bar X$: the marginal tax benefit $\tau[1 - H(K)]/(1+r_f)$ shrinks as default grows likely but stays positive, so with no deadweight cost firm value keeps rising up to the corner.
- $K = \underline X$: beyond the lowest cash flow the debt is risky and shields are lost in default states, so the marginal tax benefit $\tau[1-H(K)]/(1+r_f)$ turns negative past that point.
- Any $K$: with $C = 0$ default is only a transfer of control to creditors, which is no MM violation, so tax shields and default losses cancel and firm value does not depend on $K$.
- $K$ with $H(K) = 1/2$: the marginal tax benefit $\tau[1 - H(K)]$ equals the marginal shield lost in default $\tau H(K)$, so the optimum is where default and solvency are equally likely.
<!-- YW5zOjA= -->
> Differentiating the tax term $\tau[\int_{\underline X}^{K} X h\,dX + K(1-H(K))]$ gives $\tau[1-H(K)] \ge 0$: losing shields in default slows the gain from debt but never reverses it. Without a deadweight default cost the 100%-debt corner survives; an interior optimum needs $C > 0$. Transfer of control is not an MM violation, but that does not cancel the tax shield.
> Ref: Topic 2B slides 33 and 41–45; Amaro de Matos Ch. 2 §2.2.5 (p. 54)
> Similar: Lista R3, Ex. 10 (Grinblatt 16.2, two-state trade-off); Lista R3, Ex. 8

## dist

Q: In the static trade-off model, cash flow $X$ has density $h$ and c.d.f. $H$, debt has face value $K$, the tax rate is $\tau$ when the firm is solvent, default costs a fixed $C$, and investors are risk-neutral with rate $r_f$. Firm value is $V(K) = V_U + \frac{1}{1+r_f}\left[\tau\left(\int_{\underline X}^{K} X h(X)\,dX + K(1-H(K))\right) - C\,H(K)\right]$. Which condition defines an interior optimum $K^*$?
- $\tau = C\,h(K^*)$: each extra unit of face value saves $\tau$ in taxes, since interest is fully deductible, and it raises the expected default cost by $C$ times the density at $K^*$.
- $\tau[1 - H(K^*)] = C\,H(K^*)$: the shield is earned in solvent states and the cost is paid in default states, so the optimum balances the solvency probability against default.
- $\tau[1 - H(K^*)] = C\,h(K^*)$: an extra unit of face value saves tax only in solvent states, while it raises the default probability at the rate $h(K^*)$, each default costing $C$.
- $\tau K^* h(K^*) = C\,h(K^*)$: at the margin the firm loses the shield on the whole face value $K^*$ in the states where it just defaults, which must equal the extra expected default cost.
<!-- YW5zOjI= -->
> $V'(K) \propto \tau[1-H(K)] - C\,h(K)$. The first option forgets that the deduction is used only when solvent; the second confuses the level of the default probability with its marginal change; the fourth keeps a term, $\tau K h(K)$, that cancels against the change in the shield earned in default states. $K^*$ rises with $\tau$ and falls with $C$.
> Ref: Topic 2B slides 41–45; Ross *Fundamentos* Cap. 16 §16.6 (p. 558)
> Similar: Lista R3, Ex. 10; Lista R3, Ex. 18 (original: the same trade-off transposed to a bank and society)

Q: Van Doornik et al. (2022) find that more generous unemployment insurance shifts labour supply towards riskier firms and lowers the wage premium those firms must pay. Read through the static trade-off, what does more generous insurance predict for corporate leverage?
- Lower leverage: workers protected by insurance quit more readily when the firm weakens, so distress drains talent faster, the indirect cost of distress rises and the optimal debt level falls.
- No change: a wage premium is a transfer from shareholders to workers, not a deadweight loss, so like the transfer of control in default it leaves firm value and the optimal debt level unaffected.
- Higher leverage, but only through taxes: insurance is financed by payroll taxes that firms deduct like interest, so the tax benefit of debt rises relative to that of paying wages to workers.
- Higher leverage: insurance lowers an indirect cost of distress, the premium workers demand for bearing job loss, so the marginal expected distress cost falls and the optimal debt level rises.
<!-- YW5zOjM= -->
> Risk-averse workers demand compensation for working at firms likely to fail (Brown and Matsa 2016; Baghai et al. 2021); that premium is an ex ante cost of leverage borne by shareholders, unlike a pure transfer of control. Insurance absorbs part of the workers' risk, lowers the premium and so the effective distress cost, moving $K^*$ up: the paper reads insurance as a subsidy to risky firms.
> Ref: Topic 2B slides 38–39 and 41–45; Higgins 13e Ch. 6 §6.2.3 (p. 208)
> Similar: Lista R3, Ex. 8 (implied PV of distress costs); Lista R5b, Ex. 12 (lost supplier credit as a cost of leverage)

## pol

Q: A bank executive argues that more equity raises the bank's funding cost because the required return on equity exceeds the deposit rate, and computes the new average cost by applying today's required return on equity to the higher equity weight. Without taxes or other frictions, what is wrong?
- Today's required return reflects today's leverage; with more equity the shares are safer and their required return falls, so the weighted average stays at the return required on the bank's assets.
- Nothing in a frictionless world: equity is the costlier claim at every leverage, so moving weight from deposits to equity must raise the average cost, and only taxes or subsidies could offset it.
- The weights are wrong: they should be book values rather than market values, and in book terms the bank's equity share barely changes, so the higher funding cost is real but negligible in size.
- Deposits are not debt but a service the bank sells, so MM does not apply to banks; the argument fails because it ignores the fees that depositors pay, not because of the return on equity.
<!-- YW5zOjA= -->
> This is Statement 2 of Admati et al. (2013). By MM II, $r_E = r_A + \frac{D}{E}(r_A - r_D)$ falls as $D/E$ falls, and $\frac{E}{V}r_E + \frac{D}{V}r_D = r_A$ at every mix. Holding $r_E$ at its high-leverage value prices safer equity as if it were still risky. Deposit services are a real friction, but they are not what makes this computation wrong.
> Ref: Topic 2B slides 46–47; Topic 2A slides 97–102 (MM II, conservation of value)
> Similar: Lista R3, Ex. 16 (original: bank capital without taxes, Statements 1 and 2)

Q: A regulator chooses a bank's minimum equity ratio to minimise society's cost of the bank's funding mix. Deposits are insured at a flat premium and provide liquidity services, interest is tax-deductible, and bank failures impose losses on the rest of the economy. Which items belong in the social cost the regulator trades off?
- The higher required return on equity and the lost interest tax shield, since both raise the bank's cost of funds as equity rises, and a bank's cost of funds is ultimately borne by its borrowers.
- The liquidity services deposits would have provided and the expected failure losses imposed on others; the equity premium is risk compensation and the lost tax shield a transfer.
- The lost interest tax shield and the expected failure losses, since the shield is a real saving for the bank, while the liquidity services of deposits are already priced into the deposit rate.
- Only the expected failure losses, since under MM every other item nets out: liquidity services, the equity premium and the tax shield are all transfers between the bank's own claimants.
<!-- YW5zOjE= -->
> Society's cost counts only real resources: the deposit liquidity given up when equity replaces deposits, and the failure externality that flat-premium insurance and limited liability keep off the bank's books. The equity premium compensates for risk (MM II), and the tax shield is a transfer from taxpayers (Statement 3), so counting either one biases the chosen ratio downwards. Liquidity services are a genuine benefit, not a transfer.
> Ref: Topic 2B slides 44–47 (trade-off, Admati et al. 2013)
> Similar: Lista R3, Ex. 18 (original: socially optimal capital ratio); Lista R3, Ex. 17 (original: the lost tax shield as a transfer)

Q: With its investment plan fixed, an all-equity firm's value is $V_t = E\sum_{i \ge 1} \delta^i (X_{t+i} - I_{t+i})$ whatever its dividends, where $X$ is cash flow, $I$ investment and $\delta$ the discount factor. A firm pays a large special dividend by cancelling a positive-NPV project. What happens, and does it contradict dividend irrelevance?
- Value is unchanged, since by dividend irrelevance shareholders receive in cash what they lose in share price, whatever the source of the funds used to pay the dividend to them.
- Value rises, since shareholders can reinvest the dividend at the market rate and the dividend signals confidence; irrelevance fails because the cash now sits in investors' hands.
- Value falls by the project's NPV, with no contradiction: irrelevance compares payout policies under a fixed investment plan, so the loss comes from the cut, not the dividend.
- Value falls by the dividend amount, which contradicts irrelevance: the proposition only holds when dividends are financed by new shares, so any other source of funds destroys value.
<!-- YW5zOjI= -->
> Sources equal uses each period, so with $I_t$ fixed a higher dividend must be met by issuing claims at a fair price, a zero-NPV exchange. Here $I_t$ changes: value falls by the NPV forgone, through the investment term in $V_t$. The proposition is a statement about financing, given investment; it extends to debt-financed payouts and to risk aversion.
> Ref: Topic 2B slides 48–51; Ross *Fundamentos* Cap. 17 §17.2 (p. 587); Amaro de Matos Ch. 4 §4.1 (p. 100)
> Similar: Lista R3, Ex. 2 (dividend vs. repurchase in a perfect market); PS2 Ex. 1(f)
