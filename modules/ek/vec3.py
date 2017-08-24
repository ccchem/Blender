import math

class Vec3:

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)


    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"


    @staticmethod
    def distance(v1, v2):
        dx = v2.x - v1.x
        dy = v2.y - v1.y
        dz = v2.z - v1.z
        
        return math.sqrt(dx*dx + dy*dy + dz*dz)
