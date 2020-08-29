#!/usr/bin/env python
from scTools.invariance import vtics

print '\nPyVTICS v0.1, index vector generation program\n'
print 'Copyright (c) 2004 by Hee-Seng Kye'
print 'All rights reserved.\n'
print 'Questions or comments: katsura@msbx.net\n'
print "Type 'h' or 'help' for help.\n"

while 1:
    try:
        s = raw_input("Enter a set: ")
    except (EOFError, KeyboardInterrupt):
        print
        break

    r = s.split()

    print

    if s == 'q' or s == 'quit':
        break
    elif s == 'v' or s == 'version':
        print 'PyVTICS v0.1, index vector generation program'
        print 'Copyright (c) 2004 by Hee-Seng Kye'
        print 'All rights reserved.'
        print 'Questions or comments: katsura@msbx.net\n'
    elif s == 'h' or s == 'help':
        print 'q, quit\t\tQuit.'
        print 'h, help\t\tThis help message.'
        print 'v, version\tVersion info.\n'
    else:
        k = [int(x) for x in r]
        l = vtics(k)
        print '\t\t0 1 2 3 4 5 6 7 8 9 A B'
        print '\t\t', '_' * 23
        print 'VTICS =\t\t',
    
        for y in l:
            print '%X' % y,
    
        print '\n'
