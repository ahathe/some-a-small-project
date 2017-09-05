#!/usr/bin/env python
import os

filename = raw_input("enter file name :")
fobj = open(filename,'w')
while True:
	aline = raw_input("enter a line ('.' to quit):")
	if aline != '.':
		fobj.write('%s%s' % (aline,os.linesep))
	else:
		break
fobj.close()
