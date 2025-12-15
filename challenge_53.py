n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

choice = input("Enter sorting order (asc / desc): ")

# Sorting logic
for i in range(n):
    for j in range(i + 1, n):
        if choice == "asc":
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        elif choice == "desc":
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

print("Sorted array:", arr)
