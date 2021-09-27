d = { "apples" : 5, "beets" : 2, "lemons" : 1 }

def countItems(foodCounts):
    for j in foodCounts:
        print(foodCounts[j], j)
    values = foodCounts.values()
    sum = 0 
    for i in values:
        sum = sum + i
    return sum
                
print(countItems(d))