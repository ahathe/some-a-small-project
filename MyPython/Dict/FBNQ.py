#!/usr/bin/env python


def run(num):
	a = 1
	b = 1
	c = num / 2
	d =  num % c
	if d == 1:
		c = c + d
		while c > 0:
			print a
			print b
			a = a + b
			b = a + b
			c -= 1
			if c == 1:
				print a
				break
	else:
		while c > 0:
			print a
			print b
			a = a + b
			b = a + b
			c -= 1


get1 = int(raw_input("get you input number:"))
run(get1)
