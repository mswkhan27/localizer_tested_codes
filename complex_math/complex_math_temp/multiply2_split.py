def multiply2(x, y, z):
    print("Inputs: ", x, y, z)
    rxy = 0
    rxyz = 0
    # y + y + y....+ y, x times
    # x*y
    rxy = sum([y if x >= 0 else -y for _ in range(abs(x))])
    c[7] += 1
    for j in range(abs(z)):
        c[8] += 1
        if z >= 0:
            c[9] += 1
            if(z<0):
                c[10] += 1
                rxyz += rxy
        else:
            c[11] += 1
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
