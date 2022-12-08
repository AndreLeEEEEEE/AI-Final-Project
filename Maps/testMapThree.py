# A map of two tiles. Each tile is a unit spawn point. One enemy unit and one player unit

# Initialize empty space
testMapThree = [['_' for col in range(8)] for row in range(8)]
# Set enemy spawn points
testMapThree[0][0] = 2
testMapThree[1][1] = 2
# Set player spawn points
testMapThree[7][7] = 1
testMapThree[6][6] = 1

# [[ 2 , '_', '_', '_', '_', '_', '_', '_'], 
#  ['_',  2 , '_', '_', '_', '_', '_', '_'],
#  ['_', '_', '_', '_', '_', '_', '_', '_'],
#  ['_', '_', '_', '_', '_', '_', '_', '_'],
#  ['_', '_', '_', '_', '_', '_', '_', '_'],
#  ['_', '_', '_', '_', '_', '_',  1 , '_'],
#  ['_', '_', '_', '_', '_', '_', '_',  1 ]]

#print(testMapThree)