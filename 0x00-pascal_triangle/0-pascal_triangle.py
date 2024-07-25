def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        List[List[int]]: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []  # Return an empty list for non-positive n

    triangle = []  # Initialize an empty list to store the rows

    for i in range(n):
        row = [1] * (i + 1)  # Create a new row with i + 1 elements, all initialized to 1
        for j in range(1, i):
            # Update the middle elements based on the sum of elements from the previous row
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)  # Add the row to the triangle

    return triangle

def print_triangle(triangle):
    """
    Prints the Pascal's Triangle.

    Args:
        triangle (List[List[int]]): The Pascal's Triangle to print.
    """
    for row in triangle:
        print("[{}]".format(", ".join(map(str, row))))

# Example usage
#if __name__ == "__main__":
#   print_triangle(pascal_triangle(5))
