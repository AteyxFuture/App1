from Item import *
from Creature import *


class Level:


    def __init__(self, tiles_number):
        ground = []
        for i in range(tiles_number):
            ground.append([])
        self.ground = ground

    def place(self, _object, tile):
        _object.location.remove(_object)
        self.ground[tile].append(_object)
        _object.location = self.ground[tile]
        _object.level = self

    def get_left_index(self, _object):
        for i, e in enumerate(self.ground):
            if _object in e:
                return i - 1

    def get_right_index(self, _object):
        for i, e in enumerate(self.ground):
            if _object in e:
                return i + 1


L1 = Level(100)
