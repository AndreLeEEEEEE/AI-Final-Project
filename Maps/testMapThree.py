# A map of two tiles. Each tile is a unit spawn point. One enemy unit and one player unit

# Initialize empty space
testMapThree = [['_' for col in range(5)] for row in range(5)]
# Set enemy spawn points
testMapThree[0][0] = 2
# Set player spawn points
testMapThree[4][4] = 1

# [[ 2 , '_', '_', '_', '_'], 
#  ['_', '_', '_', '_', '_'],
#  ['_', '_', '_', '_', '_'],
#  ['_', '_', '_', '_', '_'],
#  ['_', '_', '_', '_',  1 ]]

#print(testMapThree)