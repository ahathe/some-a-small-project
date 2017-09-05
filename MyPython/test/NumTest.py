#!/usr/bin/env python

'is input number to count mean and total'


empty = []

def Input():
	while True:
		num = raw_input("input you number to count mean!,input 'q' is going to quit!:")
		if num == ('q' or 'Q'):
			print 'rechoice input type,input or to count or remove or view!'
			Choice()
		else:
			try:
				number = float(num)
			except ValueError:
				print 'is not number,reinput!'
			else:
				if type(number) == type(1.2):
					empty.append(number)
					print empty

def Count():
	length = len(empty)
	total =	sum(empty)	
	mean = float(total) / float(length)
	print "is working!"
	print 'the mean is %s' % mean


def Remove():
	print 'what number you want to remove?!'
	while True:		
		print 'make you choice ,input you want to remove that number! %s' % empty
		remove = raw_input("input you want to remove float value!:")
		if remove == ('q' or 'Q'):
			Choice()
			break
		try:
			move = float(remove)
		except ValueError:
			print 'invalid value ,plaese input int or float type!,thank you!'
		else:
			if move in empty:
				empty.remove(move)
				print 'is been removed %s' % move
				print 'new number total is %s' % empty
				break
			else:
				print "plaese input float type value!"


def View():
	Count()
	print 'the mean list is %s' % empty

def Choice():
	while True:
		choice = raw_input("input you choice,count or input or remove or view:").strip().lower()
		string = ["input","count","remove","view"]
		dict1 = {"input":Input,"count":Count,"remove":Remove,"view":View}
		if choice not in string:
			print "is invalid option,plaese choice input or count to make mean!"
		else:
			dict1[choice]()
Choice()
