---
quiz: "Macroeconomic implications (hard) — rationing, asset values, aggregate liquidity, policy"
tags:
  ratio: "Credit rationing, the interest rate and wealth dynamics"
  assets: "Asset resale and fire sales (Shleifer–Vishny)"
  aggliq: "Aggregate liquidity: inside, outside, premia"
  polit: "Time consistency, bailouts and borrowing abroad"
---

## ratio

Q: In a closed economy, entrepreneurs with heterogeneous wealth $A$ run fixed-size projects; a project is financed iff the pledgeable income $p_H(R - B/\Delta p)$ covers $(1+r)(I - A)$, and savers' supply $S(r)$ rises with $r$. Better investor protection lowers the private benefit $B$. What happens in equilibrium?
- The interest rate falls: lower agency costs make every loan safer, so savers accept a lower return, and the cheaper credit lets even more entrepreneurs invest, amplifying the expansion.
- The interest rate is unchanged, as it is pinned down by savers' patience; only the wealth cutoff $A^*$ falls, and the whole gain in pledgeable income becomes credit for poorer entrepreneurs.
- The interest rate rises until the financed share is back at its old level, because each extra loan must be matched by extra saving and savers demand a higher rate for every unit.
- More entrepreneurs pass the solvency test, so the demand for funds and $r$ rise; the higher $r$ lifts the cutoff $A^*$ again, which dampens the credit expansion without reversing it.
<!-- YW5zOjM= -->
> The cutoff is $A^*(r) = I - p_H(R - B/\Delta p)/(1+r)$, rising in $B$ and in $r$. Market clearing, $S(r) + \int_0^{A^*} A\,dG = [1 - G(A^*(r))]I$, has a left side rising in $r$ and a right side falling in $r$. A lower $B$ shifts loan demand out, so $dr/dB < 0$. General equilibrium transfers part of the gain to savers and partly offsets the fall in $A^*$, but cannot fully offset it, or demand would not have risen in the first place.
> Ref: Tirole Ch. 13 §13.2 (the balance-sheet channel, pp. 471–478); Tirole Ch. 3 §3.2
> Similar: Lista R10, Ex. 1 (Tirole 13.1)

Q: Credit-rationed entrepreneurs sell their output at a price $P$. Does credit rationing make aggregate investment more or less responsive to $P$ than in a first-best economy with no agency cost?
- Always more: a higher $P$ raises net worth and pledgeable income, so rationing amplifies every price change, and past investment crowds out current investment more than one for one.
- It depends: with fixed-size projects more entrepreneurs qualify as $P$ rises, a net-worth effect; with constant returns part of each gain is not pledgeable, so investment responds less.
- Always less: part of every gain from a higher $P$ accrues to entrepreneurs as rent, so investors expand by less than entrepreneurs would like, whatever the shape of the technology.
- Neither: competitive investors pass the whole NPV to entrepreneurs, so rationing changes the level of investment but not how it moves with $P$, which technology alone determines.
<!-- YW5zOjE= -->
> Fixed size: without rationing investment is flat in $P$ once NPV is positive, while with rationing the share $1 - G(I - p_H[PR - B/\Delta p])$ of funded firms rises with $P$ (net-worth effect). Constant returns: the first best has full crowding out, $\partial I/\partial I_0 = -1$, while under rationing $-1 < \partial I^{SB}/\partial I_0 < 0$, because investors capture only the pledgeable part of a better market (hindering effect). With decreasing returns both effects appear, and near the point where the constraint stops binding the second-best responds more.
> Ref: Tirole Ch. 13 §13.5.1 (pp. 489–491)
> Similar: Lista R10, Ex. 11 (Tirole 13.3)

