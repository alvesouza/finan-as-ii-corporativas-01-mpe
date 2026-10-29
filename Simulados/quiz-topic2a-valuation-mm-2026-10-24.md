---
quiz: "Topic 2A — Valuation, the NPV rule and the Modigliani–Miller benchmark"
tags:
  val: "Valuation and cost of capital"
  mm: "Modigliani–Miller benchmark"
---

## val

Q: To estimate the cost of capital of a project, an analyst finds a traded firm in the same line of business that is heavily financed with debt. Why can't the analyst plug that firm's equity beta straight into the CAPM?
- Equity betas are estimated from past returns, which are backward-looking, while the CAPM needs a forward-looking beta implied by current option prices.
- Leverage makes the comparable's equity riskier than its assets; the project's risk is the asset beta, a value-weighted average of the equity and debt betas.
- The comparable pays taxes at a different rate, and every CAPM beta has to be adjusted for the tax rate before it can be used for a different firm.
- The CAPM holds only for diversified portfolios, so a single firm's beta must be replaced by the industry's average equity beta before it is used.
<!-- YW5zOjE= -->
> Because $A = D + E$ in market value, returns and betas are value-weighted averages: $\beta_A = \frac{E}{D+E}\beta_E + \frac{D}{D+E}\beta_D$. A levered comparable's $\beta_E$ overstates the asset risk, so the analyst unlevers it (with $\beta_D \approx 0$ when debt is nearly riskless) and uses $\beta_A$ for the project.
> Ref: Topic 2A slides 10–23; Higgins 13e Ch. 8 App. 8.A.1 (p. 319); Ross *Fundamentos* Cap. 14 §14.5 (p. 476)
> Similar: PS2 Ex. 4(a) (equity beta after a debt-financed repurchase)

Q: A firm evaluating a new machine has already paid a consultancy fee for the study, would bear part of the overhead allocated to the project anyway, and could sell its current machine instead of keeping it. Which treatment of these items is correct?
- Include the fee and all allocated overhead, since both are real costs of the decision, and ignore the old machine's resale value because it is not a cash outflow.
- Exclude the fee, include all allocated overhead to stay conservative, and count the old machine's resale value only if it is above the machine's book value.
- Include the fee, exclude all overhead, and value the old machine at book value, since the accounting figure is the verifiable measure of what is given up.
- Exclude the fee as sunk and the overhead incurred anyway, keep only incremental overhead, and treat the forgone after-tax resale of the old machine as a cost.
<!-- YW5zOjM= -->
> Cash flows are incremental: with the project minus without it. Sunk costs are already incurred whatever is decided; overhead that exists anyway is not caused by the project; an asset that could be sold has an opportunity cost equal to its after-tax resale value (taxed on the gain over book value).
> Ref: Topic 2A slides 26–27; Ross *Fundamentos* Cap. 10 §10.2 (p. 320); Higgins 13e Ch. 7 §7.3.3–7.3.4 (pp. 263–264)
> Similar: PS1 Ex. 2(a), PS1 Ex. 3

Q: An all-equity firm with symmetric information and competitive capital markets has a positive-NPV project that it can fund with insiders' money, by selling new shares, or with safe debt. What happens to the original shareholders' wealth?
- It rises by the NPV in all three cases, because outsiders who supply funds at a fair price earn zero NPV and so capture none of the project's surplus.
- It rises by the NPV only if insiders fund the project, because issuing new shares dilutes the original owners and hands part of the NPV to the newcomers.
- It rises by more than the NPV with debt, because borrowing at the risk-free rate is cheaper than equity and adds a financing gain on top of the project.
- It rises by the NPV only with equity, because safe debt shifts part of the project's payoff to creditors, who must be paid before the shareholders.
<!-- YW5zOjA= -->
> Competitive financiers break even: new shareholders buy a fraction worth exactly what they pay, and safe creditors are repaid at the fair rate. The whole NPV stays with the original owners, so the NPV rule equals shareholder-value maximisation. This breaks down with risky debt (debt overhang) or asymmetric information.
> Ref: Topic 2A slides 31–36; Amaro de Matos Ch. 1 §1.1.6 (p. 14)
> Similar: Amaro de Matos 1.1.8 #8 (prove the NPV rule)

