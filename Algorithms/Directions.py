def pre_up(field, row, col):
    """Check if the unit can move up."""
    newRow = row - 1
    # If out of bounds
    if newRow < 0: return False
    # If there's already something there
    if field[newRow][col] != '_': return False 
    return True

def pre_down(field, row, col):
    """Check if the unit can move down."""
    newRow = row + 1
    # If out of bounds
    if newRow >= len(field): return False
    # If there's already something there
    if field[newRow][col] != '_': return False 
    return True

def pre_left(field, row, col):
    """Check if the unit can move left."""
    newCol = col - 1
    # If out of bounds
    if newCol < 0: return False
    # If there's already something there
    if field[row][newCol] != '_': return False
    return True

def pre_right(field, row, col):
    """Check if the unit can move right."""
    newCol = col + 1
    # If out of bounds
    if newCol >= len(field[0]): return False
    # If there's already something there
    if field[row][newCol] != '_': return False
    return True

def up(tile):
    """Move unit one tile up"""
    row, col = tile
    return (row - 1, col)

def down(tile):
    """Move unit one tile down"""
    row, col = tile
    return (row + 1, col)

def left(tile):
    """Move unit one tile left"""
    row, col = tile
    return (row, col - 1)

def right(tile):
    """Move unit one tile right"""
    row, col = tile
    return (row, col + 1)

def applicable_rules(field, tile):
    """Find which rules are applicable from a tile."""
    applicable = []
    row, col = tile
    # Get the blank's position
    if pre_up(field, row, col):
        applicable.append(up)
    if pre_down(field, row, col):
        applicable.append(down)
    if pre_left(field, row, col):
        applicable.append(left)
    if pre_right(field, row, col):
        applicable.append(right)

    return applicable