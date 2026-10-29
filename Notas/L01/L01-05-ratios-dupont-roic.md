---
tags: [notes, lecture-01, accounting, ratios, dupont, roe, roic, leverage]
date: 2026-10-24
status: taught
source: "Aula/Topic1.pdf slides 40–51 (block 1.7); Higgins 13e Ch. 2 'Return on Equity' and Table 2.1 (pp. 38–40), 'The Timing Problem', 'The Risk Problem' (p. 54), 'Return on Invested Capital' (pp. 55–56), 'The Value Problem' and P/E (pp. 56–57), Ch. 1 'Imputed Costs' (pp. 27–28); Berk 2e Ch. 2 §2.5, eqs. (2.17)–(2.19), Example 2.3, pp. 34–39; Ross Fundamentos Cap. 3 §3.4, eq. [3.24], p. 72"
---

# 1.7 · Income-statement analysis: margins, coverage, DuPont, ROE vs ROIC

> **Claim.** Every ratio here answers one narrow question, and most mix **operations** with
> **financing**. The DuPont identity splits ROE into margin × turnover × leverage, so ROE can rise
> purely because equity shrinks. ROIC strips the financing out. The exact bridge between the two is
> $\mathrm{ROE}=\mathrm{ROIC}+\frac{D}{E}\left[\mathrm{ROIC}-r_D(1-\tau)\right]$: leverage adds
> the **spread** times $D/E$, and it multiplies ROE's sensitivity to ROIC by $1+D/E$. That is why
> the slide's question "should managers maximize financial leverage?" has no accounting answer.

Prev: [[L01-04-income-statement]] · Next: [[L01-06-cash-flows-fcf]] · Map: [[L01-00-map]]

**Notation.**

| Symbol | Meaning | Range |
|---|---|---|
| $\text{NI}$, $S$ | net income, sales | real, $\ge0$ |
| $N$ | shares outstanding | $>0$ |
| $A$, $E$, $L$ | total assets, book equity, total liabilities | $A>0$, $E>0$ here |
| $D$ | interest-bearing debt | $\ge0$ |
| $r_D$ | interest rate on debt (interest $=r_DD$) | $\ge0$ |
| $\tau$ | tax rate on pre-tax income (full loss offset assumed in §8) | $[0,1)$ |
| $r_E$ | required return on equity (hurdle rate) | $>0$ |
| $\mathrm{ROIC}$ | return on invested capital, (5.16) | real |

---

## 1 · C — earnings per share, basic and diluted (slide 40)

$$\mathrm{EPS}=\frac{\text{NI}}{N} \tag{5.1}$$

$$\mathrm{EPS}^{\text{diluted}}=\frac{\text{NI}}{N+N^{\text{options}}+N^{\text{convertibles}}} \tag{5.2}$$

Stock options for employees and convertible bonds can raise the share count; that growth is
**dilution**. Diluted EPS assumes all options exercised and all convertibles converted (slide 40).
**Berk, Global 2010 (p. 34):** $\mathrm{EPS}=2.0/3.6=0.56$ per share.

---

## 2 · C — margins (slides 41, 43)

$$\text{Gross margin}=\frac{\text{Gross profit}}{S} \tag{5.3}$$

$$\text{Operating margin}=\frac{\text{Operating income}}{S} \tag{5.4}$$

$$\text{Net margin}=\frac{\text{NI}}{S} \tag{5.5}$$

| Margin | What it measures (slides 41, 43) | What else moves it |
|---|---|---|
| Gross (5.3) | selling for more than the **direct** cost; the contribution to fixed costs and profit | — |
| Operating (5.4) | selling for more than direct **and indirect** cost; efficiency of operations | **market power** (mark-ups) |
| Net (5.5) | share of each sales dollar left to shareholders after all expenses, interest and taxes | **capital structure** (interest) |

**GM 2020 (slide 39 numbers, note 04 §6):**

