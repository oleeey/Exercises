
class Square():
    square_list = []

    def __init__(self, l):
        self.length = l
        self.square_list.append(l)

    def __repr__(self):
        return """{sq} by {sq} by {sq} by {sq}
               """.format(sq = self.length)

sq1 = Square(4)
print(Square.square_list)
print(sq1)


sq2 = Square(8)

def isSameObj(obj1, obj2):
    if obj1 is obj2:
        return True
    else:
        return False

print(isSameObj(sq1,sq2))
sq3 = sq1
print(isSameObj(sq1,sq3))