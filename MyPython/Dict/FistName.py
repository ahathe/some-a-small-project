#!/usr/bin/env python

list2 = list()
def Fname(num):
	count = 0
	num1 = 0
	while count < num:
		ge1 = raw_input("input you name last name , first name:")
		if ',' in ge1:
			list1 = ge1.split(',')
			list2.append(list1)
		elif ',' not in ge1:
			num1 += 1
			print 'you have done this %s time already.fixing input..' % num1
		count += 1
	else:
		if count >= num:
			for i in list2:
				a = ','.join(i)
				print a
try:
	get = int(raw_input("input you want to make how many of name number:"))
	#Fname(get)
except ValueError:
	print 'must be number ~'
else:
	Fname(get)
