---
quiz: "Trade credit and working capital — hard conceptual quiz"
tags:
  cyc: "Operating and cash conversion cycles"
  cost: "Cost of trade credit, payables and bank credit"
  crp: "Credit policy, collection and inventory"
  fin: "Seasonal financing and why suppliers lend"
---

## cyc

Q: A retailer collects from customers within days, turns its inventory quickly and pays suppliers after two months, so its cash conversion cycle is negative. Holding these day counts fixed, what happens to its need for outside financing as its sales grow?
- It rises: net working capital is a fixed share of sales, so faster sales growth always raises the amount of inventory and receivables that the firm has to finance with debt or equity.
- It falls: payables exceed inventory plus receivables and all three grow with sales, so each extra unit of sales is paid for by suppliers before customers pay for it, and growth releases cash.
- It is unchanged: with the day counts held fixed, the cash conversion cycle keeps the same length, and a cycle of constant length implies a constant amount of working capital at any level of sales.
- It rises sharply: a negative cycle means the firm owes suppliers more than it is owed, so it is illiquid, and lenders will demand that faster growth be backed by new equity before they lend more.
<!-- YW5zOjE= -->
> With a negative cycle, operating working capital (inventory + receivables − payables) is negative and proportional to sales, so growth makes it more negative: suppliers finance the expansion. The cycle's length is constant, but the money amounts scale with sales. A negative cycle is a sign of bargaining power over suppliers, not of illiquidity, though it makes the firm dependent on their terms.
> Ref: Berk *Fundamentals* Ch. 19 §19.1 (p. 566); Ross *Fundamentos* Cap. 18 §18.2 (p. 627); Topic 1 slides 15–21 and 40–51 (net working capital, receivable and payable days)
> Similar: Lista R5b, Ex. 8 (Toyota vs. Apple); Lista R5b, Ex. 1

Q: Which change shortens a firm's cash conversion cycle while leaving its operating cycle unchanged, and what is the catch?
- Offering customers a discount for early payment: receivable days fall and the cash cycle shortens with them; the catch is that the discount is a price cut granted to customers who would have paid anyway.
- Moving to just-in-time inventory: inventory days fall and the cash cycle shortens with them; the catch is that a supply disruption can now halt production because there is no buffer stock left.
- Factoring the receivables to a bank: receivable days fall to zero and the cash cycle shortens with them; the catch is that the factor charges a fee and takes over the relationship with customers.
- Paying suppliers later: payable days rise and only the cash cycle shortens; the catch is that the extra days may cost a forgone early-payment discount or, past the due date, the supplier's goodwill.
<!-- YW5zOjM= -->
> The operating cycle is inventory days plus receivable days; the cash conversion cycle subtracts payable days. Faster collection, leaner inventory or factoring shorten both cycles. Only stretching payables shortens the cash cycle alone, and it is financing from suppliers, priced by the discount forgone and by the relationship.
> Ref: Ross *Fundamentos* Cap. 18 §18.2 (p. 627); Berk *Fundamentals* Ch. 19 §19.1 and §19.4 (pp. 566, 578)
> Similar: Lista R5b, Ex. 2 (Mediadora); Lista R5b, Ex. 13 (IMC payables against net-30 terms)

## cost

Q: A supplier's terms offer a discount $d$ for payment within $t_d$ days, with the full price due at day $t_n$. Which expression gives the effective annual cost of skipping the discount and paying at day $t_n$?
- $\left(1 + \frac{d}{1-d}\right)^{365/(t_n - t_d)} - 1$, since the buyer pays $d/(1-d)$ interest on the discounted price for the extra $t_n - t_d$ days
- $(1 + d)^{365/t_n} - 1$, since the buyer pays the discount $d$ as interest on the full price for all the $t_n$ days that the invoice remains outstanding
- $\left(1 + \frac{d}{1-d}\right)^{365/t_n} - 1$, since the buyer pays $d/(1-d)$ interest on the discounted price for all $t_n$ days the invoice stays unpaid
- $\frac{d}{1-d}\cdot\frac{365}{t_d}$, since the buyer forgoes the rate $d/(1-d)$ once for every discount period $t_d$ that fits in a year, without compounding
<!-- YW5zOjA= -->
> Skipping the discount means borrowing $1-d$ (the discounted price) and repaying 1, so the period rate is $d/(1-d)$. The loan lasts only $t_n - t_d$ days: the buyer could have paid at $t_d$ anyway. Compounding over $365/(t_n - t_d)$ periods gives the effective annual cost, which is large even for small $d$ because the period is short.
> Ref: Berk *Fundamentals* Ch. 19 §19.2 (p. 570); Ross *Fundamentos* Cap. 20 (pp. 702–742, credit terms and cash discounts)
> Similar: Lista R5b, Ex. 7 (3/15, net 40); Lista R5b, Ex. 3

