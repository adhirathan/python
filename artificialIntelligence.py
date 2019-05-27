def displayPathtoPrincess(n,grid):
        positionOfMan = [0,0]
        positionOfPrincess = [0,0]

        for x in range(0,n):
            for y in range(0,n):
                if grid[x][y] == 'm':
                    positionOfMan = [x,y]
                if grid[x][y] == 'p':
                    positionOfPrincess = [x,y]

        diffInHeight  = positionOfPrincess[0] - positionOfMan[0]
        diffInLength = positionOfPrincess[1] - positionOfMan[1]

        while(True):
            if diffInHeight > 0:
                for _ in range(0,diffInHeight):
                    print("DOWN")
                    diffInHeight-=1

            elif diffInHeight < 0:
                for _ in range(0, abs(diffInHeight)):
                    print("UP")
                    diffInHeight+=1

            elif diffInHeight == 0:
                if diffInLength < 0:
                    for _ in range(0,abs(diffInLength)):
                        print("LEFT")
                        diffInLength+=1

                elif diffInLength > 0:
                    for _ in range(0,diffInLength):
                        print("RIGHT")
                        diffInLength-=1
                else:
                    break


grid = ['---','-m-','p--']
displayPathtoPrincess(len(grid), grid)