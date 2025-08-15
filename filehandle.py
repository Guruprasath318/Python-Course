with open("file.txt","w") as f:
    f.write("This is an file handling concept for python!")

with open("file.txt") as f:
    print(f.read())
