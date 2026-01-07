#Coding Challenge 22: Display the Series 1,4,7,12,23…N
n = int(input("Enter N: "))

term = 1
increment = 3

while term <= n:
    print(term, end=" ")
    term = term + increment
    increment = increment * 2 - 1
