row = int(input("Enter an number: "))

for i in range(row):
    print(" " * (row - i - 1) + "*" * (2 * i + 1))

for i in range(row - 1, -1, -1):
    print(" " * (row - i - 1) + "*" * (2 * i + 1))

