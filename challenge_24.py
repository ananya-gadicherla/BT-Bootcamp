#Coding Challenge 24: Display the Series 1,1,2,3,5,8,13,21…N

n = int(input("Enter N: "))

a = 1
b = 1

while a <= n:
    print(a, end=" ")
    a, b = b, a + b