Q: Dynasties live one period each, consume a share $1 - a$ of income and bequeath a share $a$; each generation also receives an endowment $\hat A$. A fixed-size project is financed only if wealth exceeds a threshold $\bar A$; otherwise wealth earns the storage return. Why can two dynasties with almost equal initial wealth stay unequal forever?
- Below $\bar A$ a dynasty cannot borrow, earns only storage and tends to $\hat A/(1-a) < \bar A$; just above, it earns the NPV and settles higher. With no agency cost all would converge.
- They cannot: since only a share $a < 1$ of income is bequeathed, wealth dynamics are stable and every dynasty converges to the same level; credit rationing only slows the convergence.
- Rich dynasties earn a higher interest rate on their savings than poor ones, so their wealth compounds faster, and the gap between them widens even with no threshold for financing.
- Poor dynasties bequeath a smaller share $a$ of their income, because consumption is more urgent near subsistence, so their wealth settles at a lower level than that of rich dynasties.
<!-- YW5zOjA= -->
> Below $\bar A$: $A_{t+1} = \hat A + aA_t$, fixed point $\hat A/(1-a) < \bar A$ (poverty trap). Above: $A_{t+1} = \hat A + a(R - I + A_t)$, a higher fixed point. Both maps have slope $a < 1$, so each branch is stable, but the jump at $\bar A$ splits the dynamics. With $B = 0$ there is no threshold and all lineages converge to $[\hat A + a(R - I)]/(1-a)$. Closing the loan market adds a second channel: many poor lenders keep $r$ low, which keeps them from saving their way out (Matsuyama 2000).
> Ref: Tirole Ch. 13 §13.4.2 (warm-glow lineages, pp. 484–487)
> Similar: Lista R10, Ex. 14 (Tirole 13.2)

## assets

Q: Two firms use the same specialised assets; if one is in distress its assets can only be sold to the other, and the seller's lenders make a take-it-or-leave-it offer. Per unit, the assets yield $\rho_1 = p_H R$ in expectation, of which $\rho_0 = p_H(R - B/\Delta p) < 1$ is pledgeable. Why do they sell at a discount?
- Outside buyers could run the assets but fear adverse selection about their quality, so they bid a lemons discount, and the peer firm only has to match that low outside bid to win the sale.
- The buyer has time on its side: it can wait until the seller's lenders grow desperate, so bargaining splits the surplus and the price ends halfway between $\rho_0$ and $\rho_1$.
- The buyer can pay no more than its pledgeable income $\rho_0$ per unit, because the extra assets raise its own manager's rent; the price is below their value $\rho_1$ and below their cost.
- The assets are worth less to the buyer than to the seller, who has the specific knowledge to run them, so the price reflects the buyer's lower productivity, $\rho_0$ instead of $\rho_1$.
<!-- YW5zOjI= -->
> To keep its entrepreneur behaving on $I_1 + I_2$ units, the buyer's lenders must raise her stake by $BI_1/\Delta p$, so they can pay at most $PI_1 = \rho_0 I_1$. The asset is sold below its value even though the seller has all the bargaining power; the buyer's entrepreneur pockets the rent $(\rho_1 - \rho_0)I_1$. There are no outside buyers in the model, and the distressed firm's assets have no internal use, so the discount is a pledgeability limit, not a productivity gap or a bargaining split.
> Ref: Tirole Ch. 14 §14.2.2 (Shleifer–Vishny, pp. 500–503)
> Similar: Lista R10, Ex. 6 (Tirole 14.1); Lista R10, Ex. 7 (Tirole 14.4)

Q: Two firms with specialised assets can buy each other's assets after distress, at a price limited by the buyer's pledgeable income. Why is one firm's investment a positive externality for its peer under constant returns, and when can that externality turn negative?
- It is negative even under constant returns, because the firms compete in the product market and a larger rival lowers prices; it turns positive only when shocks are perfectly correlated.
- A firm that invests stands ready to buy its peer's assets if the peer fails, which raises their resale value; with decreasing returns a big buyer pays less for more, so it can turn negative.
- It is positive because the investing firm's lenders share the peer's losses in distress; it turns negative when shocks are perfectly correlated, since both firms then dump their assets at once.
- It is positive because investment by one firm raises the other's debt multiplier directly; it turns negative when investor protection improves and pledgeable income stops depending on the peer.
<!-- YW5zOjE= -->
> With constant returns, $U_{bi} = \alpha I_i + \kappa I_j$ with $\kappa = x(1-\mu)(\rho_1 - \rho_0) > 0$: firm $j$'s size is the market for $i$'s assets. With decreasing returns the price is $p_H[R(I_i + I_j) - R(I_i)] - bI_j$, which falls with the buyer's own scale, and $\partial U_{bj}/\partial I_i \propto B/\Delta p - [R'(I_i) - R'(I_i + I_j)]$ can be negative. Under perfect correlation both firms fail together and no sale happens at all, so the externality vanishes rather than turning negative; the firms do not compete in the product market.
> Ref: Tirole Ch. 14 §14.2.2 (pp. 500–503, including the remark on decreasing returns)
> Similar: Lista R10, Ex. 6 (Tirole 14.1)

