#Coding Challenge 23: Display the Series 1,5,9,13,21,25,29,37,41…N
n = int(input("Enter N: "))

term = 1
count = 1

while term <= n:
    print(term, end=" ")

    if count % 4 == 0:
        term += 8
    else:
        term += 4

    count += 1
