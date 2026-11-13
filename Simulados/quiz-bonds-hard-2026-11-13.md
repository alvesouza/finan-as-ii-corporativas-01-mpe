---
quiz: "Bonds (hard) — Prices, yields, the term structure and default risk"
tags:
  px: "Prices, yields and the term structure"
  sens: "Why bond prices move: time, rates and call features"
  credit: "Default risk, spreads and the cost of debt"
---

## px

Q: Two default-free bonds have the same maturity, but one pays a high coupon and the other a low one. The zero-coupon (spot) curve slopes upward. How do their yields to maturity compare?
- They are equal, since both are default-free and mature on the same date, and the yield to maturity depends only on maturity and default risk.
- The high-coupon bond has the lower yield, since more of its value comes from early payments that are discounted at the lower short spot rates.
- The high-coupon bond has the higher yield, since it pays more interest each year, and the yield to maturity rises one for one with the coupon rate.
- Both yields equal the spot rate for their common maturity, since a coupon bond is priced off the zero curve and so inherits its long-end rate.
<!-- YW5zOjE= -->
> A coupon bond is a portfolio of zeros, $P = \sum_t CF_t/(1+r_t)^t$ (slide 5), and its yield to maturity is the single rate that reproduces that price — a weighted average of the spot rates, weighted toward the dates where its value sits. A high coupon puts more weight on the early, low rates, so its yield is lower. Only with a flat curve, or for a zero, does the yield equal one spot rate.
> Ref: Topic 2A slides 4–6; Berk *Fundamentals* Ch. 6 §6.3 (p. 151), App. B Eq. 6.4 (p. 179); Grinblatt–Titman Ch. 10 App. 10A (pp. 363–367)
> Similar: Lista R2b, Ex. 8 (Berk 6.10); Lista R2b, Ex. 13 (G&T 10A.3)

Q: A default-free coupon bond trades below the sum of its cash flows each discounted at the spot rate for its date. Short sales and stripping (trading each payment as a separate zero-coupon bond) are free. Which trade earns a riskless profit?
- Sell the coupon bond short and buy the zeros that match its payments, since the bond's low price means its yield to maturity is too low for the curve.
- Buy the coupon bond and hold it to maturity, since its yield to maturity is above the spot rates, so it earns more than the zeros with no risk at all.
- Buy the coupon bond and sell short the zeros that match each of its payments, keeping the price gap today with every future cash flow offset.
- No trade earns a riskless profit, since a coupon bond and its zeros have different yields to maturity, so they are not the same asset for arbitrage.
<!-- YW5zOjI= -->
> The bond and the matching strip of zeros have identical payoffs on every date, so by the law of one price they must cost the same (slides 50–51). Buying the cheap side and shorting the dear side gives cash today and nets to zero on every future date — a free lunch. A low price means a high yield, not a low one; and simply holding the bond is not an arbitrage, since it locks in no profit today.
> Ref: Topic 2A slides 5, 50–51; Berk *Fundamentals* Ch. 6 App. B (p. 179); Ross *Fundamentos* Cap. 7 §7.7 (p. 223)
> Similar: Lista R2b, Ex. 8 (Berk 6.10); Lista R2b, Ex. 14 (Ross 7.32)

Q: A default-free bond trades above its face value, and its yield to maturity stays the same until it matures. What is correct?
- Its coupon rate exceeds its yield; its price drifts down toward face value over time, and the return over each period still equals the yield.
- Its coupon rate exceeds its yield, and an investor earns the coupon rate each period, since the coupons are high and the price stays at its premium.
- Its yield exceeds its coupon rate; its price rises toward face value over time, so each period's return beats the yield thanks to that capital gain.
- Its coupon rate exceeds its yield, but its price stays above face value until the final date and then falls at once, giving a loss at maturity.
<!-- YW5zOjA= -->
> A premium means the coupon pays more than the market requires, so coupon rate > yield. At a constant yield the price at each date is the PV of the remaining flows, which falls smoothly to face value as premium coupons are used up; the coupon minus that steady capital loss gives exactly the yield each period. Discount bonds mirror this, with a rising price.
> Ref: Topic 2A slides 4–5; Berk *Fundamentals* Ch. 6 §6.3–6.4 (pp. 151–156); Ross *Fundamentos* Cap. 7 §7.1 (p. 192)
> Similar: Lista R2b, Ex. 7 (Berk 6.16–6.18); Lista R2b, Ex. 3 (Ross 7.6)

