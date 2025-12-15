# Retail Shopping - Coding Challenge 25 to 29

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

# -------- Discounts --------

# 10% discount if grand total > 10,000
if grand_total > 10000:
    discount_10 = grand_total * 0.10
    grand_total -= discount_10
    print("10% Discount Applied: ₹", discount_10)
else:
    discount_10 = 0

# 5% discount if total quantity > 20
if total_quantity > 20:
    discount_5 = grand_total * 0.05
    grand_total -= discount_5
    print("5% Quantity Discount Applied: ₹", discount_5)
else:
    discount_5 = 0

# Membership discount
member = input("\nIs the customer a member? (y/n): ").lower()

if member == 'y':
    member_discount = grand_total * 0.02
    grand_total -= member_discount
    print("2% Membership Discount Applied: ₹", member_discount)
else:
    member_discount = 0

print("\nAmount After Discounts: ₹", grand_total)

# -------- Tax Calculation --------

if grand_total < 5000:
    tax_rate = 0.05
elif grand_total <= 20000:
    tax_rate = 0.10
else:
    tax_rate = 0.15

tax_amount = grand_total * tax_rate
grand_total += tax_amount

print(f"Tax Applied ({int(tax_rate*100)}%): ₹", tax_amount)

print("\n----------------------------")
print("Final Payable Amount (Including Tax): ₹", grand_total)
