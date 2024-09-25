def fibonacci(n):
    if n <= 1:
        c[5] += 1
        return n
    else:
        c[6] += 1
        return fibonacci(n-1) + fibonacci(n-2)
