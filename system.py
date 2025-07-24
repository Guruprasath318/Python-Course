import sys

full_name = " ".join(sys.argv[1:])

email = full_name.lower().replace(" ", ".") + "@gmail.com"

print("First Name and Last Name:", full_name)
print("-----Your output-----")
print("Your name is :", full_name)
print("Your email is :", email)

