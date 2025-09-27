# a number is a multiple of 3 or 5 if its is divisible by either 3 or 5

for i in range(1,31):
    if i%3==0 or i%5==0:
        print(i,end=" ")
