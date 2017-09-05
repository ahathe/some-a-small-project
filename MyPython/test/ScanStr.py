#!/usr/bin/env python

def findchar(string,char):
	if char in string:
		length = len(string)
		for x in range(length):
			if string[x] == char:
				print 'the char index has find %s' % x
				break
	else:
		print "not exist  -1"




String = raw_input("input you string!:")
Scan = raw_input("input you want to find string!:")
if __name__=="__main__":
	findchar(String,Scan)
