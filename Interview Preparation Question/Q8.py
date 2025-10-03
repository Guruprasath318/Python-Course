def count_up_to(n):
    i = 1
    while i <= n:
        yield i   # pause here and return value
        i += 1

gen = count_up_to(5)
for num in gen:
    print(num)

def numbers():
    return [1, 2, 3]

print(numbers())   # [1, 2, 3] (all at once)
