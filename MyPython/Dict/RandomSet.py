#!/usr/bin/env python

import random 


A = set()
B = set()
#def st():
	

def ts():
	while len(A) < 10 and len(B) < 10:
		C = random.randint(0,9)
		D = random.randint(5,15)
		A.add(C)
		B.add(D)
	print A.union(B)
	set1 = set()
	count = 0
	while count < 3:
		try:
			while True:
				set1.add(int(raw_input("must be number,A | B set() guess,any key to break:")))
				print set1
		except ValueError:
			print 'is break'
			if set1 == A.union(B):
				print A.union(B)
				print "is right"
				break
			else:
				result = count + 1
				print "is wrong,try again~ you has been crash %s chance,total three chance" % result
		finally:
				
			count += 1
			if count == 3:
				print "you do not have chance anymore,the resulted is %s" % A.union(B)
	print 
	print 'next A & B try~'
	set2 = set()	
	count1 = 0
	print A.intersection(B)
	while count1 < 3:
		try:
			while True:
				set2.add(int(raw_input("must be number,A & B set() guess,any key to break:")))
				print set2
		except ValueError:
			print 'is break'
			if set2 == A.intersection(B):
				print A.intersection(B)
				print "is right"
				break
			else:
				result = count1 + 1
				print "is wrong ,try again~ you has been crash %s chance,total three chance" % result
		finally:
			count1 += 1
			if count1 == 3:
				print 'you do not have chance anymore ,the resulted is %s' % A.intersection(B)

ts()
