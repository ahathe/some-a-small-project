#!/usr/bin/env python


def a1(a,b,c):
	for x in range(a,b+1,c):
		print x

get1 = int(raw_input("from:"))
get2 = int(raw_input("to:"))
get3 = int(raw_input("increment:"))
a1(get1,get2,get3)
