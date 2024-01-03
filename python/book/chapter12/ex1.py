
class Shape():
    def what_am_i(self):
        print("I am a shape")


class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return 2 * (self.width + self.length)
    


class Square(Shape):
    def __init__(self, l):
        self.length = l

    def calculate_perimeter(self):
        return 4 * self.length
    
    def change_size(self, num):
        self.length += num


    


rec1 = Rectangle(4,8)
print(rec1.calculate_perimeter())

sq1 = Square(5)
print(sq1.calculate_perimeter())
sq1.change_size(-2)
print(sq1.length)
print(sq1.calculate_perimeter())

rec1.what_am_i()


    
    
    

    