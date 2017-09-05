#!/usr/bin/env python

class MoneyFmt(object):
	def __init__(self,money,C='-'):
		self.money = money
		self.C = C

	def updata(self,other):
		self.money = other
		return self.money

	def  __str__(self):
		if isinstance(self.money,float):
			get = False
			list1 = list(str(self.money))
			listr = list1[:list1.index('.')]
			if '-' in listr:
				listr.remove('-')
				get = True
			listr.insert(1,',')
			listl = listr[listr.index(',')+1:]
			if len(list1) > 4:
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
			if get:
				if len(self.C) == 2:
					result = result[:1] + self.C[0] + '-' + result[1:] + self.C[1]
				else:
					result = result[:1] + self.C + result[1:]

			return repr(result)
		else:
			raise TypeError,\
				'must be float type ,try again'
	__repr__ = __str__
		
	def __repr__(self):
		return self.money

	def __nonzero__(self):
		if self.money:
			return True
		else:
			return False


M = MoneyFmt(-12356.52,'<>')
print M
print M.__repr__()
print M.__nonzero__()
