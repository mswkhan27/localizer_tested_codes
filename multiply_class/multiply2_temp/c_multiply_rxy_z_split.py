from src.utils import Count 

def multiply_rxy_z(rxy, z):
    Count.incC(12)
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
            rxyz = rxyz - rxy
        print('rxyz: ', rxyz)
    return rxyz
