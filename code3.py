d = { "apples" : 5, "beets" : 2, "lemons" : 1 }

def countItems(foodCounts):
    keys = foodCounts.keys()
    values = foodCounts.values()
    for k in keys:
        print(k)
        for j in values:
            Items = str(j)+ ' ' +k
        print(Items)
    sum = 0 
    for i in values:
        sum = sum + i
    return sum
                
print(countItems(d))