"""Checks every number in lista-r6-liquidity-risk-management-solutions.tex.

Run: python -I lista-r6-liquidity-risk-management-solutions_check.py
Exercises 10 and 11 (Tirole 5.7 and 5.9) are checked in
lista-topic5-nonverifiable-income-termination-solutions_check.py (their exercises 8 and 9).
Tolerance: 1e-6 absolute unless stated.
"""
from math import sqrt

N_CHECKS = 0
TOL = 1e-6


def ok(cond):
    global N_CHECKS
    assert cond
    N_CHECKS += 1


def close(a, b, tol=TOL):
    ok(abs(a - b) < tol)


# ---------------------------------------------------------------- Ex 1 (own numbers)
C, k, r_cash, T = 100.0, 0.10, 0.04, 0.34
after_tax = r_cash * (1 - T)
close(after_tax, 0.0264)
close((k - after_tax) * C, 7.36)

# ---------------------------------------------------------------- Ex 2 (own numbers, Tirole 5.6.1)
r, rho_star, I = 0.6, 0.4, 100.0
close((r - rho_star) * I, 20.0)

# ---------------------------------------------------------------- Ex 3 (own numbers)
K, b = 0.5, 0.002          # $ millions fixed cost; benefit per $ of exposure
close(K / b, 250.0)

# ---------------------------------------------------------------- Ex 4 (G&T Example 21.3)
h = 17 / 24
close(24 * h - 6, 11.0)                      # floor at S = 0
close(h, 0.708333, 1e-6)
partial = lambda S: 24 * h + (1 - h) * S - 6
full = lambda S: 24 - 6
none = lambda S: S - 6
close(partial(0), 11.0); close(partial(24), 18.0); close(partial(30), 19.75)
close(full(0), 18.0); close(none(0), -6.0); close(none(24), 18.0); close(none(30), 24.0)
close((1 - h) * 30, 8.75)

# ---------------------------------------------------------------- Ex 5 (Berk 20.6)
cash = [100, 100, 100, 100]
ar = [200, 100, 100, 600]
inv = [200, 500, 900, 50]
ap = [100, 100, 100, 100]
nwc = [c + a + i - p for c, a, i, p in zip(cash, ar, inv, ap)]
ok(nwc == [400, 600, 1000, 650])
perm = min(nwc)
ok(perm == 400)
temp = [x - perm for x in nwc]
ok(temp == [0, 200, 600, 250])
excess0 = 400 - 100
ok(excess0 == 300)
stb = [max(t - excess0, 0) for t in temp]
ok(stb == [0, 0, 300, 0])
ok(max(stb) == 300)
excess = [max(excess0 - t, 0) for t in temp]
ok(excess == [300, 100, 0, 50])
ok([100 + e for e in excess] == [400, 200, 100, 150])
ok(perm + excess0 == 700)
ok(max(temp) == 600)                         # Problem 5 benchmark (no excess cash)

# ---------------------------------------------------------------- Ex 6 (Tirole 5.1, own numbers)
pH, pL, B, R, I = 0.8, 0.3, 1.0, 5.0, 2.8
dp = pH - pL
N = pH * R - I
M = pH * B / dp
close(dp, 0.5); close(N, 1.2); close(M, 1.6)
close(pL * R - I + B, -0.3)                  # (3.2)
Abar = I - pH * (R - B / dp)
close(Abar, 0.4); close(Abar, M - N)
cond = pH * N + (N - M)
close(cond, 0.56)
D = M - (1 - pH) * N
close(D, 1.36)
xi = ((1 + pH) * N - M) / D
close(xi, 7 / 17); close(xi, 0.411765, 1e-6)
wS = (B / dp) * (1 + xi * pH) / pH
VS, VF = pH * wS, xi * M
close(wS, 3.323529, 1e-6); close(VS, 2.658824, 1e-6); close(VF, 0.658824, 1e-6)
close(dp * (VS - VF), B)                     # period-1 IC binds
ok(wS >= B / dp)                             # period-2 IC after success
pledge = N + pH * (N - VS) + (1 - pH) * xi * (N - M)
close(pledge, 0.0)
close(pH * (N - VS), -1.167059, 1e-6); close((1 - pH) * xi * (N - M), -0.032941, 1e-6)
NPV = N * (1 + pH + (1 - pH) * xi)
close(NPV, 2.258824, 1e-6)
close(pH * VS + (1 - pH) * VF, NPV)
close((1 + xi) * M, pH * pH * wS + (1 - pH) * xi * M)   # total rent identity
# book's (ii) formula (with Delta p) vs ours at xi = 0
book = lambda x: (pH + x * (1 - pH)) * (N - M) + (N - (M - (1 - x) * dp * M))
ours = lambda x: pH * N + N - M + x * ((1 - pH) * (N - M) - pH * M)
close(ours(0), cond)
close(ours(xi), 0.0)
for x in (0.0, 0.3, xi):
    close(ours(x) - book(x), (1 - x) * pL * M)   # book's (ii) formula: Delta p in place of p_H
