num=int(input("enter a number:"))
for i in range(10):
    if i==num:
        print("Your allowed",num)
        continue
    else:
        print("your not allowed")