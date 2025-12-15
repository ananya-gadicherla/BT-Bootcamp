rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element [{i}][{j}]: "))
        row.append(element)
    matrix.append(row)

search = int(input("Enter the element to search: "))

found = False

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == search:
            found = True
            break
    if found:
        break

print("\n2D Array:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

if found:
    print(f"\nElement {search} found in the 2D array")
else:
    print(f"\nElement {search} not found in the 2D array")
