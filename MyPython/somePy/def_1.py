#!/usr/bin/env python

def Type(num):
	print num,'is',
	if isinstance(num,(int,long,float,complex)):
		print 'a number of type:',type(num).__name__
	else:
		print 'not a number at all!!'
Type(-69)
Type(9999999999999999999999L)
Type(98.6)
Type(-5.2+1.9j)
Type('xxx')
