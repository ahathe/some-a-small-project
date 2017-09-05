#!/usr/bin/env python

import os

def line25(files):
	truef = os.path.isfile(files)
	if truef:
		count = 25
		if '/' in files:
			os.chdir(os.path.split(files)[0])
			files = files.split('/')[-1]
	
		f = open(files,'r')
		while f.readline():
			while count:
				count -= 1
				print f.readline(),
			if f.readline() != '':
				Get25 = raw_input("input Enter key to continue~:")
				if Get25 == '':
					count = 25
		if f.readline() == '':
			print 'The End'
			f.close()
	else:
		print 'not file name or full file path name ,retry again~'
GET_FILEs = raw_input("input you file name or full file path name~:")

line25(GET_FILEs)
