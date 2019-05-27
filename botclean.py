def printGrid():
    for x in range(0,size):
        for y in range(0,size):
            print(grid[x][y]),
        print("\n")
    print("\n")

def assignDiagonal(fromx,tox,fromy,toy,xsign,ysign,step):

    condition = True
    x = fromx
    y = fromy

    while condition:
        print("in while")

        if x == tox and y == toy:
            condition = False


        if x<size and y<size and x>=0 and y>=0:
            grid[x][y] = " "+str(step)+" "

        if xsign == "+":
            x+=1
        elif xsign == "-":
            x-=1
        if ysign == "+":
            y+=1
        elif ysign == "-":
            y-=1




def calPossiblity(size,xf,yf):
    step = 0
    upLimit = xf
    lowLimit = xf
    leftLimit = yf
    rightLimit = yf

    condition = True

    while condition:

        condition = False

        if upLimit >= 0:
            assignDiagonal(upLimit,xf,yf,rightLimit,"+","+",step)
            condition = True

        if leftLimit >= 0:
            assignDiagonal(xf,upLimit,leftLimit,yf,"-","+",step)
            condition = True

        if  rightLimit < size:
            assignDiagonal(xf,lowLimit,rightLimit,yf,"+","-",step)
            condition = True

        if lowLimit < size:
            grid[lowLimit][yf] = " "+str(step)+" "
            assignDiagonal(lowLimit,xf,yf,leftLimit,"-", "-", step)
            condition = True

        printGrid()
        upLimit-=1
        lowLimit+=1
        leftLimit-=1
        rightLimit+=1
        step+=1



grid = []

size = 10
xf = 5
yf = 5

for x in range(0,size):
    grid.append([])
    for y in range(0,size):
         grid[x].append(" * ")

grid[xf][yf] = " B "

calPossiblity (size,xf,yf)
