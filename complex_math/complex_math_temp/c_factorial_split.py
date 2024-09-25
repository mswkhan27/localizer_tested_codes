from src.utils import Count 

def factorial(n):
    if n == 0:
        Count.incC(3)
        return 1
    else:
        Count.incC(4)
        return n * factorial(n-1)
