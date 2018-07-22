class creature:

    def __init__(self, name, values):
        self.name = name
        self.age = values[0]
        self.height = values[1]
        self.weight = values[2]
        self.exp = values[3]
        self.items = values[4]
        self.property = [self.age, self.height, self.weight, self.exp, self.items]

    def get_name(self):
        return self.name

    def get_values(self):
        return self.property

class item:

    def __init__(self, weight):
        self.weight = weight


C0001 = creature('hobbit',
                 [15, 20, 40, 2, ['boots', 'knife', 'cape', 'bottle']])
print(C0001.get_values())
print(C0001.items)
