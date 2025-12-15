#Coding Challenge 19: Display the Series 4,16,36,64…N

n = int(input("Enter a positive integer N: "))

i = 2
while i*i <= n:
    print(i*i, end=" ")
    i += 2 
