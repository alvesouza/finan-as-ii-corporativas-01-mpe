---
tags: [aula-01, notes, topic-1]
date: 2026-10-09
---

# Class 1 — What Is Corporate Finance? Introduction and Stylized Facts

**Readings.** Before: Tirole, Introduction (pp. 1–12); Ch. 1 §1.1–1.2 (pp. 15–28).
After: Ch. 2 §2.2 (pp. 77–80) and §2.5–2.6 (pp. 95–102); opening of §3.2 (pp. 115–118).
Complementary: Ross *Fundamentos* Cap. 1; Higgins Ch. 4 §New Equity Financing.
Pages are printed pages (PDF = printed + 13). Rules: [[rules/01_introducao_fatos|Topic 1]].
Video: `Videos/aula-01-what-is-corporate-finance/`. **Interactive companion:**
`Videos/aula-01-what-is-corporate-finance/companion.html` (see §5).

> **Thesis of the class.** Modigliani and Miller show that how the pie is carved cannot change
> its size. Corporate finance exists because, once the people who run a firm are not the people
> who fund it, the carving *does* change the size, and a positive-NPV project can go unfunded.

---

## 1. What the field studies (Introduction, pp. 1–2)

- **Two sides of the firm.** *Insiders* (entrepreneur, managers) run it; *outsiders*
  (shareholders, banks, bondholders) fund it. Money flows in; claims on future income flow out.
- **Why Arrow–Debreu is not enough.** It prices claims under complete contracts but "said little
  about the firms' financial choices and about their governance": if every action is in the
  contract, there is nothing to govern.
- **A principal–agent problem.** Outsiders are the principal, insiders the agent. Three
  asymmetries, sorted by timing:

| Asymmetry | When | What the insider knows or does |
|---|---|---|
| Adverse selection | before the contract | quality of technology, riskiness of the market |
| Hidden knowledge | after the outcome | how much income was actually earned |
| Moral hazard | in between | effort, project choice, risk taken (unobserved) |

Moral hazard is the one used in §4 below.

## 2. Corporate governance (Ch. 1 §1.1–1.2, pp. 15–28)

### 2.1 Separation of ownership and control
- Berle and Means (1932): dispersed ownership "creates substantial managerial discretion, which
  can be abused". Monitoring is a public good among small shareholders, so it is under-supplied.
- **Definition used in the course** (Shleifer–Vishny, p. 15): governance is the set of ways in
  which suppliers of finance "assure themselves of getting a return on their investment". It is
  written from the outsiders' side.
- Two shapes of the agency problem (p. 15): **dispersed owners vs. manager** (frequent in
  Anglo-Saxon countries) and **controlling shareholder vs. minority** (typical of continental
  Europe). In the second, the question is who monitors the controller.

### 2.2 "Moral hazard comes in many guises" (§1.1.1, pp. 16–17)

| Guise | Examples in Tirole |
|---|---|
| Insufficient effort | avoiding cost-cutting, hard bargaining, firing friends; too many outside boards |
| Extravagant investments | empire building; Jensen on late-1970s oil exploration when buying oil was cheaper |
| Entrenchment | indispensability investments; gambling for resurrection; resisting takeovers |
| Self-dealing | perks (RJR Nabisco: 10 aircraft, 36 pilots); theft (Maxwell pension fund; Tyco, > 100 million dollars) |

Common thread: an action **that cannot be written into a contract** and that shrinks what is
left for outsiders.

### 2.3 Evidence of dysfunctional governance (pp. 17–20)
- US large-firm CEO pay roughly tripled in real terms 1980–94 and doubled again by 2001; 531× the
  average worker's wage in 2000 vs. 42× in 1982.
- Bertrand–Mullainathan: pay as sensitive to a "lucky dollar" as to a general dollar; a large
  shareholder on the board cuts pay-for-luck by 23–33%.
- WorldCom's profits overstated by 7.1 billion dollars.
- **The iceberg.** Observed scandals are the tip; below are "the averted ones" (covenants, boards,
  auditors, lenders who refuse). Few scandals can mean good governance or little outside finance.

