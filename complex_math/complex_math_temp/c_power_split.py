from src.utils import Count 

def power(base, exponent):
    result = 1
    for _ in range(exponent):
        Count.incC(1)
        result *= base
    return result
