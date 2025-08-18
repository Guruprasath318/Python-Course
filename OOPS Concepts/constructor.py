class student:
    def __init__(self,name,age):
        self.x = name
        self.y = age
        print(f"Name : {self.x} is age {self.y}")

    def name(self):
        print(f"Name : {self.x}")

    def age(self):
        print(f"Age : {self.y}")


sr = student("Guruprasath",23)
print(sr.name())
print(sr.age())