Q: The two-year spot rate $r_2$ exceeds the one-year spot rate $r_1$. An investor with a two-year horizon compares a two-year zero with a one-year zero rolled into another one-year zero next year. With $f$ defined by $(1+r_2)^2=(1+r_1)(1+f)$, which statement is right?
- The two-year zero dominates, since $r_2>r_1$ means it earns more in each year, whatever the one-year rate turns out to be next year.
- Rolling over dominates, since $r_2>r_1$ shows that the market expects short rates to rise, so next year's rate must end up above $f$.
- Both strategies give the same return in every state, since no arbitrage requires next year's one-year rate to be equal to $r_2$.
- Rolling over wins only if next year's one-year rate ends up above $f$, which exceeds $r_2$; the curve alone does not pin that rate down.
<!-- YW5zOjM= -->
> The two-year zero locks in $r_1$ for the first year and the implied forward rate $f$ for the second; since $r_2$ is the average of $r_1$ and $f$ and $r_1 < r_2$, $f > r_2$. Rolling over earns $r_1$ and then whatever one-year rate prevails next year, which is unknown today. An upward curve may reflect expected rate rises or a premium for bearing interest-rate risk, so it guarantees neither strategy.
> Ref: Topic 2A slides 4–6; Berk *Fundamentals* Ch. 6 §6.2 (p. 147), App. B (p. 179); Ross *Fundamentos* Cap. 7 §7.7 (p. 223)
> Similar: Lista R2b, Ex. 1 (Berk 6.4); Lista R2b, Ex. 13 (G&T 10A.3)

## sens

Q: Two default-free bonds have the same maturity and the same yield; one is a zero-coupon bond and the other pays a high coupon. Why does the zero's price move more, in percentage terms, when yields change?
- All of its value sits in one payment at the final date, while the coupon bond collects much of its value earlier, so its value-weighted timing is shorter.
- The zero is riskier because it pays nothing until maturity, so it carries a larger credit premium, and that premium reacts more strongly to rate moves.
- The coupon bond is protected by reinvesting its coupons at the new yield, which offsets its price change exactly, while the zero has nothing to reinvest.
- The zero trades at a deep discount to face, and since a percentage change is larger the smaller the starting price, the zero moves by more than the coupon bond.
<!-- YW5zOjA= -->
> A payment due in $t$ years has price elasticity to the yield of roughly $-t/(1+y)$, so a bond's sensitivity is the value-weighted average of its payment dates — its duration. The zero's duration equals its maturity; coupons pull the coupon bond's duration below it. Both are default-free here, reinvestment does not erase the price change, and the level of the price is not what drives the sensitivity.
> Ref: Berk *Fundamentals* Ch. 6 §6.4 (p. 156); Ross *Fundamentos* Cap. 7 §7.1 (p. 192)
> Similar: Lista R2b, Ex. 11 (Berk 6.21–6.22)

Q: An investor buys a default-free coupon bond at yield $y$. Right after the purchase, market yields rise and stay higher until maturity. Which statement about the investor's realised returns is correct?
- The return over the next year falls short of $y$ due to the price drop, and the return to maturity also ends below $y$, since the loss is never recovered.
- The return over the next year falls short of $y$ due to the price drop, while the return to maturity, with coupons reinvested at the new yields, ends above $y$.
- Both returns equal $y$, since the yield to maturity is locked in at purchase, and later changes in market yields matter only to an investor who sells early.
- The return over the next year exceeds $y$, since the new coupons are worth more at the higher yields, while the return to maturity ends exactly at $y$.
<!-- YW5zOjE= -->
> The price falls at once when yields rise, so a one-year holding-period return is below $y$. Held to maturity, the bond still pays its promised flows, and coupons reinvested at the higher rates grow faster than the yield assumed, so the realised return to maturity exceeds $y$. Only a zero, with nothing to reinvest, locks in exactly $y$ if held to maturity.
> Ref: Berk *Fundamentals* Ch. 6 §6.4 (p. 156); Higgins 13e Ch. 5 §5.1.1 (p. 143)
> Similar: Lista R2b, Ex. 2 (Higgins 5.5); Lista R2b, Ex. 7 (Berk 6.16–6.18)

Q: A callable bond is identical to a noncallable one except that the issuer may redeem it at a fixed call price after some date. Which statement holds?
- The callable bond has the lower yield, since investors value the flexibility the issuer gains, and its price rises more when rates fall because calls grow likelier.
- The callable bond trades at a higher price, since the call price acts as a floor that protects investors, and so its yield is below that of the noncallable bond.
- The two trade at the same price at issue, since the call option belongs to the issuer, who pays nothing for it, and they differ only once the call is exercised.
- The callable bond is cheaper and yields more, since investors have written a call to the issuer, and its gains as rates fall are capped near the call price.
<!-- YW5zOjM= -->
> By the law of one price, callable bond = noncallable bond − call option held by the issuer, so it is cheaper and its yield is higher. The issuer calls when rates have fallen and the bond is worth more than the call price, so investors lose their upside exactly when rates drop; the call price is a ceiling, not a floor.
> Ref: Higgins 13e Ch. 5 §5.1.1 (p. 143); Ross *Fundamentos* Cap. 7 §7.2 (p. 203); Topic 2A slides 50–51
> Similar: Lista R2b, Ex. 4 (Higgins 5.4); Lista R2b, Ex. 14 (Ross 7.32)

