def med(u: int, v: int, w: int):
    #Apply adjustments to the transformed value based on additional conditions.
    
    # Example adjustment: If x is negative, subtract y squared from the value
    med = w
    if v < w: #fault: was <
        if u < w: #was u < v
            med = v
        elif u < w:
            med = u
    elif u > v:
        med = v
    elif u > w:
        med = u
    return med

def multiply2(x, y, z):
    print("Inputs: ", x, y, z)
    rxy = 0
    rxyz = 0

    # y + y + y....+ y, x times
    #x*y
    for i in range(abs(x)):
        if (x>=0):
            rxy = rxy + y
        else:
            rxy = -(rxy + y)
        print("rxy: ", rxy)

    #res + res + res + ...+ res, c times
    #rxy*z
    for j in range(abs(z)):
        if (z >= 0):
            rxyz = rxyz + rxy
        else:
            rxyz = rxyz+rxy
        print("rxyz: ", rxyz)
    print("multiply done", rxyz)
    return rxyz





def main(x, y, z):
    a=1
    b=1
    if a==1:
        multiply2(x, y, z)

    if b==1:
        med(x, y, z)
