def Leap(years):
	if years % 4 == 0 and years % 100 != 0:
		print 'is leap years,thank you!'
	elif years % 4 != 0 and years % 100 != 0:
		print 'is not leap years,thank you!'
	elif years % 4 == 0 and years % 100 == 0:
		print 'is century leap years,thank you!'
	else:
		print 'i do not konw what is that ,im so sory!'

while True:
	try:
		years = int(raw_input("you can input years number going to prove is leap years or not!:"))
	except ValueError,e:
		print 'is illegality,please input int() type,thank you!,try again!'	
	else:
		Leap(years)
	break
