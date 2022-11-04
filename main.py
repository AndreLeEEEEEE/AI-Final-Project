from CharacterCreation.EnemyUnit import EnemyUnit
from CharacterCreation.PlayerUnit import PlayerUnit

def main():
    print("New")
    Enemies = [EnemyUnit(10) for create in range(11)]
    # Add boss unit
    Enemies.append(EnemyUnit(12, True))
    print("After level ups")
    for enemy in Enemies: enemy.levelUp()
    for enemy in Enemies:
        print(enemy._name)
        print(enemy._stats)

    
    ban = PlayerUnit("Eliwood", 10)
    ban.levelUp()
    print(ban._name)
    print(ban._class)
    print(ban._stats)
    
if __name__ == "__main__":
    main()