num = int(raw_input("input you number!:"))

if num >= 1 and num <= 100:
	print 'is right number!'
while num <= 0 or num >= 101:
	print 'plaese try again'
	num = int(raw_input("input you number!:"))
print 'done'
