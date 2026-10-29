---
tags: [notes, lecture-03, capital-structure, bankruptcy-costs, financial-distress, agency]
date: 2026-10-24
status: taught
source: "Aula/Topic2B.pdf slides 33–40 (blocks 2B.5–2B.6), incl. the Jagannathan et al. (2017) Table 5 (slide 34) and Graham et al. (2015) figure (slide 35); Ross Fundamentos 9e §16.4–16.5 pp. 553–558, Table 16.7 p. 567, §16.10 pp. 567–568; Berk Fundamentals 2e §16.4 pp. 479–480; Higgins 13e Ch. 6 'Distress Costs' pp. 208–213; Amaro de Matos §2.1.4 pp. 46–47, §2.2 p. 48"
---

# 2B.5–2B.6 · The 100%-debt puzzle and the costs of financial distress

> **Claim.** MM with taxes says every unit of debt adds $\tau$ to value, so the optimum is all debt
> — and no industry is near it (slide 34: debt is 12–44% of value). The missing piece is **not**
> default itself: handing the firm to creditors is just a change of owner and costs nothing in MM.
> **It is the deadweight costs that default brings** — direct (lawyers, managers' time, fire
> sales) and indirect (lost customers, suppliers, workers, and conflicts that distort investment)
> — and these can offset the tax advantage.

Prev: [[L03-02-after-tax-wacc-apv]] · Next: [[L03-04-static-trade-off]] · Map: [[L03-00-map]]

**Notation.** $V_U$, $V_L$, $\tau$, $D$ as in [[L03-01-tax-shield-mm-taxes]]; $K$ the promised debt
repayment; $X$ the cash flow at maturity; $C$ the deadweight cost of default.

---

## 1 · C — the puzzle in one line (slide 33)

An unlevered firm issues debt $D$, fixed in perpetuity, to repurchase equity, with $\tau=35\%$. By
MM I with taxes ([[L03-01-tax-shield-mm-taxes]] (8), (5)):

$$V_L=V_U+0.35D \tag{1}$$

Divide by $V_U$:

$$\frac{V_L}{V_U}=1+0.35\frac{D}{V_U} \tag{2}$$

| $D/V_U$ | $V_L/V_U$ | value gain |
|---|---|---|
| 20% | $1+0.35\times0.20=1.07$ | **+7%** |
| 50% | $1+0.35\times0.50=1.175$ | **+17.5%** |
| 100% | $1.35$ | +35% |

(2) is increasing in $D$ without bound: *"it seems that the optimal capital structure is attained
with 100% debt. Obviously this is not true"* (slide 33). Ross reaches the same "conclusão
ilógica" (p. 553); Berk asks *"why don't firms use debt financing almost exclusively?"* (p. 478);
Amaro (§2.1.4, p. 47): *"In reality, firms are never fully financed with debt."*

## 2 · U — what firms actually do (slides 34–35)

**Slide 34 — Jagannathan et al. (2017), Table 5, WACC by Fama–French industry, 2016** (selected
columns, read off the slide):

| Industry | $\beta_S$ | $T_C$ (%) | $E[R_S]$ (%) | $E[R_D]$ (%) | $D/(D+S)$ | WACC (%) |
|---|---|---|---|---|---|---|
| Durable | 1.42 | 30.71 | 11.74 | 4.61 | **0.44** | 8.02 |
| High-tech | 0.98 | 20.60 | 8.87 | 4.22 | **0.12** | 8.21 |
| Health | 0.74 | 18.35 | 7.28 | 4.28 | 0.15 | 6.66 |
| Utilities | 0.53 | 32.32 | 5.93 | 4.61 | **0.41** | 4.69 |
| Telecom | 0.68 | 35.69 | 6.90 | 4.55 | 0.27 | 5.86 |

**Recompute one row with (1) of note 02** (Utilities):
$0.59\times5.93\%+0.41\times4.61\%\times(1-0.3232)=3.499\%+1.279\%=4.78\%$ against the printed 4.69% —
the table averages firm-level WACCs (market-cap weighted), so the industry averages of the inputs
do not reproduce it exactly. **The reading that matters: even the most levered industry sits at
44% debt, the tech industry at 12%.**

**Ross Table 16.7 (p. 567, Ibbotson 2008, debt/total capital):** pharmaceuticals 6.76%, computers
5.31%, steel 28.57%, airlines 56.30%, cable TV 61.84%, electric utilities 49.40%.

