#!/usr/bin/env python

def tomin(mins):
	t = mins / 60
	i = mins % 60
	return '%d hour and %d min' % (t,i)
def tohour(hour,mins):
	return '%d %s' % ((hour * 60) + mins,'mins')
gethour = int(raw_input('input you hour:'))
getmin = int(raw_input('input you min:'))
print tohour(gethour,getmin)
print tomin(getmin)
