def convert_list_to_hex(decimal_nums):
    c[10] += 1
    results = []
    for num in decimal_nums:
        c[3] += 1
        if num % 10 == 2:
            c[4] += 1
            results.append(decimal_to_hex(num-1)) # mistake, it should be: decimal_to_hex(num)
        else:
            c[5] += 1
            results.append(decimal_to_hex(num))  
    return results
