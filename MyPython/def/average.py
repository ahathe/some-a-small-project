#!/usr/bin/env python

def average(list1):
	count = 0
	while list1:
		count += list1.pop(0)
	return count
list1 = [1,2,3,4,5]
print average(list1)
