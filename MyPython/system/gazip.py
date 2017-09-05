#!/usr/bin/env python

import gzip
import zlib
def gtozip(make):
	if make in 'cd':
		if make == 'c':
			get_file = raw_input("input you want compress file name:")
			get_type = raw_input('input you compress file name and type gzip or bz2:')
			g = gzip.GzipFile('wb',fileobj=open(get_type,'wb'))
			g.write(open(get_file,'rb').read())
			g.close()
			print 'is done'
		elif make == 'd':
			get_file = raw_input('input decompressiong file name and type gzip or bz2:')
			get_type = raw_input('decompressiong file name type:')
			g = gzip.GzipFile('rb',fileobj=open(get_file,'rb'))
			open(get_type,'wb').write(g.read())
			print 'id done'
		else:
			print '...'
	else:
		print 'not option try again'
get_g = raw_input("(d) to decompression or (c)  to compress:")
gtozip(get_g)
