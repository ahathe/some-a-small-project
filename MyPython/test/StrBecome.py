#!/usr/bin/env python

'make string become largest to smallest orade! '

num = list(raw_input("plaese input number!thank you!:"))
choice = raw_input("input you choice!,one or two:")
one = 'one'
two = 'two'

if choice == one:
	num.sort()
	print num
elif choice == two:
	num.sort()
	for x,i in enumerate(num):
		print x,i
