def process_and_convert(decimal_nums):
    c[11] += 1
    validated_nums = []
    for num in decimal_nums:
        c[6] += 1
        if 0 <= num <= 1_000_000:
            c[7] += 1
            validated_nums.append(num)
    return convert_list_to_hex(validated_nums)
