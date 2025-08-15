class emp:
    def __init__(self,empy_name,empy_id):
        self.name = empy_name
        self.id = empy_id

    def bank(self):
        print(f"{self.name} its your id {self.id}")

    def home(self):
         print(f"{self.name} its your id {self.id}")

s = emp("Guruprasath",5821)
s.bank()
s.home()


