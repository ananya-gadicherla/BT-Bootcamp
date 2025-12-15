from math import factorial

n = int(input("Enter number of rows: "))

num = 1  # starting number for factorial

for i in range(1, n + 1):  # row number
    row_nums = []
    for j in range(i):  # numbers in the row
        row_nums.append(factorial(num))
        num += 1
    print(" ".join(str(x) for x in row_nums))
