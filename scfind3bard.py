#!/usr/bin/env python3
"""
PyTTO v0.1, SC finder

This document was generated using the pydoc module.
"""

from scTools import icv, unique, normalForm, primeForm
from scTools.scData import *

print('\nSCFinder v0.1\n')

while True:
    try:
        n = input("\nEnter a pcset: ")  # Use input() instead of raw_input()
    except (EOFError, KeyboardInterrupt):
        print()
        break

    r = n.split()

    if n == 'q' or n == 'quit':
        break
    elif n == 'v' or n == 'version':
        print('scFind v0.1, Set-Class Finder')
    elif n == 'h' or n == 'help':
        print('q, quit\t\tQuit.')
        print('h, help\t\tThis help message.')
        print('v, version\tVersion info.')
    else:
        try:
            q = [int(x) % 12 for x in r]
        except ValueError:
            print('Integers only!')
            continue

        q = unique(q)
        print('Set you entered:\t', q)

        normal = normalForm(q)
        print('Normal form:\t\t', normal)

        prime = primeForm(q)
        print('Prime form:\t\t', prime, '  ', end='')  # Use end='' for no newline

        sc = convert(len(prime))
        try:
            print('%d-%d' % (len(prime), sc.index(prime)))
        except (TypeError, AttributeError):
            print('Null set')
            continue

        # icv = icv(q)  # This line is commented out in the original code
        # print('icv:\t\t\t', icv)
