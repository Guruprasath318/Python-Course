lst=["apple", "banana", "cherry","date", "elderberry","fig"]
print(lst)
print(lst[1])  # Accessing the second element
print(lst[2])  # Accessing the third element
print(lst[0])  # Accessing the first element
print(lst[-1])  # Accessing the last element
print(lst[-2])  # Accessing the second to last element
print(lst[-3])  # Accessing the third to last element

#deleting list methods
del lst[0]  # Deleting the first element
print(lst)
del lst[1]  # Deleting the second element
print(lst)
del lst[-1]  # Deleting the last element
print(lst)

#clear
lst.clear()
print(lst)

#pop
lst.pop(5)  # Removing the last element
print(lst)
lst.pop(0)  # Removing the first element
print(lst)

#append
lst.append("grape")
print(lst)

