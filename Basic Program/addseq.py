"""
adding an whole integer 
Input = 245
Output = 2+4+5 =11

"""

num=int(input("Enter the number: "))
sum = 0
while num != 0:
    digit = num % 10
    sum = sum + digit
    num = int(num / 10)
print("Sum of integer is : ",sum)