class Calsy:
    def __init__(self):
        self.num1 = int(input("Enter a number: "))
        self.num2 = int(input("Enter a number: "))

    def add(self):
        print(f"{self.num1} + {self.num2}: {self.num1 + self.num2}")

    def sub(self):
        print(f"{self.num1} - {self.num2}: {self.num1 - self.num2}")

    def mul(self):
        print(f"{self.num1} * {self.num2}: {self.num1 * self.num2}")

    def div(self):
        try:
            print(f"{self.num1} / {self.num2}: {self.num1 / self.num2}")
        except ZeroDivisionError:
            print("Division by zero is not allowed.")


call = Calsy()

user_call = input(
    "Enter the operation you want to perform (+, -, *, /) or (exit) or (help): "
)

if user_call == "+":
    call.add()
elif user_call == "-":
    call.sub()
elif user_call == "*":
    call.mul()
elif user_call == "/":
    call.div()
elif user_call == "exit":
    print("Exiting the program.")
    exit()
elif user_call == "help":
    print("Available operations are: +, -, *, /")
else:
    print("Invalid operation.")
