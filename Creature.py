class Creature:

    def __init__(self, name, age, weight, exp, inventory, health, location, level=None):
        self.name = name
        self.age = int(age)
        self.weight = int(weight)
        self.exp = int(exp)
        self.inventory = inventory
        self.health = int(health)
        self.location = location

    def get_name(self):
        return self.name

    def take_item(self, item):
        item.location.remove(item)
        self.inventory.append(item)
        item.location = self.inventory

    def drop_item(self, item):
        self.inventory.remove(item)

    def use_item(self, item):
        item.use(self)

    def heal(self, severity):
        self.health += severity

    def hurt(self, severity):
        self.health -= severity

    def move_left(self):
        self.location.place(self, self.location.get_left_index(self))

    def move_right(self):
        self.level.place(self, self.level.get_right_index(self))

path = ("Creature_list.txt")
with open(path) as file:
    text = file.read()

creatures = text.split('\n')
for i, e in enumerate(creatures):
    creatures[i] = e.split('\t')

def make_creature(name, age, weight, exp, inventory, health, location):
    creature = Creature(name, age, weight, exp, inventory, health, location)
    return creature

for i, e in enumerate(creatures):
    creatures[i] = make_creature(e[0], e[1], e[2], e[3], eval(e[4]), e[5], eval(e[6]))

creatures_ref = creatures[:]
