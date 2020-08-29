#!/usr/bin/env python
"""
PyTTO v0.1, TTO generation program

This document was generated using the pydoc module.

Copyright (c) 2004 by Hee-Seng Kye
All rights reserved.

Questions or comments: katsura@msbx.net
"""

__author__ = "Hee-Seng Kye <katsura@msbx.net>"
__date__ = "10 July 2004"
__version__ = "$Revision: 0.1 $"

from scTools.reduce import reduceZero, reduceM5
from scTools.tto import T, TR, TI, TRI

print '\nPyTTO v0.1, TTO generation program\n'
print 'Copyright (c) 2004 by Hee-Seng Kye'
print 'All rights reserved.\n'
print 'Questions or comments: katsura@msbx.net\n'

while 1:
    s = raw_input("Enter a series: ")
    r = s.split()
    l = [int(x)%12 for x in r]
    q = reduceZero(l)
    q5 = reduceM5(l)

    print '\nM1 Transformations:\n'
    
    for y in range(12):
        a = T(q, y)
        b = TI(q, y)
        print 'T%X:\t' % y,
        for z in a:
            print '%X' % z,
        print '\tT%XI:\t' % y,
        for z in b:
            print '%X' % z,
        print ''

    print ''
    
    for y in range(12):
        a = TR(q, y)
        b = TRI(q, y)
        print 'T%XR:\t' % y,
        for z in a:
            print '%X' % z,
        print '\tT%XRI:\t' % y,
        for z in b:
            print '%X' % z,
        print ''

    print '\nM5 Transformations:\n'

    for y in range(12):
        a = T(q5, y)
        b = TI(q5, y)
        print 'T%X:\t' % y,
        for z in a:
            print '%X' % z,
        print '\tT%XI:\t' % y,
        for z in b:
            print '%X' % z,
        print ''
        
    print ''

    for y in range(12):
        a = TR(q5, y)
        b = TRI(q5, y)
        print 'T%XR:\t' % y,
        for z in a:
            print '%X' % z,
        print '\tT%XRI:\t' % y,
        for z in b:
            print '%X' % z,
        print ''
    
    print ''
