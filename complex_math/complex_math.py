import math

def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

def euclidean_distance(point1, point2):
    sum_of_squares = 0
    for i in range(len(point1)):
        sum_of_squares += (point1[i] - point2[i]) ** 2
    return math.sqrt(sum_of_squares)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def multiply2(x, y, z):
    print("Inputs: ", x, y, z)
    rxy = 0
    rxyz = 0

    # y + y + y....+ y, x times
    # x*y
    rxy = sum([y if x >= 0 else -y for _ in range(abs(x))])
    for j in range(abs(z)):
        if z >= 0:
            if(z<0):
                rxyz += rxy
        else:
            rxyz -= rxy
        print("rxyz: ", rxyz)

    print("multiply done", rxyz)

    # Call power function
    power_result = power(rxyz, 2)
    print("Power result:", power_result)

    # Call euclidean_distance function
    distance = euclidean_distance((x, y), (rxy, rxyz))
    print("Euclidean distance:", distance)

    # Call factorial function
    fact_result = factorial(abs(rxyz))
    print("Factorial result:", fact_result)

    # Call fibonacci function
    fib_result = fibonacci(abs(rxy))
    print("Fibonacci result:", fib_result)

    return rxyz
