#!/usr/bin/env python

StrProcess = raw_input(r"input you want to Process string!:")
print "input you want to scaning that string it, < '%s' >" % StrProcess
StrScan = raw_input(r"input you want to scan string!:")

CountNum = StrProcess.count(StrScan)
if CountNum != 0:
	Find = StrProcess.index(StrScan)
	rFind = StrProcess.rindex(StrScan)
	print "the < '%s' > been scan string is in process < '%s' >time" % (StrScan,CountNum)
	print "fist find the index '%s' < %s >,last find the index '%s' < %s >" % (StrScan,Find,StrScan,rFind)
else:
	print "not exsit,is < '%s' >" % StrScan
