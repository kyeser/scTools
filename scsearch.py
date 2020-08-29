#!/usr/bin/env python
from scTools import convert, primeForm
from scTools.scData import *
from scTools.rowData import *

def scSearch(data, n, name):
    
    k = 13 - n
    sc = convert(n)
    index = 0

    for x in range(k):
        count = 1
        number = 1
        print '\nIndices %d through %d' % (index, index+(12-k))
        index += 1
        for y in data:
            prime = primeForm(y[x:x+n])
            if prime == sc[name]:
                print '\n%2d\t%3d\t' % (count, number),
                for z in y:
                    print '%X' % z,
                print '\t%d-%d' % (n, name),
                count += 1
            number += 1
        print

e1 = raw_input('AIS or ATS: ')
e2 = int(raw_input('Cardinality: '))
e3 = int(raw_input('Name: '))

if 'ais' in e1.lower(): scSearch(ais, e2, e3)
elif 'ats' in e1.lower(): scSearch(ats, e2, e3)
