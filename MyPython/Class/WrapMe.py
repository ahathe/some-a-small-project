#!/usr/bin/env python

class WrapMe(object):
	def __init__(self,obj):
		self.__data = obj
	def get(self):
		return self.__data
	def __repr__(self):
		return 'self.__data'
	def __str__(self):
		return str(self.__data)
	def __getattr__(self,attr):
		return getattr(self.__data,attr)

wrappedList = WrapMe([123,'foo',45.67])
f = WrapMe(open('1.txt'))
print f
print f.get()
print f.readlines()
print f.close()
