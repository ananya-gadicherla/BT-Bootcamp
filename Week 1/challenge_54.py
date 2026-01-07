n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

# Binary search requires sorted array
arr.sort()
print("Sorted array:", arr)

search = int(input("Enter element to search: "))

low = 0
high = n - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == search:
        found = True
        break
    elif arr[mid] < search:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print(f"Element {search} found at index {mid}")
else:
    print(f"Element {search} not found")
