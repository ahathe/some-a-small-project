#!/usr/bin/env python

list1 = []

def getfactors(num):
	for x in range(1,num+1):
		num1 = num % x
		if num1 == 0:
			list1.append(x)
	else:
		print 'factors is %s' % list1
			



get1 = int(raw_input("input you number~:"))
getfactors(get1)
