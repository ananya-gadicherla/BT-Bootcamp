# Input total number of items
n = int(input("Enter the total number of items bought: "))
if n <= 0:
    print("Number of items must be positive!")
    exit()

grand_total = 0
grand_qty = 0

# Loop to accept each item
for i in range(n):
    code = input("Enter the code of an item: ")
    description = input("Enter the item description: ")

    qty = int(input("Enter the quantity: "))
    if qty <= 0:
        print("Invalid quantity! Must be positive.")
        exit()

    price = float(input("Enter the price of the item: "))
    if price <= 0:
        print("Invalid price! Must be positive.")
        exit()

    total = qty * price
    grand_qty += qty

    # Promotional discounts
    if code == "PROMO10":
        total *= 0.9
    elif code == "PROMO20":
        total *= 0.8
    elif code == "PROMO50":
        total *= 0.5

    grand_total += total

print(f"\nSubtotal (before discounts): Rs. {round(grand_total,2)}")

# Discounts
if grand_total > 10000:
    discount = 0.1 * grand_total
    grand_total -= discount
    print("Availing 10% discount...")
    print(f"Discount: Rs. {round(discount,2)}")
    print(f"Total after discount: Rs. {round(grand_total,2)}")

if grand_qty > 20:
    discount = 0.05 * grand_total
    grand_total -= discount
    print("Availing additional 5% discount for high quantity...")
    print(f"Discount: Rs. {round(discount,2)}")
    print(f"Total after discount: Rs. {round(grand_total,2)}")

membership_choice = input("Do you have membership? (y/n): ").lower()
if membership_choice == 'y':
    discount = 0.02 * grand_total
    grand_total -= discount
    print("Availing additional 2% membership discount...")
    print(f"Discount: Rs. {round(discount,2)}")
    print(f"Total after discount: Rs. {round(grand_total,2)}")

# Taxation
if grand_total <= 5000:
    tax = 0.05 * grand_total
    grand_total += tax
    print(f"5% tax applied. Tax payable: Rs. {round(tax,2)}")
elif grand_total <= 20000:
    tax = 0.10 * grand_total
    grand_total += tax
    print(f"10% tax applied. Tax payable: Rs. {round(tax,2)}")
else:
    tax = 0.15 * grand_total
    grand_total += tax
    print(f"15% tax applied. Tax payable: Rs. {round(tax,2)}")

print(f"Total after tax: Rs. {round(grand_total,2)}")

# Minimum purchase check
if grand_total < 500:
    print("Minimum purchase amount is not met.")
    exit()

# Payment Mode
print("\nSelect payment mode:")
print("1. Cash")
print("2. Credit Card")
try:
    pay_mode = int(input("Enter choice (1 or 2): "))
except:
    print("Invalid input!")
    exit()

if pay_mode == 2:
    surcharge = 0.02 * grand_total
    grand_total += surcharge
    print(f"Credit Card surcharge 2% applied: Rs. {round(surcharge,2)}")
elif pay_mode == 1:
    print("No surcharge for Cash payment.")
else:
    print("Invalid payment mode choice!")
    exit()

print(f"Final payable amount: Rs. {round(grand_total,2)}")