from CharacterCreation.EnemyUnit import EnemyUnit
from CharacterCreation.PlayerUnit import PlayerUnit

def main():
    yan = EnemyUnit(10)
    yan.setTraits()
    yan.levelUp()
    print(yan._class)
    print(yan._stats)
    
if __name__ == "__main__":
    main()