#Coding Challenge 1: Program to find the sum and average of two variables


def sum_and_average(a, b):
    sum_value = a + b
    average = sum_value / 2
    return sum_value, average

sum, avg = sum_and_average(10, 20)
print("Sum =", sum)
print("Average =", avg)


#TestCases
#a = 0, b = 0
#a = 0, b = 10
#a = -10, b = -20
#a = -10, b = 20
#a = 2.5, b = 3.5
#a = 1_000_000, b = 2_000_000 
