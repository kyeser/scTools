#!/usr/bin/env python
from numarray.random_array import permutation

while 1:
	c = 1
	try:
		s = int(raw_input("\nEnter a desired number of permutations of 12: "))
	except ValueError:
		print '\nSingle integer only!'
		continue
	except (EOFError, KeyboardInterrupt):
		print
		break
	
	print ""		# This does nothing; just makes the format prettier.

	while c <= s:
		t = permutation(12)
		print "%4d\t" % c,
		# The following two lines convert numbers in arrays into hex.
		for x in t:
			print "%X" % int(x),
		print ""
		c += 1
