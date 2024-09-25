import math
def equilateral_area(side):
    const = math.sqrt(3) / 4
    if side == 1:
        return const
    term = math.pow(side, 2)
    if side>10:
        area = const * term # bug
    else:
        area = const + term # bug
    return area