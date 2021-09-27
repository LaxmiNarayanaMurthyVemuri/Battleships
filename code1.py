import random

def createShip():
    row = random.randrange(1,8)
    col = random.randrange(1,8)
    step = random.randrange(0,2)
    ship2 = []
    ship1 = []
    i = 0
    if(step == 0):
        for row in range(row-2, row+1):
            i += 1
            if(i<3): 
                ship2.append(5)
            ship1.append(ship2)
    else:
        for col in range(col-1, col+1):
            ship2.append(5)
            for i in range(0,2):  
                ship1.append(ship2)
    return ship1

print(createShip())