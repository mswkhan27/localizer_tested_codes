c[11] += 1
if x == 0 or y == 0:
    c[1] += 1
    return 0
rxy = 0
for i in range(abs(x)):
    c[2] += 1
    if x >= 0:
        c[3] += 1
        rxy = rxy + y
    else:
        c[4] += 1
        rxy = -(rxy + y)
    print('rxy: ', rxy)
return rxy
c[12] += 1
if rxy == 0 or z == 0:
    c[5] += 1
    return 0
rxyz = 0
for j in range(abs(z)):
    c[6] += 1
    if z >= 0:
        c[7] += 1
        rxyz = rxyz + rxy
    else:
        c[8] += 1
        rxyz = rxyz - rxy
    print('rxyz: ', rxyz)
return rxyz
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
