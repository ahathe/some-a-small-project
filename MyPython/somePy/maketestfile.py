#!/usr/bin/env python

'makeTestFile.py -- create test file'
 
import os
ls = os.linesep

#get filename#
while True:
	if os.path.exists(fname):
		print "ERROR: '%s' already exists" % fname
	else:
		break
print "\nEnter lines ('.' by itself to quit). \n"

# loop until user terminates input
while True:
	fname = raw_input('> ')
	if fname == '.':
		break
	else:
		all.append(fname)


# write lines to file with proper line-ending
fobj = open(fname,'w')
fobj.writelines(['%s%s' % (x,ls) for x in all])
fobj.close()
print 'DONE!'
