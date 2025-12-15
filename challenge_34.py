n = int(input("Enter number of rows: "))

print("\nStar Pattern")
for i in range(n):
    print("*" * n)

print("\nSame Number Pattern")
for i in range(1, n + 1):
    print(str(i) * n)

print("\nSequence Number Pattern")
for i in range(n):
    for j in range(1, n + 1):
        print(j, end="")
    print()
