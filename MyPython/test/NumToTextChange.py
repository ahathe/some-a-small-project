#!/usr/bin/env python

Text_One = ['zero','one','two','three','four','five','six','seven','eight','nine','ten']

Text_Two = ['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']

Text_Three = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

Text_Four = ['zero','one','twenty-','thirty-','forty-','fifty-','sixty-','seventy-','eighty-','ninety-']

Text_Five = [' hundred ',' thousand','and ']

The_Dict = {'10':'ten','20':'twenty','30':'thirty','40':'forty','50':'fifty','60':'sixty','70':'seventy','80':'eighty','90':'ninety'}

Text_One_And_Two = Text_One + Text_Two

Text_Five_And_Text_Three = Text_Five + Text_Three

Num_list = ['1','2','3','4','5','6','7','8','9']


def Change_Four(Num4):
	Str3 = str(Num4)
	Index1 = int(Str3[0])
	if len(Str3) == 4:
		if Str3[1] and Str3[2] and Str3[3] == '0' and Str3[0] == '1':
			Result = Text_One[Index1] + Text_Five[1]
			print 'the Result :~$ %s' % Result
		else:
			print "i'm sory ,The Number is big than 1000,not gonna have some result for you!,retry again,thank you!"
	


def Change_Three(Num3):
	Str2 = str(Num3)
	if len(Str2) == 3:
		if Str2[0] in Num_list:
			Index1 = int(Str2[0])
			Index2 = int(Str2[1])
			Index3 = int(Str2[2])
			Hundred = Text_One[Index1] + Text_Five[0] + Text_Five[2]
			if Text_Four[Index2] == 'zero' and Text_One[Index3] == 'zero':
				Result = Text_One[Index1] + Text_Five[0]
				print 'is the Result :~$ %s' % Result
			else:
				if Text_Four[Index2] == 'zero' and Text_One[Index3] != 'zero':
					Result = Text_One[Index1] + Text_Five[0] + Text_Five[2] + Text_One[Index3]
					print 'the Result is:~$ %s' % Result
				else:
					if Text_Four[Index2] != 'zero' and Text_One[Index3] == 'zero':
						Index4 = str(Index2) + str(Index3)
						Result = Text_One[Index1] + Text_Five[0] + Text_Five[2] + The_Dict[Index4]
						print 'the Result is:~$ %s' % Result
					else:
						if Index2 == 1 and Text_One[Index3] != 'zero':
							Index4 = str(Index2) + str(Index3)
							Index5 = int(Index4)
							Result = Text_One[Index1] + Text_Five[0] + Text_Five[2] + Text_One_And_Two[Index5]
							print 'the Result is:~$ %s' % Result
						else:
							if Index2 != 1 and Index3 != 'zero':
								Result = Text_One[Index1] + Text_Five[0] + Text_Five[2] + Text_Four[Index2] + Text_One[Index3]
								print 'the Result is:~$ %s' % Result

	else:
		Change_Four(Num3)
							

def Change_Two(Num2):
	Str1 = str(Num2)
	if len(Str1) == 2:
		if Str1[0] in Num_list:
			Index1 = int(Str1[0])
			Index2 = int(Str1[1])
			Result = Text_Four[Index1] + Text_One[Index2]
			if 'zero' in Result:
				Result = Text_Five_And_Text_Three[Index1+1]
				print 'the Result is %s' % Result
			else:
				print 'the Result is %s' % Result
	else:
		Change_Three(Num2)


def Change_One(Num1):
	try:
		if Text_One_And_Two[Num1]:
			print 'is %s' % Text_One_And_Two[Num1]
	except IndexError:
		Change_Two(Num1)

	
def Input(Number):
	length = len(Number)
	if length > 4:
		print 'the number must between 0 ~ 1000,that is gonna work.'
	else:
		if Number[0] == '0':
			print "i'm sory ,The first cannot be zero! retry again ,thank you!"
		else:
			try:
				Number = int(Number)
			except ValueError:
				print "i't must be int type,plaese retry again,thank you!"
			else:
				Change_One(Number)


You_num = raw_input("input you want to change that number,i's must be number!:")

if __name__=='__main__':
	Input(You_num)
