class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        a = self.x * self.x
        b = self.y * self.y
        c = self.z * self.z
        self.sum = a + b + c
        return self.sum
p1 = Point(1,3,5)
print("The square of sum is ",p1.sqSum())
