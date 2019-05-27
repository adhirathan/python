import math

string = "haveaniceday"

arr = string.split(" ")

jointString = "".join(arr)

print(jointString)

a = len(jointString)

brPoint = int((math.ceil(math.sqrt(a))))
numberOfWords = int((math.floor(math.sqrt(a))))

end  = 0
for x in range(0,len(jointString)+1,brPoint):
    print(jointString[x-brPoint:x])
    end = x

print(jointString[x:])

ans = ''

for x in range(0,brPoint):
    for y in range(x,len(jointString),brPoint):
        ans+=jointString[y]

    ans+=" "


print(ans)
