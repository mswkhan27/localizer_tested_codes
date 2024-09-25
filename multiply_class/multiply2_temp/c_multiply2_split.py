from src.utils import Count 

def multiply2(x, y, z):
    Count.incC(13)
    print('Inputs: ', x, y, z)
    rxy = multiply_xy(x, y)
    if rxy == 0:
        Count.incC(9)
        return 0
    else:
        Count.incC(10)
        rxyz = multiply_rxy_z(rxy, z)
        print('Multiply done', rxyz)
    return rxyz
