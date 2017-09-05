#!/usr/bin/env python

def count(a,b):
	list1 = list()
	list1.append(a)
	list1.append(b)
	sums = sum(list1)
	return sums
	

get1 = int(raw_input("input one number:"))
get2 = int(raw_input("input two number:"))

if __name__=="__main__":
	print count(get1,get2)

