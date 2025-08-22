lst = [5, 2, 9, 1, 5, 6]
smallest = lst[0]
for num in lst:
    if num < smallest:
        smallest = num
print("The smallest number is:", smallest)

print("-------------------------------------")

a = lst.sort()
print("The smallest number is:", lst[0])
