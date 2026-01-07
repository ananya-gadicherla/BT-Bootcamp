n = int(input("Enter the number of elements: "))

arr = []
total = 0

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)
    total += element   # adding each element to sum

print("Array elements:", arr)
print("Sum of all elements:", total)
