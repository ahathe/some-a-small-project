#!/usr/bin/env python

import os

def parsing(files):
	truef = os.path.isfile(files)
	if truef:
		parsing = os.stat(files)
		print '---access mode --> %s' % parsing.st_mode
		print '---node number --> %s' % parsing.st_ino
		print '---lingering equipment --> %s' % parsing.st_dev
		print '---node link number --> %s' % parsing.st_nlink
		print '---owner user ID --> %s' % parsing.st_uid
		print '---group user ID --> %s' % parsing.st_gid
		print '---file size --> %s' % parsing.st_size
		print '---last time view the file --> %s' % parsing.st_atime
		print '---last time modification time --> %s' % parsing.st_mtime
		print '---create file time --> %s' % parsing.st_ctime
		

GET_parsingfiles = raw_input('input you want to parsing files ,or full file path name~:')

parsing(GET_parsingfiles)
