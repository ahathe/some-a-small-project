#!/usr/bin/env python

def TAKE():
	get1 = raw_input("do you want to keep ?,yes or no:")
        if get1 == 'y' or 'yes':
                number = int(raw_input("input you start number~:"))
                End = int(raw_input("input you end number:"))
                print 'start %s end %s' % (number,End)
                print 'DEC BIN OCT HEX ASCII'
                for x in range(number,End+1):
                        print x,bin(x),oct(x),hex(x)
        else:
                print 'The End'


def Take(number,End):
	print 'start %s end %s' % (number,End)
	print 'DEC BIN OCT HEX ASCII'
	try:
		for i in range(number,End+1):
			print i,bin(i),oct(i),hex(i),chr(i)
	except ValueError:
		print 'ASCII is out the range'
		TAKE()

	#get1 = raw_input("do you want to keep ?,yes or no:")
	#if get1 == 'y' or 'yes':
		#number = int(raw_input("input you start number~:"))
		#End = int(raw_input("input you end number:"))
		#print 'start %s end %s' % (number,End)
		#print 'DEC BIN OCT HEX ASCII'
		#for x in range(number,End+1):
		#	print x,bin(x),oct(x),hex(x)
	#else:
		#print 'The End'

START = int(raw_input('input START number please~:'))
END = int(raw_input('input END number please~:'))


Take(START,END)
