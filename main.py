from CharacterCreation.EnemyUnit import EnemyUnit
from CharacterCreation.PlayerUnit import PlayerUnit
from Maps.testMapTwo import testMapTwo
from MetaInfo.addrBook import addrBook

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

    Enemies = [EnemyUnit(10) for create in range(1)]
    for enemy in Enemies: enemy.levelUp()

    Players = [PlayerUnit("Eliwood", 10)]
    for player in Players: player.levelUp()

    rowNum = len(testMapTwo)
    colNum = len(testMapTwo[0])
    enemyAlloc = 0
    playerAlloc = 0
    for i in range(rowNum):
        for j in range(colNum):
            if testMapTwo[i][j] == 1:
                testMapTwo[i][j] = Players[playerAlloc]
                addrBook["Players"].append((i, j))
            elif testMapTwo[i][j] == 2:
                testMapTwo[i][j] = Enemies[enemyAlloc]
                addrBook["Enemies"].append((i, j))
    
    print(testMapTwo)
    startGame(testMapTwo, addrBook, len(Players), len(Enemies))

    
if __name__ == "__main__":
    main()