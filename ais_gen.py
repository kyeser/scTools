#!/usr/bin/env python
from scTools import permutations, interval

# Search for AIS.
f = open('ais.txt', 'w')

for x in permutations(range(12)):
    # Test only the first 19958400 permutations.
    if x <= [0,6,5,11,10,9,8,7,4,3,2,1]:
        k = interval(x)
        k.sort()
        if k == range(1, 12):
            print x
            print >>f, x
    else:
        break

f.close()
