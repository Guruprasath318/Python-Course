class Unit:
    def unit_digit(self, num1):
        unit1 = num1 % 10
        print(f"{unit1} is the Unit digit..")

u1 = Unit()

num1 = int(input("Enter a number: "))
power = input("Choose power? {y/n}: ")   

if power.lower() == "y":
    power1 = int(input("Enter a power element: "))
    print(f"{num1} ^ {power1} = {num1 ** power1}")
else:
    u1.unit_digit(num1)
