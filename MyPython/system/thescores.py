#!/usr/bin/env python

import os
list1 = list()
def testscores(files):
	truef = os.path.isfile(files)
	if truef:
		if '/' in files:
			os.chdir(os.path.split(files)[0])
			files = files.split('/')[-1]
	f = open(files,'r')
	for num in f:
		num = int(num)
		if int(num) <= 100 and int(num) >= 90:
			print '%s scores is > %s' % (num,'A')
		if num <= 89 and num >= 80:
			print '%s scores is > %s' % (num,'B')
		if num <= 79 and num >= 70:
			print '%s scores is > %s' % (num,'C')
		if num <= 69 and num > 60:
			print '%s scores is > %s' % (num,'D')
		if num < 60:
			print '%s scores is > %s' % (num,'F')
		list1.append(num)
	countadd = sum(list1)
	result = countadd / len(list1)
	print 'the mean is %s' % result
	f.close()
GET_Files = raw_input("input you file name or full file path name to test scores~:")
testscores(GET_Files)
