#!/usr/bin/env python

import os

'the is make file cleans,no whitespace'
#map(lambda x:f.writelines(x),[each for each in f.readlines() if each.isspace() != True])

def maps(fuc):
	if fuc.isspace() == True:
		return fuc.replace(fuc,'')
	else:
		return fuc
def files():
	Getfile = raw_input('input you file name:')
	trues = os.path.isfile(Getfile)
	if trues:
		f = open(Getfile,'r')
		s = f.readlines()
		f.close()
		GetNew = raw_input('(C)reate new file or (O)verwrite before that file:').lower()
		if GetNew == 'c':
			get = raw_input('input you want to create file name:')
			f = open(get,'w')
			f.writelines(map(maps,s))
			f.close()
			print 'c done'
		elif GetNew == 'o':
			f = open(Getfile,'w')
			f.writelines(map(maps,s))
			f.close()
			print 'o done'
		else:
			print 'no such option'
	else:
		print 'not such file'

files()
