def getTotalPopulation(cities):
    x= 0
    for row in range(len(cities)):
        
        x+=cities[row][2]
         
    return x
cities = [ ["Pittsburgh", "Allegheny", 302407],
           ["Philadelphia", "Philadelphia", 1584981],
           ["Allentown", "Lehigh", 123838],
           ["Erie", "Erie", 97639],
           ["Scranton", "Lackawanna", 77182] ]
print(getTotalPopulation(cities))
