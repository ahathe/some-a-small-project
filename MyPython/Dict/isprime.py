#!/usr/bin/env python

def isprime(prime):
	if prime == 1:
		print 'False'
	else:
		for each in range(2,prime):
			if prime % each == 0:
				print 'False'
				break
			else:
				print 'True'
				break
try:
	get = int(raw_input("input you number,must be number:"))
	isprime(get)
except ValueError:
	print 'must be number,sory'

