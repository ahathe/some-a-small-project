#!/usr/bin/env python

class LIFO(object):
	def __init__(self):
		self.lifo = []

	def push(self):
		while True:
			Getin = raw_input('not empty to input you want to push thing:')
			if not Getin:
				break
			self.lifo.append(Getin)

	def pop(self):
		while True:
			Getout = raw_input('(pop) to out you thing:')
			if (Stack.isempty() == 1) and (Getout == 'p'):
				print self.lifo.pop(-1)
			else:
				return self.lifo.pop(-1)

	def isempty(self):
		if self.lifo:
			return 1
		else:
			return 0

	def peek(self):
		print 'the stack top is %s'
		return self.lifo[0]

Stack = LIFO()
Stack.push()
print Stack.pop()
print Stack.peek()
print '0 is empty 1 is exists:',Stack.isempty()
