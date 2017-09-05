def Type(num):
	print num,"is",
	if type(num) == type(0):
		print 'an integer'
	elif type(num) == type(0l):
		print 'an long'
	elif type(num) == type(0.0):
		print 'is folat'
	elif type(num) == type(0+0j):
		print 'a complex number'
	else:
		print 'not a number at all'

Type(2222)
