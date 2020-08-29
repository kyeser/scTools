from scTools import primeForm
from scData import *

def findSC(row, n):
    z = 13 - n
    sc = convert(n)
    l = []
    for x in range(z):
        prime = primeForm(row[x:x+n])
        l.append(sc.index(prime))
    return l

def findAllSC(row):
    """Finds all contiguous subsets of cardinality 3 through 9."""
    m = [[]]
    for z in range(12, 0, -1):
        n = 13 - z
        sc = convert(n)
        l = []
        for x in range(z):
            prime = primeForm(row[x:x+n])
            l.append(sc.index(prime))
        m.append(l)
    return m

def findTrichord(row):
    """Equivalent to findSC(row, 3)."""
    l = []
    for x in range(10):
        prime = primeForm(row[x:x+3])
        l.append(sc3.index(prime))
    return l
