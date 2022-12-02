from Algorithms.Directions import *

def scan(field, unit, tile, target, RNG, side):
    """From the current tile, scan for targets in range."""
    """
    field - list of list of int/char, the map
    unit - tuple of int, the tile unit is currently on
    tile - tuple of int, a tile the unit could stand on
    target - int, an enemy to attack or an injured ally to heal
    RNG - tuple of int, the range at which a unit can attack
    side - int, the side the calling unit is on
    """
    def checkTile(row, col):
        # If the calling unit is a player unit
        if side == 1:
            try:
                position = field[row][col]
                # Look for injured ally
                if ((row, col) != unit 
                    and target == 1 
                    and position.get_side() == 1):
                    if (position._stats["HP"] < position._stats["MaxHP"]):
                        return True
                # Look for enemy
                elif ((row, col) != unit and target == 2 and position.get_side() == 2):
                    return True
                else:
                    return False
            except:
                return False
        # If the calling unit is an enemy unit
        else:
            try:
                position = field[row][col]
                # Look for injured ally
                if ((row, col) != unit 
                    and target == 2 
                    and position.get_side() == 2):
                    if (position._stats["HP"] < position._stats["MaxHP"]):
                        return True
                # Look for enemy
                elif ((row, col) != unit and target == 1 and position.get_side() == 1):
                    return True
                else:
                    return False
            except:
                return False

    r, c = tile
    for num in RNG:
        if num == 1:
            if checkTile(r+1, c): return True
            if checkTile(r-1, c): return True
            if checkTile(r, c+1): return True
            if checkTile(r, c-1): return True
        else:
            if checkTile(r+2, c): return True
            if checkTile(r-2, c): return True
            if checkTile(r, c+2): return True
            if checkTile(r, c-2): return True
            if checkTile(r+1, c+1): return True
            if checkTile(r+1, c-1): return True
            if checkTile(r-1, c+1): return True
            if checkTile(r-1, c-1): return True
    return False

def BFS(field: list, unit: tuple, target: int, RNG: list, side: int):
    """Scan the map for the closest target."""
    """
    field - list of list of int/char, the map
    unit - tuple of int, the unit's current position
    target - int, an enemy to attack or an injured ally to heal
    RNG - tuple of int, the range at which the unit can act
    side - int, the side the calling unit is on
    """
    visited = []
    queue = [unit]

    while queue:
        toBeQueued = []
        for tile in queue:
            if scan(field, unit, tile, target, RNG, side):
                # The tile from which a unit can interact with a target
                return tile
            appRules = applicable_rules(field, tile)
            for rule in appRules:
                newTile = rule(tile)
                if newTile not in visited and newTile not in toBeQueued:
                    toBeQueued.append(newTile)
        visited += queue
        queue.clear()
        queue += toBeQueued

    return "No target found"

field = [['_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', 1],
        ['_', '_', 1, '_', '_'],
        ['_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_']]

# field = [['_', 'V', 'V', 'V', '_'],
#         ['V', 'V', 'V', 'V', '2'],
#         ['V', 'V', 'U', 'V', 'V'],
#         ['_', 'V', 'V', 'V', '_'],
#         ['_', '_', 'V', '_', '_']]
