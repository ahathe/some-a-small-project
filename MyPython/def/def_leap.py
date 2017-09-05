#!/usr/bin/env python

list1 = []

def leap(num):
	return (num % 4 == 0 and num % 100 !=0) or (num % 400 == 0)

count = 3
while count > 0:
	list1.append(int(raw_input("input you list:")))
	count -= 1

print 'leap have',filter(leap,list1)
	
