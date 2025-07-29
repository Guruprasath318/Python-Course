vowels = ["a", "e", "i", "o", "u"]
char = input("Enter a string: ").lower()
counts = {v: 0 for v in vowels}

for c in char:
    if c in vowels:
        counts[c] += 1

for v in vowels:
    print(f"{v}: {counts[v]}")


