#!/usr/bin/env python

import os
import pickle

list2 = []
def bit(files):
	true = os.path.isfile(files)
	if true:
		f = open(files,'rb')
		list1 = pickle.load(f)
		for each in list1:
			getlist = chr(int(each,2))
			list2.append(getlist)
		get_word = raw_input("input you want to scaning word!:")	
		count = list2.count(get_word)
		if count:
			length = bin(ord(get_word)).replace('0b','')
			total = count * length
			print '%s word has %d time in the %s file,total byte length is %s' % (get_word,count,files,len(total))
		else:
			print 'the word is zero in the file'

	else:
		print 'not such file'
get = raw_input("input you byte files:")
bit(get)
