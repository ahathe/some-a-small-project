#!/usr/bin/env python

' info for zip file'
import stat
import zipfile,os
import time

list1 = []
def lszip(files):
	true = os.path.isfile(files)
	trues = os.path.splitext(files)[-1]
	if true and trues == '.zip':
		zipFile = zipfile.ZipFile(files,'r')
		for each in zipFile.namelist():
			print each
			print 'before size',zipFile.getinfo(each).file_size,'after size',zipFile.getinfo(each).compress_size,'create time',zipFile.getinfo(each).date_time
			list1.append(zipFile.getinfo(each).file_size)
		count = sum(list1)
		print 'total zip file size is %s' % count
		print 'is done'



get = raw_input('input you zip file name to show info:')
lszip(get)
