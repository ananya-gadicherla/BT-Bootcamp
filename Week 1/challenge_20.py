#Coding Challenge 20: Display the Series 1,2,4,7,11,16,22…N

n = int(input("Enter a positive integer N: "))

term = 1  
increment = 1

while term <= n:
    print(term, end=" ")
    increment += 1
    term += increment - 1 
