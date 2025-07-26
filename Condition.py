#for loop

list=["apple","banana","cherry","date","elderberry","fig","grape"]

for fruits in list:
    fruits = fruits.upper()
    print(fruits)

#while loop
password="1234"
enterpw="2345"

while password!=enterpw:
    print("incorrect password try again")
    enterpw=input("Enter password: ")
print("Password accepted")