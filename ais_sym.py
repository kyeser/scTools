#!/usr/bin/env python
from scTools import primeForm
from scTools.rowData import ais
from scTools.scData import *

count = 1
number = 1
for x in ais:
    k = [(x[y]-x[11-y])%12 for y in range(6)]
    if k == [6,6,6,6,6,6]:
        print '%2d\t%3d\t' % (count, number),
        for z in x:
            print '%X' % z,
        prime = primeForm(x[0:6])
        print '\t6-%d' % sc6.index(prime)
        count += 1
    number += 1
