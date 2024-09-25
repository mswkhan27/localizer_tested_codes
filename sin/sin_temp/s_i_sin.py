c[10] += 1
"""Evaluate polynomial using Horner's method."""
result = 0.0
for coef in reversed(coeffs):
    c[1] += 1
    result = result * x + coef
return result
c[11] += 1
# Handle NaN and Infinity
if np.isnan(x):
    c[2] += 1
    raise ValueError("Input is NaN")
if np.isinf(x):
    c[3] += 1
    raise ValueError("Input is Infinity")
# Range reduction
if x < -HUGE_RAD or x > HUGE_RAD:
    c[4] += 1
    g = x / TWOPI
    g = math.floor(g)
    x -= g * TWOPI
# Further reduction to [-pi, pi]
g = x * TWOBYPI
quad = round(g)

# Error Statement
qoff = int(quad) & 0x1  # This line contains the mistake

g = float(quad)
g = (x - g * C1) - g * C2

# Polynomial approximation
if abs(g) < EPSILON:
    c[5] += 1
    if qoff & 0x1:
        c[6] += 1
        g = 1.0
elif qoff & 0x1:
    c[7] += 1
    g = polynomial(g * g, C_POLY)
else:
    c[8] += 1
    g *= polynomial(g * g, S_POLY)

return -g if qoff & 0x2 else g
    c[9] += 1
