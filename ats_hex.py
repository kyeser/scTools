#!/usr/bin/env python
from scTools import interval, primeForm
from scTools.rowData import ats
from scTools.scData import *

count = 1
for w in ats:
    prime = primeForm(w[0:6])
    print '%3d\t' % count,

    for x in w:
        print '%X' % x,
    print '    ',

    intervals = interval(w)
    for y in intervals:
        print '%X' % y,

    print '\t%2d\t' % sc6.index(prime),

    if prime == sc6[1] or prime == sc6[7] or prime == sc6[8] or \
       prime == sc6[20] or prime == sc6[32] or prime == sc6[35]:
        print 'AC'
    elif prime == sc6[17]:
        print 'AT'
    else:
        print

    count += 1
