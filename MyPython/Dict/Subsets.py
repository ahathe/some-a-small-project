#!/usr/bin/env python

def subS(one,two):
	print 'the is set string %s' % one
	print 'the is subset of the set %s' % two
	result = set(one) > set(two)
	print 'do you think -> %s is -> %s that subset?' % (two,one)
	inpu = raw_input("yes or no:")
	if inpu == 'yes' or 'y':
		if result:
			print 'you is right %s' % result
		else:
			print 'is wrong'
			print 'the result is %s' % result
	elif inpu == 'no' or 'n':
		if result:
			print 'you is right'
			print 'the result is %s' % result
		else:
			print 'is right %s' % result
	else:
		print 'two and one not have some string in each set or subset'

get1 = raw_input("input you string:")
get2 = raw_input("input you sub string:")

subS(get1,get2)
