---
tags: [notes, lecture-01, formulas, reference]
date: 2026-10-24
status: taught
source: "Aula/Topic1.pdf slides 4–62 (blocks 1.1–1.8 of Map/lectures-index.md); equations (1.1)–(6.13) of notes L01-01 to L01-06"
---

# Topic 1 · Formula sheet: every definition, every number, the lecture's content mapped

Prev: [[L01-06-cash-flows-fcf]] · Next: [[L01-08-pitfalls]] · Map: [[L01-00-map]]

---

## 0 · The exam specification, mapped

The slides state one goal (slide 6): "introduction to basic financial statements", the "key to
measuring and understanding relevant aspects of firms". The content list is the block map of
[[../../Map/lectures-index|lectures-index]] (Topic 1), item by item:

| Block | Content item (slides) | Note |
|---|---|---|
| 1.1 | Asset pricing, corporate finance, banking (4–5) | [[L01-01-balance-sheet-view]] §1 |
| 1.2 | $A=L+E$ in book **and** market value (7–8) | [[L01-01-balance-sheet-view]] §3, §6 |
| 1.2 | Recognition: tangible vs intangible; historical cost vs market value; SVB (9–10) | [[L01-01-balance-sheet-view]] §4 |
| 1.2 | Goods **and promises**; liabilities senior, equity junior and residual (11–12) | [[L01-01-balance-sheet-view]] §5 |
| 1.2 | $FCF_A=FCF_L+FCF_E\Rightarrow A=L+E$ (13) | [[L01-01-balance-sheet-view]] §6; [[L01-06-cash-flows-fcf]] §7 |
| 1.2 | Cash flow–production cycle (14) | [[L01-01-balance-sheet-view]] §7 |
| 1.3 | Current vs non-current assets and liabilities; goodwill (15–16, 18–19) | [[L01-02-balance-sheet-items]] §1–2, §4 |
| 1.3 | Depreciation is not a cash expense; book value = cost − accumulated depreciation (16) | [[L01-02-balance-sheet-items]] §2 |
| 1.3 | Rise in corporate cash (17) | [[L01-02-balance-sheet-items]] §3 |
| 1.3 | Net working capital; GPA (20–21) | [[L01-02-balance-sheet-items]] §5–6 |
| 1.4 | Market cap; forward- vs backward-looking; off-balance-sheet items (22–23) | [[L01-03-book-vs-market-leverage]] §1–2 |
| 1.4 | Starbucks; intangibles; market-to-book (24–27) | [[L01-03-book-vs-market-leverage]] §3–5 |
| 1.5 | D/E book vs market; net debt; EV; current and quick ratios; covenants (28–31) | [[L01-03-book-vs-market-leverage]] §6–8 |
| 1.6 | Accrual and matching; depreciation spreads capex (32–35) | [[L01-04-income-statement]] §2–3 |
| 1.6 | Gross profit, opex, operating leverage, EBIT, net income (36–37) | [[L01-04-income-statement]] §4 |
| 1.6 | Statement of equity; GM income statement (38–39) | [[L01-04-income-statement]] §5–6 |
| 1.7 | EPS, diluted EPS; margins; economic earnings (40–43) | [[L01-05-ratios-dupont-roic]] §1–3 |
| 1.7 | AR/AP days; EBITDA; coverage (44–45) | [[L01-05-ratios-dupont-roic]] §4–5 |
| 1.7 | ROE, ROA, turnover, **DuPont**; "maximize leverage?" (46–48) | [[L01-05-ratios-dupont-roic]] §6, §9 |
| 1.7 | ROE pitfalls; **ROIC**; P/E (49–51) | [[L01-05-ratios-dupont-roic]] §7–8, §10 |
| 1.8 | Profits ≠ cash; operating, investing, financing sections; GM (52–58) | [[L01-06-cash-flows-fcf]] §1–4 |
| 1.8 | Net cash flow, CFO, $\Delta$cash identity (59) | [[L01-06-cash-flows-fcf]] §5 |
| 1.8 | **FCF**, **FCFE**, what each values, uses of FCF (60–62) | [[L01-06-cash-flows-fcf]] §6–8 |

