def power(base, exponent):
    result = 1
    for _ in range(exponent):
        c[1] += 1
        result *= base
    return result
