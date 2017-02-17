"""Convert a float to IEEE 32-bit floating point notation.
1 sign bit, 8 exponent bits with +127 (7 bit) bias, 23 mantissa bits.
Requires Python 3 (float division)
"""

from math import log2


def ieeefloat(f):
    # Determine sign.
    if f < 0:
        sgn = "1"
        f *= -1					# remove -ve before log or else
    else:
        sgn = "0"
    # Determine exponent with bias
    exp_dec = log2(f)			# returns infinity if out of range
    if exp_dec > 128 or exp_dec < -127:
        raise ValueError("Out of range")
    exp = bin(int(exp_dec) + 127)[2:]
    # Normalize mantissa: implied leading 1.
    mnt_dec = (f / 2**int(exp_dec)) - 1
    # Build binary mantissa:
    mnt = []
    for i in range(1, 24):
        power_of_2 = 1 / 2**i 			# e.g. 1/2, 1/4, 1/8, ...
        if mnt_dec >= power_of_2:		# mantissa contains this fraction
            mnt_dec -= power_of_2		# leave remainder
            mnt.append("1")
        else:
            mnt.append("0")
    if mnt_dec > 0:
        raise ValueError("Insufficient precision")
    return (sgn, exp, "".join(mnt))

print("2.0", ieeefloat(2.0))
print("1e6", ieeefloat(1e6))
print("1/3", ieeefloat(1 / 3))
print("1/16", ieeefloat(1 / 16))
print("-1/2", ieeefloat(-1 / 2))
print("About to go out of range...")
print("1e999", ieeefloat(1e999))
