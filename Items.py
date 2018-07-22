class item:
'''

Items are objects that fall into various specific categories.
(0) Weapons:
Can be used for various purposes and their specific value determines the damage
they are going to cause on hit.
(1) Wearables:
Items that creatures can wear eihter as means of protection or for aesthetic
purpouses. Their specific value determines their durability.
(2) Containers:
Items that can be filled with other items. Their specific value describes
the maximum weight of items they are able to hold.'''

    def __init__(self, weight, item_type, specific):
        self.weight = weight
        self.item_type = item_type
        self.specific = specific

knife = item(3, 0)
boots = item(4, 1)
cape = item(2, 1)
bottle = item(4, 2)
