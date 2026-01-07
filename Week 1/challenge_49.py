n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

search = int(input("Enter the element to search: "))

found = False

for num in arr:
    if num == search:
        found = True
        break

print("Array elements:", arr)

if found:
    print(f"Element {search} found in the array")
else:
    print(f"Element {search} not found in the array")