close(book(0) - cond, -pL * M)
close(pL * M, 0.48)
# comparative statics (finite differences)
xi_f = lambda N_, M_, p_: ((1 + p_) * N_ - M_) / (M_ - (1 - p_) * N_)
eps = 1e-6
close((xi_f(N + eps, M, pH) - xi_f(N - eps, M, pH)) / (2 * eps), 2 * pH * M / D**2, 1e-5)
close(2 * pH * M / D**2, 1.384083, 1e-6)
close((xi_f(N, M + eps, pH) - xi_f(N, M - eps, pH)) / (2 * eps), -2 * pH * N / D**2, 1e-5)
close((xi_f(N, M, pH + eps) - xi_f(N, M, pH - eps)) / (2 * eps), 2 * N * (M - N) / D**2, 1e-5)
# (iv) literal short-term sequence fails the period-1 IC
close(dp * (1 - xi) * M, 0.470588, 1e-6)
ok(dp * (1 - xi) * M < B)
AS = VS - N
close(AS, 1.458824, 1e-6)
close(AS - Abar, (B / dp) * (1 - pH + xi * pH))
# investors' payoff identical under the corrected sequence
close(pH * R - I - pH * AS - (1 - pH) * xi * Abar, pledge)

# ---------------------------------------------------------------- Ex 7 (Tirole 5.2, own numbers)
pH, pL, R1, B1 = 0.9, 0.1, 10.0, 2.0
dp = pH - pL
close(dp, 0.8); close(B1 / dp, 2.5)
rho01 = pH * (R1 - B1 / dp)
close(rho01, 6.75)
close(pL * R1 + B1, 3.0)                     # shirking: negative NPV for I1 = 8 and I1 = 5
I1 = 8.0; a, A = 0.5, 2.0
ok(pL * R1 + B1 < I1); ok(pH * R1 > I1)
close(I1 - rho01, 1.25); ok(a < I1 - rho01 < A)
close(I1 - rho01 - a, 0.75)                  # credit line
gain_l = I1 - a - rho01
loss_e = pH * B1 / dp - a
close(gain_l, 0.75); close(loss_e, 1.75); close(loss_e - gain_l, pH * R1 - I1)
close(pH * R1 - I1, 1.0)
# (iii)-(iv)
I1 = 5.0; qH, qL = 0.75, 0.25; dq = qH - qL; B0 = 0.45; A, a = 4.0, 0.0; I0 = 4.2
ok(pL * R1 + B1 < I1 < rho01)
ok(dq * pH * B1 >= dp * B0); close(dq * pH * B1, 0.9); close(dp * B0, 0.36)
xstar = 1 - dp * B0 / (dq * pH * B1)
close(xstar, 0.6)
close(dq * (1 - xstar) * pH * B1 / dp, B0)
close(I1 + I0 - (qL * A + (1 - qL) * a), 8.2); ok(8.2 > rho01)
close(qH + (1 - qH) * xstar, 0.9); close(rho01 - I1, 1.75)
be = qH * A + (1 - qH) * a + (qH + (1 - qH) * xstar) * (rho01 - I1)
close(be, 4.575); ok(be >= I0)
close(qH * B0 / dq, 0.675)
close(rho01 - qH * B0 / dq, 6.075)
close(I0 + I1 - (qH * A + (1 - qH) * a), 6.2); ok(6.2 > 6.075)
close(qH * A + (1 - qH) * a + rho01 - qH * B0 / dq, 9.075); close(I0 + I1, 9.2)
close(qL * A + (1 - qL) * a + rho01, 7.75); ok(7.75 < I0 + I1)

