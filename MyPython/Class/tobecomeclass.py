#!/usr/bin/env python

def dollarize(money):
	if isinstance(money,float):
		get_ = False
		list1 = list(str(money))
		listr = list1[:list1.index('.')]
		if '-' in listr:
			listr.remove('-')
			get_ = True
		listr.insert(1,',')
		listl = listr[listr.index(',')+1:]
		if len(listl) > 4:
			count = 0
			for each in listl:
				count += 1
				if count == 3:
					if each not in listl[-2:]:
						listl.insert(listl.index(each)+1,',')
						count = 0
						
						
			result = '$' + ''.join(listr[:listr.index(',')+1] + listl + list1[list1.index('.'):])
		else:
			result = '$' + ''.join(listr[:listr.index(',')+1] + listl + list1[list1.index('.'):])
		if get_:
			result = result[:1] + '-'+ result[1:]
		return repr(result)
	else:
		raise TypeError,\
			'must be float type ,try again'
	
			

print dollarize(1234567.8901)
