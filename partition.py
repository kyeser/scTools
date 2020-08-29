#!/usr/bin/env python
from scTools import partitions

n = int(raw_input("-> "))
c = 0

for x in partitions(n):
    print x
    c += 1

print 'Total: %d' % c
