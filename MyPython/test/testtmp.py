#!/usr/bin/env python 

def END():
	pass


string = raw_input("input you string,thank you!:")

strlen = len(string)
length = 0
while length < strlen:
	print string[length]
	length += 1
	if length == strlen:
		length = length - 1
		while length < strlen:
			print string[length]
			length -= 1
			if length == -1:
				break

