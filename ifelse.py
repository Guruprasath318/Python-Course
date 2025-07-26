#calculator for if-else statements
arith= input("Enter the operation (+, -, *, /): ") 
num1= float(input("Enter first number: "))
num2= float(input("Enter second number: "))

if arith == '+':
    result = num1 + num2
    print
elif arith == '-':
    result = num1 - num2
    print(result)
elif arith == '*':
    result = num1 * num2
    print(result)
elif arith == '/':
    result = num1 / num2
    print(result)
else:
    result = None
    print("Invalid operation")
