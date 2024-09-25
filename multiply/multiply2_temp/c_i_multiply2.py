from src.utils import Count 

def multiply_xy(x, y):
    Count.incC(10)
    if x == 0 or y == 0:
        Count.incC(1)
        return 0
    rxy = 0
    for i in range(abs(x)):
        Count.incC(2)
        if x >= 0:
            Count.incC(3)
            rxy = rxy + y
        else:
            Count.incC(4)
            rxy = -(rxy + y)
        print("rxy: ", rxy)
    return rxy

def multiply_rxy_z(rxy, z):
    Count.incC(11)
    if rxy == 0 or z == 0:
        Count.incC(5)
        return 0
    rxyz = 0
    for j in range(abs(z)):
        Count.incC(6)
        if z >= 0:
            Count.incC(7)
            rxyz = rxyz + rxy
        else:
            Count.incC(8)
            rxyz = rxyz + rxy
        print("rxyz: ", rxyz)
    return rxyz

def multiply2(x, y, z):
    Count.incC(12)
    print("Inputs: ", x, y, z)
    rxy = multiply_xy(x, y)
    if(rxy==0):
        return 0
    else:
        Count.incC(9)
        rxyz = multiply_rxy_z(rxy, z)
        print("multiply done", rxyz)
    return rxyz