## credit

Q: A one-period corporate bond has face value $F$ and market price $D$. It defaults with probability $p$, in which case holders recover $C<F$. Let $y$ be its promised yield and $r_D$ its expected return. Which statement is right?
- $(1+y)/(1+r_D)=[F(1-p)+Cp]/F$, so the yield falls short of the expected return, since buyers are paid a premium for bearing the default risk.
- $y-r_D=p$ whatever the recovery $C$, so the gap between the promised yield and the expected return measures only the probability of default.
- $(1+y)/(1+r_D)=F/[F(1-p)+Cp]$, so $y>r_D$ whenever $p>0$ and $C<F$, whatever risk premium is priced into the bond's expected return.
- $y=r_D$ whenever investors are risk neutral, since the yield is then the expected return, and a gap between them only appears with risk aversion.
<!-- YW5zOjI= -->
> From $D = F/(1+y)$ and $D = [F(1-p) + Cp]/(1+r_D)$, divide to get the ratio of gross rates: the promised payment over the expected payment, which exceeds one whenever default loses money. The gap is set by the expected loss $p(F-C)$, not by $p$ alone, and it exists even under risk neutrality, where $r_D = r_f < y$. The yield overstates the cost of debt.
> Ref: Topic 2A slides 103–105; Berk *Fundamentals* Ch. 6 §6.5 (p. 164)
> Similar: Lista R2b, Ex. 5 (Berk Critical Thinking 8); Lista R2b, Ex. 15 (G&T 7.3)

Q: Two corporate bonds have the same promised payments, the same default probability and the same recovery. Bond R defaults mainly in recessions and bond B mainly in booms. Which comparison is right?
- R trades at a wider spread and has a higher expected return, since its losses fall in states where a unit of payoff is worth more, which state prices weigh more.
- They trade at the same spread, since the expected loss is the same, and the timing of default across states is diversifiable risk that the market does not price.
- B trades at the wider spread, since booms are the more likely states, so a default concentrated in booms lowers the bond's expected payoff by more.
- R trades at the wider spread, but both have the same expected return, since the spread only compensates the expected loss, which is larger in recessions.
<!-- YW5zOjA= -->
> With equal expected losses, the difference is when the losses arrive. A claim on recession states is expensive (slide 67), so losing payoff there costs more value: R's price is lower, its spread wider, and its expected return above B's — a premium for systematic default risk. Recession timing is aggregate risk, not diversifiable, and by assumption the default probabilities are equal.
> Ref: Topic 2A slides 7–8, 60–67, 103–105; Berk *Fundamentals* Ch. 6 §6.5 (p. 164)
> Similar: Lista R2b, Ex. 6 (Berk 6.24); Lista R2b, Ex. 15 (G&T 7.3)

Q: For a firm close to distress, an analyst puts the promised yield on its bonds in place of the expected return on debt when computing the WACC from market weights and a correct cost of equity. What is the effect?
- The WACC is understated, since the promised yield ignores the recovery in default, and so the projects end up valued at too high a figure by the analyst.
- There is no bias, since the promised yield is the rate the firm would pay on new debt today, which is the marginal cost of debt that the WACC needs.
- The direction depends on the coupon, since bonds trading below par have a yield above the coupon, and the coupon is the true cost of the firm's debt.
- The WACC is overstated, since the promised yield exceeds the expected return whenever default is possible, and so the firm's projects end up undervalued.
<!-- YW5zOjM= -->
> The WACC is the market-value average of the expected returns on the claims, $r_A = \frac{E}{D+E}r_E + \frac{D}{D+E}r_D$. For distressed debt the yield is well above $r_D$, so the WACC is too high and the PV of the cash flows too low. A new issue at par sets the coupon equal to the promised yield, but that is still a promise, not an expected return; the old coupon is a historical number.
> Ref: Topic 2A slides 97–105; Topic 2B slides 54–63; Higgins 13e Ch. 8 §8.4.2 (p. 296)
> Similar: Lista R2b, Ex. 9 (Ross 7.19); Lista R2b, Ex. 5 (Berk Critical Thinking 8); Lista R2, Ex. 5 (Higgins 8.7)
