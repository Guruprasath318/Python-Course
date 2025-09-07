class Unit:
    def unit_digit(self, num1):
        unit1 = num1 % 10
        print(f"{unit1} is the Unit digit..")

    def unit_2(self,unit_after_power):
        unit2 = unit_after_power % 10
        print(f"{unit2} is the unit digit..")

u1 = Unit()

num1 = int(input("Enter a number: "))
power = input("Choose power? {y/n}: ")

if power.lower() == "y":
    power1 = int(input("Enter a power element: "))
    unit_after_power = num1 ** power1
    print(f"{unit_after_power} is an powered value of the unit digit.")
    u1.unit_2(unit_after_power)
else:
    u1.unit_digit(num1)



