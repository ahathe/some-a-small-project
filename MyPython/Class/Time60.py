#!/usr/bin/env python

class Time60(object):
	def __init__(self,hr,mins):
		self.hr = hr
		self.mins = mins
	def __str__(self):
		return '%d:%d' % (self.hr,self.mins)

	__repr__ = __str__
	
	def __add__(self,other):
		return self.__class__(self.hr + other.hr,\
				self.mins + other.mins)

	def __iadd__(self,other):
		self.hr += other.hr
		self.mins += other.mins
		return self

mins =  Time60(10,30)
tue = Time60(11,15)

print mins,id(mins)
print tue,id(tue)
print mins + tue,id(mins + tue)
mins += tue
print mins,id(mins)
