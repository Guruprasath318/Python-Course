#Multiple arguments in

def add(*keys):
    return sum(keys)

s = add(2, 3, 4)
print(s)
