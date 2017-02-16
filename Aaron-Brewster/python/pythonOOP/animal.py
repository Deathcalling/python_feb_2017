class animal(object):

    def __init__(self, name, stam = 100):
        self.name = name
        self.stam = stam

    def walk(self):
        self.stam -= 1
        return self

    def run(self):
        self.stam -= 5
        return self

    def displayS(self):
        print(self.stam, self.name)

class dog(animal):

    def __init__(self, name, stam = 150):
        self.name = name
        self.stam = stam

    def pet(self):
        self.stam += 5
        return self
        
animal = animal(animal)

animal.walk().walk().walk().run().run().displayS()

ruff = dog(dog)

ruff.run().run().pet().pet().pet().displayS()
