#!/usr/bin/env python
from scTools.reduce import *
from scTools.rowDataOriginal import ais

def removeFunc(reduceFunc):
    return [reduceFunc(ais[x]) for x in range(len(ais)) if reduceFunc(ais[x])
            in ais if ais[x] < reduceFunc(ais[x])]

def remove(p):
    for x in range(0, len(p)):
        ais.remove(p[x])

f = open('zReducedAIS.py', 'w')
print 'Out of total %d entries,' % len(ais)

# Remove retrogrades.
r = removeFunc(reduceR)
remove(r)
print '%d retrogrades removed,' % len(r),
print '%d remains' % len(ais)

# Remove retrograde inversions.
ri = removeFunc(reduceRI)
remove(ri)
print '%d retrograde-inversions removed,' % len(ri),
print '%d remains' % len(ais)

# Remove circle-of-fourths.
m5 = removeFunc(reduceM5)
remove(m5)
print '%d circle-of-fourths removed,' % len(m5),
print '%d remains' % len(ais)

# Remove circle-of-fourth retrogrades.
m5r = removeFunc(reduceM5R)
remove(m5r)
print '%d circle-of-fourths (retrograde) removed,' % len(m5r),
print '%d remains' % len(ais)

# Remove circle-of-fifths.
m7 = removeFunc(reduceM7)
remove(m7)
print '%d circle-of-fifths removed,' % len(m7),
print '%d remains' % len(ais)

# Remove circle-of-fifth retrogrades.
m7r = removeFunc(reduceM7R)
remove(m7r)
print '%d circle-of-fifths (retrograde) removed,' % len(m7r),
print '%d remains' % len(ais)

print 'Reduced list contains %d entries,' % len(ais),
print 'saved to the file, zReducedAIS.py'

print >>f, ais

f.close()
