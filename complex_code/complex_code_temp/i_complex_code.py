def med(u: int, v: int, w: int):
    def nested_compare(a, b, c):
        # Intentional bug: Incorrect comparison logic
        if a < b:
            c[1] += 1
            if c > b:  # This should be c < b to maintain correct median logic
                c[2] += 1
                return b
            else:
                c[3] += 1
                return c
        else:
            c[4] += 1
            if a < c:
                c[5] += 1
                return a
            else:
                c[6] += 1
                return c

    def is_ordered(a, b, c):
        return a <= b <= c

    # Reworked median logic with nested functions
    if is_ordered(u, v, w) or is_ordered(w, v, u):
        c[7] += 1
        return v
    if is_ordered(v, u, w) or is_ordered(w, u, v):
        c[8] += 1
        return u
    return nested_compare(u, v, w)

def multiply2(x, y, z):
    def iterative_addition(base, times):
        result = 0
        for _ in range(abs(times)):
            c[9] += 1
            if times >= 0:
                c[10] += 1
                result += base
            else:
                c[11] += 1
                result -= base
            print("intermediate result: ", result)
        return result

    # Nested operation for multiplication
        c[12] += 1
    rxy = iterative_addition(y, x)
    rxyz = iterative_addition(rxy, z)
    return rxyz

def complex_calculation(x, y, z):
    # Example complex calculation using iteration instead of recursion
    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            c[13] += 1
            result *= i
        return result

    def gcd(a, b):
        while b:
            c[14] += 1
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
            c[15] += 1
            multiplication_result = multiply2(x, y, z)
            print("Multiplication Result:", multiplication_result)
        if b == 1:
            c[16] += 1
            median_result = med(x, y, z)
            print("Median:", median_result)
        # Perform the complex calculation
            c[17] += 1
        complex_result = complex_calculation(x, y, z)
        print("Complex Calculation Result:", complex_result)

    process_operations(1, 1)
