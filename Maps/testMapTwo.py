# A map of two tiles. Each tile is a unit spawn point. One enemy unit and one player unit

# Initialize empty space
testMapTwo = [['_' for col in range(2)] for row in range(1)]
# Set enemy spawn points
testMapTwo[0][0] = 2
# Set player spawn points
testMapTwo[0][1] = 1

#print(testMapTwo)