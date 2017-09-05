#!/usr/bin/env python

'identify naming notations string'

import string
import keyword

astring = string.letters + '_'
nums = string.digits
numstring = astring + nums

def Identify(name):
	if name[0] not in astring:
		print '''im sory first string error!
			first must be string or '_' thank you!'''
	elif name in keyword.kwlist:
		print ''' sory is keyword'''		
	else:
		for other in name[1:]:
			if other not in numstring:	
				print '''first string after iliegality string!,must be
					string or number!,thank you!'''
				break
			else:
				print "ok"
			
INPUT = raw_input("input,you want to identify!:")
if __name__=='__main__':
	Identify(INPUT)
