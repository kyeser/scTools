from tto import *

def reduceZero(p):
    return [(x-p[0])%12 for x in p]

def reduceR(p):
    s = R(p)
    return reduceZero(s)

def reduceI(p):
    s = I(p)
    return reduceZero(s)

def reduceRI(p):
    s = RI(p)
    return reduceZero(s)

def reduceM5(p):
    s = M5(p)
    return reduceZero(s)

def reduceM5R(p):
    s = R(M5(p))
    return reduceZero(s)

def reduceM7(p):
    s = M7(p)
    return reduceZero(s)

def reduceM7R(p):
    s = R(M7(p))
    return reduceZero(s)
