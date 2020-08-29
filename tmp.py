#!/usr/bin/env python
from scTools import convert, uniqueCombinations, primeForm
from scTools.scData import *

n = int(4)
sc = convert(n)
s = list(uniqueCombinations(range(12), n))
count = 1

for x in s:
    prime = primeForm(x)
    print '\n%3d\t' % count,

    for y in x:
        print '%X' % y,
    print '\t',

    for z in prime:
        print '%X' % z,
    print '\t%d-%d' % (n, sc.index(prime)),
    
    count += 1
