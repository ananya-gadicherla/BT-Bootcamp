n = int(input("Enter number of rows: "))

a, b = 1, 1  # first two Fibonacci numbers
count = 0     # keeps track of numbers printed

for i in range(1, n + 1):  # for each row
    row_nums = []
    for j in range(i):  # number of elements = row number
        if count == 0:
            row_nums.append(a)
        elif count == 1:
            row_nums.append(b)
        else:
            c = a + b
            row_nums.append(c)
            a, b = b, c
        count += 1
    print(" ".join(str(num) for num in row_nums))
