#!/usr/bin/env python

list1 = []
def Isperferct(num):
	for x in range(1,num+1):
		num1 = num % x
		if num1 == 0:
			list1.append(x)
	else:
		length = len(list1)
		if length > 2:
			list1.pop()
			sumcount = sum(list1)
			if sumcount == num:
				print 'The is preferct %s -> %s' % (list1,sumcount)
			else:
				print 'not preferct %s -> %s' % (list1,sumcount)
		else:
			if num == 1:
				print 'is preferct %d' % 1
			else:
				print 'not preferct %s' % list1

get1 = int(raw_input("input you number,must be number:"))
Isperferct(get1)
