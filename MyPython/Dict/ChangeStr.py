#!/usr/bin/env python

def tr(srcstr,dststr,string):
	num1 = len(srcstr)
	num2 = len(dststr)
	if num1 >= num2:
		if srcstr in string:
			newstring = dststr.join(string.split(srcstr))
			print 'the has been repaced~ %s' % newstring
		else:
			print 'the %s not in string ,try again' % (srcstr,string)
	else:
		print '%s and %s length not matching~,try again' % (srcstr,dststr)

a = raw_input("input you want to change string:").lower()
c = raw_input("select you part that string:").lower()
b = raw_input("input you want to repace that string:").lower()

if __name__=="__main__":
	tr(c,b,a)