---

## 1 · Every numbered equation

| Eq. | Statement | Derived / used in |
|---|---|---|
| (1.1) | $A=L+E$ | [[L01-01-balance-sheet-view]] §3 (Berk (2.1), p. 26) |
| (1.2) | $\Delta A=\Delta L+\Delta E$ | §3 |
| (1.3) | creditors $\min(X,F)$, owners $\max(X-F,0)$ | §5 |
| (1.4) | $\min(X,F)+\max(X-F,0)=X$ | §5 |
| (1.5) | $FCF_A=FCF_L+FCF_E\Rightarrow A=L+E$ (slide 13) | §6 |
| (1.6) | the split holds date by date, state by state | §6 |
| (1.7) | linear pricing $\mathrm{PV}(Y+Z)=\mathrm{PV}(Y)+\mathrm{PV}(Z)$ | §6 |
| (1.8) | $A^{\text{mkt}}=L^{\text{mkt}}+E^{\text{mkt}}$ | §6 |
| (2.1) | goodwill = price paid − fair value of identifiable net assets | [[L01-02-balance-sheet-items]] §2 |
| (2.2) | straight line $\mathrm{Dep}=(K_0-S_v)/n$ | §2 |
| (2.3) | $BV_k=K_0-\sum_{j\le k}\mathrm{Dep}_j$ | §2 |
| (2.4) | $NWC=CA-CL$ | §5 (Berk (2.2), p. 28) |
| (3.1) | $E^{\text{book}}=A-L$ | [[L01-03-book-vs-market-leverage]] §1 |
| (3.2) | $E^{\text{mkt}}=P\times N$ | §1 |
| (3.3) | market-to-book $=E^{\text{mkt}}/E^{\text{book}}$ | §5 (Berk (2.3), p. 30) |
| (3.4) | $D/E$ (slide: $L/E$; Berk (2.4): debt/equity) | §6 |
| (3.5) | net debt $=D-C$ | §6 |
| (3.6) | $EV=E^{\text{mkt}}+D-C$ | §7 (Berk (2.5), p. 31) |
| (3.7) | current ratio $CA/CL$ | §8 |
| (3.8) | quick ratio $(CA-\text{Inv})/CL$ | §8 |
| (4.1) | cash collected $=S-\Delta AR$ | [[L01-04-income-statement]] §2 |
| (4.2)–(4.5) | gross profit, operating income, EBIT, NI | §4 |
| (4.6) | $\text{OI}=(1-v)S-F$ | §4 |
| (4.7) | $\Delta\text{OI}=(1-v)\Delta S$ | §4 |
| (4.8) | elasticity of OI to sales $=1+F/\text{OI}$ | §4 |
| (4.9) | $E_{\text{end}}=E_{\text{begin}}+\text{NI}-\text{Div}\pm\text{other}$ | §5 |
| (5.1)–(5.2) | EPS, diluted EPS | [[L01-05-ratios-dupont-roic]] §1 |
| (5.3)–(5.5) | gross, operating, net margin | §2 |
| (5.6) | economic earnings $=\text{NI}-r_EE$ | §3 |
| (5.7)–(5.8) | AR days, AP days | §4 |
| (5.9)–(5.10) | EBITDA, interest coverage | §5 |
| (5.11)–(5.13) | ROE, ROA, asset turnover | §6 |
| (5.14) | **DuPont** ROE = margin × turnover × leverage | §6 (Berk (2.18), p. 38) |
| (5.15) | ROE = ROA × $A/E$; ROA = margin × turnover | §6 |
| (5.16) | $\mathrm{ROIC}=\mathrm{EBIT}(1-\tau)/(D+E)$ | §8 |
| (5.17)–(5.19) | NI in terms of EBIT and ROIC | §8 |
| (5.20) | **$\mathrm{ROE}=\mathrm{ROIC}+\frac DE[\mathrm{ROIC}-r_D(1-\tau)]$** | §8 |
| (5.21) | $\mathrm{ROA}=\mathrm{ROIC}-\frac{D}{D+E}r_D(1-\tau)$ | §8 |
| (5.22) | $\operatorname{sd}(\mathrm{ROE})=(1+D/E)\operatorname{sd}(\mathrm{ROIC})$ | §9 |
| (5.23) | $P/E=E^{\text{mkt}}/\text{NI}=P/\mathrm{EPS}$ | §10 (Berk (2.19), p. 39) |
| (6.1) | $\text{CFO}=\text{NI}+\text{Dep}+\text{other}-\Delta AR+\Delta AP-\Delta\text{Inv}$ | [[L01-06-cash-flows-fcf]] §2 |
| (6.2)–(6.4) | balance sheet split, differences, $\Delta RE$ | §5 |
| (6.5) | $\Delta\text{cash}=\text{NI}-\Delta NCA+\Delta L+\Delta PIC-\text{Div}$ (slide 59) | §5 |
| (6.6) | **$FCF=\mathrm{EBIT}(1-\tau)+\text{Dep}-\text{Capex}-\Delta NWC$** | §6 |
| (6.7) | **$FCFE=FCF-\text{Int}(1-\tau)+\Delta D$** | §6 |
| (6.8) | $FCF-\text{Int}(1-\tau)=\text{NI}+\text{Dep}-\text{Capex}-\Delta NWC$ | §6 |
| (6.9) | $FCFE=\text{NI}+\text{Dep}-\Delta NWC-\text{Capex}+\Delta D$ | §6 |
| (6.10) | $CF_D=\text{Int}-\Delta D$ | §7 |
| (6.11) | $FCFE+CF_D=FCF+\tau\,\text{Int}$ | §7 |
| (6.12) | actual cash flow from assets, with actual taxes | §7 |
| (6.13) | $CF_A^{\text{actual}}=CF_D+FCFE$ | §7 |

