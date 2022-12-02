from CharacterCreation.EnemyUnit import EnemyUnit
from CharacterCreation.PlayerUnit import PlayerUnit
from Maps.testMapTwo import testMapTwo as levelMap
from MetaInfo.addrBook import addrBook
from Algorithms.BFS import *

def PlayerArmyTurn(field, players):
    for coord in players:
        unit = field[coord[0], coord[1]]
    return ()

def EnemyArmyTurn(field, enemies):
    for coord in enemies:
        unit = field[coord[0], coord[1]]
    return ()

def startGame(field, addrBook, playerCount, enemyCount):
    isPlayerTurn = True
    while(playerCount > 0 and enemyCount > 0):
        if isPlayerTurn:
            playerCount, enemyCount = PlayerArmyTurn(field, addrBook["Players"])
            isPlayerTurn = not(isPlayerTurn)
        else:
            playerCount, enemyCount = EnemyArmyTurn(field, addrBook["Enemies"])
            isPlayerTurn = not(isPlayerTurn)

def main():
    # Enemies = [EnemyUnit(10) for create in range(1)]
    # # Add boss unit
    # Enemies.append(EnemyUnit(12, True))
    # for enemy in Enemies: enemy.levelUp()
    # for enemy in Enemies:
    #     print(enemy._name)
    #     print(enemy._stats)

    # Players = [PlayerUnit("Eliwood", 10), PlayerUnit("Hector", 10),
    #             PlayerUnit("Serra", 10), PlayerUnit("Sain", 10),
    #             PlayerUnit("Kent", 10)]

    enemyID = 97
    Enemies = [EnemyUnit(10, chr(enemyID+create)) for create in range(1)]
    for enemy in Enemies: enemy.levelUp()

    Players = [PlayerUnit("Eliwood", 10, chr(65))]
    for player in Players: player.levelUp()

    # Spawn all units on the map
    rowNum = len(levelMap)
    colNum = len(levelMap[0])
    enemyAlloc = 0
    playerAlloc = 0
    for i in range(rowNum):
        for j in range(colNum):
            if levelMap[i][j] == 1:
                levelMap[i][j] = Players[playerAlloc]
                addrBook.update({Players[playerAlloc]: (i, j)})
                Players[playerAlloc].setTile((i, j))
                playerAlloc += 1
            elif levelMap[i][j] == 2:
                levelMap[i][j] = Enemies[enemyAlloc]
                addrBook.update({Enemies[enemyAlloc]: (i, j)})
                Enemies[enemyAlloc].setTile((i, j))
                enemyAlloc += 1
    
    #print(levelMap)

    field = [['_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', PlayerUnit("Eliwood", 10, chr(65))],
        ['_', '_', 1, '_', '_'],
        ['_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_']]

    print("Final result:", BFS(field, (2, 2), 1, [1], 2))
    #startGame(levelMap, addrBook, len(Players), len(Enemies))

    
if __name__ == "__main__":
    main()