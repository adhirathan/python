def organizingContainers(container):
    sumInEachBox = []
    sumInEachType = []
    for _ in container:
        sumInEachType.append(0)
    for box in container:
        sum = 0
        i = 0
        for balls in box:
            sum += balls
            sumInEachType[i]+=balls
            i+=1
        sumInEachBox.append(sum)
    print(sumInEachBox)
    print(sumInEachType)
    if set(sumInEachType) == set(sumInEachBox):
        return"Possible"
    return"Impossible"


print(organizingContainers([[2,1],[3,2]]))