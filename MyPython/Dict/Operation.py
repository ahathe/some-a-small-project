#!/usr/bin/env python

list1 = ['in','not indict']

def Opr(one,two,three):
	one = set(one)
	three = set(three)
	if two == 'not in':
		one = one.pop()
		if one not in three:
			print "is right %s not in %s" % (one,three)
		else:
			print 'is wrong %s is in %s' % (one,three)
	elif two == 'in':
		one = one.pop()
		if one in three:
			print 'is right %s in %s' % (one,three)
		else:
			print 'is wrong %s is not in %s' % (one,three)
	elif two == '&':
		result = one & three
		print 'the result is %s' % result
	elif two == '|':
		result = one | three
		print 'the result is %s' % result
	elif two == '^':
		result = one ^ three
		print 'the result is %s' % result
	elif two == '<':
		result = one < three
		print 'the result is %s' % result
	elif two == '<=':
		result = one <= three
		print 'the result is %s' % result
	elif two == '>':
		result = one > three
		print 'the result is %s' % result
	elif two == '>=':
		result = one >= three
		print 'the result is %s' % result
	elif two == '==':
		result = one == three
		print 'the result is %s' % result
	elif two == '!=':
		result = one != three
		print 'the result is %s' % result
	else:
		print 'illegality operator character~,try again'

get1 = raw_input("input you set string:")
get2 = raw_input("input you operator character:")
get3 = raw_input("input you other set string:")

Opr(get1,get2,get3)
