from Algorithms.Directions import *

def scan(field: list, unit: tuple, tile: tuple, target: int, RNG: list, side: int):
    """From the current tile, scan for targets in range."""
    """
    field - list of list of int/char, the map
    unit - tuple of int, the tile unit is currently on,
            used so the unit doesn't target themselves
    tile - tuple of int, a tile the unit could stand on
    target - int, an enemy to attack or an injured ally to heal
    RNG - list of int, the range at which a unit can attack
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
            if checkTile(r+1, c): return (r+1, c)
            if checkTile(r-1, c): return (r-1, c)
            if checkTile(r, c+1): return (r, c+1)
            if checkTile(r, c-1): return (r, c-1)
        else:
            if checkTile(r+2, c): return (r+2, c)
            if checkTile(r-2, c): return (r-2, c)
            if checkTile(r, c+2): return (r, c+2)
            if checkTile(r, c-2): return (r, c-2)
            if checkTile(r+1, c+1): return (r+1, c+1)
            if checkTile(r+1, c-1): return (r+1, c-1)
            if checkTile(r-1, c+1): return (r-1, c+1)
            if checkTile(r-1, c-1): return (r-1, c-1)
    return False

def BFS(field: list, unit: tuple, target: int, RNG: list, side: int, MOV = False):
    """Scan the map for the closest target."""
    """
    field - list of list of int/char, the map
    unit - tuple of int, the unit's current position
    target - int, an enemy to attack or an injured ally to heal
    RNG - list of int, the range at which the unit can act
    side - int, the side the calling unit is on
    MOV - int/False, if int, denotes the level at which BFS should stop
    """
    visited = []
    queue = [unit]
    # Indicates which level BFS is on
    mov = 0

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
        # Stop BFS if it doesn't find a target within these Moves
        if type(MOV) is int:
            mov += 1
            if mov >= MOV:
                break

    return False
