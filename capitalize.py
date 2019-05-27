def solve(s):
    if s[0] <= "z" and s[0] >= "a":
        s = chr(ord(s[0])-32)+s[1:]
    for x in range(0,len(s)):
           if s[x-1] == " " and s[x] <= "z" and s[x] >= "a":
               s = s[:x]+chr(ord(s[x])-32)+s[x+1:]

    return s

print(solve("hello   world   lol"))