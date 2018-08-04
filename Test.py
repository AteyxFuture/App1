from Level import *

creatures[0].take_item(items[0][0])
creatures[0].take_item(items[1][0])
creatures[0].take_item(items[3][0])

print(creatures_ref[0])
L1.place(creatures_ref[0], 0)
print(creatures_ref[0].level.ground)
creatures_ref[0].move_right()
print(creatures_ref[0].level.ground)
