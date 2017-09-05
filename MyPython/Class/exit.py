#!/usr/bin/env python

import sys

def useage():
	print 'at least 2 arguments (incl. cmd name).'
	print 'useage: args.py arg1 arg2 '
	print sys.exit(502)

argc = len(sys.argv)
if argc < 3:
	useage()
print 'number of args entered:',argc
print 'args (incl.cmd name) were:',sys.argv
