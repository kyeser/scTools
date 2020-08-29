from tto import *

def unique(pcset):
    """Removes duplicates from pcset."""
    l = []
    for x in pcset:
        if x not in l:
            l.append(x)
    return l

def fsv(pcset):
    """Finds smallest values of pcset and returns their index numbers."""
    l = []
    for x in range(len(pcset)):
        if len(l) == 0 or pcset[x] < pcset[l[0]]:
            l = [x]
        elif pcset[x] == pcset[l[0]]:
            l.append(x)
    return l

def normalForm(p):
    """Returns normal form of pcset."""
    # Remove duplicates (optional, though fail-safe).
    # p = unique(p)
    # number of elements in p
    n = len(p)
    # Test if p is null set.
    if n == 0:
        return p
    else:
        # Arrange p in ascending order.
        p.sort()
        q = 1
        # Produce the set s comprised of all rotations of p.
        s = [p[y:]+p[0:y] for y in range(n)]
        # Find the subset subset_s of all pccycs s[z] in s where
        # i<s[z][0],s[z][n-q]> is minimal.
        while 1:
            r = [(z[n-q]-z[0])%12 for z in s]
            t = fsv(r)
            subset_s = [s[xx] for xx in t]
            # Delete all members of s not in subset_s.
            s = subset_s
            # If s has only one member, the resulting pccyc is normal_form
            # If q = n, take any member of s and
            # the resulting pccyc is normal_form
            if len(s) == 1 or q == n:
                normal_form = s[0]
                return normal_form
                break
            # Otherwise, increment the value of q by 1 and continue.
            else:
                q += 1
                continue

def primeForm(p):
    """Returns prime form of pcset."""
    # Remove duplicates.
    # p = unique(p)
    # number of elements in p
    n = len(p)
    # Test if p is null set.
    if n == 0:
        return p
    else:
        # Produce inversion of p, ip.
        ip = [(12-x)%12 for x in p]
        # Arrange p and ip in ascending order.
        p.sort(), ip.sort()
        q = 1
        # Produce the set s comprised of all rotations of p and ip.
        s = []
        for y in range(n):
            rotation_p = p[y:]+p[0:y]; s.append(rotation_p)
            rotation_ip = ip[y:]+ip[0:y]; s.append(rotation_ip)
        # Find the subset subset_s of all pccycs s[z] in s where
        # i<s[z][0],s[z][n-q]> is minimal.
        while 1:
            r = [(z[n-q]-z[0])%12 for z in s]
            t = fsv(r)
            subset_s = [s[xx] for xx in t]
            # Delete all members of s not in subset_s.
            s = subset_s
            # If s has only one member, transpose the sole member of s
            # so it begins on 0; if q = n, take any member of s and
            # transpose it so it begins on 0.
            # The resulting pccyc is prime form.
            if len(s) == 1 or q == n:
                s = s[0]
                prime_form = [(yy-s[0])%12 for yy in s]
                return prime_form
                break
            # Otherwise, increment the value of q by 1 and continue.
            else:
                q += 1
                continue

def interval(p):
    return [(p[x]-p[x-1])%12 for x in range(1, len(p))]

def icv(p):
    """Returns interval-class vector of pcset."""
    l = []
    c = 1 
    n = len(p)
    while c < n:
        for x in p:
            for y in range(c, n):
                k = (x-p[y])%12
                if k > 6:
                    k = 12 - k
                l.append(k)
            c += 1
    return [l.count(z) for z in range(1, 7)]

def sim(a, b):
    l = []
    va, vb = icv(a), icv(b)
    for x in range(6):
        k = abs(va[x]-vb[x])
        l.append(k)
    s = sum(l)
    return s

def asim(a, b):
    va, vb = icv(a), icv(b)
    s = sim(a, b)
    sv = sum(va) + sum(vb)
    return float(s) / sv

def uniqueCombinations(items, n):
    if n==0:
        yield []
    else:
        for i in xrange(len(items)):
            for cc in uniqueCombinations(items[i+1:], n-1):
                yield [items[i]]+cc

def permutations(k):
    if k:
        for i, ith in enumerate(k):
            for x in permutations(k[:i] + k[i+1:]):
                x.insert(0, ith)
                yield x
    else:
        yield []

def partitions(n):
    # Base case of recursion: zero is the sum of the empty list.
    if n == 0:
        yield []
        return
    # Modify partitions of n-1 to form partitions of n.
    for p in partitions(n-1):
        yield [1] + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield [p[0] + 1] + p[1:]
