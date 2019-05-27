def taumBday(b, w, bc, wc, z):
    bcf = bc
    wcf = wc

    if bc + z < wc:
        wcf = bc + z
    elif wc + z < bc:
        bcf = wc + z

    return b*bcf + w*wcf



print(taumBday(7,7,4,2,1))