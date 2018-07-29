from Item import *


class Creature:

    def __init__(self, name, age, height, weight, exp, items):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.exp = exp
        self.items = items
        self.property = [self.age, self.height, self.weight, self.exp, self.items]

    def get_name(self):
        return self.name

    def get_values(self):
        return self.property


path = ("Creature_list.txt")
with open(path) as file:
    text = file.read()

def make_creature(name, age, height, weight, exp, items):
    
C0001 = Creature('hobbit',15, 20, 40, 2, [items[0][0], items[1][0], items[2][0], items[1][1]])
print(C0001.get_values())
print(C0001.items)
