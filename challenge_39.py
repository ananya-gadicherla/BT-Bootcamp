n = int(input("Enter number of rows: "))

num = 1  # current number to square

for i in range(1, n + 1):  # rows
    row_nums = []
    for j in range(i):  # numbers in the row
        square = num * num
        # Alternate sign: odd positions negative, even positions positive
        if j % 2 == 0:
            row_nums.append(square)
        else:
            row_nums.append(-square)
        num += 1
    print(" ".join(str(x) for x in row_nums))
