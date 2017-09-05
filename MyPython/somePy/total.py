one = int(raw_input("input you first one number,please!:"))
two = int(raw_input("input you other two number,please!:"))
three = int(raw_input ("input you next three number,please!:"))
if one > two and two > three:
	print '%d %d %d' % (one,two,three)
elif two > three and three > one:
	print '%d %d %d' % (two,three,one)
elif three > one and one > two:
	print '%d %d %d' % (three,one,two)
elif two > one and one > three:
	print '%d %d %d' % (two,one,three)
elif three > two and two > one:
	print '%d %d %d' % (three,two,one)
elif one > three and three > two:
	print '%d %d %d' % (one,three,two)
