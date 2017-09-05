#!/usr/bin/env python

import string 
letter = string.letters
dict1 = string.letters[26:]
dict2 = string.letters[:26]

dict3 = dict1[13:]
dict4 = dict1[:13]
dict7 = dict2[:13]
dict8 = dict2[13:]

dict5 = dict(zip(dict3,dict4))
dict6 = dict(zip(dict4,dict3))

dict9 = dict(zip(dict7,dict8))
dict10 = dict(zip(dict8,dict7))

dict9.update(dict10)
dict5.update(dict6)

Newdict = dict5
Newdict.update(dict9)

def Get(string):
	print "You rot13 string to en/decrypt was: [%s]." % string
	list1 = list(string)
	length = len(list1)
	for x in range(length):
		index = list1[x]
		if index in Newdict:
			list1[x] = Newdict[index]
	result = ''.join(list1)
	print 'The rot13 string is: [%s].' % result

get = raw_input("Enter string to rot13: ")

Get(get)

