#!/usr/bin/env python

def Count(count):
	if ' ' in count:
		count = count.split(' ')
	lisT = ['+','-','*','/','%','**']
	if count[1] in lisT:
		
	

Input = raw_input("input you want to count number and operator!:")
Count(Input)
