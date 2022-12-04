from CharacterCreation.EnemyUnit import EnemyUnit
from CharacterCreation.PlayerUnit import PlayerUnit
from Maps.testMapThree import testMapThree as levelMap
from MetaInfo.statusBook import statusBook
from Algorithms.BFS import *
import copy

def checkLords(statusBook):
    lords = 0
    for player in statusBook["Players"]:
        if player.getClass() == "Lord": lords += 1

    return False if lords != statusBook["Lords"] else True

def updateInfo(statusBook):
    """Remove dead units from statusBook."""
    # For player units
    playerCopy = copy.deepcopy(statusBook["Players"])
    for player in statusBook["Players"]:
        if player.getDead(): playerCopy.remove(player)
    statusBook["Players"] = playerCopy
    # For enemy units
    enemyCopy = copy.deepcopy(statusBook["Enemies"])
    for enemy in statusBook["Enemies"]:
        if enemy.getDead(): enemyCopy.remove(enemy)
    statusBook["Enemies"] = enemyCopy

def PlayerArmyTurn(statusBook):
    for player in statusBook["Players"]:
        player.startTurn()
        updateInfo(statusBook)
    return len(statusBook["Players"])

def EnemyArmyTurn(statusBook):
    for enemy in statusBook["Enemies"]:
        enemy.startTurn()
        updateInfo(statusBook)
    return len(statusBook["Enemies"])

def startGame(statusBook, playerCount, enemyCount):
    isPlayerTurn = True
    endCondition = ""
    win = False
    while(playerCount > 0 and enemyCount > 0):
        if isPlayerTurn:
            playerCount = PlayerArmyTurn(statusBook)
        else:
            enemyCount = EnemyArmyTurn(statusBook)
        # If any Lord player unit died
        if not checkLords(statusBook):
            endCondition = "A Lord unit has died."
            break
        isPlayerTurn = not(isPlayerTurn)

    if playerCount <= 0:
        endCondition = "The player army was routed."
    elif enemyCount <= 0:
        endCondition = "The enemy army was routed."
        win = True

    return (endCondition, win)


def main():
    # Create enemy units
    enemyID = 97
    Enemies = [EnemyUnit(10, chr(enemyID+create)) for create in range(1)]

    # Create player units
    Players = [PlayerUnit("Eliwood", 10, chr(65))]

    # Spawn all units on the map
    rowNum = len(levelMap)
    colNum = len(levelMap[0])
    enemyAlloc = 0
    playerAlloc = 0
    for i in range(rowNum):
        for j in range(colNum):
            if levelMap[i][j] == 1:
                levelMap[i][j] = Players[playerAlloc]
                statusBook["Players"].append(Players[playerAlloc])
                Players[playerAlloc].setTile((i, j))
                Players[playerAlloc].levelUp()
                if Players[playerAlloc].getClass() == "Lord": statusBook["Lords"] += 1
                playerAlloc += 1
            elif levelMap[i][j] == 2:
                levelMap[i][j] = Enemies[enemyAlloc]
                statusBook["Enemies"].append(Enemies[enemyAlloc])
                Enemies[enemyAlloc].setTile((i, j))
                Enemies[enemyAlloc].levelUp()
                enemyAlloc += 1
    
    endMessage, win = startGame(statusBook, len(Players), len(Enemies))
    if win:
        print("\nThe player army has won!")
    else:
        print("\nThe enemy army has won.")
    print(endMessage)

    
if __name__ == "__main__":
    main()