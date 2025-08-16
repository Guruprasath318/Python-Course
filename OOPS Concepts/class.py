class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)
print(p.name)
print(p.age)

print(f"{p.name} is {p.age} years old.")
print(f"Name: {p.name}, Age: {p.age}")
