#!/usr/bin/env python


def RUNING(String):
	if String[0] == ' ':  		# tset that first index if was white space!
		while True:
			Space = String.index(' ')   #copy that index ,then assignment new string!
			String = String[1:]
			if String[0] != ' ':  		#if that is not equal with the space,then make that loop to other judge
				RUNING(String)   
				break

	elif String[-1] == ' ':  	#test last index if is that white space
		while True:
			Space = String.rindex(' ')  	#some as before ,make a new string!
			String = String[:Space]
			if String[-1] != ' ':  			#make other loop judge ,if exist that tap key!
				RUNING(String)
				break

	elif String[0] == '	':  		#test first index if is that tap key
		while True:
			Space = String.index('	') 	#make a loop ,going to test and reassignment
			String = String[1:]
			if String[0] != '	': 		#make judge going to loop
				RUNING(String)
				break

	elif String[-1] == '	':  	#test last one if is that tap key,
		while True:
			Space = String.rindex('	')  	#make that some
			String = String[:Space]
			if String[-1] != '	':  		#going loop judge
				RUNING(String)
				break



									#is gonna happen no tap key and white space in that new string to print


	else:
		while True:
			print "the string is been process it STRIP()!,that is good! >->->$ %s "  %  String
			break

Take = raw_input('input you normal string!,not for null value! thank you!:')   
						# make input it and going loop procedure
if __name__=='__main__':
	if Take is not '':
		RUNING(Take)
