def decimal_to_hex(n):
    c[9] += 1
    if n == 0:
        c[1] += 1
        return "0"
    hex_str = ""
    while n > 0:
        c[2] += 1
        x = n % 16
        hex_str = digit_to_hex(x) + hex_str
        n = n // 16
    return hex_str