**Slide 35 — Graham, Leary and Roberts (2015).** US corporate leverage 1920–2010: book debt +
preferred over capital roughly 20–50%, market leverage roughly 10–35% (read off the figure),
rising sharply after the 1960s. **A century of data, and never near 100%.**

> **Two facts for any theory to fit (Berk p. 482):** firms choose debt "too low to fully exploit
> the interest tax shield", and leverage differs systematically **across industries** — low in
> tech and pharma, high in utilities and cable.

---

## 3 · C — default is not the cost (slide 36)

*"A bankruptcy process transfers ownership to debtholders. This transfer of control is not a
violation of MM per se. The violation comes from bankruptcy costs."*

**Why the transfer is free.** In the MM world of Topic 2A, debt is a claim $\min(X,K)$ and equity
$\max(X-K,0)$ ([[../L02/L02-06-mm1-arbitrage-put-call|L02 risky debt and equity as a call]]). They
always sum to $X$: in default creditors simply receive all of $X$. Nothing is lost, so $V$ does not
depend on $K$. Ross (p. 556): *"Em uma situação de mercados perfeitos, não há custos associados a
essa transferência de propriedade, e os credores nada perderiam."*

**With a deadweight cost $C$ in default**, the claims sum to $X-C$ in default states and to $X$
otherwise. The expected loss $C\times\Pr(X<K)$ grows with $K$: **that** is what can "countervail
the tax advantage of debt financing" (slide 36) — made exact in [[L03-04-static-trade-off]] (7).

## 4 · C — direct costs (slide 37)

*Ex post*, conditional on actual liquidation or reorganization:

- legal and administrative costs;
- time and resources of managers and creditors dealing with the bankruptcy;
- fire sales of assets, due to asset specificity and illiquid assets.

**Magnitudes.** Berk (p. 479): direct costs "approximately 3% to 4% of the pre-bankruptcy market
value of total assets", higher for smaller and more complex firms; Enron's fees exceeded 750 million.
Ross (p. 557): Enron spent more than 1 billion on lawyers, accountants and consultants; WorldCom 600
million. Amaro (p. 48), citing Warner (1977) on 11 railroads: about **5.3 cents per dollar**, with a
strong inverse size effect — 1.7% for the largest. **Small relative to a 35% tax rate** — which is
why the indirect costs carry the argument.

**What a bankruptcy cost is not** (Higgins p. 210): ACE's apartment complex lost value through
local overbuilding; that loss happens whatever the financing, so it is *not* a bankruptcy cost. The
cost is only what bankruptcy itself adds — high when assets have low **resale value** (Moletek,
a genetic-engineering firm whose assets are a research team and growth options), low for
redeployable, tangible assets (pp. 210–211).

## 5 · C — indirect costs (slides 38–40)

*Ex ante*: incurred **before** any filing, as the probability of distress rises.

| Channel | Mechanism | Evidence on the slides |
|---|---|---|
| **Customers** | demand falls where the product needs the firm to survive — airlines (frequent-flier programs), autos (warranties, parts, service) | Hortaçsu et al. (2013): a rise in a manufacturer's CDS lowers its used-car auction prices, more so for longer-lived cars |
| **Suppliers and banks** | credit from suppliers and banks dries up (credit-market imperfections) | — |
| **Workers** | risk-averse workers want stable jobs and avoid unemployment scarring | Brown & Matsa (2016): fewer applications per opening in distress; Baghai et al. (2021): firms lose the most skilled workers near bankruptcy, and talent-dependent firms choose more conservative capital structures; Van Doornik et al. (2022): more generous UI shifts labour supply to riskier firms and shrinks the wage premium they must pay |
| **Equity–debt conflicts** | poor investment decisions: **debt overhang** (underinvestment), **asset substitution / risk-shifting** (excessive risk), **cashing out** (withdrawing cash ahead of senior claimants) | — |

Berk (p. 480) adds fire sales and puts the total at **10–20% of firm value** (Andrade and Kaplan's
highly levered firms); Higgins (p. 211) stresses that indirect costs feed on one another —
cut-backs in R&D and marketing, lost sales, nervous suppliers, competitors who "smell blood".

### 5.1 · U — the two investment distortions, in numbers (own illustration)

*The slides name these conflicts; their formal treatment is the agency-cost topic (syllabus item 4,
Tirole Ch. 3). The numbers below are an own illustration, risk-neutral investors, $r_f=0$, no taxes.*