Q: Two mutually exclusive projects are on the table: a small one with a very high IRR, and a large one with a lower IRR but a higher NPV at the cost of capital. Which statement about the choice is right?
- Choose the high-IRR project, because the IRR measures return per unit invested and the firm can always repeat the small project to reach the larger scale.
- Choose the high-IRR project only if its IRR beats the other's by more than the cost of capital, which is how the IRR rule ranks exclusive projects.
- Choose the higher-NPV project, because the IRR ignores scale, so a high rate on a small outlay can add less value than a lower rate on a large one.
- Either project is fine, because both clear the hurdle rate, and the NPV and IRR rules always agree on accept-or-reject choices for single projects.
<!-- YW5zOjI= -->
> NPV measures value added in currency; IRR is a rate and ignores scale. Repeating a project is not generally possible, and the IRR rule has no "beat by the cost of capital" version. IRR also fails with multiple roots, non-existence, and lending-type cash flows.
> Ref: Topic 2A slides 37–38; Ross *Fundamentos* Cap. 9 §9.5 (p. 294); Higgins 13e Ch. 7 §7.2.7–7.2.8 (pp. 256–257)
> Similar: Ross *Fundamentos* Cap. 9 problems (pp. 309–317)

Q: If competitive markets rule out arbitrage, how can positive-NPV projects exist in equilibrium at all?
- They cannot: in equilibrium every project has zero NPV, and positive measured NPVs only reflect forecasting errors in cash flows or discount rates.
- A positive NPV is an "arbitrage" across the firm's boundary that cannot be scaled up, since it rests on the firm's own assets, ideas or synergies.
- They exist only when the firm has market power in the capital market, which lets it raise funds below the rate investors require for the risk.
- They exist because the CAPM ignores idiosyncratic risk, so projects with high idiosyncratic risk look better than they are and keep a positive NPV.
<!-- YW5zOjE= -->
> The NPV compares the value of a cash-flow stream inside the firm with its cost outside. Unlike a financial arbitrage, it cannot be replicated at will by others, which is why it survives. An acquisition with synergies or market-power gains is the lecture's example.
> Ref: Topic 2A slides 29–30; Amaro de Matos Ch. 1 §1.2.3 (p. 23)
> Similar: Amaro de Matos 1.2.6 exercises (p. 28)

## mm

Q: In a two-state economy, a claim paying 1 in the slump costs more than a claim paying 1 in the boom, although the two states are equally likely. Why?
- Investors are risk averse, and a unit of consumption is worth more to them when they are poorer, so the claim that pays in the slump commands a higher price.
- The risk-free bond pays more in the slump than in the boom, so any claim built from the bond inherits the higher slump payoff and the higher price.
- The stock pays nothing in the slump, so the slump claim cannot be replicated and its price must carry a premium for the incompleteness of the market.
- State prices equal probabilities discounted at the risk-free rate, and the slump is discounted less heavily because interest rates fall in recessions.
<!-- YW5zOjA= -->
> With equal probabilities, any price gap reflects marginal utility: a dollar is worth more in bad times. The bond pays the same in both states, and the slump claim is replicated by going long the bond and short the stock, so the market is complete.
> Ref: Topic 2A slides 48–54, 60–67; Amaro de Matos Ch. 1 §1.2.1–1.2.2 (pp. 18–22)
> Similar: PS2 Ex. 1(a)

