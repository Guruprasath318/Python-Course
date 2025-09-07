number = int(input("Enter an number: "))
last_digit = number % 10

if last_digit == 5:
    print(f"{number} is divisible by 5..")
elif last_digit == 0:
    print(f"{number} is divisible by 10..")
elif last_digit == 2 or number % 2 == 0:
    print(f"{number} is divisible by 2..")
elif number:
    print(f"{number} is divisible by 5..")