**Risk-shifting.** Debt promises $K=100$. The firm can keep a safe asset paying 90, or switch to a
gamble paying 160 or 0 with probability 1/2 each (mean 80, **worse by 10**).

| | Safe (90) | Gamble (160 / 0) |
|---|---|---|
| Equity $E[\max(X-100,0)]$ | $\max(90-100,0)=0$ | $\tfrac12(60)+\tfrac12(0)=30$ |
| Debt $E[\min(X,100)]$ | 90 | $\tfrac12(100)+\tfrac12(0)=50$ |
| Total | 90 | 80 |

Shareholders gain 30 by destroying 10 of value — creditors lose 40. Equity is a call option on the
assets, and a call gains from volatility (Higgins p. 212's "go-for-broke" problem).

**Debt overhang.** Same $K=100$; assets in place pay 60 or 120 (prob. 1/2). A new project costs 20
today and pays 30 for sure (NPV +10), financed by the shareholders.

| | Without project | With project (assets pay 90 / 150) |
|---|---|---|
| Equity | $\tfrac12(0)+\tfrac12(20)=10$ | $\tfrac12(0)+\tfrac12(50)=25$ |
| Debt | $\tfrac12(60)+\tfrac12(100)=80$ | $\tfrac12(90)+\tfrac12(100)=95$ |

Shareholders put in 20 to raise their claim by $25-10=15$: they **reject** a project with NPV +10,
because 15 of its 30 goes to creditors (Higgins p. 212, *"debt overhang"*).

> **These are costs of debt even if no court is ever involved**: creditors anticipate the
> distortion and price it into the debt, so shareholders bear it ex ante (Ross p. 557–558: *"o
> efeito líquido é a perda de valor, porque a empresa optou por usar dívida"*).

## 6 · C — the logic that the trade-off model formalizes

| Force | Grows with leverage because | Direction |
|---|---|---|
| Tax shield | more interest deducted | **more debt** |
| Expected distress cost | probability of default × cost if it happens (Higgins p. 209: "the probability bankruptcy will occur times the costs incurred when it does") | **less debt** |

Higgins's checklist (p. 213) is the whole model in words: (1) the firm's **ability to use** the
extra shields, (2) the **increased probability** of distress, (3) the **magnitude** of distress costs.
In [[L03-04-static-trade-off]] these become $1-H(K)$, $h(K)$ and $C$ in one first-order condition.

## 7 · G — Miller's objection and DeAngelo–Masulis (Amaro §2.2, pp. 48, 54–55; named, not examinable)

Miller (1977) argued that bankruptcy costs are **too small** to balance a 48-cent tax gain per
dollar (the 20% figure people cited applied to individuals; Warner found 5.3%), and proposed
personal taxes instead ([[L03-01-tax-shield-mm-taxes]] §10). DeAngelo and Masulis (1980) restore an
interior optimum from the **supply** side: with uncertain earnings, more borrowing raises the
chance that **some shields go unused**, so the effective $\tau_c$ falls with debt; add
leverage-related deadweight costs $d(B)$ and the supply curve of corporate bonds slopes down
(pp. 55–56). The slides' model has the first effect built in: no tax is paid in default, so an
extra unit of $K$ saves tax only with probability $1-H(K)$.

---

## Links

- Before: [[L03-01-tax-shield-mm-taxes]], [[L03-02-after-tax-wacc-apv]]. Next: [[L03-04-static-trade-off]].
- Topic 2A: [[../L02/L02-06-mm1-arbitrage-put-call|L02 MM I, risky debt, equity as a call]].
- Forward: debt overhang and risk-shifting are the agency frictions of syllabus item 4
  ([[../../Map/lectures-index|lectures-index]], "Bridges forward").
- Bankruptcy procedure (named only): Ross §16.10, pp. 567–568 (liquidation vs. reorganization,
  absolute priority rule).
- Practice: PS2 Ex. 3(c) ([PS2](../../Listas/PS2.pdf), p. 2: a direct cost of 7% of the realized cash
  flow — who bears it); [[../../Listas/lista-r3-mm-taxes-tradeoff|Lista R3]] Ex. 8 (Berk 16.22,
  p. 494), Ex. 10 (Grinblatt–Titman 16.2, pp. 591–592); quiz block `dist` of
  [[../../Simulados/quiz-topic2b-taxes-tradeoff-2026-10-24|quiz Topic 2B]].
