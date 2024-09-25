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
