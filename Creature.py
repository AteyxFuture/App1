from Item import *


class Creature:

    def __init__(self, name, age, weight, exp, inventory):
        self.name = name
        self.age = int(age)
        self.weight = int(weight)
        self.exp = int(exp)
        self.inventory = inventory
        self.property = [self.age, self.weight, self.exp, self.inventory]

    def get_name(self):
        return self.name

    def get_values(self):
        return self.property

    def take_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)

    def use_item(self, item):
        item.use()


path = ("Creature_list.txt")
with open(path) as file:
    text = file.read()

creatures = text.split('\n')
for i, e in enumerate(creatures):
    creatures[i] = e.split('\t')

def make_creature(name, age, weight, exp, inventory):
    creature = Creature(name, age, weight, exp, inventory)
    return creature

for i, e in enumerate(creatures):
    creatures[i] = make_creature(e[0], e[1], e[2], e[3], eval(e[4]))
