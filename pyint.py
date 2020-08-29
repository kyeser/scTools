#!/usr/bin/env python
print '\nPyInt v0.1, interval generation program\n'
print 'Copyright (c) 2004 by Hee-Seng Kye'
print 'All rights reserved.\n'
print 'Questions or comments: katsura@msbx.net\n'
print "Type 'h' or 'help' for help.\n"

while 1:
    # Proper ctrl+d / ctrl+c escape
    try:
        s = raw_input("Enter a series: ")
    except (EOFError, KeyboardInterrupt):
        print
        break

    r = s.split()
    l = []
    
    print ''

    if s == 'q' or s == 'quit':
        break
    elif s == 'v' or s == 'version':
        print 'PyInt v0.1, interval generation program'
        print 'Copyright (c) 2004 by Hee-Seng Kye'
        print 'All rights reserved.'
        print 'Questions or comments: katsura@msbx.net\n'
    elif s == 'h' or s == 'help':
        print 'q, quit\t\tQuit.'
        print 'h, help\t\tThis help message.'
        print 'v, version\tVersion info.\n'
    else:
        # Filter out non-integer types
        try:
            for x in r:
                int(x)
        except ValueError:
            print 'Integers only!\n'
            continue
        # Convert strings of list into integers
        for x in r:
            print '%X' % (int(x)%12),

        print ''
        print '',
        # Compute contiguous pitch intervals and append the values to list
        for y in range(1, len(r)):
            k = (int(r[y])+12-int(r[y-1]))%12
            l.append(k)
            print '%X' % k,
        # Sort list and check whether it's an all-interval series
        l.sort()
        if l == range(1, 12):
            print '\t\tThis is an all-interval series!',
    
        print '\n'
