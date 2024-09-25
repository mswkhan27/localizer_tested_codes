import math
import numpy as np

# Constants (replace these with actual values)
TWOPI = 2 * math.pi
TWOBYPI = 2 / math.pi
HUGE_RAD = 1e307
EPSILON = 1e-16
C1 = 1.0  # Replace with actual value
C2 = 1.0  # Replace with actual value
# Example coefficients, replace with actual polynomial coefficients
C_POLY = [0.0, 0.0, 0.0]
S_POLY = [0.0, 0.0, 0.0]

def polynomial(x, coeffs):
    """Evaluate polynomial using Horner's method."""
    result = 0.0
    for coef in reversed(coeffs):
        result = result * x + coef
    return result

def sin_function(x, qoff):
    # Handle NaN and Infinity
    if np.isnan(x):
        raise ValueError("Input is NaN")
    if np.isinf(x):
        raise ValueError("Input is Infinity")

    # Range reduction
    if x < -HUGE_RAD or x > HUGE_RAD:
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
        if qoff & 0x1:
            g = 1.0
    elif qoff & 0x1:
        g = polynomial(g * g, C_POLY)
    else:
        g *= polynomial(g * g, S_POLY)
    
    return -g if qoff & 0x2 else g

