def getstring(a,s):
    str = ""
    for x in range(s,s-a,-1):
        str+=chr(x+96)+'-'

    str+=chr(s-a+96)+'-'

    for x in range(s-a+1,s+1):
        str+=chr(x+96)+'-'

    return str[:len(str)-1]





def print_rangoli(size):
    str = ""
    for x in range(0,size):
        str = getstring(x,size)
        print(str.center((size-1)*4+1,"-"))

    for x in range(size-2,-1,-1):
        str = getstring(x,size)
        print(str.center((size-1)*4+1,"-"))


print_rangoli(5)