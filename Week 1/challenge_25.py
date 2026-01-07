# Retail Shopping - Coding Challenge 25

item_code = input("Enter item code: ")
description = input("Enter item description: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))

total_cost = quantity * price

print("\nItem Details")
print("Item Code:", item_code)
print("Description:", description)
print("Quantity:", quantity)
print("Price per Item: ₹", price)
print("Total Cost: ₹", total_cost)
