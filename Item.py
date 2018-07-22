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
    '''


    def __init__(self, name, weight, item_type, specific):
        self.name = name
        self.weight = weight
        self.item_type = item_type
        self.specific = specific
        if self.specific == 2:
            self.contents = {}

    def get_weight(self):
        if self.item_type == 2:
            total_weight = 0
            for i in self.contents:
                total_weight += i.get_weight
            return total_weight
        else:
            return self.weight

    def add(self, item):
        if instance(item, Item):
            if (self.get_weight+item.get_weight) <= self.specific:
                self.contents.add(item)
            else:
                return str('Not enough space in' + self.name + 'to hold this item!')
        else:
            return str(self.name + 'is only able to hold items!')

knife = Item(3, 0)
boots = Item(4, 1)
cape = Item(2, 1)
bottle = Item(4, 2)
