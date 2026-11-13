---
quiz: "Topic 2A (hard) — Valuation, the NPV rule and the frictionless benchmark"
tags:
  dr: "Discount rates, comparables and unlevering"
  npv: "Relevant cash flows and the NPV rule"
  ss: "Contingent claims and the MM arbitrage"
  mm: "MM II, risky debt and the cost of debt"
---

## dr

Q: To unlever the equity beta of a heavily indebted comparable firm, an analyst sets its debt beta $\beta_D$ to zero, although the comparable's bonds carry real default risk that rises in recessions. How does this bias the discount rate of the project?
- It biases the rate upward, since setting $\beta_D=0$ loads all of the systematic risk onto equity, so the asset beta that comes out exceeds the true one.
- It leaves the rate unbiased, since the equity beta $\beta_E$ already reflects the default risk of the debt and the market-value weights correct for it.
- The direction depends on book values, since $\beta_A$ is computed with book weights and the market value of risky debt lies below its book value.
- It biases the rate downward, since $\beta_A=\frac{E}{D+E}\beta_E+\frac{D}{D+E}\beta_D$ loses a positive term and so understates the true asset beta.
<!-- YW5zOjM= -->
> The asset beta is the market-value-weighted average of the claims' betas. $\beta_E$ is observed, so dropping a positive $\beta_D$ removes a positive term and understates $\beta_A$, hence the CAPM rate and the cost of capital, and overstates the project's value. The $\beta_D = 0$ shortcut is safe only when leverage is low and default unlikely (slide 11); otherwise use bond indices of the same rating.
> Ref: Topic 2A slides 10–11, 16–23; Higgins 13e Ch. 8 App. 8.A.1 (p. 319); Ross *Fundamentos* Cap. 14 §14.5 (p. 476)
> Similar: Lista R2, Ex. 6 (G&T 11.10–11.13); Lista R2, Ex. 9 (Berk 13.20)

Q: A diversified firm whose current businesses are low-risk uses its own WACC to evaluate every new project, including some in a much riskier industry and some safer than the firm. Which error results?
- It rejects too many high-risk projects, since its WACC already contains a premium for the risk of all its divisions together and therefore sits above the right rate.
- It accepts some negative-NPV high-beta projects and rejects some positive-NPV low-beta ones, since the right rate is set by each project's own systematic risk.
- It makes no error, since shareholders hold the firm as a whole, so the firm-wide beta is the only risk that they bear on any project the firm undertakes.
- It errs only on projects with volatile cash flows, since the right rate rises with the total variance of a project's cash flows, whether systematic or not.
<!-- YW5zOjE= -->
> The discount rate is the expected return investors require on the project's own cash flows: $r = r_f + \beta(E[\tilde r_m] - r_f)$ with the project's $\beta$, found from comparables in the same line of business. A firm-wide rate is too low for high-beta projects (they look better than they are) and too high for low-beta ones. Diversifiable variance carries no premium in the CAPM.
> Ref: Topic 2A slides 7–10, 23; Higgins 13e Ch. 8 §8.5.1 (p. 304); Ross *Fundamentos* Cap. 14 §14.5 (p. 476)
> Similar: Lista R2, Ex. 9 (Berk 13.20); Lista R2, Ex. 6 (G&T 11.10–11.13)

## npv

Q: An analyst subtracts the after-tax interest on a project's debt from its free cash flows and then discounts the result at the firm's after-tax WACC. What is wrong with this valuation?
- The cost of debt is counted twice, once in the cash flows and again in the WACC, so the value is understated; financing costs belong only in the discount rate.
- Nothing is wrong if the debt is safe, since safe interest is a certain outflow, and the WACC discounts certain and risky flows of a project in the same way.
- The interest should be subtracted before tax, since the tax saving is already in the after-tax WACC, so the error lies only in the tax treatment, not the approach.
- Discounting at the WACC is right, but the after-tax interest must be replaced by the principal repayments, since those are the cash that actually leaves the firm.
<!-- YW5zOjA= -->
> Unlevered FCF, $EBIT(1-\tau) + \text{Dep} - \text{Capex} - \Delta NWC$, is the cash available to all investors before any payment to creditors; the return creditors require, and the tax subsidy on interest, are both carried by the after-tax WACC (slide 25). Deducting interest from the flows charges the cost of debt a second time. A consistent alternative is to discount FCFE at $r_E$ — the enterprise vs. equity perspective.
> Ref: Topic 2A slides 24–25; Topic 1 slides 60–61; Higgins 13e Ch. 7 §7.3.7 (p. 267), Ch. 8 §8.6.1 (p. 307)
> Similar: Lista R2, Ex. 10 (Higgins 8.16); Lista R2, Ex. 11 (Berk 9.25)

