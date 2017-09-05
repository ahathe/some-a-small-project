#!/usr/bin/env python

import os

def Text(File):
	trues = os.path.isfile(File)
	if trues:
		f = open(File,'r+')
		count = 80
		while True:
			if f.read(1) == '':
				break
			f.seek(80,1)
			f.write('\n')
			count += 80
			
		f.close()
		print 'is done'
	else:
		print 'not such file,try again'


get_files = raw_input("input you file name to scan:")
Text(get_files)
