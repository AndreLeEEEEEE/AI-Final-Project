from Algorithms.Directions import *
import math

def find_lowest_f(open):
    """Find the index of the tile with the lowest f."""
    """
    open - list of Tile, the open queue
    """
    lowF = math.inf
    lowInd = None
    for index, tile in enumerate(open):
        if tile.get_f() < lowF:
            lowF = tile.get_f()
            lowInd = index

    return lowInd


class Tile:
    def __init__(self, coord, parent=None, rule=None, F=0, H=0):
        # x,y coordinates of the tile
        self.coord = coord
        # Parent tile
        self.parent = parent
        # Rule taken from parent to this tile
        self.rule = rule
        # F value
        self.F = F
        # Heuristic value (optimistic)
        self.H = H

    def get_coord(self):
        return self.coord

    def set_f(self, calculation):
        self.F = calculation

    def set_h(self, calculation):
        self.H = calculation

    def get_f(self):
        return self.F

    def get_g(self):
        # Cost taken to reach this tile from the start
        tile = self
        G = 0
        while tile:
            tile = tile.parent
            G += 1
        return G

    def get_h(self):
        return self.H

    def find_children(self, field):
        children = []
        appRules = applicable_rules(field, self.coord)
        for rule in appRules:
            newTile = rule(self.coord)
            if self.parent and newTile == self.parent.get_coord():
                continue
            else:
                children.append(Tile(newTile, self, rule))

        return children
            
    def success(self):
        tile = self
        appliedRules = []
        while tile:
            appliedRules.append(tile.rule)
            tile = tile.parent
        return list(reversed(appliedRules))[1:]

def manhattan_dist(tile, target):
    """Get the Manhattan distance between a tile and the target."""
    """(Ignores walls and unit positions)"""
    """
    tile - tuple of int, value of the tile
    target - tuple of int, the target tile
    """
    row, col = tile
    tRow, tCol = target
    return int(abs(tRow-row) + abs(tCol-col))

def return_tiles(queue):
    """Get the list of coordinates of all tiles in the queue."""
    return [tile.get_coord() for tile in queue]

def Astar(field, open, target):
    """Find path to target."""
    """
    field - list of list of int/char, the map
    open - list of Tile, tiles to investigate/expand
    target - tuple of int, the tile the unit is trying to reach
    """
    closed = []
    while open:
        q = open.pop(find_lowest_f(open))
        # print("From this tile: ", q.get_coord())
        closed.append(q)

        if q.get_coord() == target:
            return q.success()

        for genTile in q.find_children(field):
            succTile = genTile.get_coord()
            # print(succTile)
            if succTile == target:
                return genTile.success()
            else:
                manDist = manhattan_dist(succTile, target)
                genTile.set_h(manDist)
                genTile.set_f(genTile.get_g() + genTile.get_h())

            if (succTile not in return_tiles(open)
                and succTile not in return_tiles(closed)):
                open.append(genTile)
            elif succTile in return_tiles(open):
                for tile in open:
                    if (succTile == tile.get_coord()
                        and genTile.get_f() < tile.get_f()):
                        open.pop(open.index(tile))
                        open.append(genTile)
                        break

field = [['_', '_', '_', '_', '_'],
        ['_', '_', '_', 'U', '_'],
        ['_', 'W', 'W', 'W', '_'],
        ['_', '_', '_', '_', '_'],
        ['_', '_', '_', 'W', '_']]


def moveTowardsTarget(field: list, unit: tuple, target: int, mov: int):
    """Move as close to the target as possible with the given MOV."""
    """
    field - list of list of int/char, the map
    unit - tuple of int, the tile the unit is on
    target - tuple of int, the tile to move to
    mov - int, the number of tiles the unit can move
    """
    path = Astar(field, [Tile(unit)], target)
    # print(path)
    newPosition = list(unit)
    for m in range(mov):
        # print(path[m])
        newPosition = list(path[m](newPosition))
        # Prevent invalid indexing when the unit needs less
        # movement than they have to reach the target
        if tuple(newPosition) == target:
            break
    return tuple(newPosition)
