from src.utils import Count 

def multiply2(x, y, z):
    print("Inputs: ", x, y, z)
    rxy = 0
    rxyz = 0
    # y + y + y....+ y, x times
    # x*y
    rxy = sum([y if x >= 0 else -y for _ in range(abs(x))])
    Count.incC(7)
    for j in range(abs(z)):
        Count.incC(8)
        if z >= 0:
            Count.incC(9)
            if(z<0):
                Count.incC(10)
                rxyz += rxy
        else:
            Count.incC(11)
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
