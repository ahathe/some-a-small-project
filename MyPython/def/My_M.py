#!/usr/bin/env python

def My_Max(a):
	return max(a)
def My_Min(a):
	return min(a)

list1 = []
while True:
	Get = raw_input('q to quit:')
	if Get == 'q':
		break
	list1.append(Get)

print My_Max(list1),'\n',My_Min(list1)
