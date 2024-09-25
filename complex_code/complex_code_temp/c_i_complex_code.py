from src.utils import Count 

def med(u: int, v: int, w: int):
    def nested_compare(a, b, c):
        # Intentional bug: Incorrect comparison logic
        if a < b:
            Count.incC(1)
            if c > b:  # This should be c < b to maintain correct median logic
                Count.incC(2)
                return b
            else:
                Count.incC(3)
                return c
        else:
            Count.incC(4)
            if a < c:
                Count.incC(5)
                return a
            else:
                Count.incC(6)
                return c

    def is_ordered(a, b, c):
        return a <= b <= c

    # Reworked median logic with nested functions
    if is_ordered(u, v, w) or is_ordered(w, v, u):
        Count.incC(7)
        return v
    if is_ordered(v, u, w) or is_ordered(w, u, v):
        Count.incC(8)
        return u
    return nested_compare(u, v, w)

def multiply2(x, y, z):
    def iterative_addition(base, times):
        result = 0
        for _ in range(abs(times)):
            Count.incC(9)
            if times >= 0:
                Count.incC(10)
                result += base
            else:
                Count.incC(11)
                result -= base
            print("intermediate result: ", result)
        return result

    # Nested operation for multiplication
        Count.incC(12)
    rxy = iterative_addition(y, x)
    rxyz = iterative_addition(rxy, z)
    return rxyz

def complex_calculation(x, y, z):
    # Example complex calculation using iteration instead of recursion
    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            Count.incC(13)
            result *= i
        return result

    def gcd(a, b):
        while b:
            Count.incC(14)
            a, b = b, a % b
        return a

    def nested_operations(a, b, c):
        result1 = factorial(a)  # Factorial of the first parameter
        result2 = gcd(b, c)     # GCD of the second and third parameters
        result3 = multiply2(a, b, c)  # Complex multiplication
        median_value = med(result1, result2, result3)
        return median_value

    return nested_operations(x, y, z)

def main(x, y, z):
    def process_operations(a, b):
        if a == 1:
            Count.incC(15)
            multiplication_result = multiply2(x, y, z)
            print("Multiplication Result:", multiplication_result)
        if b == 1:
            Count.incC(16)
            median_result = med(x, y, z)
            print("Median:", median_result)
        # Perform the complex calculation
            Count.incC(17)
        complex_result = complex_calculation(x, y, z)
        print("Complex Calculation Result:", complex_result)

    process_operations(1, 1)
