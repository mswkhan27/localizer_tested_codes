result = 1
for _ in range(exponent):
    c[1] += 1
    result *= base
return result
sum_of_squares = 0
for i in range(len(point1)):
    c[2] += 1
    sum_of_squares += (point1[i] - point2[i]) ** 2
return math.sqrt(sum_of_squares)
if n == 0:
    c[3] += 1
    return 1
else:
    c[4] += 1
    return n * factorial(n-1)
if n <= 1:
    c[5] += 1
    return n
else:
    c[6] += 1
    return fibonacci(n-1) + fibonacci(n-2)
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
