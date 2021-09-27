def Firstname(fullname):
    for i in range(len(fullname)):
        if fullname[i]==" ":
           return fullname[:i]
print(Firstname("Donald Knuth"))