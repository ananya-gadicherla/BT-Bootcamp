#Coding Challenge 8: To find the largest of 3 numbers

def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


x = 10
y = 25
z = 15

largest = largest_of_three(x, y, z)
print(f"The largest number is {largest}")


#other way
#def largest_of_three(a, b, c):
#   return max(a, b, c)
