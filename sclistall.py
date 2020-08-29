#!/usr/bin/env python
from scTools import findAllSC
from scTools.rowData import *

# Find all SCs for every AIS/ATS.
sc = raw_input('AIS or ATS: ')
if sc.lower() == 'ais': sc = ais
elif sc.lower() == 'ats' : sc = ats

count = 1
for x in sc:
    print '\n%4d\t' % count,
    for y in x:
        print '%X' % y,
    print '\n'
    s = findAllSC(x)
    for z in range(3, 10):
        print '[%d]' % z,
        for w in s[z]:
            print '%2d' % w,
        print
    count += 1
