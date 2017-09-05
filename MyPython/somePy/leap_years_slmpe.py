get_input_number1 = raw_input("input you number count,thank you!:")
get_input_number2 = raw_input("input you want to count to!:")
get_input_number3 = raw_input("input you number count to!:")

num1 = int(get_input_number1)
num2 = int(get_input_number3)

if get_input_number2 == '+':
	num3 = num1 + num2
	print "the result is %s" % num3
elif get_input_number2 == '-':
	num3 = num1 - num2
	print "the result is %s" % num3
elif get_input_number2 == '*':
	num3 = num1 * num2
	print "the result is %s" % num3

	
	
