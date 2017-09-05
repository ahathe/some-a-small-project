#!/usr/bin/env python



def Choice():
	print 'what is you choice?,go to split space to scan or just scan?'
	choice = raw_input('SS or JS!:').upper()
	string = {'JS':JS,'SS':SS}
	if choice not in string:
		print 'not exists'
	else:
		string[choice]()

def JS():
	NewString = raw_input("input you want to sacn that string:").strip()
	ReString = raw_input("input you want to sacn other string:").strip()

	num = NewString.find(ReString)
	num1 = num + 1
	if num1:
		print 'is rigth both string'
	else:
		print 'is not right thank you!'


def SS():
	NewString = raw_input("input you want to sacn that string:").strip()
	ReString = raw_input("input you want to sacn other string:").strip()
	RNEW = '.'.join(NewString.split('	'))
	RERES = '.'.join(ReString.split('	'))
	rNEW = '.'.join(RNEW.split(' '))
	rERES = '.'.join(RERES.split(' '))
	rLnEW = rNEW.split('.')
	rLrES = rERES.split('.')
	num1 = rLnEW.count('')
	num2 = rLrES.count('')
	while num1:
		rLnEW.remove('')
		num1 -= 1
	while num2:
		rLrES.remove('')
		num2 -= 1
	if '' not in (rLrES and rLnEW):
		str1 = '.'.join(rLnEW)
		str2 = '.'.join(rLrES)
		num3 = str1.find(str2)
		num3 += 1
		if num3:
			print 'is right both string!'
		else:
			print 'is not right thank you!'

Choice()
