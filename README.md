# AI-Final-Project

Make the enemy army full of generic units.

Make the player army full of named units.

The enemy AI will have three states: passive, aggro, heal
- Passive: The unit will stay on their starting tile
- Aggro (Exclusive to offensive classes): The unit will move towards the closest player unit to attack
- Heal (Exclusive to support classes): The unit will move towards an injured ally unit and heal them  

The player AI will have three states: aggro, retreat, and heal
- Aggro (Exclusive to offensive classes): The unit will move towards the closest enemy unit to attack
- Retreat: The unit will move away from enemy units and use their healing item
- Heal (Exclusive to support classes): The unit will move towards an injured ally unit and heal them

Offensive units will use the breadth-first algorithm to find the nearest enemy unit to attack.
Support units will use the breadth-first algorithm to find the nearest injured ally unit to heal.
All units will use the A* algorithm to move to their target.
