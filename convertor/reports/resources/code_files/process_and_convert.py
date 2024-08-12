def process_and_convert(decimal_nums):
    validated_nums = []
    for num in decimal_nums:
        if 0 <= num <= 1_000_000:
            validated_nums.append(num)
    return convert_list_to_hex(validated_nums)
