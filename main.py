from CharacterCreation.EnemyUnit import EnemyUnit
from CharacterCreation.PlayerUnit import PlayerUnit
from Maps.testMapThree import testMapThree as levelMap
from MetaInfo.statusBook import statusBook
from Algorithms.BFS import *
import copy

def checkLords(statusBook):
    lords = 0
    for player in statusBook["Players"]:
        if (player.getClass() == "Lord"
            and not player.getDead()): lords += 1

    return False if lords != statusBook["Lords"] else True

def unitCount(statusBook):
    playersLeft = len(list(filter(lambda unit: not unit.getDead(), statusBook["Players"])))
    enemiesLeft = len(list(filter(lambda unit: not unit.getDead(), statusBook["Enemies"])))
    
    return (playersLeft, enemiesLeft)

def PlayerArmyTurn(statusBook):
    print("---------Player turn start---------")
    for player in statusBook["Players"]:
        if not player.getDead(): player.startTurn()
    return unitCount(statusBook)

def EnemyArmyTurn(statusBook):
    print("---------Enemy turn start---------")
    for enemy in statusBook["Enemies"]:
        if not enemy.getDead(): enemy.startTurn()
    return unitCount(statusBook)

def startGame(statusBook, playerCount, enemyCount):
    isPlayerTurn = True
    endCondition = ""
    win = False
    while(playerCount > 0 and enemyCount > 0):
        if isPlayerTurn:
            playerCount, enemyCount = PlayerArmyTurn(statusBook)
        else:
            playerCount, enemyCount = EnemyArmyTurn(statusBook)
        # If any Lord player unit died
        if not checkLords(statusBook):
            endCondition = "\nA Lord unit has died."
            break
        isPlayerTurn = not(isPlayerTurn)

    if playerCount <= 0:
        endCondition = "\nThe player army was routed."
    elif enemyCount <= 0:
        endCondition = "\nThe enemy army was routed."
        win = True

    return (endCondition, win)


def main():
    # Create enemy units
    Enemies = [EnemyUnit(10) for create in range(2)]

    # Create player units
    Players = [PlayerUnit("Hector", 10), PlayerUnit("Serra", 10)]

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
    print(endMessage)
    if win: print("The player army has won!")
    else: print("The enemy army has won.")

    
if __name__ == "__main__":
    main()