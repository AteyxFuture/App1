class Item:
    
    '''Items are objects that fall into various specific categories.
    (0) Weapons:
    Can be used for various purposes and their specific value determines the damage
    they are going to cause on hit.
    (1) Wearables:
    Items that creatures can wear eihter as means of protection or for aesthetic
    purpouses. Their specific value determines their durability.
    (2) Containers:
    Items that can be filled with other items. Their specific value describes
    the maximum weight of items they are able to hold. They use the self.contents
    attribute for holding other items.
    (3) Consumables:
    Items that can be consumed to gain health. Their specific value determines the
    number of health point they are going to recover.
    '''


    def __init__(self, name, weight, item_type, specific):
        self.name = name
        self.weight = int(weight)
        self.item_type = int(item_type)
        self.specific = int(specific)
        self._contents = []

    def get_name(self):
        if len(self._contents) > 0:
            full_name = []
            for i in self._contents:
                full_name.append(i.name)
            full_name_str = self.name + " with " + ', '.join(full_name)
            return full_name_str
        else:
            return self.name

    def get_weight(self):
        if self.item_type == 2:
            total_weight = 0
            for i in self._contents:
                total_weight += i.get_weight()
            return total_weight + self.weight
        else:
            return self.weight

    def add(self, item):
        if isinstance(item, Item) == True and self.item_type == 2:
            if (self.get_weight()-self.weight+item.get_weight()) <= self.specific:
                self._contents.append(item)
                return str(item.name + ' added to ' + self.name + '.')
            else:
                return str('Not enough space in ' + self.name + ' to hold this item!')
        elif isinstance(item, Item) == False:
            return str(self.name + ' is only able to hold items!')
        elif self.item_type != 2:
            return str(self.name + ' cannot hold other items!')

    def empty(self):
        if self.item_type == 2:
            self._contents.clear()
            return str(self.name + ' is now empty.')
        else:
            return str(self.name + ' cannot hold other items!')

    def remove(self, item):
        if self.item_type == 2:
            self._contents.remove(item)
            return str(item.name + ' removed from ' + self.name + '.')
        else:
            return str(self.name + ' cannot hold other items!')

    def use(self):
        pass


    @property
    def contents(self):
        return ('{' + ', '.join([str(item) for item in self._contents]) + '}')

path = "Item_list.txt"
with open(path) as file:
    text = file.read()

items = text.split('\n\n')
for i, e in enumerate(items):
    items[i] = e.split('\n')

for i, e in enumerate(items):
    for j, f in enumerate(e):
        e[j] = f.split('\t')

item_type_0 = items[0]
item_type_1 = items[1]
item_type_2 = items[2]
item_type_3 = items[3]
items = [item_type_0, item_type_1, item_type_2, item_type_3]


def make_item(name, weight, item_type, specific):
    item = Item(name, weight, item_type, specific)
    return item

done = []

for i, e in enumerate(items):
    for j, f in enumerate(e):
        e[j] = make_item(f[0], f[1], f[2], f[3])


