from CharacterCreation.EnemyUnit import EnemyUnit
from CharacterCreation.PlayerUnit import PlayerUnit
from MetaInfo.matchUpMatrix import mum
from MetaInfo.addrBook import addrBook

def main():
    Enemies = [EnemyUnit(10) for create in range(11)]
    # Add boss unit
    Enemies.append(EnemyUnit(12, True))
    for enemy in Enemies: enemy.levelUp()
    for enemy in Enemies:
        print(enemy._name)
        print(enemy._stats)

    
    Players = [PlayerUnit("Eliwood", 10), PlayerUnit("Hector", 10),
                PlayerUnit("Serra", 10), PlayerUnit("Sain", 10),
                PlayerUnit("Kent", 10)]
    
if __name__ == "__main__":
    main()