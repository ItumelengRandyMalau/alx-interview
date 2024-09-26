#!/usr/bin/python3
"""
Function to find the perimeter of an island represented in a grid.
"""

def island_perimeter(grid):
    """
    Calculates the perimeter of the island in the grid.
    
    Args:
        grid (list): A list of lists where 1 represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0  # Initialize counter to track the perimeter
    row = len(grid)  # Total number of rows in the grid
    column = len(grid[0]) if row else 0  # Total number of columns in the grid

    # Loop through every cell in the grid
    for i in range(row):
        for j in range(column):

            # If the current cell is land (1)
            if grid[i][j] == 1:
                # Check top neighbor
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check bottom neighbor
                if i == row - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check left neighbor
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check right neighbor
                if j == column - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter  # Return the total calculated perimeter

