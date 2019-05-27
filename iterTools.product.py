from itertools import combinations

s = "zoba"
num = 3

string = "".join(sorted(s))


for number in range(1,num):
    perm = list(combinations(string,number))
    srtprm = []
    for subarray in perm:
        a = ""
        for letter in subarray:
            a+=letter
        srtprm.append(a)

    srtprm.sort()

    for word in srtprm:
        print(word)
