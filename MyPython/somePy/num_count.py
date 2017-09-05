def Get(get_num):
	if get_num[1] == '*':
		get = int(get_num[0]) * int(get_num[2])
		print 'the is result is %s' % get
	elif get_num[1] == '-':
		get = int(get_num[0]) - int(get_num[2])
		print 'the is result is %s' % get
	elif get_num[1] == '+':
		get = int(get_num[0]) + int(get_num[2])
		print 'the is result is %s' % get
	elif get_num[1] == '/':
		get = int(get_num[0]) / int(get_num[2])
		print 'the is result is %s' % get
	elif get_num[1] == '%':
		get = int(get_num[0]) % int(get_num[2])
		print 'the is result is %s' % get
	elif get_num[1] == '**':
		get = int(get_num[0]) ** int(get_num[2])
		print 'the is result is %s' % get


get_num = raw_input("input count,please:")
Get(get_num)
