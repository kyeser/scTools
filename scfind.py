#!/usr/bin/env python
"""
PyTTO v0.1, SC finder

This document was generated using the pydoc module.

Copyright (c) 2004 by Hee-Seng Kye
All rights reserved.

Questions or comments: katsura@msbx.net
"""

__author__ = "Hee-Seng Kye <katsura@msbx.net>"
__date__ = "10 July 2004"
__version__ = "$Revision: 0.1 $"

from scTools import icv, unique, normalForm, primeForm
from scTools.scData import *

print '\nSCFinder v0.1\n'
print 'Copyright (c) 2004 by Hee-Seng Kye'
print 'All rights reserved.\n'
print 'Questions or comments: katsura@msbx.net\n'

while 1:
    try:
        n = raw_input("\nEnter a pcset: ")
    except (EOFError, KeyboardInterrupt):
        print
        break

    r = n.split()

    if n == 'q' or n == 'quit':
        break
    elif n == 'v' or n == 'version':
        print 'scFind v0.1, Set-Class Finder'
        print 'Copyright (c) 2004 by Hee-Seng Kye'
        print 'All rights reserved.'
        print 'Questions or comments: katsura@msbx.net'
    elif n == 'h' or n == 'help':
        print 'q, quit\t\tQuit.'
        print 'h, help\t\tThis help message.'
        print 'v, version\tVersion info.'
    else:
        try:
            q = [int(x)%12 for x in r]
        except ValueError:
            print 'Integers only!'
            continue

        q = unique(q)
        print 'Set you entered:\t', q

        normal = normalForm(q)
        print 'Normal form:\t\t', normal

        prime = primeForm(q)
        print 'Prime form:\t\t', prime, '    ',

        sc = convert(len(prime))
        try:
            print '%d-%d' % (len(prime), sc.index(prime))
        except (TypeError, AttributeError):
            print 'Null set'
            continue
"""
    icv = icv(q)
    print 'icv:\t\t\t', icv
"""
