# Simple map with walls scattered across the middle

# Initialize empty space
testMapOne = [['_' for col in range(18)] for row in range(18)]
# Set enemy spawn points
testMapOne[0][0] = 2
testMapOne[0][17] = 2
testMapOne[0][8] = 2
testMapOne[0][10] = 2
testMapOne[1][3] = 2
testMapOne[1][4] = 2
testMapOne[1][14] = 2
testMapOne[2][8] = 2
# Set player spawn points
testMapOne[17][0] = 1
testMapOne[17][17] = 1
testMapOne[17][8] = 1
testMapOne[17][10] = 1
testMapOne[16][3] = 1
testMapOne[16][14] = 1
testMapOne[15][8] = 1
# Set walls
testMapOne[8][4] = 3
testMapOne[8][5] = 3
testMapOne[7][8] = 3
testMapOne[7][6] = 3
testMapOne[6][3] = 3
testMapOne[6][4] = 3
testMapOne[9][7] = 3
testMapOne[5][8] = 3
testMapOne[12][10] = 3
testMapOne[11][14] = 3
testMapOne[10][15] = 3
testMapOne[10][13] = 3
testMapOne[11][15] = 3
testMapOne[12][14] = 3
testMapOne[13][9] = 3
testMapOne[13][8] = 3

print(testMapOne)