Q: Two firms have identical assets; one has safe debt in its capital structure and the other is all-equity. If the levered firm traded at a higher total value, which trade would exploit the gap?
- Buy the levered firm's equity and short its debt, since a higher total value means its equity is underpriced relative to the debt that creditors hold.
- Buy equal fractions of both firms' equity, since diversifying across capital structures removes the risk that makes the two market values differ.
- Short the unlevered firm's equity and lend at the risk-free rate, since the unlevered equity is overpriced and lending replicates the debt payoff.
- Short the levered firm's equity, and buy the unlevered firm's equity while borrowing on personal account to copy the leverage: homemade leverage.
<!-- YW5zOjM= -->
> Investors can lever up an all-equity firm themselves. Buying the unlevered equity with personal borrowing reproduces the levered equity's payoff more cheaply, so shorting the levered equity locks in a riskless profit. No arbitrage forces $V_L = V_U$ — MM I.
> Ref: Topic 2A slides 83–89; Ross *Fundamentos* Cap. 16 §16.2 (p. 542); Amaro de Matos Ch. 2 §2.1.1 (p. 40)
> Similar: Amaro de Matos 2.1.5 #2 (home-made leverage)

Q: A firm's assets pay a random amount at maturity and it has risky debt with a face value $K$ outstanding. Which decomposition of the two claims is correct?
- Debt is a call on the assets with strike $K$ and equity is a risk-free bond minus a put, so their sum depends on $K$ through the option prices.
- Debt is a risk-free bond plus a put on the assets with strike $K$, since creditors are insured against default by the owners' limited liability.
- Debt is a risk-free bond with face $K$ minus a put with strike $K$, equity is a call with strike $K$, and their sum is the assets, free of $K$.
- Debt and equity are both calls on the assets with different strikes, so their sum equals the assets only if the two strikes add up to $K$.
<!-- YW5zOjI= -->
> Debt pays $\min(K, X) = K - \max(K - X, 0)$: a safe bond minus a put. Equity pays $\max(X - K, 0)$: a call. By put–call parity $C(K) + K/(1+r_f) - P(K)$ is the value of the assets for any $K$, which is MM I with risky debt.
> Ref: Topic 2A slides 45, 90–96
> Similar: PS2 Ex. 1(b)–(d)

Q: Debt has a lower expected return than equity. Why does replacing equity with safe debt not lower the firm's overall cost of capital in the frictionless benchmark?
- Safe debt turns risky as soon as it is issued, so $r_D$ rises to $r_E$ and the costs of the two sources are equalised at every level of leverage.
- More debt makes the remaining equity riskier, so $r_E$ rises with $D/E$ by just enough to keep the weighted average $r_A$ unchanged.
- The tax rate is zero in the benchmark, so cheaper debt carries no tax shield that could offset the higher bankruptcy costs it brings.
- Shareholders demand compensation for losing control rights to creditors, which offsets the lower interest rate on the new debt issued.
<!-- YW5zOjE= -->
> MM II: $r_E = r_A + \frac{D}{E}(r_A - r_D)$. Even riskless debt makes equity riskier, so the cheap source raises the cost of the other one; $r_A = r_{WACC}$ stays put. Financial transactions repackage risk; they neither create nor destroy value.
> Ref: Topic 2A slides 74–80, 97–102; Ross *Fundamentos* Cap. 16 §16.3 (p. 547); Amaro de Matos Ch. 2 §2.1.2, Prop. 2.1.2 (p. 43)
> Similar: PS2 Ex. 4(b), PS2 Ex. 1(e)

Q: A firm's bonds trade at a yield to maturity well above the risk-free rate because default is possible. Why is that yield a biased estimate of the expected return on its debt, $r_D$?
- The yield is computed from book values while $r_D$ uses market values, so the yield understates the cost of debt whenever bond prices fall.
- The yield includes a liquidity premium unrelated to default, so $r_D$ lies above the yield for any bond that trades infrequently.
- The yield equals the coupon rate fixed at issuance, which reflects past market conditions rather than the current cost of borrowing.
- The yield discounts promised payments, while $r_D$ discounts expected ones net of default losses, so the yield overstates $r_D$.
<!-- YW5zOjM= -->
> $D = F/(1+y)$ uses the promised face value; $D = [F(1-p) + Cp]/(1+r_D)$ uses the expected payoff. With $p > 0$ and recovery $C < F$, the expected payoff is lower, so $y > r_D$. Neither the coupon nor the yield is the debt cost of capital.
> Ref: Topic 2A slides 103–105; Ross *Fundamentos* Cap. 7 (pp. 191–235)
> Similar: Ross *Fundamentos* Cap. 7 problems (bond yields)
