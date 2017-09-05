#!/usr/bin/env python

# make a number_string
num_str = raw_input('Enter a number: ')

# change number_string to int type number
num_num = int(num_str)

# make range function for inside each number beforer input it + 1 to assignment for beforer complete total input then print
fac_list = range(1,num_num + 1)
print "BEFORE:",'%s' % fac_list


# zero for assignment to i
i = 0


# if i not big than fac_list,then to loop
while i < len(fac_list):  #the fac_list slef add not change then print result
	
	# if beforer that input it is remainder gonna be del it
	for i in range(len(fac_list)+1):

	# for every time i going to add 1
		i = i + 1

# print the result
print "AFTER:",'%s' % fac_list
