def decimal_to_hex(n):
    if n == 0:
        return "0"
    hex_str = ""
    while n > 0:
        x = n % 16
        hex_str = digit_to_hex(x) + hex_str
        n = n // 16
    return hex_str
