
def three_3_9():

    while number != 0:
        digit = number % 10
        sum = sum + digit
        number = int(number/10)
        print(sum)

number = int(input("Enter an number: "))
three_3_9(number)


