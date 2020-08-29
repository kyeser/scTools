#!/usr/bin/env python
from scTools import primeForm, permutations

# Search for trichord-derived series.
f = open('trichord.txt', 'w')

for x in permutations(range(12)):
    # Test only the first 19958400 permutations.
    if x <= [0,6,5,11,10,9,8,7,4,3,2,1]:
        l = [primeForm(x[y:y+3]) for y in range(0, 12, 3)]
        if l[0] == l[1] == l[2] == l[3]:
            print x
            print >>f, x
    else:
        break

f.close()
