class Multiplier:
    def multiply_xy(self, x, y):
        if x == 0 or y == 0:
            return 0
        rxy = 0
        for i in range(abs(x)):
            if x >= 0:
                rxy = rxy + y
            else:
                rxy = -(rxy + y)
            print("rxy: ", rxy)
        return rxy

    def multiply_rxy_z(self, rxy, z):
        if rxy == 0 or z == 0:
            return 0
        rxyz = 0
        for j in range(abs(z)):
            if z >= 0:
                rxyz = rxyz + rxy
            else:
                rxyz = rxyz - rxy  # Corrected logic for negative z
            print("rxyz: ", rxyz)
        return rxyz

    def multiply2(self, x, y, z):
        print("Inputs: ", x, y, z)
        rxy = self.multiply_xy(x, y)
        if rxy == 0:
            return 0
        else:
            rxyz = self.multiply_rxy_z(rxy, z)
            print("Multiply done", rxyz)
        return rxyz