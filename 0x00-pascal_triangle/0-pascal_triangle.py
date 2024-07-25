from math import factorial

def pascal_triangle(num_rows):
    triangle = []
    for n in range(num_rows):
        row = [1] * (n + 1)
        for r in range(1, n):
            row[r] = triangle[n - 1][r - 1] + triangle[n - 1][r]
        triangle.append(row)
    return triangle

#def print_triangle(triangle):
#    for row in triangle:
 #       print(" ".join(map(str, row)))

# Example usage
#num_rows = 5
#triangle = pascal_triangle(num_rows)
#print_triangle(triangle)

