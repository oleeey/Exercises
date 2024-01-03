
class Horse():
    def __init__(self, n, o):
        self.name = n
        self.owner = o

class Rider():
    def __init__(self, n):
        self.name = n

john = Rider("John")
molly = Horse("Molly", john)

print(molly.owner.name)