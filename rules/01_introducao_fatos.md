# Topic 1 - Introduction and stylized facts

> **Class 1 (proposed, see Map/study-guide.md)** - Qual o objeto de estudo de finanças corporativas? Introdução e fatos estilizados
> **Tirole** - Introduction; Ch. 1 Corporate Governance; Ch. 2 Corporate Financing: Some Stylized Facts
> **Other refs** - Higgins Ch. 4 §New Equity Financing (equity-issuance trends); Ross Cap. 1 (Introdução às Finanças Corporativas)
> **Notes** - [Aula/aula-01-notes.md](../Aula/aula-01-notes.md) · companion `Videos/aula-01-what-is-corporate-finance/companion.html`

Pages are printed pages (PDF = printed + 13).

---

## Scope of corporate finance
- Insiders (entrepreneur, managers) vs. outsiders (investors): a principal–agent relation.
  Three asymmetries (Intro, pp. 1–2): adverse selection (before contract), hidden knowledge
  of realized income (after), moral hazard (in between).
- Corporate governance (Shleifer–Vishny, adopted p. 15): the ways in which suppliers of
  finance "assure themselves of getting a return on their investment".
- Moral hazard "comes in many guises" (§1.1.1, pp. 16–17): insufficient effort, extravagant
  investment, entrenchment, self-dealing.
- Instruments (§1.2): monetary pay, implicit incentives, monitoring (active / speculative),
  product-market competition. Jensen–Murphy: 3.25 dollars per 1,000 of shareholder value (p. 24).

## MM benchmark (Tirole p. 78; full treatment is Topic 3)
- Value additivity: $V_E+V_D=\mathbb E[\max(0,R-D)]+\mathbb E[\min(R,D)]=\mathbb E[R]$, independent of $D$.
- Payout irrelevance: $P_t=\beta\mathbb E[d_{t+1}+P_{t+1}]$, $R_t+P_t(n_t-n_{t-1})=n_{t-1}d_t+I_t$
  $\Rightarrow V_t=\mathbb E\big[\sum_{\tau\ge1}\beta^\tau(R_{t+\tau}-I_{t+\tau})\big]$.
- Breaks when decisions cannot be specified contractually: "the split of the pie matters" (p. 79).

## Stylized facts on corporate financing (§2.5, pp. 95–102)
- Retentions dominate; loans are the bulk of external finance; new shares small (Table 2.2, p. 96).
- US 1984–86: net equity issuance negative (p. 97). Equity share of fixed-capital formation 1999:
  US 12, UK 9, France 9, Japan 8, Germany 6 (%).
- Typical debt/equity ≈ 2; banks ≈ 11 (Table 2.4, p. 98). High leverage with steady cash flow
  and redeployable assets.
- Announcement returns: equity −3.1%, convertibles −2.0%, straight bonds −0.3% n.s. (Table 2.6, p. 101);
  bank loans positive.

## Fixed-investment model (preview of Topic 4; Tirole §3.2, pp. 115–118)
- Assumptions: $p_HR-I>0$ (3.1); $p_LR-I+B<0$ (3.2); $\Delta p\equiv p_H-p_L$.
- IC: $(\Delta p)R_b\ge B$. Pledgeable income $\mathcal P=p_H\left(R-\dfrac{B}{\Delta p}\right)$.
- Breakeven $\mathcal P\ge I-A$ $\iff$ $A\ge\bar A=p_H\dfrac{B}{\Delta p}-(p_HR-I)$ (3.3).
- Identity: $\mathcal P-(I-A)=A-\bar A$.
- Funded: $p_HR_l=I-A$, $1+\iota=1/p_H$; $U_b=p_HR-I$ if $A\ge\bar A$, else 0 (3.6).
- $B=0$ (contractible behaviour): $\bar A=-(p_HR-I)<0$, every positive-NPV project funded — MM.

### Signed comparative statics of $\bar A$ (higher $\bar A$ = harder to fund)

| Parameter ↑ | $\partial\bar A/\partial\cdot$ | Sign | Meaning |
|---|---|---|---|
| $B$ | $p_H/\Delta p$ | + | larger private benefit, more rationing |
| $p_L$ | $p_HB/\Delta p^2$ | + | outcome less informative about effort |
| $I$ | $1$ | + | bigger outlay |
| $R$ | $-p_H$ | − | more pledgeable income |
| $p_H$ | $-R-p_LB/\Delta p^2$ | − | higher NPV and better informativeness |

### Armadilhas frequentes
- Positive NPV does **not** imply funding; the test is pledgeable income vs. $I-A$, not NPV vs. 0.
- Agency rent $p_HB/\Delta p$ is an expected payoff; minimum stake $B/\Delta p$ is a payoff in success.
- The interest rate $1/p_H-1$ is a pure default premium (investors' expected return is 0).
- A rationed borrower would accept a higher rate, but lenders refuse: raising $R_l$ violates IC.

## Code Patterns
- Calibration check: `Videos/aula-01-what-is-corporate-finance/check_numbers.py` (exact fractions).