Q: A buyer forgoes a 2/10, net 30 discount and, instead of paying on day 30, pays on day 50. The effective annual cost computed from the terms falls. Why is this not a free cut in its financing cost?
- It is not a cut at all: paying later means paying interest for 40 days rather than 20, so the effective annual cost computed over the longer period rises with the number of days the buyer waits.
- It is free only if the supplier charges no late fee: trade credit is unsecured and interest-free, so beyond the stated penalty the supplier has no way to make the buyer bear any cost for paying late.
- The formula prices only the lost discount; paying past the due date breaches the terms and invites penalties, tighter terms or cash in advance, and signals distress that other creditors can read.
- It is not free because the buyer must record the late payment as short-term debt, which raises its leverage ratios and so its cost of bank credit by exactly the interest it saved on trade credit.
<!-- YW5zOjI= -->
> The same discount spread over 40 days instead of 20 lowers the computed rate, which is why stretching looks attractive. But the computed rate ignores what the supplier does next: penalties, a lower credit limit, cash-on-delivery terms, a worse credit report. Persistent stretching is read as a distress signal, so its true cost is the loss of a cheap, flexible source of funds.
> Ref: Berk *Fundamentals* Ch. 19 §19.4 (p. 578)
> Similar: Lista R5b, Ex. 7(b) (paying on day 50); Lista R5b, Ex. 13(b)

Q: A firm can fund a 30-day need by forgoing a supplier's early-payment discount or by a bank loan with a stated APR, an origination fee and a non-interest-bearing compensating balance. How should the two be compared?
- By the stated rates: the bank's APR against the discount rate on the invoice, since fees and balances are one-off items that do not change the interest rate the firm is charged on the loan.
- By effective annual cost on usable funds: the fee and the idle balance force the firm to borrow more than it needs, lifting the loan's cost above its APR, as the lost discount lifts trade credit's.
- By preferring trade credit: it carries no stated interest, so its only cost is the administrative effort of paying later, whereas the bank loan carries interest, a fee and a balance that cannot be spent.
- By preferring the bank loan: the compensating balance stays in the firm's account and is returned at maturity, so it lowers the net cost of the loan below its APR, while trade credit has no such offset.
<!-- YW5zOjE= -->
> Both sources must be put on the same footing: the effective annual rate per unit of money the firm can spend. A fee is paid up front and a compensating balance cannot be used, so the firm borrows a grossed-up amount and pays interest on all of it. Trade credit is "free" only within the discount period; beyond it, its cost is the forgone discount, often far above bank rates.
> Ref: Berk *Fundamentals* Ch. 20 §20.3 (p. 601); Ch. 19 §19.2 (p. 570)
> Similar: Lista R5b, Ex. 9 (Hand-to-Mouth: forgone discount vs. two bank loans)

## crp

Q: A seller with variable cost $v$ per unit, credit price $P$ and required return $R$ per period faces new customers who default with probability $\pi$. Why can it rationally extend credit even when $\pi$ exceeds its profit margin?
- Because only the variable cost $v$ is at risk while the full price $P$ is gained, and with repeat business a paying customer yields $(P - v)/R$ for ever, raising the default rate it can tolerate.
- Because the default probability applies to the margin $P - v$ only, while the variable cost $v$ is recovered by repossessing the goods, so the loss in default is small whatever the default rate.
- Because the seller can charge a higher credit price $P$ that exactly compensates the expected default, so the NPV $-v + (1-\pi)P/(1+R)$ is zero by construction for any default probability.
- Because repeat customers never default, so the one-off NPV $-v + (1-\pi)P/(1+R)$ applies to the first order only, after which the default probability on that customer falls to zero.
<!-- YW5zOjA= -->
> For a one-off sale, $NPV = -v + (1-\pi)P/(1+R)$, so the break-even default rate is $1 - v(1+R)/P$: the seller risks $v$ to gain $P$. With repeat business, $NPV = -v + (1-\pi)(P-v)/R$: a paying customer becomes a perpetuity, so credit is granted much more liberally. Repossession plays no role in the model, and the zero-default assumption on repeat customers is a simplification, not the reason credit pays.
> Ref: Ross *Fundamentos* Cap. 20, "Quando o crédito deve ser concedido?" (pp. 717–718); Berk *Fundamentals* Ch. 19 §19.3 (p. 574)
> Similar: Lista R5b, Ex. 10 (Peças Aéreas, one-off vs. repeat order); Lista R5b, Ex. 14 (Senna, break-even credit price)

Q: A firm cuts its inventory days by $k$ while its cost of goods sold stays at $COGS$ per year. What is the cash effect?
- An annual cash inflow of about $k \cdot COGS/365$, since inventory is turned over more times each year and every turn frees the same amount of cash that used to be tied up in stock.
- A one-time release of about $k \cdot Sales/365$, since inventory is measured at selling price in the cash conversion cycle and the cash freed is the revenue tied up in the goods held.
- No cash effect, since inventory is carried at cost and a cut in days only changes the ratio of inventory to $COGS$, which rearranges the balance sheet without changing the cash balance.
- A one-time release of about $k \cdot COGS/365$ as stock falls to its new level; the lasting gain is only the yearly carrying cost saved on that amount, not a new release each year.
<!-- YW5zOjM= -->
> Inventory is a stock: cutting days lowers its level once, by $k$ days of COGS, and the cash comes in while the stock runs down. Afterwards the firm saves the cost of carrying that amount (financing, storage, obsolescence) every year. Treating the release as an annual flow, or valuing inventory at selling price, are the two common errors.
> Ref: Berk *Fundamentals* Ch. 19 §19.5 (p. 580); Ross *Fundamentos* Cap. 20 (inventory management)
> Similar: Lista R5b, Ex. 5 (Happy Valley Homecare); Lista R5b, Ex. 6(c)

