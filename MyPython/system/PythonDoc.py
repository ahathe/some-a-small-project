#!/usr/bin/env python

import os

list1 = []
count = 1
list2 = []
def Doc(count):
	os.chdir("/usr/lib/python2.7")
	files = os.listdir(os.getcwd())
	for x in files:
		if '.py' == os.path.splitext(x)[1]:
			list1.append(x)

	for each in list1:
		f = open(each,'r')
		string = f.readlines()
		string = ''.join(string)
		string = string.split('"""')
		print 'The File Name Is [ %s ] and by DOC  ><><><><><>><><><><><><><><><><><><><><>><><> DOC AND FileName' % each
		length = len(string)
		if length == 1:
			list2.append(each)
			continue

		for x in range(len(string)):
			s = x % 2
			if s != 0:
				print '--------------line-----number---------------%s' % count
				print string[x]
				count += 1
		else:
			f.close()
			count = 1
	else:
		print "These file don't have doc yet !"
		print list2
		return count
	
			
	
	
Doc(count)
