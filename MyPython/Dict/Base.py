#!/usr/bin/env python

list1 = []
list2 = []
list3 = []
list4 = []
def bas(num):
	for x in range(1,num+1):
		num1 = num % x
		if num1 == 0:
			list1.append(x)

	if len(list1) <= 2:
		print '%s not factors' % list1
	elif len(list1) > 2:
		listnum2 = list1[1]
		del list1[0]
		del list1[-1]
		for x in list1:
			num3 = listnum2 ** x
			list3.append(num3)
			if num in list3:
				list2.append(listnum2)
				list2.append(x)
				print 'is factors %s' % list2
				break
			elif num not in list3:
				for s in list3:
					for j in range(len(list1)):
						result = s * list1[j]
						if result == num:
							list2.append(listnum2)
							list2.append(x)
							list2.append(list1[j])
							print 'is factors %s' % list2
							break
					else:
						break
				else:
					break
		else:
			num123 = 1
			while num123 != num:
				for l in list1:
					list4.append(l)
					num123 *= l
					if num123 == num:
						print 'is factors %s' % list4
						break
	else:
		print 'let me counting...'
			




get1 = int(raw_input("input you nunber:"))
bas(get1)
