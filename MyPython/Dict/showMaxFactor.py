#!/usr/bin/env python

def showMaxFactor(num):
	count = num / 2
	while count > 1:
		if num % count == 0:
			print 'of %d is %d' % (num,count)
			break
		count -= 1
	else:
		print num, 'is prime'
while True:
	get1 = int(raw_input("get input:"))
	showMaxFactor(get1)
