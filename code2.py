def emptyGrid(rows, cols):
    lst = []
    for i in range(rows): 
        lst1 = []
        for j in range(cols): 
            lst1.append(5)
        lst.append(lst1)
    return lst

print(emptyGrid(4,4))