Q: A project's sales and operating costs are forecast in today's prices (real terms), but its depreciation is fixed in nominal currency by the tax code, and inflation is positive. Which discounting is consistent?
- Discount everything at the real rate, since the operating flows are real and the depreciation tax shields are too small to matter for the decision.
- Discount everything at the nominal rate, since the tax code is nominal and a nominal rate is always the safer choice for a project's whole cash flow.
- Discount the operating flows at the real rate and the depreciation tax shields at the nominal rate, or turn every flow into nominal terms first.
- Discount the operating flows at the nominal rate and the tax shields at the real rate, since the shields are fixed and so carry no inflation risk.
<!-- YW5zOjI= -->
> Nominal flows go with nominal rates and real flows with real rates (slide 26). The tax shield $\tau \cdot \text{Dep}$ is a fixed nominal amount, so its real value erodes with inflation; discounting it at the real rate overstates it. Discounting real operating flows at the nominal rate, or the reverse, misprices them by the inflation factor. Converting every flow to nominal and using the nominal rate is equivalent.
> Ref: Topic 2A slide 26; Higgins 13e Ch. 8 §8.6.2 (p. 310), Ch. 7 §7.3.1 (p. 260)
> Similar: Lista R2, Ex. 13 (Ross 10.31); Lista R2, Ex. 11 (Berk 9.25)

