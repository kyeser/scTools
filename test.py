#!/usr/bin/env python
from scTools import findAllSC

# Find all SCs of a series.
while 1:
    try:
        sc = raw_input('Enter a series: ')
    except (EOFError, KeyboardInterrupt):
        print
        break

    if sc == 'q' or sc == 'quit':
        break
    else:
        sc = sc.split()
        try:
            for x in sc:
                int(x)
        except ValueError:
            print 'Intergers only!\n'
            continue

        l = [int(x) for x in sc]
        s = findAllSC(l)
        for x in range(3, 10):
            print '[%d]' % x,
            for y in s[x]:
                print '%2d' % y,
            print
