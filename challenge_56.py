rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
total_sum = 0

for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element [{i}][{j}]: "))
        row.append(element)
        total_sum += element
    matrix.append(row)

print("\n2D Array:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

print("\nSum of all elements in the 2D array:", total_sum)
