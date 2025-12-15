#Coding Challenge 21: Display the Series 1,4,9,25,36,49,81…N

n = int(input("Enter N: "))

i = 1
while i * i <= n:
    square = i * i
    if square % 16 != 0:   # skip 16, 64, etc.
        print(square, end=" ")
    i += 1
