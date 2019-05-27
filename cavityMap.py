a = ['1112', '1912', '1892', '1234']

for x in range(1,len(a)-1):
    for y in range(1,len(a[x])-1):
        if a[x][y] > a[x][y-1] and a[x][y] > a[x][y+1] and a[x][y] > a[x+1][y] and a[x][y] > a[x-1][y]:
            a[x] = a[x][:y] + 'X' + a[x][y+1:]



print(a)