# ---------------------------------------------------------------- Ex 8 (Tirole 5.5, own numbers)
rL, r0, rH, r1, IA, lam, Tb = 0.2, 1.0, 1.5, 2.0, 0.5, 0.1, 0.3
ok(r0 - rL > IA)
q = 1 + lam * (r1 - rH) / (rH - r0)
close(q - 1, 0.1)
rhs2 = (1 - lam) * (r0 - rL) - lam * (rH - r0) - IA
close(rhs2, 0.17)
close((q - 1) * (rH - r0), 0.05); ok((q - 1) * (rH - r0) < rhs2)
close((1 - lam) * (r0 - rL), 0.72); ok(0.72 >= IA)
close(Tb / (rH - r0), 0.6)
close(1 - lam, 0.9)
lam_bar = (r0 - rL - IA) / (r1 - rL)
close(lam_bar, 0.166667, 1e-6); ok(lam < lam_bar)
close(q - (1 - lam), 0.2); close(lam * (r1 - r0) / (rH - r0), 0.2)

# ---------------------------------------------------------------- Ex 9 (Tirole 5.11, own numbers)
pH, B, dp, R, r, mu = 0.6, 0.5, 0.25, 3.0, 1.0, 0.5
l0 = pH * B / ((1 + mu) * dp)
close(l0, 0.8)
for P in (0.8, 1.0, 1.2):
    rho = pH * P * R - mu / (1 + mu) * pH * B / dp
    d = P * r - l0
    close((P * r - d) + pH * (P * R - B / dp), rho)

# ---------------------------------------------------------------- Ex 12 (G&T 22.12)
x1, x2, x3 = 1.1, -0.9, -0.2
close(x1 + x2 + x3, 0.0)
close(-4 * x1 - 2 * x2 - 3 * x3, -2.0)
close(0 * x1 + 6 * x2 - 2 * x3, -5.0)
close(4 * x1 + 6 * x2 + 3 * x3, 4.4 - 5.4 - 0.6)
close(4 * x1 + 6 * x2 + 3 * x3, -1.6)
# variant: swap treated as costless (as in Example 22.16)
y1, y2, y3 = 11.0, -4.5, -11.0
close(y1 + y3, 0.0); close(-4 * y1 - 2 * y2 - 3 * y3, -2.0); close(6 * y2 - 2 * y3, -5.0)

# ---------------------------------------------------------------- Ex 13 (Tirole 5.6)
IA = 0.09; R = 2 * sqrt(IA); Rb = R / 2
close(R, 0.6); close(Rb, 0.3); close(Rb * (R - Rb), IA); close(R**2 / 4, IA)
# (ii) numerical example: F uniform on [0,1], R = 0.8, I - A = 0.01
R, IA = 0.8, 0.01
Rb = 0.5; rho = R * Rb / 2; mu = Rb / (2 * Rb - R)
close(rho, 0.2); close(mu, 2.5)
close(Rb * (R - Rb) + Rb**2 / (2 * mu), rho)
close(rho * Rb * (R - Rb) - rho**2 / 2, IA)        # binding breakeven
close(rho * Rb**2 / 2, 0.025)
g = lambda x: 0.24 * x**2 - 0.4 * x**3
close(g(0.5), 0.01); close(g(0.4), 0.0128)
best = (-1.0, None)
n = 400
for i in range(1, n):
    rb = R * i / n
    for j in range(1, n):
        rh = j / n
        if rh * rb * (R - rb) - rh**2 / 2 >= IA - 1e-12:
            u = rh * rb**2 / 2
            if u > best[0]:
                best = (u, (rb, rh))
