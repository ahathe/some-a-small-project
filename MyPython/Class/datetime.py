#!/usr/bin/env python

import time 

class Timecode(object):
	times = time.strftime('%Y %m %d %H:%M:%S %A',time.localtime())

	def __init__(self,formats=times):
		self.formats = formats

	def update(self,take=False):
		if take != False:
			if '/' in take:
				list1 = list(take)
				for each in list1:
					if list1.count(each) >= 2:
						list1.remove(each)
					else:
						continue
				list1.remove('/')
				self.take = ''.join(list1)
		else:
			self.take = self.formats



	def display(self):
		if self.take != self.formats:
			Y = 'y'
			if self.take.count(self.take[-1]) >= 2:
				Y = 'Y'
			self.take = time.strftime('%%%s/%%%s/%%%s' % (self.take[0].lower(),self.take[1].lower(),Y),time.localtime())

		return self.take


get = raw_input('input you time formats:')
Timeshow = Timecode()
Timeshow.update(get)
print Timeshow.display()