### 2.4 Instruments (§1.2, pp. 20–28)
1. **Monetary compensation**: salary, bonus, shares, stock options. Jensen–Murphy (p. 24): median
   CEO of the 250 largest US firms held 0.25% of shares; a 1,000-dollar rise in shareholder wealth
   moves the CEO's pocket by **3.25 dollars**. The grocer who keeps 0.3 cents per dollar "would
   start eating the apples". Hall–Liebman, counting options properly: mean 25, median 5.30 per
   1,000. Too large a stake makes a risk-averse manager refuse good risky projects.
   - Share pays $P$; option with strike $P_S$ pays $\max(0,P-P_S)$. Options give stronger
     incentives per unit of cost near the top, but under-water options invite gambling, and
     boards reprice them (Ascend Communications).
2. **Implicit incentives**: dismissal, takeover, bankruptcy. Gilson: 52% of financially
   distressed firms replace senior management vs. 19% with equally poor stock returns but no distress.
3. **Monitoring**: *active* (forward-looking, uses control rights: board, bank, large
   shareholder) vs. *speculative* (backward-looking, through prices and exit: analysts, rating
   agencies, short-term lenders). Monitors have their own conflicts (auditors' non-audit fees).
4. **Product-market competition**: a yardstick, but it "will never substitute for a proper
   governance structure".

## 3. The benchmark: Modigliani–Miller (§2.2, pp. 77–79)

**Claim.** Under MM's conditions, total firm value is independent of the financial structure:
debt level, seniority, dividends. "Decisions concerning the financial structure affect only how
the 'corporate pie' … is shared, but has no effect on the total size of the pie."

### 3.1 Value additivity (p. 78)
Debt with face value $D$, risk-neutral investors, random income $R\ge0$.
Equity pays $\max(0,R-D)$; debt pays $\min(R,D)$. Case split:

$$
R\ge D:\ (R-D)+D=R,\qquad R<D:\ 0+R=R.
$$

So $\max(0,R-D)+\min(R,D)=R$ state by state, and taking expectations

$$
V_E+V_D=\mathbb E[\max(0,R-D)]+\mathbb E[\min(R,D)]=\mathbb E[R],
$$

independent of $D$. *Example:* $R\in\{0,200\}$ with probability $1/2$ each. $D=80$: $V_D=40$,
$V_E=60$. $D=150$: $V_D=75$, $V_E=25$. Total 100 in both.

### 3.2 Payout irrelevance (p. 78)
All-equity firm; dates $t=0,1,\dots$; revenue $R_t$, per-share dividend $d_t$, shares $n_t$,
investment $I_t$, end-of-period price $P_t$, discount factor $\beta$.

$$
\text{Arbitrage: } P_t=\beta\,\mathbb E[d_{t+1}+P_{t+1}],\qquad
\text{Cash identity: } R_t+P_t(n_t-n_{t-1})=n_{t-1}d_t+I_t .
$$

Then, using the identity at $t+1$ to replace $n_t d_{t+1}$:

$$
\begin{aligned}
V_t\equiv n_tP_t&=\beta\,\mathbb E[n_td_{t+1}+n_tP_{t+1}]\\
&=\beta\,\mathbb E[R_{t+1}-I_{t+1}+(n_{t+1}-n_t)P_{t+1}+n_tP_{t+1}]\\
&=\beta\,\mathbb E[R_{t+1}-I_{t+1}+V_{t+1}]
=\mathbb E\Big[\sum_{\tau\ge1}\beta^\tau(R_{t+\tau}-I_{t+\tau})\Big].
\end{aligned}
$$

Value depends only on real characteristics (income and investment), not on dividends or issues.

### 3.3 Where it breaks (p. 79)
"Whenever managerial decisions cannot be perfectly specified contractually, the incentives given
to those who pick those decisions affect the firm's income (the size of the pie) and therefore
the split of the pie matters." Full MM (MM2, taxes, default costs) is Topic 3 (Classes 4–5).

## 4. Stylized facts MM has to face (§2.5, pp. 95–102)

**Internal finance dominates** — Table 2.2 (Mayer 1990), % of total financing, 1970–85, p. 96:

| | U.S. | U.K. | Germany | Japan | France |
|---|---|---|---|---|---|
| Retentions | 66.9 | 72.0 | 55.2 | 33.7 | 44.1 |
| Loans | 23.1 | 21.4 | 21.1 | 40.7 | 41.5 |
| Bonds | 9.7 | 0.8 | 0.7 | 3.1 | 2.3 |
| Shares | 0.8 | 4.9 | 2.1 | 3.5 | 10.6 |

Tirole's three conclusions: retentions dominate everywhere; bank loans are the bulk of external
finance; bond markets matter little outside North America.

**Net equity is small or negative** (p. 97). Rajan–Zingales, US 1984–86: new issues 65% of
external financing, buybacks 68% — "basically all external financing was debt". Equity share of
gross fixed-capital formation in 1999: US 12, UK 9, France 9, Japan 8, Germany 6 (%).
Caveat: retentions are also shareholders' money; the puzzle is why leaving profits in is so much
easier than buying new shares (Classes 11–12).

**Leverage** — Table 2.4 (White 1991), US 1985, p. 98:

| | Equity / (debt + equity) | Debt / equity |
|---|---|---|
| All industries | 0.32 | 2.11 |
| Manufacturing | 0.45 | 1.20 |
| Wholesale and retail trade | 0.29 | 2.49 |
| Services | 0.31 | 2.25 |
| Commercial banks | 0.08 | 11.00 |

High debt goes with steady cash flow and redeployable (resaleable) assets; low debt with risk,
little cash flow, and intangible value.

**Banks vs. markets** — Table 2.5 (p. 99), liabilities of non-financial firms, 2002: bonds 15.6%
in the US vs. 2.3% in Germany and Italy; loans 10% in the US vs. 43% in Germany and 39.5% in
Japan. Market-based vs. bank-based systems; relevant for active vs. speculative monitoring.

**Announcement effects** — Table 2.6 (Eckbo–Masulis 1995), 2-day abnormal return, US
industrials, p. 101: common stock **−3.1%**, convertible bonds **−2.0%**, straight bonds −0.3%
(not significant). Bank loan announcements: positive. Under MM these should all be zero.

**Timing** (p. 101): bank finance is countercyclical; strong firms lend to weak ones in
recessions; small, bank-dependent firms are hit harder; equity issues cluster in upswings and
after price run-ups (market timing).

**Map to the course** (§2.6, p. 102): "information and incentives in general, and … capital,
liquidity, value of collateral, and external monitoring more specifically".

| Fact | Explained in |
|---|---|
| Retentions and bank debt, little equity | agency costs, borrowing capacity (Classes 6–8) |
| Leverage tracks steady cash flow and collateral | pledgeable income, collateral (Class 7) |
| Equity issues lower the price; loans raise it | asymmetric information (11–12); monitoring (13) |
| Bank- vs. market-based systems | active vs. speculative monitoring (13) |
| Cyclicality; the small hit hardest | liquidity (9–10); macro implications (15–16) |

## 5. The resolution in one model (§3.2, pp. 115–118)

Holmström–Tirole fixed-investment model. Units: thousand reais. Calibration from the video
(verified in `check_numbers.py`):

| $I$ | $A$ | $R$ | $p_H$ | $p_L$ | $B$ |
|---|---|---|---|---|---|
| 100 | 10 | 160 | 0.8 | 0.4 | 20 |

**Setup.** The entrepreneur has net worth $A<I$ and borrows $I-A$. Success yields verifiable $R$,
failure 0. Behave: probability $p_H$, no private benefit. Shirk: $p_L<p_H$, private benefit $B$.
Everyone risk neutral, interest rate 0, limited liability, competitive lenders. Contract: $R_b$
to the borrower and $R_l=R-R_b$ to lenders on success; 0 to both on failure.

**Assumptions.**

$$
p_HR-I>0 \quad(3.1)\qquad\qquad p_LR-I+B<0 \quad(3.2)
$$

Check: $128-100=28>0$; $64-100+20=-16<0$.

**Step 1 — incentive compatibility.**

$$
p_HR_b\ge p_LR_b+B\iff (\Delta p)R_b\ge B \quad(\mathrm{IC}_b),\qquad \Delta p\equiv p_H-p_L .
$$

Minimum stake $B/\Delta p=20/0.4=50$.

**Step 2 — pledgeable income.** The most that can be promised on success is $R-B/\Delta p=110$, so

$$
\mathcal P=p_H\Big(R-\frac{B}{\Delta p}\Big)=0.8\times110=88 .
$$

**Step 3 — breakeven and the threshold.** Lenders need $\mathcal P\ge I-A=90$ $(\mathrm{IR}_l)$:

$$
A\ \ge\ \bar A=p_H\frac{B}{\Delta p}-(p_HR-I)=40-28=12 \quad(3.3).
$$

$p_HB/\Delta p$ is the **agency rent** (40). Our founder has $A=10<12$: **rationed by 2**,
although NPV is $+28$. Equivalently $\mathcal P-(I-A)=88-90=-2=A-\bar A$. "One only lends to the rich."

**Step 4 — when funded.** $p_HR_l=I-A$, so $1+\iota=1/p_H$: the nominal rate is a pure default
premium. Borrower's net utility

$$
U_b=\begin{cases}0 & A<\bar A\\ p_HR-I & A\ge\bar A\end{cases}\quad(3.6)
$$

— a jump at $\bar A$. *Richer founder,* $A=20$: $R_l=80/0.8=100$, $R_b=60\ge50$, $U_b=28$.

**Comparative statics** (p. 118). Credit rationing comes from low $A$ or high agency cost
($B$ and the likelihood ratio $\Delta p/p_H$):

| Parameter ↑ | $\partial\bar A/\partial\cdot$ | at calibration | Effect on funding |
|---|---|---|---|
| $B$ | $p_H/\Delta p$ | $+2$ | harder |
| $p_L$ | $p_HB/\Delta p^2$ | $+100$ ($+1$ per 0.01) | harder |
| $I$ | $1$ | $+1$ | harder |
| $R$ | $-p_H$ | $-0.8$ | easier |
| $p_H$ | $-R-p_LB/\Delta p^2$ | $-210$ ($-2.1$ per 0.01) | easier |

**MM recovered.** Set $B=0$: behaviour is in effect contractible, $\bar A=-(p_HR-I)=-28<0$, and
every positive-NPV project is funded whatever $A$. One assumption separates the two worlds.

> **Companion.** `companion.html` puts all six parameters on sliders, draws $U_b(A)$ with $\bar A$
> marked, compares $\mathcal P$ with $I-A$, and splits $R$ into what can be promised and what the
> founder must keep. Try: $B\to0$; $B=15$ (then $\bar A=2$, funded); raise $p_L$ toward $p_H$.

## 6. Scope line
- Classes 4–5 own MM in full; Class 6 owns the fixed-investment model in full (§3.2.3 onward).
- Classes 11–12 explain the announcement effects; here they are facts only.
- No Brazilian numbers: none are in the course books.

## 7. Self-check
1. State the three asymmetries and give one example of each for a startup founder.
2. Show that $\max(0,R-D)+\min(R,D)=R$ and explain why this implies capital-structure irrelevance.
3. Derive $V_t=\mathbb E[\sum_{\tau\ge1}\beta^\tau(R_{t+\tau}-I_{t+\tau})]$ from the arbitrage and cash identities.
4. Which stylized facts contradict MM most directly, and why?
5. With the calibration above, find the largest $B$ at which $A=10$ is funded. *(Answer: $\bar A\le10\iff 2B-28\le10\iff B\le19$.)*
6. Why will a rationed borrower's offer of a higher interest rate be refused?

Practice: Tirole Ch. 3 exercises 3.1–3.3 (p. 144); Ross *Fundamentos* Cap. 1 conceptual questions.
