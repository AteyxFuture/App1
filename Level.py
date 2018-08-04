from Item import *
from Creature import *

class Level:


    def __init__(self, ground):
        self.ground = ground

    def place(self, _object, tile):
        _object.location.remove(_object)
        ground[tile].append(_object)
        _object.location = ground[tile]
