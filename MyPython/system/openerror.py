#!/usr/bin/env python

def opener(obj):

	try:
		f = open(obj,'r')
	except (IOError,TypeError),e:
		return None
	else:
		return f

def safe_input():
	try:
		find = raw_input('input you files:')
	except (EOFError,KeyboardInterrupt),e:
		e =  None
		print e
	else:
		s = opener(find)
		print s
safe_input()
	



