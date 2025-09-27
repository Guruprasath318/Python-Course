num = int(input("Enter a number: "))
count=0
#Method 1
print(f"Divisors of {num} are: ",end=" ")
for i in range(1,num+1):
    if num%i==0:
        print(i,end=" ")
        count+=1

print(f"\nTotal number of divisors are: {count}")

