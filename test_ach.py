#!/usr/bin/env python
from scTools import primeForm
from scTools.rowData import ais
from scTools.scData import *

britten = [[9, 2, 11, 4, 1, 6, 8, 3, 5, 10, 7, 0]]

def searchHex(sc):
    count = 1
    index = 1
    for x in britten:
        prime = primeForm(x[0:6])
        if prime == sc6[sc]:
            print '\n%2d\t%3d\t' % (count, index),
            for y in x:
                print '%X' % y,
            print '\t6-%d' % sc,
            count += 1
        index += 1
    print

searchHex(1)
searchHex(8)
searchHex(32)
searchHex(7)
searchHex(20)
searchHex(35)
