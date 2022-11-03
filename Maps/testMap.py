# Initialize empty space
testMap = [['_' for col in range(18)] for row in range(18)]
# Set enemy spawn points
testMap[0][0] = '2'
testMap[0][17] = '2'
testMap[0][8] = '2'
testMap[0][10] = '2'
testMap[1][3] = '2'
testMap[1][4] = '2'
testMap[1][14] = '2'
testMap[2][8] = '2'
# Set player spawn points
testMap[17][0] = '1'
testMap[17][17] = '1'
testMap[17][8] = '1'
testMap[17][10] = '1'
testMap[16][3] = '1'
testMap[16][14] = '1'
testMap[15][8] = '1'
# Set walls
testMap[8][4] = '3'
testMap[8][5] = '3'
testMap[7][8] = '3'
testMap[7][6] = '3'
testMap[6][3] = '3'
testMap[6][4] = '3'
testMap[9][7] = '3'
testMap[5][8] = '3'
testMap[12][10] = '3'
testMap[11][14] = '3'
testMap[10][15] = '3'
testMap[10][13] = '3'
testMap[11][15] = '3'
testMap[12][14] = '3'
testMap[13][9] = '3'
testMap[13][8] = '3'

print(testMap)