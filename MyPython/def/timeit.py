#!/usr/bin/env python

import time

def timeit(fuc,*agr):
	try:
		result = fuc(*agr)
	except (ValueError,TypeError),e:
		result = e
		print e
	return result


def test():
	fucs = (int,float,long)
	var = ('12.34','1234',1234,12.34)
	for each in fucs:
		print '-'*20
		for values in var:
			get = timeit(each,values)
			print 'the time is',time.time()
			print get

test()
