tuple1 = ("apple","banana","orange","grape","lemon","lime","grapefruit")

#accessing elements
print(tuple1)
print(type(tuple1))
print(len(tuple1))
print(tuple1[0])
print(tuple1[1])
print(tuple1[-1])
print(tuple1[-2])
print(tuple1[2:5])
print(tuple1[4:])
print(tuple1[:4])
print(tuple1[:])
print("-------------------------------------------------------------------------")

#update elements
y = list(tuple1)
y.append("kiwi")
tuple1 = tuple(y)
print(tuple1)

y[1] = "blueberry"
tuple1 = tuple(y)
print(tuple1)

y.remove("blueberry")
tuple1 = tuple(y)
print(tuple1)

y.clear()
tuple1 = tuple(y)
print(tuple1)
