def factorial(n):
    if n == 0:
        c[3] += 1
        return 1
    else:
        c[4] += 1
        return n * factorial(n-1)
