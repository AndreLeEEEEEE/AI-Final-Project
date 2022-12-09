def translate(indices):
    """Convert 2D array indices to chess notation."""
    """
    indices - tuple of int, the indices for a 2D array
    """
    row, col = indices
    row = (row - 17) * -1
    col += 65
    return f"{chr(col)}{row}"
