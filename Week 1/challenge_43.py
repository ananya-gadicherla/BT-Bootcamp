#Coding Challenge 43: Whole and Fraction value separation
#Write a program to accept a double value. Separate the whole value from the fractional value and
#store them in two variables. Display the same

num = float(input("Enter a number: "))

whole_part = int(num)
fractional_part = num - whole_part

print("Whole part:", whole_part)
print("Fractional part:", fractional_part)
