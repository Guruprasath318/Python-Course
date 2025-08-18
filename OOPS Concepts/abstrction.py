from abc import ABC,abstractmethod
class MyClass(ABC):
    @abstractmethod
    def class1(self):
        pass

    @abstractmethod
    def class2(self):
        pass

class Myclass1(MyClass):
    def class1(self):
        print(f"This is an Abstrcted method")

    def class23(self):
        print(f"This is an Abstrcted method")


c = Myclass1()
c.class1()
c.class23() # its give an error because it has an normal method but we are implemted an abstrat class for class2 
