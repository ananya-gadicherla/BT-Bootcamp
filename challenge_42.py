#Coding Challenge 42: Generate Series - 1, -5, 9, -13, 17, -21, ... N
n = int(input("Enter N: "))

num = 1

for i in range(1, n + 1):
    if i % 2 == 0:
        print(-num, end=" ")
    else:
        print(num, end=" ")
    num += 4
