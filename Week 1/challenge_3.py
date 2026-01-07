#Coding Challenge 3: Program to calculate the discount on the total amount

def calculate_discount(total_amount, discount_percent):
    discount = (total_amount * discount_percent) / 100
    final_amount = total_amount - discount
    return discount, final_amount


amount = 2000
discount_percent = 10

discount, payable_amount = calculate_discount(amount, discount_percent)

print("Discount =", discount)
print("Final Amount =", payable_amount)

