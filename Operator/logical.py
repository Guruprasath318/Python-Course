# Logical Operator

a = int(input("Enter number: "))

match a:
    case a if a>=10 and a<=100 :
        print(f"{a} is an less than 100")

    case a if a >= 200 or a <= 1000 :
        print(f"{a} is an less than 1000 or greater than 200")

    case a if not(a >= 0):
        print(f"{a} is less than zero")