### 1.1 · Definitions without an equation number

| Term | Definition (slide) |
|---|---|
| Current asset / liability | converted to cash / due within one year (15, 18) |
| Accrual principle | revenue at sale, expense at purchase, not at payment (32) |
| Matching principle | revenues and expenses in the period of the transaction (32) |
| Operating leverage | high share of fixed costs → vulnerable to sales declines (36) |
| Dilution | growth in shares from options and convertibles (40) |
| Growth / value stock | high / low market-to-book (27) |
| Net cash flow (cash earnings) | NI + non-cash items (59; Higgins p. 21) |
| Working-capital investment | increase in operating current assets − increase in non-interest-bearing current liabilities (60) |

---

## 2 · Every number and worked case

| Case | Numbers | Note |
|---|---|---|
| Plant on credit (slide 9) | $\Delta A=\Delta L=+1$ bn | 01 §3 |
| Ross Brasil S/A 2009 (pp. 38–41) | OCF 547, NCS 130, ΔNWC 330 → CFA 87 = 24 + 63; unlevered FCF 63.22, τ·Int 23.78 | 01 §6, 06 §7 |
| Intangibles ≈ 90% of S&P 500 EV (slide 9) | — | 01 §4 |
| Higgins facility (p. 13) | 50 m, 10 years → 5 m/yr; $BV_3=35$ | 02 §2, 04 §3 |
| Corporate cash (slide 17) | < 1 tn (1994) → ≈ 4 tn (2017); cash/GDP index 100 → ≈ 160 (read off the chart) | 02 §3 |
| Berk Global NWC (p. 28) | 57.0 − 34.7 = 22.3 | 02 §5 |
| **GPA 2020 (slide 21)** | A 53,295; L 36,488; E 16,807; **NWC −842**; payables 61.8% of CL, 21.4% of A; current 0.954, quick 0.601; book $L/E$ 2.171 | 02 §6, 03 §6, §8 |
| Berk Global (pp. 29–31) | market cap 36 vs book 22.2; D 118.7; book D/E 5.3, market 3.3; EV 131.5 | 03 §1, §6, §7 |
| Polaris (Higgins p. 25) | market cap 5,898 vs book 1,434 (4.1×) | 03 §1 |
| **Starbucks 2020 (slides 24–25)** | **book E −7,904**; market cap 122.6 bn; debt 15,917; net debt 10,889; **EV 133,489** (142,512 with leases); market $L/E$ 0.309, $D/E$ 0.130; current 1.060, quick 0.873 | 03 §3–8 |
| Amazon June 2005 (Berk p. 29) | book E −64 m, market > 15 bn | 03 §3 |
| Intangible share (slide 26) | 17.1% (1975) → 84.0% (2018) | 03 §4 |
| Market-to-book (Berk p. 30) | AmeriServ 0.52, Citigroup 0.82, large U.S. ≈ 3, Amazon > 11 | 03 §5 |
| Heinz (Berk Ex. 2.2, p. 32) | cap 14.59 bn, book 1.83, D 4.83, EV 18.858 bn | 03 §7 |
| Ross Exemplo 3.1 (p. 62) | 4/2 → 3/1 = 3; 2/4 → 1/3 | 03 §8 |
| Polaris receivables (Higgins pp. 12–13) | revenue 7,108, ΔAR 67 → cash 7,041 | 04 §2 |
| **GM 2020 P&L (slide 39)** | sales 122,485; gross 13,672; OI 6,634; EBIT 9,193; pre-tax 8,095; NI 6,321; **τ = 21.915%**; DOL 2.061 | 04 §4, §6 |
| Berk Global retained earnings (p. 44) | 2 − 1 = 1; payout 50% | 04 §5 |
| GM margins and coverage | gross 11.16%, operating 5.42%, net 5.16%; EBITDA 22,008; coverage 8.37 (20.04 on EBITDA) | 05 §2, §5 |
| Polaris economic earnings (Higgins pp. 27–28) | 414 − 143 = 271 | 05 §3 |
| Berk Global AR days (p. 37) | 18.5 / 0.5115 = 36 days (27.5 in 2009) | 05 §4 |
| **DuPont 2013 (slide 48)** | Google 14.8, JPMorgan 8.5, Hyundai 15.9, Chevron 14.4 (%) | 05 §6 |
| Berk Ex. 2.3 (p. 39) | Wal-Mart 22.5%, Nordstrom 31.4%, required margin 5.0% | 05 §6 |
| Higgins risk problem (p. 54) | 6% × 5.0 = 30% vs 10% × 2.0 = 20% | 05 §7 |
| Higgins value problem (p. 56) | ROE 28.9% vs earnings yield 7.0% | 05 §7 |
| Polaris ROIC (Higgins p. 55) | 467.2 / 2,870 = 16.3% | 05 §8 |
| **Two firms (slide 50)** | A: ROE 18%, ROA 1.8%, ROIC 7.2%; B: 7.2% three times; flat at $r_D=12\%$ | 05 §8 |
| Same firms, Higgins 13e (pp. 55–56) | τ = 25%: A's ROE 22.5%, ROIC 9.0% | 05 §8 |
| P/E | Berk Global 18 (p. 39); Polaris 14.2 (Higgins p. 57) | 05 §10 |
| Berk Global CFO (p. 44) | positive NI, CFO −0.4 m | 06 §1 |
| **GM 2020 cash flows (slide 58)** | CFO 16,670; CFI −21,826; CFF 5,552; FX −222; Δcash 174; 22,943 → 23,117 | 06 §4 |
| **GM FCF bridge** | NOPAT 7,178.4; ΔNWC 1,403; **FCF 13,290.4**; after-tax interest 857.4; net borrowing 6,141; **FCFE 18,574.0** | 06 §6 |
