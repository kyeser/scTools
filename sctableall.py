#!/usr/bin/env python
from scTools import convert, uniqueCombinations, normalForm, primeForm
from scTools.scData import *

#n = int(raw_input('-> '))
n = 6
sc = convert(n)
s = list(uniqueCombinations(range(12), n))
count = 1

for x in s:
    normal = normalForm(x)
    prime = primeForm(x)
    print '\n%3d\t' % count,

    for y in x:
        print '%X' % y,
    print '\t',

    for w in normal:
        print '%X' % w,
    print '\t',

    for z in prime:
        print '%X' % z,
    print '\t%d-%d' % (n, sc.index(prime)),
    
    count += 1
