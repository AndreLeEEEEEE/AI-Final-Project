# Initialize empty space
mapOne = [['_' for col in range(18)] for row in range(17)]
# Set enemy spawn points: 12 points
mapOne[6][3] = 2
# This is the boss tile
mapOne[10][2] = 4
mapOne[10][5] = 2
mapOne[10][17] = 2
mapOne[11][1] = 2
mapOne[11][3] = 2
mapOne[12][15] = 2
mapOne[13][2] = 2
mapOne[13][9] = 2
mapOne[14][7] = 2
mapOne[14][16] = 2
mapOne[15][9] = 2
# Set player spawn points: 6 points
mapOne[2][12] = 1
mapOne[3][11] = 1
mapOne[3][14] = 1
#mapOne[3][15] = 1
mapOne[4][13] = 1
#mapOne[4][15] = 1
#mapOne[4][16] = 1
mapOne[5][12] = 1
mapOne[5][13] = 1
#mapOne[5][17] = 1
# Set walls
mapOne[0][0] = 3
mapOne[0][1] = 3
mapOne[0][2] = 3
mapOne[0][4] = 3
mapOne[0][5] = 3
mapOne[0][6] = 3
mapOne[0][7] = 3
mapOne[0][8] = 3
mapOne[0][9] = 3
mapOne[0][10] = 3
mapOne[0][11] = 3
mapOne[0][12] = 3
mapOne[0][15] = 3
mapOne[0][16] = 3
mapOne[0][17] = 3
mapOne[1][0] = 3
mapOne[1][1] = 3
mapOne[1][2] = 3
mapOne[1][7] = 3
mapOne[1][9] = 3
mapOne[1][10] = 3
mapOne[1][15] = 3
mapOne[1][16] = 3
mapOne[1][17] = 3
mapOne[2][0] = 3
mapOne[2][2] = 3
mapOne[2][16] = 3
mapOne[2][17] = 3
mapOne[3][5] = 3
mapOne[3][6] = 3
mapOne[3][7] = 3
mapOne[4][0] = 3
mapOne[4][1] = 3
mapOne[4][3] = 3
mapOne[4][4] = 3
mapOne[4][5] = 3
mapOne[4][6] = 3
mapOne[4][7] = 3
mapOne[4][8] = 3
mapOne[5][0] = 3
mapOne[5][1] = 3
mapOne[5][3] = 3
mapOne[5][7] = 3
mapOne[5][8] = 3
mapOne[6][7] = 3
mapOne[6][8] = 3
mapOne[7][7] = 3
mapOne[7][8] = 3
mapOne[7][9] = 3
mapOne[7][10] = 3
mapOne[7][11] = 3
mapOne[7][12] = 3
mapOne[7][13] = 3
mapOne[7][14] = 3
mapOne[7][15] = 3
mapOne[7][16] = 3
mapOne[8][1] = 3
mapOne[8][2] = 3
mapOne[8][3] = 3
mapOne[8][7] = 3
mapOne[8][8] = 3
mapOne[8][9] = 3
mapOne[8][10] = 3
mapOne[8][11] = 3
mapOne[8][12] = 3
mapOne[8][13] = 3
mapOne[8][14] = 3
mapOne[9][1] = 3
mapOne[9][2] = 3
mapOne[9][3] = 3
mapOne[9][7] = 3
mapOne[9][8] = 3
mapOne[9][9] = 3
mapOne[9][10] = 3
mapOne[9][11] = 3
mapOne[9][13] = 3
mapOne[10][1] = 3
mapOne[10][3] = 3
mapOne[10][7] = 3
mapOne[10][8] = 3
mapOne[10][9] = 3
mapOne[11][9] = 3
mapOne[12][9] = 3
mapOne[12][10] = 3
mapOne[13][5] = 3
mapOne[13][6] = 3
mapOne[13][10] = 3
mapOne[13][17] = 3
mapOne[14][4] = 3
mapOne[14][5] = 3
mapOne[14][17] = 3
mapOne[15][3] = 3
mapOne[15][4] = 3
mapOne[15][5] = 3
mapOne[15][15] = 3
mapOne[15][16] = 3
mapOne[15][17] = 3
mapOne[16][2] = 3
mapOne[16][3] = 3
mapOne[16][4] = 3
mapOne[16][10] = 3
mapOne[16][14] = 3
mapOne[16][15] = 3
mapOne[16][16] = 3
mapOne[16][17] = 3

#print(mapOne)
