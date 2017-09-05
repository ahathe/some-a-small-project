#!/usr/bin/env python

import os

def Finfo(files):
	truef= os.path.isfile(files)
	if truef:
		if '/' in files:
			os.chdir(os.path.split(files)[0])
			files = files.split('/')[-1]
		f = open(files,'r')
		count = 0
		for x in f:
			count += 1
		print 'the total line is %s' % count
	else:
		print 'not exists filename try again'
	



GET_FILE = raw_input("input you file name or full file path name~:")
Finfo(GET_FILE)
