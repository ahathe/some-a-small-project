#!/usr/bin/env python

def subchr(string,origchar,newchar):
	if origchar in string:
		result = newchar.join(string.split(origchar))
		print 'The result it is %s' % result
	else:
		print 'char not in string!'



String = raw_input("input you string ,thank you !:")
Input_You_Find = raw_input("input you want to find string !:")
Input_You_Repace = raw_input("input you want to repace that string !:")
if __name__=="__main__":
	subchr(String,Input_You_Find,Input_You_Repace)
