#Coding Challenge 44: Reverse of a number
#Write a program to find the reverse of a number. Store the reverse value in a different variable.
#Display the reverse.
num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)
