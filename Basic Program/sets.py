set1 = {"apple", "banana", "orange", "grape", "lemon", "lime", "grapefruit"}

print(set1)
print(type(set1))
print(len(set1))
print("orange" in set1)
print("kiwi" in set1)
print("-------------------------------------------------------------------------")

#update elements
set1.add("kiwi")
print(set1)

set1.remove("kiwi")
print(set1)

set1.discard("banana")
print(set1)

set1.clear()
print(set1)


