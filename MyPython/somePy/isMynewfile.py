import os

print 'please input one filename,create or reading,thank you.'
while True:
	try:
		string = int(raw_input("please input number 1 or 2 to choose reading file or create!:"))
	except ValueError,a:
		print 'please try again,is not int() type,im so sory!'
	else:
		while string == 1:
			read = raw_input("plases input you wnnt to read file name!:")
			try:
				fobj = open(read,'r')
			except IOError,e:
				print 'does not exsits',e
			else:
				for eachLine in fobj:
					print eachLine.strip()
				fobj.close()
				break

	if string == 2:
		write = raw_input("write you want to in that file:")		
		fobj = open(write,'w')
		otherstring = raw_input("input you want to write about it!,thank you,but you gonna understand ,the is going to coverrage thes file,before you write that!:")
		fobj.write(otherstring)
		fobj.close()
		print 'DONE!'
	if string == 3:
		rewrite = raw_input("choose file to rewrite it,thank you!:")
		fobj = open(rewrite,'a')
		fobj.tell()
		fobj.close()
	break