Q: A firm has risky debt outstanding, so its creditors are not paid in full in bad states. It takes a riskless positive-NPV project paid for entirely by its shareholders. Why can the shareholders' gain be smaller than the project's NPV, or even negative?
- Because competitive outside investors capture the NPV of any project, so the shareholders earn only a normal return on the money they put into the firm.
- Because the project's safe payoff is paid out to creditors in the default states, so part of its value goes to raising the value of the existing debt.
- Because the risk-free project lowers the firm's asset beta and so its WACC, which reduces the value of the firm's other assets by the same amount.
- Because the NPV rule fails under limited liability, since the project's value must be computed at the shareholders' cost of equity, not the riskless rate.
<!-- YW5zOjE= -->
> The slide-31 equivalence between NPV and shareholder gain needs no risky leverage. With risky debt, equity is a call on the assets: the project's payoff is added in every state, but in the default states it goes to creditors, raising $D$. Shareholders pay the whole cost and receive only the part of the payoff that arrives in solvent states — the debt-overhang mechanism of Topic 4B. A riskless project is still discounted at $r_f$.
> Ref: Topic 2A slides 29, 31–36, 43–45; Topic 4B slides 19–26; Higgins 13e Ch. 6 §6.2.3 (p. 208)
> Similar: Lista R2, Ex. 15 (Amaro de Matos 1.2.6 #4); Lista R7, Ex. 8–10 (debt overhang)

## ss

Q: In a complete one-period market with two equally likely states, the price $p_s$ of the claim paying 1 in the slump exceeds the price $p_b$ of the claim paying 1 in the boom, and a riskless bond pays $1+r_f$ in both states. Which statement is correct?
- Each claim earns $r_f$ in expectation, since no arbitrage forces every asset to earn the riskless rate, and $p_s>p_b$ only reflects the state probabilities.
- $p_s+p_b=1$, since the two claims together pay one unit in every state, and the slump claim earns more than $r_f$ because it is the costlier of the two.
- $p_s+p_b=1/(1+r_f)$; the boom claim earns less than $r_f$ in expectation and the slump claim more, since the slump is the riskier state to be paid in.
- $p_s+p_b=1/(1+r_f)$; the boom claim earns more than $r_f$ in expectation and the slump claim less, since a unit paid in the slump is worth more to investors.
<!-- YW5zOjM= -->
> Holding one of each claim replicates a riskless payment of 1, so by the law of one price $p_s + p_b = 1/(1+r_f)$. Each claim's expected return is $0.5/p - 1$: the cheap boom claim earns more than $r_f$ and the expensive slump claim less, because risk-averse investors value a unit most when they are poor (slide 67). The states are equally likely, so probabilities cannot explain $p_s > p_b$.
> Ref: Topic 2A slides 48–54, 60–67; Amaro de Matos Ch. 1 §1.2.1–1.2.4 (pp. 18–24)
> Similar: Lista R2, Ex. 14 (Amaro de Matos 1.2.6 #5)

Q: Two firms have identical assets; firm L has safe debt and firm U is all-equity. Firms borrow at the riskless rate, but individuals can borrow only at a higher rate, though they can still lend at the riskless one. Which mispricing can survive?
- L can trade above U, since closing that gap needs investors to lever up U on their own account; a premium on U is still removed by buying L's debt and equity.
- U can trade above L, since closing that gap needs investors to borrow in order to buy L's equity; a premium on L is still removed by short-selling L's equity.
- Neither can survive, since the arbitrage in either direction only requires short-selling the overpriced firm, which needs no borrowing at all by the investors.
- Both can survive, up to the full gap in borrowing rates, since every leg of the MM arbitrage requires investors to borrow at the same rate as the firms.
<!-- YW5zOjA= -->
> If $V_U > V_L$, the arbitrage sells U short and buys L's debt and equity in proportion — undoing L's leverage, which is lending, still available at $r_f$. If $V_L > V_U$, it sells L's equity short, buys U and borrows on personal account to replicate L's leverage (homemade leverage); at a higher personal rate that trade loses its edge, so a premium on the levered firm can persist. This is why the MM assumptions require that individuals and firms borrow on the same terms.
> Ref: Topic 2A slides 47, 82–89; Ross *Fundamentos* Cap. 16 §16.2 (p. 542); Amaro de Matos Ch. 2 §2.1.1 (Prop. 2.1.1, p. 42)
> Similar: Lista R3, Ex. 15 (Amaro de Matos 2.1.5 #3–#4); Lista R3, Ex. 7 (Ross 16.18)

## mm

Q: In the frictionless benchmark, leverage rises far enough that the firm's debt becomes risky and its expected return $r_D$ starts to climb. How does the cost of equity $r_E$ respond to further increases in $D/E$?
- $r_E$ rises faster than before, since equity now bears default risk on top of the leverage effect, while $r_A$ rises too because default destroys part of the assets.
- $r_E$ keeps rising linearly with the same slope $r_A-r_f$, since $r_A$ is fixed and the expression for $r_E$ does not depend on how risky the debt has become.
- $r_E$ still rises but more slowly, and may flatten, since creditors now bear part of the asset risk, while $r_A$ stays fixed because financing does not change the assets.
- $r_E$ starts to fall, since part of the firm's risk has moved to the creditors, so equity becomes safer and its required return declines as $D/E$ keeps going up.
<!-- YW5zOjI= -->
> From $r_E = r_A + \frac{D}{E}(r_A - r_D)$ with $r_A$ fixed by MM I, the slope is $(r_A - r_D) - \frac{D}{E}\,\frac{\partial r_D}{\partial (D/E)}$. While debt is safe, $r_D = r_f$ and the relation is linear; once $r_D$ rises, creditors absorb part of the asset risk and the curve bends down — with finitely many states it can go flat. There are no bankruptcy costs in the benchmark, so $r_A$ does not move.
> Ref: Topic 2A slides 97–102; Ross *Fundamentos* Cap. 16 §16.3 (p. 547); Amaro de Matos Ch. 2 §2.1.2 (Prop. 2.1.2, p. 43)
> Similar: Lista R3, Ex. 5 (Berk 16.5); Lista R2, Ex. 4 (Berk 13.4)

Q: A firm's assets pay $X$ at $t=1$ and its zero-coupon debt has face value $K$. Let $C(K)$ and $P(K)$ be the prices of a call and a put on $X$ with strike $K$. If the firm raises $K$, what happens in the frictionless benchmark?
- $V$ falls, since the put $P(K)$ that creditors implicitly write gains value as default becomes likelier, and that loss is borne by the firm as a whole.
- $E=C(K)$ falls and $D=K/(1+r_f)-P(K)$ rises by exactly the same amount, so the total $V=C(K)+K/(1+r_f)-P(K)$ does not change with $K$.
- $E=C(K)$ rises, since more leverage magnifies the equity's upside, and $D$ rises as creditors are promised more, so that $V$ rises with $K$.
- $D$ rises by the full change in $K/(1+r_f)$, since the creditors' promise grows, and $E$ falls by that amount, so $V$ is unchanged.
<!-- YW5zOjE= -->
> Equity is a call with strike $K$; risky debt is a riskless bond minus a put. A higher strike lowers the call, and raises the bond leg by more than the put rises, so $D$ gains exactly what $E$ loses: by put–call parity $C(K) + K/(1+r_f) - P(K)$ equals the value of $X$ whatever $K$. The option with $D$ rising by the full change in $K/(1+r_f)$ reaches the right total for the wrong reason: it ignores that the put, the discount for default, also grows.
> Ref: Topic 2A slides 45, 90–96; Amaro de Matos Ch. 2 §2.1.1 (p. 40)
> Similar: Lista R3, Ex. 11 (G&T 14.2–14.3); Lista R2b, Ex. 15 (G&T 7.3)

Q: A firm's bonds were issued years ago with coupon rate $c$; today they trade at a promised yield $y$ above the riskless rate $r_f$ because default is possible. Which rate is the cost of debt $r_D$ in the firm's WACC today?
- The coupon rate $c$, since it is the rate written into the contract and the interest the firm actually pays each year on the debt that it has outstanding.
- The yield $y$, since it is today's market rate on the firm's debt and so already reflects every change in interest rates and in the firm's default risk.
- The riskless rate $r_f$, since creditors are senior and so are paid first in every state, which makes their expected return equal to the riskless one.
- The bonds' expected return, which lies below $y$ because $y$ assumes every promise is kept, and which moves with rates and default risk in a way $c$ does not.
<!-- YW5zOjM= -->
> $r_D$ is the expected return investors require today: $D = [F(1-p) + Cp]/(1+r_D)$, while the yield solves $D = F/(1+y)$, so with default risk $y > r_D$ (slides 104–105). The coupon is a historical contract term that ignores later changes in rates and risk (slide 103). Seniority does not make debt riskless: with default possible, creditors bear risk and $r_D$ can exceed $r_f$.
> Ref: Topic 2A slides 103–105; Topic 2B slides 54–63; Berk *Fundamentals* Ch. 6 §6.5 (p. 164)
> Similar: Lista R2b, Ex. 5 (Berk Critical Thinking 8); Lista R2b, Ex. 9 (Ross 7.19)
