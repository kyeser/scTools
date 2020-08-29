#!/usr/bin/env python
from scTools import permutations, findTrichord

# Search for ATS.
f = open('ats.txt', 'w')

for x in permutations(range(12)):
    # Test only the first 19958400 permutations.
    if x <= [0, 1, 2, 4, 11, 7, 6, 10, 8, 3, 9, 5]:
        k = findTrichord(x)
        k.sort()
        if k == [1,2,3,4,5,6,7,8,9,11]:
            print x
            print >>f, x
    else:
        break

f.close()
