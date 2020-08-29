#!/usr/bin/env python
from scTools import convert, uniqueCombinations, primeForm
from scTools.scData import *

def subset(sc, n):
    s = list(uniqueCombinations(sc, n))
    sc = convert(n)
    print '[%d]' % n,

    l = []
    for x in s:
        prime = primeForm(x)
        l.append(sc.index(prime))

    k = [l.count(z) for z in range(1, len(sc))]
    return k

print subset([0,2,4,7,9], 3)
print subset([0,1,2,3,4,5,6,7], 6)
