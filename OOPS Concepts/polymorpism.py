class student:
    def school(self):
        print("I am an school Student")

class student1(student):
    def college(self):
        print("I am an College student")

    def school(self):
        print(" I am an School student, but now i am an college student")

s = student1()
s.college()
s.school()