## aggliq

Q: Firms face independent liquidity shocks, so there is no aggregate uncertainty, and there is no outside store of value; the corporate sector as a whole is a net borrower. Can the sector meet its distressed firms' refinancing needs on its own?
- No: without an outside store of value, liquidity has to come from outside the corporate sector, so government bonds are needed even when the shocks are fully independent across firms.
- Yes, and holding the stock index is enough: each distressed firm sells its shares in healthy firms at date 1, and the proceeds cover its own reinvestment need in every realisation.
- Only partly: healthy firms' claims are worth exactly the distressed firms' need when the sector breaks even, so any agency cost leaves a shortfall that outside liquidity must cover.
- Yes: as a net borrower, its healthy firms' pledgeable value exceeds the distressed firms' net need; but a stock index wastes it, so liquidity must be pooled, e.g. through credit lines.
<!-- YW5zOjM= -->
> Break-even with $I - A > 0$ implies $(1-\lambda)(\rho_0 - \rho_L) > \lambda(\rho_H - \rho_0)$: gross inside liquidity exceeds the net refinancing need. But if each firm simply holds the index, healthy firms end up with excess cash they will not reinvest in distressed firms, while distressed firms hold too little; the index spreads liquidity over firms that do not need it. An intermediary holding the shares and granting credit lines concentrates it where the shocks hit.
> Ref: Tirole Ch. 15 §15.2.1–15.2.2 (sufficiency result, wasting inside liquidity, pp. 518–522)
> Similar: Lista R10, Ex. 8 (Review Problem 6); Lista R10, Ex. 3 (Tirole 15.3)

Q: Liquidity shocks are perfectly correlated across firms: in the bad state every firm needs $\rho_H > \rho_0$ per unit of investment at once. Why does the supply of outside liquidity matter, and what happens if it is scarce?
- Claims on other firms lose value exactly when all need cash, so only claims paying in that state help; if scarce, they trade at a premium $q > 1$, and firms rescue or invest less.
- It matters only with independent shocks; under a common shock firms diversify across one another, so the supply of government bonds affects their price $q$ but not corporate investment.
- Scarce outside liquidity leaves investment unchanged, because firms replace it one for one with credit lines from one another, at a premium $q > 1$ that is a pure transfer between them.
- Scarce outside liquidity trades below par, $q < 1$, because firms sell it at date 0 to fund their initial investment, so its scarcity lowers its price and raises corporate investment.
<!-- YW5zOjA= -->
> With a common shock all firms are valueless in the bad state, so distressed firms cannot raise cash by selling claims on healthy ones: inside liquidity fails and $x = 0$ without outside liquidity. Assets that pay in that state, such as government bonds, become scarce inputs; when supply falls short of the second-best need, $q > 1$, the cost of continuation rises, and firms cut scale or continuation. The optimal continuation threshold under abundant liquidity is the same in every macro state; scarcity is what makes it move.
> Ref: Tirole Ch. 15 §15.3.1 (aggregate shocks and the value of outside liquidity, pp. 523–525)
> Similar: Lista R10, Ex. 10 (Tirole 15.2); Lista R10, Ex. 13 (Tirole 15.4)

