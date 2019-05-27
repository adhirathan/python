def surfaceArea(A):
    sfArea = len(A)*len(A[0])*2
    zeroAry =[]

    for row in A:
        row.insert(0,0)
        row.append(0)

    for _ in range(0,len(A[0])):
        zeroAry.append(0)
    A.insert(0,zeroAry)
    A.append(zeroAry)


    print (A)

    for x in range(0,len(A)-1):
           for y in range(0,len(A[x])-1):
                   sfArea+=abs(A[x][y]-A[x][y+1])
                   sfArea+=abs(A[x][y]-A[x+1][y])

    return sfArea


print(surfaceArea([[51,32,28,49,28,21,98,56,99,77]]))
