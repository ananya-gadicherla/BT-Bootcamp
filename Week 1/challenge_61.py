n = 15 

first = 5
second = 6

print(first, end=", ")
print(second, end=", ")

for i in range(n - 2):
    c = first+second
    print(c, end=", ")
    first = second
    second = c

