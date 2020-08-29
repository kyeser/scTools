from tto import *

def matrixT(a, b):
    l = [(y-x)%12 for x in a for y in b]
    return [l.count(z) for z in range(12)]

def matrixTI(a, b):
    l = [(y+x)%12 for x in a for y in b]
    return [l.count(z) for z in range(12)]

def matrixM(a, b):
    ma = M5(a)
    l = [(y-x)%12 for x in ma for y in b]
    return [l.count(z) for z in range(12)]

def matrixMI(a, b):
    ma = M5(a)
    l = [(y+x)%12 for x in ma for y in b]
    return [l.count(z) for z in range(12)]

def vtics(r):
    l = [(x+y)%12 for x in r for y in r]
    return [l.count(z) for z in range(12)]
