# Input dimensions for first matrix
r1 = int(input("Enter number of rows for Matrix 1: "))
c1 = int(input("Enter number of columns for Matrix 1: "))

# Input dimensions for second matrix
r2 = int(input("Enter number of rows for Matrix 2: "))
c2 = int(input("Enter number of columns for Matrix 2: "))

# Check if multiplication is possible
if c1 != r2:
    print("Matrix multiplication not possible! Columns of Matrix 1 must equal rows of Matrix 2.")
else:
    # Input Matrix 1
    matrix1 = []
    print("\nEnter elements for Matrix 1:")
    for i in range(r1):
        row = []
        for j in range(c1):
            row.append(int(input(f"Matrix1[{i}][{j}]: ")))
        matrix1.append(row)

    # Input Matrix 2
    matrix2 = []
    print("\nEnter elements for Matrix 2:")
    for i in range(r2):
        row = []
        for j in range(c2):
            row.append(int(input(f"Matrix2[{i}][{j}]: ")))
        matrix2.append(row)

    # Initialize result matrix with zeros
    result = []
    for i in range(r1):
        result.append([0] * c2)

    # Multiply matrices
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    # Display result
    print("\nMatrix 1:")
    for row in matrix1:
        print(row)

    print("\nMatrix 2:")
    for row in matrix2:
        print(row)

    print("\nResult of multiplication:")
    for row in result:
        print(row)
