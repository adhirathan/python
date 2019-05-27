def print_formatted(number):

    firstGap = len(str(number))
    gap = len(str(bin(number))[2:])

    for x in range(1,number+1):
        dec = str(x)
        octal = str(oct(x))[1:]
        hexa = str(hex(x))[2:].upper()
        binary = str(bin(x))[2:]
        print(dec.rjust(gap)),
        print(octal.rjust(gap)),
        print(hexa.rjust(gap)),
        print(binary.rjust(gap))


print_formatted(17)
