from Directions import *
import math

def find_lowest_f(open):
    """Find the index of the node with the lowest f."""
    """
    open - list of nodes, the open queue
    """
    lowF = math.inf
    lowInd = None
    for index, node in enumerate(open):
        if node.get_f() < lowF:
            lowF = node.get_f()
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
        # Heuristic value
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
    """
    tile - tuple of int, value of the tile
    goal - tuple of int, the target tile
    """
    row, col = tile
    tRow, tCol = target
    return abs(tRow-row) + abs(tCol-col)

def return_tiles(queue):
    return [tile.get_coord() for tile in queue]

def Astar(field, open, target, mov):
    # Move towards the target
    # Tiles are tuples of x,y coordinates
    closed = []
    while open:
        q = open.pop(find_lowest_f(open))
        closed.append(q)

        if q.get_coord() == target:
            return q.success()

        for genTile in q.find_children(field):
            succTile = genTile.get_coord()
            if succTile == target:
                return succTile.success()
            else:
                h = 0
                manDist = manhattan_dist(succTile, target)
                # Heuristic value one - number of tiles out of place, or
                h += 1
                # Heuristic value two - sum of the distances of the tiles from their goal positions
                #h += manDist
                genTile.set_h(h)
                genTile.set_f(genTile.get_g() + genTile.get_h())

            if (succTile not in return_tiles(open)
                and succTile not in return_tiles(closed)):
                open.append(genTile)
            elif succTile in return_tiles(open):
                for tile in open:
                    if (succTile == tile.get_state()
                        and genTile.get_f() < tile.get_f()):
                        open.pop(open.index(tile))
                        open.append(genTile)
                        break

field = [['_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_'],
        ['_', '_', 'U', '_', '_'],
        ['_', '_', '_', '_', '_'],
        ['_', 'T', '_', '_', '_']]

s = Tile((2, 2))

Astar(field, [s], (4, 1), 4)