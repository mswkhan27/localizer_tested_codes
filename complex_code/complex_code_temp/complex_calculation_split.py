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
