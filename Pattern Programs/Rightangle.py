num = int(input("Enter an number: "))

for i in range(num+1):
    for j in range(i):
        print("*",end="")
    print("")

print("------------------")

for i in range(num,0,-1):
    for j in range(i):
        print("*",end="")
    print("")
