#print the multiple of 3 and 5 ,must be divisible by 15

for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i,end=" ")
print("\n------------------")
for i in range(15,101,15):
    print(i,end=" ")
