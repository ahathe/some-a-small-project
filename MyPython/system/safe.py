#!/usr/bin/env python

def safe(object):

	try:
		retval = float(object)
	except (ValueError,TypeError),diag:
		retval = str(diag)
	return retval

g = raw_input('---:')
s = safe(g)
print s
