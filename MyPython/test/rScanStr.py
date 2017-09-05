#!/usr/bin/env python

def rfindchar(string,char):
	if char in string:
		a = range(len(string))
		a.reverse()
		for x in a:
			if string[x] == char:
				print 'The last index find is %s' % x
				break
			
	


rString = raw_input("input you string!:")
rScan = raw_input("input you want to scan char!:")
if __name__=="__main__":
	rfindchar(rString,rScan)
