def printbox(length,width,qx,qy,obstacles,path):
    for x in range(1,length+1):
        for y in range(1,width+1):
            if [x,y] == [qx,qy]:
                print (" Q "),
            elif [x,y] in path:
                print(" $ "),
            elif [x,y] in obstacles:
                print(" 8 "),
            else:
                print(" . "),
        print("\n")

def findN(n,k,q_x,q_y,obstacle):
    path = []

    x = q_x
    y = q_y
    while x < n :
        x += 1

        if [x, y] in obstacles:
            break
        path.append([x, y])

    x = q_x
    y = q_y
    while x > 1:
        x -= 1

        if [x, y] in obstacles:
            break
        path.append([x, y])

    x = q_x
    y = q_y
    while y < n:
        y += 1

        if [x, y] in obstacles:
            break
        path.append([x, y])

    x = q_x
    y = q_y
    while y > 1:
        y -= 1

        if [x, y] in obstacles:
            break
        path.append([x, y])




    x = q_x
    y = q_y
    while x<n and y<n:
        x+=1
        y+=1
        if [x,y] in obstacles:
            break
        path.append([x,y])

    x = q_x
    y = q_y
    while x > 1 and y > 1:
        x -= 1
        y -= 1
        if [x,y] in obstacles:
            break
        path.append([x, y])

    x = q_x
    y = q_y
    while x < n and y > 1:
        x += 1
        y -= 1
        if [x,y] in obstacles:
            break
        path.append([x, y])

    x = q_x
    y = q_y
    while x > 1 and y < n:
        x -= 1
        y += 1
        if [x,y] in obstacles:
            break
        path.append([x, y])

    return path



def calculateN(n,k,q_x,q_y,obstacle):
    xp = length-q_x
    xn = q_x-1
    yp = length-q_y
    yn = q_y-1
    pp = min(length-q_x,length-q_y)
    pm = min(q_y-1,length-q_x)
    mp = min(q_x-1,length-q_y)
    mm = min(q_x-1,q_y-1)

    for [x,y] in obstacle:
        if x == q_x:
            if q_y-y-1 < yn and q_y-y-1 >= 0 :
                yn = qy-y-1

            if y-q_y-1 < yp and y-q_y-1 >= 0:
                yp = y-q_y-1

        if y == q_y:

            if q_x - x - 1 < xn and q_x - x - 1 >= 0:
                xn = qx - x - 1

            if x - q_x - 1 < xp and x - q_x - 1 >= 0:
                xp = x - q_x - 1

        if abs(q_x-x) == abs(q_y-y):
            if q_x < x:
                if q_y < y:
                    temp = min(x-q_x,y-q_y)-1
                    if pp > temp:
                        pp = temp
                if q_y > y:
                    temp = min(x-q_x,q_y-y)-1
                    if pm > temp:
                        pm = temp

            elif q_y < y:
                temp = min(q_x-x,y-q_y)-1
                if mp > temp:
                    mp = temp

            elif q_y >y:
                temp = min(q_x-x,q_y-y)-1
                if mm > temp:
                    mm = temp


    print("pp = "),
    print(pp)
    print("mp = "),
    print(mp)
    print("pm = "),
    print(pm)
    print("mm = "),
    print(mm)

    number = xp+xn+yp+yn+pp+mp+pm+mm

    return number


length = 11
qx = 5
qy = 5
obstacles = [[5,1],[5,11],[1,5],[11,5],[5,3],[11,11],[7,7],[1,1],[3,3],[7,3],[3,7]]
path = []

path = findN(length,len(obstacles),qx,qy,obstacles)

print(path)
print(len(path))

printbox(length,length,qx,qy,obstacles,path)

print(calculateN(length,len(obstacles),qx,qy,obstacles))