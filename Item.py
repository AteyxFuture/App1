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

    def __str__(self):
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

    @property
    def contents(self):
        return ('{' + ', '.join([str(item) for item in self._contents]) + '}')

path = "C:/Users/a/Documents/GitHub/App1/Item_list.txt"
with open(path) as Item_list:
    text = Item_list.read()

items = text.split('\n')
for i in range(len(items)):
    items[i] = items[i].split(', ')

I0000 = Item(items[0][0], items[0][1], items[0][2], items[0][3])
I0001 = Item(items[1][0], items[1][1], items[1][2], items[1][3])
I0002 = Item(items[2][0], items[2][1], items[2][2], items[2][3])
I0003 = Item(items[3][0], items[3][1], items[3][2], items[3][3])
I0004 = Item(items[4][0], items[4][1], items[4][2], items[4][3])
I0005 = Item(items[5][0], items[5][1], items[5][2], items[5][3])

'''bottle.add(water)
print(bottle.get_weight())
print(bottle.contents)
chest.add(bottle)
print(chest.get_weight())
print(chest.contents)
'''
