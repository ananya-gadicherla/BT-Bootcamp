# Retail Shopping - Coding Challenge 25 & 26

grand_total = 0

n = int(input("Enter number of items: "))

for i in range(1, n + 1):
    print(f"\nEnter details for item {i}")

    item_code = input("Enter item code: ")
    description = input("Enter item description: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))

    item_total = quantity * price
    grand_total += item_total

    print("Item Total: ₹", item_total)

print("\n----------------------------")
print("Grand Total: ₹", grand_total)
