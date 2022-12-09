from CharacterCreation.EnemyUnit import EnemyUnit
from CharacterCreation.PlayerUnit import PlayerUnit
from Maps.testMapThree import testMapThree as levelMap
from MetaInfo.statusBook import statusBook
from Algorithms.BFS import *
from Results.Write import *
import os

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
    write("---------Player turn start---------")
    for player in statusBook["Players"]:
        if not player.getDead(): player.startTurn()
    return unitCount(statusBook)

def EnemyArmyTurn(statusBook):
    write("---------Enemy turn start---------")
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
        writeMap(levelMap)
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
    # Delete old text files in Results
    if os.path.exists("Results/roster.txt"): os.remove("Results/roster.txt")
    if os.path.exists("Results/turns.txt"): os.remove("Results/turns.txt")

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
                writeUnit(Players[playerAlloc])
                if Players[playerAlloc].getClass() == "Lord": statusBook["Lords"] += 1
                playerAlloc += 1
            elif levelMap[i][j] == 2:
                levelMap[i][j] = Enemies[enemyAlloc]
                statusBook["Enemies"].append(Enemies[enemyAlloc])
                Enemies[enemyAlloc].setTile((i, j))
                Enemies[enemyAlloc].levelUp()
                writeUnit(Enemies[enemyAlloc])
                enemyAlloc += 1
    
    write("1 is a player unit\n2 is an enemy unit\n3 is an untraversable wall\n")
    write("Inital state of the level:")
    writeMap(levelMap)
    endMessage, win = startGame(statusBook, len(Players), len(Enemies))
    write("Result:")
    write(endMessage)
    if win: write("The player army has won!")
    else: write("The enemy army has won.")

    
if __name__ == "__main__":
    main()