n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

# Assume first element is minimum
minimum = arr[0]

# Compare with remaining elements
for num in arr:
    if num < minimum:
        minimum = num

print("Array elements:", arr)
print("Minimum value:", minimum)
