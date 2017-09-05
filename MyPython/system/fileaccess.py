#!/usr/bin/env python

import os

def Fileaccess(name):
	truef = os.path.isfile(name)
	if truef:
		if '/' in name:
			dirs = os.path.split(name)
			os.chdir(dirs[0])
			name = name.split('/')[-1]		
		zero = 0
		count = 3
		while count > 0:
			try:
				GET_The_N = int(raw_input("input the N to F lines number~ N:"))
				GET_The_F = int(raw_input("F:"))
				if type(GET_The_N) and type(GET_The_F) == type(0):
					zero = 1
					break
			except ValueError:
				count -= 1
				print 'must be a number try again,you have %s chance over' % count
		if zero == 1:
			N = GET_The_N
			F = GET_The_F
			files = open(name,'r')
			count2 = 0
			while count2 < N:
				count2 += 1
				n = files.readline()
			f = F - N
			while f:
				f -= 1
				print files.readline(),
		files.close()
	else:
		print 'The < %s > is not file name or full file name path,please try again~' % name
				


GET_Th_FN = raw_input("input you current file name or absolute path that file name:")

Fileaccess(GET_Th_FN)
