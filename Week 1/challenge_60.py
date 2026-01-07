# Level 7: Services & Costs
services = ["General Consultation", "Blood Test", "Covid Test", "X-Ray", "CT Scan", "MRI"]
costs = [500, 300, 800, 1500, 4000, 7000]

# Level 1: Patient Details
name = input("Enter patient name: ")
age = int(input("Enter patient age: "))
gender = input("Enter patient gender: ")
contact = input("Enter patient contact number: ")

# Level 2: Display services for selection
print("\nAvailable Services:")
i = 0
while i < 6:
    print(str(i+1) + ". " + services[i])
    i += 1

# Patient selects services
selected_services = []
selected_costs = []

num_services = int(input("How many services do you want to select? "))
count = 0
while count < num_services:
    service_num = int(input("Enter service number (1-6): "))
    if service_num >= 1 and service_num <= 6:
        selected_services.append(services[service_num - 1])
        selected_costs.append(costs[service_num - 1])
        count += 1
    else:
        print("Invalid service number! Try again.")

# Level 4: Calculate subtotal
subtotal = 0
i = 0
while i < num_services:
    subtotal += selected_costs[i]
    i += 1

# Level 8: Discounts
discount = 0

# Senior Citizen Discount
if age >= 60:
    discount = discount + (0.10 * subtotal)

# High-Bill Discount
if subtotal - discount > 5000:
    discount = discount + (0.05 * (subtotal - discount))

subtotal_after_discount = subtotal - discount

# Level 5: Apply GST
gst = 0.18 * subtotal_after_discount
grand_total = subtotal_after_discount + gst

# Level 6: Display Invoice
print("\n-----------------------------------------------")
print("HealWell Care Hospital")
print("Patient Invoice")
print("-----------------------------------------------")
print("Patient Information:")
print("Name: " + name)
print("Age: " + str(age))
print("Gender: " + gender)
print("Contact: " + contact)
print("\nServices Availed:")

i = 0
while i < num_services:
    print(selected_services[i] + ": ₹" + str(selected_costs[i]))
    i += 1

print("\nSubtotal: ₹" + str(subtotal))
if discount > 0:
    print("Discount: ₹" + str(round(discount,2)))
print("GST (18%): ₹" + str(round(gst,2)))
print("Grand Total: ₹" + str(round(grand_total,2)))
print("\nThank you for choosing HealWell Care Hospital!")
print("-----------------------------------------------")
