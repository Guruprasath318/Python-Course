class parent:
    def __init__(self):
        self.a = "I am a Public"
        self._b = "I am a protected"
        self.__c = "I am a private"

    def access_from_same_class(self):
        print("Public   : ",self.a)
        print("Protected: ",self._b)
        print("private  : ",self.__c)

class child(parent):
    def access_from_parent_class(self):
        print("Public   : ",self.a)
        print("Protected: ",self._b)
        try:
           print("private  : ",self._parent__c) #name mangaling
        except:
            print("it not access from the parent class")

class stranger:
    def stranger_class(self,obj):
        print("Public   : ",obj.a)
        print("Protected: ",obj._b)
        try:
           print("private  : ",obj.__c)#With out name mangaling
        except:
            print("it not access from the parent class")


s = parent()
s1 = child()
s2 = stranger()
s.access_from_same_class()
print("-----------------------------------------------------")
s1.access_from_parent_class()
print("-----------------------------------------------------")
s2.stranger_class(s)
