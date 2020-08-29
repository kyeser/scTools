"""PySco v0.1, random Csound score file generator

Runs on all platforms.  Python 2.3.4 or higher and Numarray 1.0 or higher required.

This document was generated using pydoc module.

Copyright (c) 2004 by Hee-Seng Kye
All rights reserved.

Questions or comments: katsura@msbx.net
"""

__author__ = "Hee-Seng Kye <katsura@msbx.net>"
__date__ = "7 July 2004"
__version__ = "$Revision: 0.1 $"

from numpy.random import randint, random

def midi(file, tempo, count, low, high, soft, loud, shape):
    """
    file = Name of the output file:
    The filename must be enclosed within '' or "" (e.g., 'test.sco').
    
    tempo = Desired initial tempo
    
    count = Number of instruments (count > 0):
    Total number of instruments.  The value for count must be bigger than 0.
    
    low = Minimum frequency value (min >= 0):
    Lowest pitch.  0 is equivalent to C1.
    
    high = Maximum frequency value:
    Highest pitch.  While there is no maximum value, it is good to keep in
    mind that 127 is equivalent to G9.
        
    soft = Minimum amplitude value (min >= 0):
    Lower bound of dynamic value.  40 is roughly equivalent to ppp
    (pianississimo).
    
    loud = Maximum amplitude value:
    Higher bound of dynamic value.  100 is roughly equivalent to fff
    (fortississimo).

    shape = Number of notes (shape > 0):
    Total number of notes per instrument.

    Usage example:
    >>> from pysco import *     # or (>>> from pysco import midi)
    >>> midi('test.sco', 60, 4, 0, 128, 0, 121, 250)
    
    or
    
    >>> import pysco
    >>> pysco.midi('test.sco', 60, 4, 0, 128, 0, 121, 250)  
    """
    f = open(file, "w")
    # Provide built-in functions (f-statements) to be used
    print >>f, '; Csound score file created by PySco v0.1\n'
    print >>f, '; Built-in Functions'
    print >>f, '; Function 1 uses the GEN10 subroutine to compute a sine wave'
    print >>f, '; Function 2 uses the GEN10 subroutine to compute the first sixteen partials of a sawtooth wave'
    print >>f, '; Function 6 uses the GEN20 subroutine to compute a Hanning window for use as a grain envelope'

    print >>f, ""
    
    print >>f, 'f1 0 4096 10 1'
    print >>f, 'f2 0 4096 10 1 .5 .333 .25 .2 .166 .142 .125 .111 .1 .09 .083 .076 .071 .666 .062'
    print >>f, 'f3 0 4096 10 1 0 .3 0 .2 0 .14 0 .111'
    print >>f, 'f4 0 4096 10 1 1 1 1 .7 .5 .3 .1'
    print >>f, 'f5 0 4096 10 21 1 0 22 1 0 25 1 0 27 1 0 31 1 0 33 1 0 34 1 0 35 1 0'
    print >>f, 'f6 0 4097 20 2 1'

    print >>f, '\nt 0 %d' % (tempo)

    print >>f, '\n;ins\tstr\tdur\tamp\tfrq\tfunc\tpan'
    print >>f, ';p1\tp2\tp3\tp4\tp5\tp6\tp7\n'

    inst = 1
    while inst <= count:

        amp = randint(soft, loud, (shape, ))
        frq = randint(low, high, (shape, ))
        func = randint(1, 7, (shape, ))
        # First i-statement of each instrument
        print >>f, '; instr', inst
        print >>f, 'i', inst, '\t',                         #p1
        print >>f, '0\t', '%0.3f\t' % (random()),           #p3
        print >>f, '%d\t' % int(amp[shape-2]),              #p4
        print >>f, '%d\t' % int(frq[shape-2]),              #p5
        print >>f, '%d\t' % int(func[shape-2]),             #p6
        print >>f, '%0.3f' % (random())                     #p7
        # Second i-statement of each instrument
        print >>f, 'i', inst, '\t',                         #p1
        print >>f, '+\t', '%0.3f\t' % (random()),           #p3
        print >>f, '%d\t' % int(amp[shape-1]),              #p4
        print >>f, '%d\t' % int(frq[shape-1]),              #p5
        print >>f, '%d\t' % int(func[shape-1]),             #p6
        print >>f, '%0.3f' % (random())                     #p7
        # Remaining i-statements of each instrument
        for x in range(0, shape-2):
            print >>f, 'i', inst, '\t',                     #p1
            print >>f, '.\t', '%0.3f\t' % (random()),       #p3
            print >>f, '%d\t' % int(amp[x]),                #p4
            print >>f, '%d\t' % int(frq[x]),                #p5
            print >>f, '%d\t' % int(func[x]),               #p6
            print >>f, '%0.3f' % (random())                 #p7

        print >>f, ""
        inst += 1
    f.close()
