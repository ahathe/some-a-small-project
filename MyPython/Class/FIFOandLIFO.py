#!/usr/bin/env python

class Both(object):
	def __init__(self):
		self.list1 = []

	def unshift(self,unshif):
		return self.list1.insert(0,unshif)

	def push(self,pushs):
		return self.list1.append(pushs)

	def shift(self):
		return self.list1.pop(0)

	def pop(self):
		return self.list1.pop(-1)

both = Both()

