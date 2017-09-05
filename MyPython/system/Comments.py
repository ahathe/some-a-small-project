#!/usr/bin/env python

import os

def Filter(files):
	absp = os.path.isabs(files)
	isfile = os.path.isfile(files)
	if absp and isfile:
		filename = os.path.split(files)[1]
		f = open(filename,'r')
		for x in f:
			if x[0] != '#':
				a = x[:x.find('#')]
				stripout = a.strip()
				print stripout
		else:
			print '------------------------'
			print "Is Done.The file inside those that script All  comment '#' has been ignored ~"
			f.close()
	elif isfile:
		f = open(files,'r')
		for x in f:
			if x[0] != '#':
				a = x[:x.find('#')]
				stripout = a.strip()
				print stripout
		else:
			print '------------------------'
			print "'Is Done.The file inside those that script All comment '#' has been ignored~'"
			f.close()
	else:
		print "The's file not existed,look over if was exist current directory \
or absolute path file names~,try again"

Get_Filename = raw_input("input you filenames or path file names:")

if __name__=="__main__":
	Filter(Get_Filename)
