"""Verify every computed number the narration states (Tirole §3.2 calibration).

Run: python check_numbers.py   (aborts on any mismatch)
"""
from fractions import Fraction as F

I, A, R = 100, 10, 160              # thousand reais
pH, pL, B = F(8, 10), F(4, 10), 20
dp = pH - pL

npv = pH * R - I
assert npv == 28                    # (3.1) holds
assert pL * R - I + B == -16        # (3.2) holds: shirking destroys value
assert dp == F(4, 10)

min_stake = B / dp                  # IC: dp * R_b >= B
assert min_stake == 50
max_promise = R - min_stake
assert max_promise == 110
pledgeable = pH * max_promise
assert pledgeable == 88
assert I - A == 90 and pledgeable < I - A          # 2 short: rationed

rent = pH * B / dp
assert rent == 40
A_bar = rent - npv                  # (3.3)
assert A_bar == 12 and A < A_bar
assert pledgeable - (I - A) == A - A_bar == -2     # the same 2, two ways

# Value additivity example (BeatValueAdditivity): R in {0, 200}, prob 1/2 each
for D, debt, equity in ((80, 40, 60), (150, 75, 25)):
    assert F(1, 2) * min(200, D) == debt and F(1, 2) * max(0, 200 - D) == equity
    assert debt + equity == 100
# A_bar negative when NPV exceeds the rent (BeatThreshold aside): NPV 50 -> 40 - 50
assert rent - 50 == -10
# Viewer exercise in BeatClose, B = 15: stake 37.5, pledgeable 98, A_bar 2 -> funded at A = 10
assert 15 / dp == F(75, 2) and pH * (R - 15 / dp) == 98 and pH * 15 / dp - npv == 2

# The richer sister, A = 20 (BeatRicherFounder)
A2 = 20
R_l = (I - A2) / pH
assert R_l == 100 and R - R_l == 60 and R - R_l >= min_stake
assert pH * (R - R_l) - A2 == npv == 28
assert R_l / (I - A2) == 1 / pH == F(5, 4)        # 1 + iota = 1/p_H: pure default premium

# Comparative statics of A_bar = pH*B/dp - (pH*R - I) (BeatComparativeStatics)
abar = lambda B_, R_, I_: pH * B_ / dp - (pH * R_ - I_)
assert abar(B + 1, R, I) - abar(B, R, I) == pH / dp == 2
assert abar(B, R + 1, I) - abar(B, R, I) == -pH
assert abar(B, R, I + 1) - abar(B, R, I) == 1

# BeatStep "jump moves left" example: p_L 0.4 -> 0.3 (success more informative)
pL2 = F(3, 10); dp2 = pH - pL2
assert dp2 == F(1, 2) and pH * B / dp2 == 32 and pH * B / dp2 - npv == 4
assert pL2 * R - I + B == -32 < 0                   # (3.2) still holds
# BeatMMRecovered intermediate steps
assert [pH * b / dp - npv for b in (10, 5)] == [-8, -18]

# B -> 0: contractible behaviour, the MM world
assert pH * 0 / dp - npv == -28

# Facts quoted on screen, as printed in Tirole (checked against the PDF text, 2026-10-09)
table_2_2 = {  # Mayer (1990), % of total financing, 1970-1985, p. 96
    "U.S.": dict(retentions=66.9, loans=23.1, bonds=9.7, shares=0.8),
    "U.K.": dict(retentions=72.0, loans=21.4, bonds=0.8, shares=4.9),
    "Germany": dict(retentions=55.2, loans=21.1, bonds=0.7, shares=2.1),
    "Japan": dict(retentions=33.7, loans=40.7, bonds=3.1, shares=3.5),
    "France": dict(retentions=44.1, loans=41.5, bonds=2.3, shares=10.6),
}
for c, r in table_2_2.items():
    assert r["retentions"] > r["shares"] and r["loans"] > r["shares"], c
equity_share_1999 = {"U.S.": 12, "U.K.": 9, "France": 9, "Japan": 8, "Germany": 6}  # p. 97
table_2_4 = {  # White (1991), U.S. 1985: equity/(debt+equity), debt/equity, p. 98
    "All industries": (0.32, 2.11), "Manufacturing": (0.45, 1.20),
    "Wholesale and retail trade": (0.29, 2.49), "Services": (0.31, 2.25),
    "Commercial banks": (0.08, 11.00),
}
for k, (e, de) in table_2_4.items():
    assert abs((1 - e) / e - de) / de < 0.1, k     # the two columns agree
table_2_6 = {  # Eckbo-Masulis (1995), 2-day abnormal return %, industrials, p. 101
    "Common stock": -3.1, "Convertible bonds": -2.0, "Straight bonds": -0.3,
}
assert 1000 * F(325, 100000) == F(13, 4)            # 3.25 per 1,000 (Jensen-Murphy, p. 24)
print("all numbers check")