ok(abs(best[1][0] - 0.5) < 0.01 and abs(best[1][1] - 0.2) < 0.01)
ok(abs(best[0] - 0.025) < 5e-4)
nu = mu - 1
close(nu, 1.5)
close((Rb * R - Rb**2 / 2 + nu * Rb * (R - Rb)) / (1 + nu), rho)
close(Rb * (R - Rb), 0.15); close(Rb * R - Rb**2 / 2, 0.275)

# ---------------------------------------------------------------- Ex 14 (Tirole 5.10, own numbers)
pH, pL, R, B, I, tau = 0.5, 0.2, 4.0, 0.6, 1.5, 0.25
dp = pH - pL
close(dp, 0.3); close(B / dp, 2.0); close(pL * R + B, 1.4); ok(pL * R + B < I)
rho1, rho0 = pH * R, pH * (R - B / dp)
close(rho1, 2.0); close(rho0, 1.0); ok(rho1 > I > rho0)
mu = tau / pH; h1, h0 = mu * rho1, mu * rho0
close(mu, 0.5); close(h1, 1.0); close(h0, 0.5)
F = lambda x: x / 2.0
Int = lambda x: x**2 / 4.0
close(rho0 * (1 + mu * F(h1)), 1.25); close(Int(h1), 0.25)
close(I + Int(h1) - rho0 * (1 + mu * F(h1)), 0.5)          # A_1
close(rho0 * (1 + mu * F(h0)), 1.125); close(Int(h0), 0.0625)
close(I + Int(h0) - rho0 * (1 + mu * F(h0)), 0.4375)       # A_0
A = 0.46
roots = [(1 + 0.6) / 2, (1 - 0.6) / 2]
close(sqrt(1 - 0.64), 0.6)
for x in roots:
    close(rho0 * (1 + mu * F(x)) - (I - A + Int(x)), 0.0)
close(roots[0], 0.8); close(roots[1], 0.2)
close(roots[0] - h0, 0.3)
close(I - rho0 - 0.0625, 0.4375)

# ---------------------------------------------------------------- Ex 15 (Tirole 5.8, own numbers)
pH, pL, R, B, I1, I0 = 0.5, 0.3, 10.0, 1.0, 4.0, 1.0
dp = pH - pL
ok(B < dp * R); close(B / dp, 5.0)
t1 = I1 / R - pH; t0 = I1 / (R - B / dp) - pH
close(t1, -0.1); close(t0, 0.3)
lo, hi = -pL, 1 - pH
fden = 1 / (hi - lo)
close(fden, 1.25)
Pa = lambda t: fden * ((2.5 * hi**2 - 1.5 * hi) - (2.5 * t**2 - 1.5 * t))
close(Pa(t0), 0.125); close(Pa(t1), -0.375)
close(I0 - Pa(t0), 0.875); close(I0 - Pa(t1), 1.375)
close(Pa(0.1), 0.0)
close(B / (dp * R), 0.5)
close((pH + t0) * R, 8.0)
R1s = I1 / pH; R0s = R1s + B / dp
close(R1s, 8.0); close(R0s, 13.0)
Pb = lambda x: 0.05 * ((0.25 * 400 - 6.5 * 20) - (0.25 * x**2 - 6.5 * x))
close(Pb(R0s), 0.6125); close(Pb(R1s), 0.3)
close(I0 - Pb(R0s), 0.3875); close(I0 - Pb(R1s), 0.7)
close(Pb(10.0), 0.5); close(Pb(16.0), 0.5)
close(sqrt(676 - 640), 6.0)
close(pH * B / dp, 2.5); close(pH * R0s, 6.5)

print(f"PASS {N_CHECKS} checks")
