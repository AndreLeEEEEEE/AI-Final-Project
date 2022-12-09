from CharacterCreation.EnemyUnit import EnemyUnit
from CharacterCreation.PlayerUnit import PlayerUnit
from Maps.mapOne import mapOne as levelMap
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

def PlayerArmyTurn(statusBook, turn):
    write("---------Player turn start---------")
    write(f"Turn: {turn}")
    for player in statusBook["Players"]:
        if not player.getDead(): player.startTurn()
    return unitCount(statusBook)

def EnemyArmyTurn(statusBook, turn):
    write("---------Enemy turn start---------")
    write(f"Turn: {turn}")
    for enemy in statusBook["Enemies"]:
        if not enemy.getDead(): enemy.startTurn()
    return unitCount(statusBook)

def startGame(statusBook, playerCount, enemyCount):
    isPlayerTurn = True
    endCondition = ""
    win = False
    turns = 1
    while(playerCount > 0 and enemyCount > 0):
        if isPlayerTurn:
            playerCount, enemyCount = PlayerArmyTurn(statusBook, turns)
        else:
            playerCount, enemyCount = EnemyArmyTurn(statusBook, turns)
        turns += 1
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

    return (endCondition, win, turns)

def main():
    # Delete old text files in Results
    if os.path.exists("Results/roster.txt"): os.remove("Results/roster.txt")
    if os.path.exists("Results/turns.txt"): os.remove("Results/turns.txt")

    # Create enemy units
    Enemies = [EnemyUnit(10) for create in range(11)]
    boss = EnemyUnit(12, True)

    # Create player units
    Players = [PlayerUnit("Hector", 10), PlayerUnit("Kent", 10),
                PlayerUnit("Nino", 10), PlayerUnit("Rebecca", 10),
                PlayerUnit("Sain", 10), PlayerUnit("Serra", 10)]

    # Spawn all units on the map
    rowNum = len(levelMap)
    colNum = len(levelMap[0])
    enemyAlloc = 0
    playerAlloc = 0
    for i in range(rowNum):
        for j in range(colNum):
            if levelMap[i][j] == 1:
                player = Players[playerAlloc]
                levelMap[i][j] = player
                statusBook["Players"].append(player)
                player.setTile((i, j))
                player.levelUp()
                writeUnit(player)
                if player.getClass() == "Lord": statusBook["Lords"] += 1
                playerAlloc += 1
            elif levelMap[i][j] == 2:
                enemy = Enemies[enemyAlloc]
                levelMap[i][j] = enemy
                statusBook["Enemies"].append(enemy)
                enemy.setTile((i, j))
                enemy.levelUp()
                writeUnit(enemy)
                enemyAlloc += 1
            elif levelMap[i][j] == 4:
                levelMap[i][j] = boss
                statusBook["Enemies"].append(boss)
                boss.setTile((i, j))
                boss.levelUp()
                writeUnit(boss)
    
    write("1 is a player unit\n2 is an enemy unit\n3 is an untraversable wall\n")
    write("Inital state of the level:")
    writeMap(levelMap)
    endMessage, win, turns = startGame(statusBook, len(Players), len(Enemies))
    write("Result:")
    write(f"After {turns} turns")
    write(endMessage)
    if win:
        write("The player army has won")
        write("What's left of the winning army:")
        for player in statusBook["Players"]:
            if not player.getDead(): write(player.getName())
    else:
        write("The enemy army has won.")
        write("What's left of the winning army:")
        for enemy in statusBook["Enemies"]:
            if not enemy.getDead(): write(enemy.getName())

    
if __name__ == "__main__":
    main()