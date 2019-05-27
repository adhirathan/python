def fairRations(B):
    lastOddIndex = 0
    length = 0
    oddCount = 0

    for x in range(0,len(B)):
        if B[x]%2 != 0:
            if oddCount%2 == 1:
                length+=(x-lastOddIndex-1)
                print("lastoddIndex = "),
                print(lastOddIndex)
                print("x = "),
                print(x)
            else:
                lastOddIndex = x
            oddCount+=1

    if oddCount%2 == 0 or oddCount == 0:
        print("oddcount = "),
        print(oddCount)
        print("length = "),
        print(length)
        return(oddCount+length*2)
    else:
        return("No")



fairRations([5,2,4,6,1,3,6,7])