Q: A firm with decreasing returns invests $I$ at date 0; with probability $\lambda$ it is distressed at date 1 and can salvage $J \le I$ units at cost $\rho$ per unit, while with probability $1 - \lambda$ it keeps all $I$ units at no cost. When does the distressed firm optimally downsize, $J < I$?
- Iff $\rho > \rho_0$: any unit whose rescue costs more than its pledgeable income is cut back, as in the cutoff rule for a fixed-size project hit by a single liquidity shock.
- Iff $\rho > 1/\lambda$: the rescue cost is paid only in the distressed state, which occurs with probability $\lambda$, so $1/\lambda$ is the break-even reinvestment cost per unit.
- Iff $\rho > 1/(1-\lambda)$: a unit of initial scale costs 1 and survives without reinvestment only with probability $1-\lambda$, and a rescued unit is worth keeping only if cheaper.
- Iff $\rho > \rho_1$: downsizing happens only when a rescued unit has negative NPV, because otherwise the firm salvages every unit that it can finance at date 1.
<!-- YW5zOjI= -->
> The first-order conditions are $p_H R'(I) = \frac{1}{1-\lambda} + \frac{\mu}{1+\mu}\frac{p_H B}{\Delta p}$ and $p_H R'(J) = \rho + \frac{\mu}{1+\mu}\frac{p_H B}{\Delta p}$, with the same agency wedge. So $J < I$, i.e. $R'(J) > R'(I)$, iff $\rho > 1/(1-\lambda)$. The comparison is between two ways of having a unit in place in the distressed-or-intact lottery, not between the rescue cost and pledgeable or total income. With a common shock this sets the demand for outside liquidity, and a premium $q > 1$ cuts $J$ further.
> Ref: Tirole Ch. 15 exercise 15.1 (pp. 530–531); Tirole Ch. 15 §15.3.1 (pp. 523–525)
> Similar: Lista R10, Ex. 12 (Tirole 15.1)

## polit

Q: A government that maximises total welfare can subsidise firms at date 1, after productivity is revealed, at a social cost of $1 + \lambda$ per unit; stopping a viable low-productivity firm costs output and unemployment benefits. What happens if the government cannot commit at date 0?
- Nothing of substance: a subsidy is a transfer from taxpayers to investors, so firms still hoard the privately optimal liquidity, and only the distribution of income is affected.
- Firms hoard more liquidity than without a government, because the state subsidises only firms that hoarded, rewarding prudence, so over-insurance becomes privately profitable.
- Welfare rises: commitment would force the layoff of viable firms in the low state, so a government free to bail out avoids those job losses and saves the unemployment benefits.
- It always bails out the low-productivity firm, so firms hoard no liquidity and taxpayers supply it at the shadow cost of funds; commitment avoids this without losing a job.
<!-- YW5zOjM= -->
> Without a government, the firm continues in the low state using liquidity $L^* = w + \mathcal R - y_L$ hoarded at date 0. Ex post, the government prefers paying that gap to losing output and paying unemployment benefits, so it bails out; anticipating this, firms hoard nothing and the subsidy costs $(1+\lambda)$ per unit, a deadweight loss $\lambda s$. A committed government sets $s = 0$; firms then hoard $L^*$ and still continue, so no job is lost. This is Chapter 5's soft budget constraint in a policy setting.
> Ref: Tirole Ch. 5 §5.5 (soft budget constraint, from p. 220); Tirole Ch. 16 §16.3.2 (pp. 546–549)
> Similar: Lista R10, Ex. 9 (Tirole 16.4)

Q: After firms have borrowed, a government chooses a costly policy that raises their success probability and hence their pledgeable income. How does its choice compare with the one it would make under commitment, and what changes when the lenders are foreign?
- With investment sunk, the policy no longer raises borrowing capacity, so the government weighs cost against the output gain alone and picks less; foreign lenders' gains count less still.
- Voters are myopic and discount future output, so the government underinvests in every policy with delayed benefits; foreign lenders worsen this by charging a risk premium on the country's debt.
- It chooses more, since ex post it wants to maximise investors' recovery in order to attract future loans; foreign lenders change nothing because they are price takers in a world market.
- It chooses the same as under commitment, because rational lenders anticipate the policy and the government internalises that anticipation at every date, so time consistency costs nothing.
<!-- YW5zOjA= -->
> Ex post the government solves $\max_\tau (p_H + \tau)RI - \gamma(\tau)I$, giving $\gamma'(\tau^*) = R$. Under commitment it also counts $dI/d\tau > 0$, since a higher $\tau$ raises pledgeable income and investment: $\tau^c > \tau^*$. With foreign lenders weighted by $\omega < 1$, $\gamma'(\tau) = R - (1-\omega)(R - B/\Delta p) < R$, so it provides even less and lenders, anticipating it, lend less. Domestic savings work as a commitment device for the same reason: taxing investors then hurts the government's own constituents.
> Ref: Tirole Ch. 16 §16.3 (property rights and time inconsistency, pp. 544–551); Tirole Ch. 3 §3.4
> Similar: Lista R10, Ex. 2 (Tirole 16.2); Lista R10, Ex. 4 (Review Problem 5); Lista R10, Ex. 5 (Tirole 16.1)
