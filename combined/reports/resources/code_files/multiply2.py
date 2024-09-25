print("Inputs: ", x, y, z)
rxy = 0
rxyz = 0
# y + y + y....+ y, x times
#x*y
for i in range(abs(x)):
    c[6] += 1
    if (x>=0):
        c[7] += 1
        rxy = rxy + y
    else:
        c[8] += 1
        rxy = -(rxy + y)
    print("rxy: ", rxy)
#res + res + res + ...+ res, c times
#rxy*z
for j in range(abs(z)):
    c[9] += 1
    if (z >= 0):
        c[10] += 1
        rxyz = rxyz + rxy
    else:
        c[11] += 1
        rxyz = rxyz+rxy
    print("rxyz: ", rxyz)
print("multiply done", rxyz)
return rxyz
