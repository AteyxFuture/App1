from Item import *


class Creature:

    def __init__(self, name, age, weight, exp, inventory, health):
        self.name = name
        self.age = int(age)
        self.weight = int(weight)
        self.exp = int(exp)
        self.inventory = inventory
        self.health = int(health)

    def get_name(self):
        return self.name

    def take_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)

    def use_item(self, item):
        item.use(self)

    def heal(self, severity):
        self.health += severity

    def hurt(self, severity):
        self.health -= severity

path = ("Creature_list.txt")
with open(path) as file:
    text = file.read()

creatures = text.split('\n')
for i, e in enumerate(creatures):
    creatures[i] = e.split('\t')

def make_creature(name, age, weight, exp, inventory, health):
    creature = Creature(name, age, weight, exp, inventory, health)
    return creature

for i, e in enumerate(creatures):
    creatures[i] = make_creature(e[0], e[1], e[2], e[3], eval(e[4]), e[5])
