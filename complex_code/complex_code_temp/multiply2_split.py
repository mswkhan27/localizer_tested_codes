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