## fin

Q: A seasonal manufacturer considers switching to level production: it would produce the same quantity every quarter, build up finished-goods inventory before the selling season, and lower its unit production cost. Which assessment is right?
- It needs no extra financing: annual production and sales are unchanged, so the pro forma for the year shows the same external financing whether production is level or follows the season.
- It should be financed with long-term debt or equity: level production is a permanent change of policy, so the matching principle treats the inventory it creates as a permanent current asset.
- The build-up is a temporary, self-liquidating need suited to a seasonal secured line, but lenders haircut stock that may go obsolete, so the cost saving must beat bigger, earlier borrowing.
- It lowers external financing: higher margins raise retained earnings in every quarter, and the extra profit more than covers the inventory build-up, so the quarterly need for outside funds falls.
<!-- YW5zOjI= -->
> Level production front-loads inventory: the need peaks before the season and unwinds as goods are sold and collected, which is the textbook case for short-term, asset-backed seasonal credit under the matching principle. The catch is the collateral: unsold seasonal goods may be worth little, so the lender limits the line and the firm bears the obsolescence risk. The margin gain is small relative to the build-up.
> Ref: Higgins 13e Ch. 3 §3.1.3 (p. 86); Berk *Fundamentals* Ch. 20 §20.2 (p. 598) and §20.5 (p. 606)
> Similar: Lista R5b, Ex. 15 (Toys-4-Kids, seasonal vs. level production); Lista R5b, Ex. 11

Q: Banks ration a manufacturer's credit, yet its suppliers keep selling to it on 60-day terms. Which explanation fits the theory and evidence on trade credit, including Giannetti, Burkart and Ellingsen (2011)?
- Inputs are harder to divert than cash, above all services and differentiated goods worth little to anyone else, and suppliers learn about buyers through trade; both make the credit enforceable.
- Suppliers have a lower cost of capital than banks, since they finance receivables out of their own trade payables, so they can lend at a lower rate and still break even on buyers that banks reject.
- Trade credit is senior to bank debt in bankruptcy, since unpaid suppliers can reclaim all goods delivered, so suppliers bear little default risk and lend freely where banks, being junior, refuse.
- Suppliers lend because trade credit is interest-free, so buyers always prefer it to bank credit, and suppliers accept the cost as a marketing expense that is recovered through higher list prices.
<!-- YW5zOjA= -->
> Credit in kind is harder to misuse than cash: a buyer can divert money but not easily resell a custom part or a service, so less of the loan is at risk of diversion. Suppliers also see orders and payments in the normal course of business and have a stake in a buyer that is hard to replace. Giannetti, Burkart and Ellingsen find more trade credit where goods are differentiated or are services. Trade creditors are usually unsecured, and forgone discounts make trade credit far from free.
> Ref: Giannetti, Burkart and Ellingsen (2011), *Review of Financial Studies* 24(4):1261–1298 (syllabus item 5); Berk *Fundamentals* Ch. 19 §19.2 (p. 570); Topic 4A slides 2–7 (credit rationing)
> Similar: Lista R5b, Ex. 12 (supplier credit and leverage); no list exercise covers the paper itself

Q: A firm plans a debt-financed share repurchase for its interest tax shield. Its suppliers threaten to withdraw their net-30 terms if it goes ahead. How does the static trade-off read this threat?
- As irrelevant to the decision: trade credit is an operating item, not a financing source, so it belongs in working capital and has no bearing on the capital structure choice that the repurchase makes.
- As a pure transfer: whatever the suppliers stop lending, the firm borrows elsewhere at the same rate, so by MM the value of the firm is unchanged and only the tax shield matters for the choice.
- As an indirect cost of distress: suppliers facing more default risk shorten credit, so cheap trade credit must be replaced by costlier funds; this, and similar reactions, offset the shield.
- As a direct bankruptcy cost: suppliers' claims are senior to the new debt, so their withdrawal raises the legal costs of a future reorganisation, which is the cost the tax shield must exceed.
<!-- YW5zOjI= -->
> Suppliers are creditors and stakeholders who bear costs if the firm fails; more leverage makes them cut credit before any default. Losing that credit raises the firm's cost of funds, an ex ante (indirect) cost of distress in the trade-off, alongside customers and workers who react the same way. The decision compares the shield with the after-tax cost of replacing the credit and those wider reactions.
> Ref: Topic 2B slides 38 and 41–45 (indirect costs: credit from suppliers; trade-off); Grinblatt–Titman Ch. 17 (exercise 17.5, p. 619)
> Similar: Lista R5b, Ex. 12 (BCD Manufacturing: debt tax shield vs. lost supplier credit)
