#!/usr/bin/env python
from scTools import T, unique, normalForm, primeForm
from scTools.scData import *

def kc(s):
    for qw in range(12):
        pcset = T(s, qw)

        print 'KC\t\tNF\t\tSC\tKC\t\tNF\t\tSC'
        for x in range(6):
            l = []
            k = (12-x)%12
            print '%X |' % k,
            l.append(k)
            for y in T(pcset, x):
                print '%X' % y,
                l.append(y)
    
            print '\t',
            q = unique(l)
            normal = normalForm(q)
            prime = primeForm(q)
            sc = convert(len(prime))
            for z in normal:
                print '%X' % z,
            print '\t%d-%d' % (len(prime), sc.index(prime)),

            l = []
            x = x + 6
            k = (12-x)%12
            print '\t%X |' % k,
            l.append(k)
            for y in T(pcset, x):
                print '%X' % y,
                l.append(y)
    
            print '\t',
            q = unique(l)
            normal = normalForm(q)
            prime = primeForm(q)
            sc = convert(len(prime))
            for z in normal:
                print '%X' % z,
            print '\t%d-%d' % (len(prime), sc.index(prime))
        print
    print '=' * 80

'''
kc([0,1,2])
kc([0,1,3])
kc([0,1,4])
kc([0,1,5])
kc([0,1,6])
kc([0,2,4])
kc([0,2,5])
kc([0,2,6])
kc([0,2,7])
kc([0,3,6])
kc([0,3,7])
kc([0,4,8])
'''
kc([0,11,9])
kc([0,11,8])
kc([0,11,7])
kc([0,11,6])
kc([0,10,7])
kc([0,10,6])
kc([0,9,5])
