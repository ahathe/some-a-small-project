#!usr/bin/ env python

'the is grade count,haha,lol!'

#score = int(raw_input("please,input you want to view score number!:"))

def View(number):
	if number <= 100 and number >= 90:
		print 'you score is good A!'
	elif number <= 89 and number >= 80:
		print 'you score is good B!'
	elif number <= 79 and number >= 70:
		print 'you score is little Better C!'
	elif number <= 69 and number >= 60:
		print 'you score is bad D!'
	elif number >= 0 and number <= 59:
		print 'you score is so bad F!'
	else:
		print 'plaese input number between 0~100 view you score,thank you for you try again!'
while True:
	try:
		score = int(raw_input("please,input you want to view score number!,between 0~100,thank you!:"))
	except ValueError,e:
		print 'thes value is illegality,plaese input int() type number,thank you!',e
	else:
		View(score)
		break
