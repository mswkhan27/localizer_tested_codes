def med(u: int, v: int, w: int):
    def nested_compare(a, b, c):
        # Intentional bug: Incorrect comparison logic
        if a < b:
            c[1] += 1
            if c > b:  # This should be c < b to maintain correct median logic
                c[2] += 1
                return b
            else:
                c[3] += 1
                return c
        else:
            c[4] += 1
            if a < c:
                c[5] += 1
                return a
            else:
                c[6] += 1
                return c
    def is_ordered(a, b, c):
        return a <= b <= c
    # Reworked median logic with nested functions
    if is_ordered(u, v, w) or is_ordered(w, v, u):
        c[7] += 1
        return v
    if is_ordered(v, u, w) or is_ordered(w, u, v):
        c[8] += 1
        return u
    return nested_compare(u, v, w)
