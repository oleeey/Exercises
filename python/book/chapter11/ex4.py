
class Hexagon():
    def __init__(self, a):
        self.a = a

    def calculate_perimeter(self):
        return self.a * 6
    
h1 = Hexagon(6)
print(h1.calculate_perimeter())