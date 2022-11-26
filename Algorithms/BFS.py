from Directions import *

def BFS(field, unit, mov):
    # Scan the map for the closest target
    # Tiles are tuples of x,y coordinates
    visited = []
    queue = [unit]

    while mov >= 0:
        toBeQueued = []
        for tile in queue:
            appRules = applicable_rules(field, tile)
            for rule in appRules:
                newTile = rule(tile)
                if newTile not in visited and newTile not in toBeQueued:
                    toBeQueued.append(newTile)
        visited += queue
        queue.clear()
        queue += toBeQueued
        mov -= 1

    print(visited)

field = [['_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_'],
        ['_', '_', 'U', '_', '_'],
        ['_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_']]

BFS(field, (2, 2), 3)
