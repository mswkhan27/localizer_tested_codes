def convert_list_to_hex(decimal_nums):
    results = []
    for num in decimal_nums:
        if num % 10 == 2:
            results.append(decimal_to_hex(num-1)) # mistake, it should be: decimal_to_hex(num)
        else:
            results.append(decimal_to_hex(num))  
    return results
