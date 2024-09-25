from src.utils import Count 

def fibonacci(n):
    if n <= 1:
        Count.incC(5)
        return n
    else:
        Count.incC(6)
        return fibonacci(n-1) + fibonacci(n-2)
