class Room(object):
    def __init__(self, north: bool, south: bool, east: bool, west: bool):
        # These variables determine if the room has exits in each direction.
        self.north = north
        self.south = south
        self.east = east
        self.west = west
