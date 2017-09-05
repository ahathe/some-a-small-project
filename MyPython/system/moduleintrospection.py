#!/usr/bin/env python

import sys
import os

linecommand = sys.argv
del linecommand[0]

module = [module for module in linecommand if type(eval(module)) == type(sys)]

modulelist = dir(eval(module[0]))
for index in range(len(modulelist)):
	types = type(eval(module[0]+'.'+modulelist[index]))
	values = eval((module[0]+'.'+modulelist[index]))
	print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
	print 'module name -->',module,'module attribute-->',modulelist[index],'types-->',types,'values-->',values
