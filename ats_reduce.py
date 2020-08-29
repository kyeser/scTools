#!/usr/bin/env python
from scTools.reduce import *
from scTools.rowDataOriginal import ats

def removeFunc(reduceFunc):
    return [reduceFunc(ats[x]) for x in range(len(ats)) if reduceFunc(ats[x])
            in ats if ats[x] < reduceFunc(ats[x])]

def remove(p):
    for x in range(0, len(p)):
        ats.remove(p[x])

f = open('zReducedATS.py', 'w')
print 'Out of total %d entries,' % len(ats)

# Remove retrogrades.
r = removeFunc(reduceR)
remove(r)
print '%d retrogrades removed,' % len(r),
print '%d remains' % len(ats)

# Remove retrograde inversions.
ri = removeFunc(reduceRI)
remove(ri)
print '%d retrograde-inversions removed,' % len(ri),
print '%d remains' % len(ats)

# Remove circle-of-fourths.
m5 = removeFunc(reduceM5)
remove(m5)
print '%d circle-of-fourths removed,' % len(m5),
print '%d remains' % len(ats)

# Remove circle-of-fourth retrogrades.
m5r = removeFunc(reduceM5R)
remove(m5r)
print '%d circle-of-fourths (retrograde) removed,' % len(m5r),
print '%d remains' % len(ats)

# Remove circle-of-fifths.
m7 = removeFunc(reduceM7)
remove(m7)
print '%d circle-of-fifths removed,' % len(m7),
print '%d remains' % len(ats)

# Remove circle-of-fifth retrogrades.
m7r = removeFunc(reduceM7R)
remove(m7r)
print '%d circle-of-fifths (retrograde) removed,' % len(m7r),
print '%d remains' % len(ats)

print 'Reduced list contains %d entries,' % len(ats),
print 'saved to the file, zReducedATS.py'

print >>f, ats

f.close()
