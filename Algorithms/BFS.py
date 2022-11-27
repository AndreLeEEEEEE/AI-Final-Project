from Directions import *

def scan(field, tile, target, RNG):
    """From the current tile, scan for targets in range."""
    """
    tile - tuple of int, a tile the unit could stand on
    target - int, an enemy to attack or an injured ally to heal
    RNG - tuple of int, the range at which a unit can attack
    """
    r, c = tile
    for num in RNG:
        if num == 1:
            try: 
                if field[r+1][c] == target: return True
            except: pass
            try:
                if field[r-1][c] == target: return True
            except: pass
            try:
                if field[r][c+1] == target: return True
            except: pass
            try:
                if field[r][c-1] == target: return True
            except: pass
        else:
            try:
                if field[r+2][c] == target: return True
            except: pass
            try:
                if field[r-2][c] == target: return True
            except: pass
            try:
                if field[r][c+2] == target: return True
            except: pass
            try:
                if field[r][c-2] == target: return True
            except: pass
            try:
                if field[r+1][c+1] == target: return True
            except: pass
            try:
                if field[r-1][c+1] == target: return True
            except: pass
            try:
                if field[r+1][c-1] == target: return True
            except: pass
            try:
                if field[r-1][c-1] == target: return True
            except: pass
    return False

def BFS(field, unit, target, RNG):
    """Scan the map for the closest target"""
    """
    field - list of list of int/char, the map
    unit - tuple of int, the unit's current position
    target - int, an enemy to attack or an injured ally to heal
    RNG - tuple of int, the range at which the unit can act
    """
    visited = []
    queue = [unit]

    while queue:
        toBeQueued = []
        for tile in queue:
            print("From this tile", tile)
            if scan(field, tile, target, RNG):
                    return tile
            appRules = applicable_rules(field, tile)
            for rule in appRules:
                newTile = rule(tile)
                if newTile not in visited and newTile not in toBeQueued:
                    print(newTile)
                    toBeQueued.append(newTile)
        visited += queue
        queue.clear()
        queue += toBeQueued

    return "No target found"

field = [['_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', 2],
        ['_', '_', 'U', '_', '_'],
        ['_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_']]

# field = [['_', 'V', 'V', 'V', '_'],
#         ['V', 'V', 'V', 'V', '2'],
#         ['V', 'V', 'U', 'V', 'V'],
#         ['_', 'V', 'V', 'V', '_'],
#         ['_', '_', 'V', '_', '_']]

# Find the closest enemy
print("Final result:", BFS(field, (2, 2), 2, [1, 2]))

# Find the closest ally
