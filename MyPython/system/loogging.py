#!/usr/bin/env python

import sys
import shelve

def count():
	list1 = sys.argv[1:]
	if len(list1) >= 1:
		if list1[0] !=  'print':
			string = ''.join(list1)
			if '^' in string:
				string = '**'.join(string.split('^'))
			result = eval(string)
			print 'the result is %s' % result
			dictfiles = shelve.open('count')
			if '**' in string:
				string = '^'.join(string.split('**'))
			news = ' '.join(string)
			dictfiles[news] = result
			dictfiles.close()
		else:
			dictfiles = shelve.open('count')
			for do in dictfiles:
				print do
				print dictfiles[do]

count()
