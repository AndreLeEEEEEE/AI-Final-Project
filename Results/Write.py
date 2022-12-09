def write(string):
    with open("Results/turns.txt", "a") as f:
        f.write(f"{string}\n")

def writeUnit(unit):
    with open("Results/roster.txt", "a") as f:
        f.write(f"Name: {unit._name}\n")
        if unit._side == 1:
            f.write(f"Class: {unit._class}\n")
        else:
            f.write(f"Class: {unit._name}\n")
        f.write(f"Type: {unit._type}\n")
        if unit._side == 1:
            f.write(f"Army: Player\n")
        else:
            f.write(f"Army: Enemy\n")
        f.write(f"Level: {unit._level}\n")
        f.write(f"HP: {unit._stats['MaxHP']}\n")
        f.write(f"STR: {unit._stats['STR']}\n")
        f.write(f"MAG: {unit._stats['MAG']}\n")
        f.write(f"DEF: {unit._stats['DEF']}\n")
        f.write(f"RES: {unit._stats['RES']}\n")
        f.write(f"SPD: {unit._stats['SPD']}\n")
        f.write(f"SKL: {unit._stats['SKL']}\n")
        f.write(f"MOV: {unit._stats['MOV']}\n")
        f.write("\n")

def writeMap(map):
    with open("Results/turns.txt", "a") as f:
        f.write("\n")
        rowNum = len(map)
        colNum = len(map[0])
        for i in range(rowNum):
            # Print numbers on the first column
            f.write(str((i - 17) * -1) + " ")
            for j in range(colNum):
                if map[i][j] == '_': cell = "_ "
                elif map[i][j] == 3: cell = "3 "
                elif map[i][j].get_side() == 1: cell = "1 "
                elif map[i][j].get_side() == 2: cell = "2 "
                f.write(cell)
            f.write("\n")
        for k in range(colNum+1):
            # Put nothing in the bottom-left corner
            if k == 0: cell = "  "
            # Print letters along the bottom
            else: cell = f" {chr(k+64)}"
            f.write(cell)
        f.write("\n\n")
