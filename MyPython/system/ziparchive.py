#!/usr/bin/env python
import zipfile,os
def zip(option):
	if option in 'cae':
		if option == 'c':
			zipname = raw_input('input you want to create zip name!:')
			filepath = raw_input('input you wanna archive file path or name:')
			filename =raw_input('filename in to saved:')
			zipFile = zipfile.ZipFile(zipname,'w')
			zipFile.write(filepath,filename,zipfile.ZIP_STORED)
			zipFile.close()
			print 'is done'
		elif option == 'a':
			zipname = raw_input('input you zip name to add:')
			zipadd = raw_input('you wannt add file name:')
			zipFile = zipfile.ZipFile(zipname,'a')
			zipFile.write(zipadd)
			zipFile.close()
			print 'is done'
		elif option == 'e':
			zipname = raw_input("input you zip name to extract:")
			zipFile = zipfile.ZipFile(zipname,'r')
			for each in zipFile.namelist():
				zipFile.extract(each,'ok')
			zipFile.close()
			print 'is done'
		else:
			print 'no such options ,try again'
	else:
		print 'not such options,try again!'

options = raw_input("(c) to create zip,((a)to add file in zip,(e) to extract zip:")
zip(options)
