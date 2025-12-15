#Coding Challenge 2: Program to calculate simple interest

def simple_interest(p, r, t):
    if p < 0 or r < 0 or t < 0:
        return "Invalid input"
    interest = (p * r * t) / 100
    return interest

p = 1000
r = 5
t = 2

si = simple_interest(p, r, t)
print("Simple Interest =", si)