$$\text{gross}=\frac{13{,}672}{122{,}485}=11.16\%,\quad \text{operating}=\frac{6{,}634}{122{,}485}=5.42\%,\quad \text{net}=\frac{6{,}321}{122{,}485}=5.16\%$$

Berk (pp. 35–36) adds that operating margins differ by **strategy** as well as efficiency: in 2010
Wal-Mart's was 5.87% and Nordstrom's 9.67%, with Wal-Mart's sales more than 45 times Nordstrom's.

---

## 3 · C — economic earnings (slide 42)

"Does a positive net income imply that equityholders are properly compensated?" No. Owners earn an
economic profit only if their return beats the **required** return on equity, which covers the
time value of money and risk (slide 42). The accountant charges interest for debt and **nothing**
for equity. Charging equity at its hurdle rate:

$$\text{Economic earnings}=\text{NI}-r_E\,E \tag{5.6}$$

**Higgins, Polaris 2020 (pp. 27–28).** $\text{NI}=414$ million, $E=1{,}434$ million, and an illustrative
$r_E=10\%$. Substituting into (5.6):

$$414-0.10\times1{,}434=414-143.4=270.6\approx271\ \text{million}$$

(Higgins's table rounds the charge to 143.) "The accountant pretends equity is free."

---

## 4 · C — receivable and payable days (slide 44)

$$\text{AR days}=\frac{AR}{S/365} \tag{5.7}$$

$$\text{AP days}=\frac{AP}{\text{purchases}/365} \tag{5.8}$$

AR days measure how long customers take to pay. **Berk, Global 2010 (pp. 36–37).** Average daily
sales $186.7/365=0.5115$ million; substituting $AR=18.5$ into (5.7):

$$\frac{18.5}{0.5115}=36.2\approx36\ \text{days}$$

up from 27.5 days in 2009. Berk (p. 37) computes AP days with **cost of goods sold** in the
denominator when purchases are not reported. **State which denominator you use.**

---

## 5 · C — EBITDA and interest coverage (slide 45)

$$\mathrm{EBITDA}=\mathrm{EBIT}+\text{depreciation}+\text{amortization} \tag{5.9}$$

$$\text{Interest coverage}=\frac{\mathrm{EBIT}}{\text{interest expense}} \tag{5.10}$$

Depreciation and amortization (the depreciation of intangibles) are not cash expenses, so EBITDA is
"a better measure of the cash the firm obtains from its operations". Coverage measures the current
ability to pay interest (slide 45). Berk (p. 37) notes that operating income or EBITDA are also used
in the numerator of (5.10).

**GM 2020** (EBIT from slide 39; D&A 12,815 from the cash-flow statement, slide 58):

$$\mathrm{EBITDA}=9{,}193+12{,}815=22{,}008$$

$$\text{coverage}=\frac{9{,}193}{1{,}098}=8.37,\qquad \frac{\mathrm{EBITDA}}{\text{interest}}=\frac{22{,}008}{1{,}098}=20.04$$

> **Same leverage, different coverage:** coverage depends on profitability as well as debt. A low
> coverage ratio does not bar borrowing if large cash flows are expected later, as for start-ups and
> fast growers (slide 45). The same logic applies to negative book equity (note 03 §6).

---

## 6 · C — ROE, ROA, asset turnover and the DuPont identity (slides 46–48)

$$\mathrm{ROE}=\frac{\text{NI}}{E} \tag{5.11}$$

$$\mathrm{ROA}=\frac{\text{NI}}{A} \tag{5.12}$$

$$\text{Asset turnover}=\frac{S}{A} \tag{5.13}$$

ROE measures "the return the firm has earned on its past equity investments" and depends on capital
structure. Turnover measures how efficiently assets generate sales (slide 46).

**Deriving DuPont (Berk (2.17)–(2.18), p. 38).** Multiply (5.11) by $S/S=1$:

$$\mathrm{ROE}=\frac{\text{NI}}{S}\cdot\frac{S}{E}$$

Multiply the second factor by $A/A=1$:

$$\mathrm{ROE}=\frac{\text{NI}}{S}\cdot\frac{S}{A}\cdot\frac{A}{E}$$

$$\boxed{\;\mathrm{ROE}=\underbrace{\frac{\text{NI}}{S}}_{\text{net margin}}\times\underbrace{\frac{S}{A}}_{\text{turnover}}\times\underbrace{\frac{A}{E}}_{\text{financial leverage}}\;} \tag{5.14}$$

The first two factors are (5.12): $\frac{\text{NI}}{S}\cdot\frac{S}{A}=\frac{\text{NI}}{A}$, so

$$\mathrm{ROE}=\mathrm{ROA}\times\frac{A}{E}\qquad\text{and}\qquad \mathrm{ROA}=\text{margin}\times\text{turnover} \tag{5.15}$$

Why is $A/E$ "leverage"? Substitute $A=L+E$ from (1.1) (Higgins p. 39, fn. 1):

$$\frac{A}{E}=\frac{L+E}{E}=\frac{L}{E}+1$$

which rises one for one with the liabilities-to-equity ratio (3.4).

**Slide 48 (Higgins, 2013 data), each product recomputed:**

| Firm | Net margin | Turnover | Leverage | Product | Slide ROE |
|---|---|---|---|---|---|
| Google | 21.6% | 0.54 | 1.27 | $0.216\times0.54\times1.27=14.81\%$ | 14.80% |
| JPMorgan | 18.6% | 0.04 | 11.44 | $0.186\times0.04\times11.44=8.51\%$ | 8.50% |
| Hyundai Motor | 10.3% | 0.65 | 2.36 | $0.103\times0.65\times2.36=15.80\%$ | 15.90% |
| Chevron | 9.7% | 0.87 | 1.7 | $0.097\times0.87\times1.7=14.35\%$ | 14.40% |

(Hyundai's 0.1-point gap is rounding in the printed inputs.)

> **Many roads lead to the same ROE.** JPMorgan reaches 8.5% with a turnover of 0.04, which only
> leverage of 11.44 can offset. Google gets 14.8% with almost no leverage. "Net profit margin and
> asset turnover tend to vary inversely: companies that add a lot of value to a product and thus can
> charge higher prices usually require lots of assets" (slide 48; Higgins 13e p. 40). Higgins's
> explanation of why ROEs cluster while their parts do not is **competition**: unusually high ROEs
> attract entry (p. 39).

Two more textbook cases. **Berk, Example 2.3 (p. 39):** Wal-Mart $3.6\%\times2.4\times2.6=22.5\%$,
Nordstrom $7.7\%\times1.7\times2.4=31.4\%$; to match Nordstrom at its own turnover and leverage,
Wal-Mart needs a margin of $31.4\%/(2.4\times2.6)=31.4\%/6.24=5.0\%$. **Ross (p. 72):** Bank of
America 2008, ROA 0.53% and ROE about 5.75%, so an equity multiplier of 10.85.

![Two log-log panels. Left: net profit margin against asset turnover with straight iso-ROA lines for 1, 2, 5, 10 and 15 percent, the slide's four 2013 firms in blue and Higgins 13e's ten 2020 firms in grey. Right: ROA against financial leverage with iso-ROE lines for 5 to 30 percent; JPMorgan and Citigroup sit at leverage above 11 with ROA below 1 percent](figures/L01-dupont.png)

*Eq. (5.15) twice: the left panel multiplies margin by turnover, the right multiplies ROA by
leverage; on log axes every iso-line is a straight line of slope −1. Data: slide 48 (2013) and
Higgins 13e Table 2.1, p. 40 (2020).*

On the left, Google and Alphabet sit near the 10% ROA line through high margins, Kroger and Target
through high turnover, and the banks sit far below it. On the right, the banks climb back to ordinary
ROEs on leverage alone. Their low ROA, high leverage position is the "bank equity" problem of
[[../L03/L03-00-map|L03]] (block 2B.8).

---

## 7 · C — ROE as a performance measure: three problems (slide 49)

"Is a company with a high ROE better…? Not necessarily" (slide 49). Higgins's three problems
(pp. 54–57):

| Problem | Statement | Worked case |
|---|---|---|
| **Timing** | backward-looking, one year | an equity issue to fund a project lowers ROE until the project pays (slide 49); start-up costs of a new product (Higgins p. 54) |
| **Risk** | ignores the risk taken to earn it | Take-a-Risk: ROA 6% × leverage 5.0 = **30%**; Never-Dare: ROA 10% × leverage 2.0 = **20%**. Higgins prefers Never-Dare (pp. 54–55) |
| **Value** | return on **book**, not market, equity | Polaris: ROE $414/1{,}434=28.9\%$, but at the market price the return is $414/5{,}898=7.0\%$ (p. 56) |

Swapping in market equity gives the **earnings yield** (7.0% for Polaris), which has its own timing
problem: "a bright future, a high stock price, and a low earnings yield go together" (Higgins p. 57).

---

## 8 · C — ROIC and the exact leverage bridge (slide 50)

$$\mathrm{ROIC}=\frac{\mathrm{EBIT}(1-\tau)}{D+E} \tag{5.16}$$

This is also called return on net assets (RONA). The numerator is what the firm would earn after tax if
all-equity financed. The denominator is every source of capital "on which a return must be
earned". Accounts payable are excluded because "they carry no explicit cost" (Higgins p. 55).
**Higgins, Polaris 2020 (p. 55):** EBIT 588, tax rate $107/521=0.2054$, interest-bearing debt
$142+1{,}294$, equity 1,434:

$$\mathrm{ROIC}=\frac{588\times(1-0.2054)}{142+1{,}294+1{,}434}=\frac{467.2}{2{,}870}=16.3\%$$

**The two-firm example (slide 50, from Higgins).** Identical firms, A levered, B all equity:

| | Company A | Company B |
|---|---|---|
| Debt (10% interest) | 900 | 0 |
| Equity | 100 | 1000 |
| EBIT | 120 | 120 |
| Interest expense | 90 | 0 |
| Earnings before tax | 30 | 120 |
| Tax (40%) | 12 | 48 |
| Net income | 18 | 72 |
| ROE | $18/100=18\%$ | $72/1000=7.2\%$ |
| ROA | $18/1000=1.8\%$ | $72/1000=7.2\%$ |
| ROIC | $120\times0.6/1000=7.2\%$ | $120\times0.6/1000=7.2\%$ |

> **ROE rewards A's leverage, ROA punishes it, and only ROIC sees two identical businesses.**
> "ROIC thus reflects the company's fundamental earning power before it is confounded by
> differences in financing strategies" (Higgins p. 56).

**Deriving the bridge.** With interest $r_DD$, a proportional tax on pre-tax income, and no
nonoperating income, net income is

$$\text{NI}=(\mathrm{EBIT}-r_DD)(1-\tau) \tag{5.17}$$

Expand the product:

$$\text{NI}=\mathrm{EBIT}(1-\tau)-r_D(1-\tau)D \tag{5.18}$$

From (5.16), $\mathrm{EBIT}(1-\tau)=\mathrm{ROIC}\,(D+E)$. Substitute into (5.18):

$$\text{NI}=\left(\mathrm{ROIC}\,(D+E)\right)-r_D(1-\tau)D \tag{5.19}$$

Divide by $E$ and use (5.11):

$$\mathrm{ROE}=\mathrm{ROIC}\,\frac{D+E}{E}-r_D(1-\tau)\frac{D}{E}$$

Split $\frac{D+E}{E}=1+\frac DE$:

$$\mathrm{ROE}=\mathrm{ROIC}+\mathrm{ROIC}\,\frac{D}{E}-r_D(1-\tau)\frac{D}{E}$$

Collect the $D/E$ terms:

$$\boxed{\;\mathrm{ROE}=\mathrm{ROIC}+\frac{D}{E}\Big[\mathrm{ROIC}-r_D(1-\tau)\Big]\;} \tag{5.20}$$

**Check on Company A.** $\mathrm{ROIC}=0.072$, $r_D(1-\tau)=0.10\times0.60=0.060$, $D/E=900/100=9$.
Substituting into (5.20):

$$\mathrm{ROE}=0.072+9\times(0.072-0.060)=0.072+9\times0.012=0.072+0.108=0.180\quad\checkmark$$

**ROA under leverage.** In the example $A=D+E$. Divide (5.19) by $D+E$:

$$\mathrm{ROA}=\mathrm{ROIC}-\frac{D}{D+E}\,r_D(1-\tau) \tag{5.21}$$

For A: $0.072-0.9\times0.060=0.072-0.054=0.018$. ROA falls with **any** debt, whatever the spread.

**The same firms in Higgins 13e (pp. 55–56) use $\tau=25\%$:** $\mathrm{ROIC}=120\times0.75/1000=9.0\%$,
$r_D(1-\tau)=7.5\%$, and (5.20) gives

$$9.0\%+9\times(9.0\%-7.5\%)=9.0\%+13.5\%=22.5\%$$

which is Higgins's printed ROE for A (B: 9.0%).

> **Read (5.20).** The assumptions are (5.17): interest proportional to book debt, taxes
> proportional to pre-tax income, with a refund when it is negative, and no nonoperating items.
> - Leverage raises ROE **iff** the spread $\mathrm{ROIC}-r_D(1-\tau)$ is positive. At $r_D=12\%$
>   with $\tau=40\%$ the spread is zero and ROE stays at 7.2% for every $D/E$. At $r_D=14\%$ leverage
>   **lowers** ROE.
> - ROE is affine in $D/E$ with slope equal to the spread: a straight line through
>   $(0,\mathrm{ROIC})$.

![ROE against book D/E from 0 to 10 at a fixed ROIC of 7.2% for interest rates of 8, 10, 12 and 14 percent: four straight lines from the common point (0, 7.2%), rising for 8 and 10, flat for 12, falling for 14; Company A marked at D/E 9 with ROE 18% and Company B at D/E 0 with 7.2%; a dashed ROA curve falls to 1.8% at D/E 9](figures/L01-roe-leverage.png)

*Eq. (5.20) at $\mathrm{ROIC}=7.2\%$, $\tau=40\%$ (slide 50), for four values of $r_D$; ROA from
(5.21) at $r_D=10\%$.*

Every line starts at Company B, since at $D/E=0$ ROE is ROIC. The line through Company A has slope
1.2 points per unit of $D/E$, the spread. The flat line is the break-even rate $r_D=\mathrm{ROIC}/(1-\tau)=12\%$.
ROA, dashed, falls with leverage on every line.

> **Interactive companion.** [Leverage and ROE](companions/companion-leverage-roe.html): move the
> debt share from 0 to 0.90 and the interest rate across 12% and watch the ROE line rotate around
> ROIC. The presets load Company A, Company B, the flat case, Higgins 13e's 25% tax and a negative
> spread.

---

## 9 · C/G — "Should managers maximize financial leverage?" (slide 47)

DuPont (5.14) makes leverage look like a free lever. Three reasons it is not:

**(i) Leverage scales risk as well as return.** Rewrite (5.20) with ROIC collected:

$$\mathrm{ROE}=\left(1+\frac DE\right)\mathrm{ROIC}-\frac DE\,r_D(1-\tau)$$

Hold $D/E$ and $r_D$ fixed and let ROIC vary from year to year. Then $\Delta\mathrm{ROE}=(1+D/E)\,\Delta\mathrm{ROIC}$, so

$$\operatorname{sd}(\mathrm{ROE})=\left(1+\frac DE\right)\operatorname{sd}(\mathrm{ROIC}) \tag{5.22}$$

Company A's ROE is **ten times** as volatile as its ROIC. This is Higgins's risk problem (§7), made
exact.

**(ii) The required return rises too.** A higher expected ROE on a riskier equity claim is
compensation, not value. With frictionless markets the cost of equity rises one for one with this
leverage effect, and firm value does not change (MM II, [[../L02/L02-00-map|L02]] block 2A.9).
Higgins's footnote makes the same point from the investor's side: you can lever a safe firm's
return yourself with personal borrowing (p. 55, fn. 3), which is **homemade leverage**.

**(iii) Taxes and distress break the tie** in opposite directions: interest is deductible and
default is costly. The static trade-off is [[../L03/L03-00-map|L03]].

Berk adds a mechanical caveat (p. 38, fn. 7): raising leverage raises interest expense, which
**lowers the net margin** in (5.14). The DuPont factors are not independent levers.

---

## 10 · C — the price-earnings ratio (slide 51)

$$\frac{P}{E}\ \text{ratio}=\frac{E^{\text{mkt}}}{\text{NI}}=\frac{P}{\mathrm{EPS}} \tag{5.23}$$

This is Berk's (2.19), p. 39. **Better growth prospects raise P/E, more risk lowers it**. P/E varies
over time and across industries; a high P/E relative to industry peers *could* indicate
overvaluation; and P/E is influenced by leverage (slide 51).

**Berk, Global (p. 39):** $36/2.0=18$ on totals, or $10/0.56\approx18$ per share. **Higgins, Polaris
2020 (p. 57):** $95.28/6.69=14.2$. When earnings are temporarily depressed P/E rises: Polaris's
exceeded 45 in 2017 after earnings fell 19% (p. 57).

> **P/E depends on leverage because both its numerator and its denominator are equity measures.**
> The leverage-neutral alternatives use enterprise value (3.6) over EBIT or EBITDA (Berk pp. 39–40).
> How EPS and P/E respond to a debt-financed repurchase is PS2 Ex. 4, Topic 2A.

---

## Links

- Prev / next: [[L01-04-income-statement]] · [[L01-06-cash-flows-fcf]].
- The balance-sheet inputs: [[L01-02-balance-sheet-items]], [[L01-03-book-vs-market-leverage]].
- Forward: MM II and the cost of equity, [[../L02/L02-00-map|L02]] (blocks 2A.9–2A.10); bank capital
  and "ROE falls with equity", [[../L03/L03-00-map|L03]] (block 2B.8).
- Rules: [[../../rules/03_benchmark_mm|rules/03]] (MM benchmark).
- Practice: [Lista R1](../../Listas/lista-r1-accounting-capital-structure.md) Ex. 5 (Higgins 2.3,
  p. 71), Ex. 7 (Berk 2.27, p. 56: DuPont), **Ex. 8 (Higgins 2.7, p. 73: ROE, ROA, ROIC, the
  identity (5.20))**, Ex. 12 (Berk 2.19, p. 54), Ex. 13 (Berk 2.23, p. 55: EPS and dilution);
  solutions [PDF](../../Listas/lista-r1-accounting-capital-structure-solutions.pdf), checked by
  `Listas/lista-r1-accounting-capital-structure-solutions_check.py` (item 8 asserts (5.20));
  quiz [[../../Simulados/quiz-topic1-accounting-2026-10-24|Topic 1 quiz]] tag `is`.
- Books: Higgins 13e Ch. 2 (pp. 38–40, 54–58); Berk 2e §2.5 (pp. 34–40); Ross *Fundamentos*
  Cap. 3 §3.4 (pp. 71–72).
