# Input dimensions
rows = int(input("Enter number of rows (M): "))
cols = int(input("Enter number of columns (N): "))

# Create the matrix
matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element [{i}][{j}]: "))
        row.append(element)
    matrix.append(row)

# Display original matrix
print("\nOriginal Matrix:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

# Compute transpose
transpose = []

for j in range(cols):
    new_row = []
    for i in range(rows):
        new_row.append(matrix[i][j])
    transpose.append(new_row)

# Display transpose
print("\nTranspose of the Matrix:")
for row in transpose:
    for element in row:
        print(element, end=" ")
    print()
