def nextMove(n,r,c,grid):
    r-=1
    c-=1
    xf = 0
    yf = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 'p':
                xf = x
                yf = y
                #print(x,y)
                #print(r,c)

    diffInHeight = xf-r
    diffInLength = yf-c

    if diffInHeight > 0:
        return "DOWN"

    elif diffInHeight < 0:
        return "UP"

    elif diffInLength > 0:
        return "RIGHT"

    elif diffInLength < 0:
        return "LEFT"





n=5
r=1
c=4
grid = ["--p-","----","----","----"]
print(nextMove(n,r,c,grid))