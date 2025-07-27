num=int(input("enter a number:"))
for i in range(100):
    if i==num:
        print("Your allowed",num)
        break
    else:
        print("your not allowed")