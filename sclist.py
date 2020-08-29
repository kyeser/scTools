#!/usr/bin/env python
from scTools import findSC
from scTools.rowData import *

# Find specified SCs for every AIS/ATS.
sc = raw_input('AIS or ATS: ')
s = int(raw_input('Cardinality: '))
if 'ais' in sc.lower(): sc = ais
elif 'ats' in sc.lower(): sc = ats

count = 1
for x in sc:
    print '\n%4d\t' % count,
    for y in x:
        print '%X' % y,
    print '\t[%d]' % s,
    for z in findSC(x, s):
        print '%2d' % z,
    count += 1
