import math

class Triangle():
    def __init__(self, a):
        self.a = a

    def area(self):
        return (self.a ** 2 * math.sqrt(3)) * (1/4)
    
t1 = Triangle(4)
print(t1.area())
