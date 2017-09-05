#!/usr/bin/env python

import os
import sys

def copy():
	if len(sys.argv) == 3:
		files = sys.argv[1:]
		trues_1 = files[0] in os.listdir(os.getcwd())
		trues_2 = files[1] in os.listdir(os.getcwd())
		if trues_1 and trues_2:
			print 'yet you fisrt file and second files is exists'
			f = open(files[0],'r')
			get_r = f.readlines()
			f.close()
			f = open(files[1],'a+')
			f.writelines(get_r)
			f.close()
			print 'is done'
			print 'is copy'
		elif trues_1 and not trues_2:
			print 'the second file is not in dir,do you want to create?'
			get_y = raw_input("input y to create file then copy in second file!:")
			if get_y in 'yY':
				f = open(files[0],'r')
				read = f.readlines()
				f.close()
				f = open(files[1],'w')
				f.writelines(read)
				f.close()
				print 'is done'
			else:
				print 'is quit'
		else:
			print 'not such file pelase try again!'
	else:
		print 'must be two files,then copy'
copy()
		
