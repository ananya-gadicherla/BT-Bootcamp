# Retail Shopping - Coding Challenge 25, 26 & 27

grand_total = 0
total_quantity = 0

n = int(input("Enter number of items: "))

for i in range(1, n + 1):
    print(f"\nEnter details for item {i}")

    item_code = input("Enter item code: ")
    description = input("Enter item description: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))

    item_total = quantity * price
    grand_total += item_total
    total_quantity += quantity

    print("Item Total: ₹", item_total)

print("\nInitial Grand Total: ₹", grand_total)

# Discount 1: 10% if grand total > 10,000
discount = 0
if grand_total > 10000:
    discount = grand_total * 0.10
    grand_total -= discount
    print("10% Discount Applied: ₹", discount)

# Discount 2: 5% if total quantity > 20
quantity_discount = 0
if total_quantity > 20:
    quantity_discount = grand_total * 0.05
    grand_total -= quantity_discount
    print("Additional 5% Quantity Discount Applied: ₹", quantity_discount)

print("\n----------------------------")
print("Final Payable Amount: ₹", grand_total)
