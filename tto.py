def R(pcset):
    """Returns retrograde of pcset."""
    return [pcset[x] for x in range(len(pcset)-1, -1, -1)]

def I(pcset):
    """Returns inversion of pcset."""
    return [(12-x)%12 for x in pcset]

def RI(pcset):
    """Returns retrograde inversion of pcset."""
    return I(R(pcset))

def M5(pcset):
    return [(x*5)%12 for x in pcset]

def M7(pcset):
    return [(x*7)%12 for x in pcset]

def T(pcset, n=0):
    return [(x+n)%12 for x in pcset]

def TR(pcset, n=0):
    return T(R(pcset), n)

def TI(pcset, n=0):
    return T(I(pcset), n)

def TRI(pcset, n=0):
    return T(RI(pcset), n)

def TM5(pcset, n=0):
    return T(M5(pcset), n)

def TM7(pcset, n=0):
    return T(M7(pcset), n)
