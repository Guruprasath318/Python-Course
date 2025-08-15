class college:
    def __init__(self,name,total):
        self.name = name
        self.total = total
    def dep1(self):
        print(f"{self.name} contians only {self.total}")

clg = college("CSE",60)
dp1 = college("MECH",60)
dp2 = college("IT",58)
dp3 = college("AIDS",53)
dp1.dep1()
dp2.dep1()
dp3.dep1()
clg.dep1()
