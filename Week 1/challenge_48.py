n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

# Assume first element is maximum
maximum = arr[0]

# Compare with remaining elements
for num in arr:
    if num > maximum:
        maximum = num

print("Array elements:", arr)
print("Maximum value:", maximum)
