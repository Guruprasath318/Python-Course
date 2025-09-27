# print an odd number in a given sequences

num = int(input("Enter a number: "))

#Method 1
for i in range(1,num,2):
    print(i,end=" ")

#Method 2
for i in range(num):
    if i%2 != 0:
        print(i,end=" ")

#Method 3
for i in range(1,num):
    print(2*i-1,end=" ")
