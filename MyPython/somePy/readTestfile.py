#!/usr/bin/env python

'readTextfile.py -- read and display test file'
fname = raw_input("Enter filename:")
print

try:
	fobj = open(fname,'r')
except IOError,e:
	print " file open error:",e
else:
	for eachLine in fobj:
		print eachLine.strip()
	fobj.close()
