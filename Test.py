from Creature import *

creatures[0].take_item(items[0][0])
creatures[0].take_item(items[1][0])
creatures[0].take_item(items[3][0])

creatures[0].use_item(creatures[0].inventory[2])

for i in creatures[0].inventory:
    print(i.get_name())

