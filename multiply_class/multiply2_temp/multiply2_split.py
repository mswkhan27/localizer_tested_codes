def multiply2(x, y, z):
    c[13] += 1
    print('Inputs: ', x, y, z)
    rxy = multiply_xy(x, y)
    if rxy == 0:
        c[9] += 1
        return 0
    else:
        c[10] += 1
        rxyz = multiply_rxy_z(rxy, z)
        print('Multiply done', rxyz)
    return rxyz
