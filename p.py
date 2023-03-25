SHIP_UNCLICKED = 2
EMPTY_UNCLICKED = 1

def shipIsValid(grid, ship):
    # Check if ship is length 3
    if len(ship) != 3:
        return False
    
    # Check if ship overlaps with any other ship
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == SHIP_UNCLICKED:
                if (i,j) in ship:
                    return False
    
    # Check if ship is in a straight line
    if not checkShip(ship):
        return False
    
    # Check if ship is vertical
    if isVertical(ship):
        for cell in ship:
            if cell[1] != ship[0][1]:
                return False
    # Check if ship is horizontal
    elif isHorizontal(ship):
        for cell in ship:
            if cell[0] != ship[0][0]:
                return False
    else:
        return False
    
    return True

def checkShip(grid, ship):
    for i in ship:
        x = i[0]
        y = i[1]
        if grid[x][y] != EMPTY_UNCLICKED:
            return False
    return True
def isVertical(ship):
    if ship[0][1] == ship[1][1] == ship[2][1]:
        ship.sort()
        for i in ship:
            if ship[0][0] + 1 == ship[1][0] == ship[2][0] - 1:
                return True
    return False


def isHorizontal(ship):
    if ship[0][0] == ship[1][0] == ship[2][0]:
        ship.sort()
        for i in ship:
            if ship[0][1] + 1 == ship[1][1] == ship[2][1] - 1:
                return True
    return False