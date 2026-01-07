n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

reversed_arr = []

for i in range(n - 1, -1, -1): #range(start, stop, step)
    reversed_arr.append(arr[i])

print("Original array:", arr)
print("Reversed array:", reversed_arr)

