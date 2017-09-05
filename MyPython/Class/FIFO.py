#!/usr/bin/env python

class Queue(object):
	def __init__(self):
		self.list1 = []

	def enqueue(self):
		while True:
			getIn = raw_input('input you enqueue!:')
			if getIn == '':
				break
			self.list1.append(getIn)

	def dequeue(self):
		while True:
			getOut = raw_input('out you dequeue!:')
			print self.list1.pop(0)
			if not self.list1:
				break

queue = Queue()
queue.enqueue()
queue.dequeue()
