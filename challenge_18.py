#Coding Challenge 18: Display the Series 1,3,5,7,9…N

n = int(input("Enter a positive integer N: "))

for i in range(1, n + 1, 2):  # start=1, step=2
    print(i, end=" ")
