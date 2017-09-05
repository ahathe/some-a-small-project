#!/usr/bin/env python

import os
import requests


def opens():
	a = 10537
	b = 0
	os.chdir('/home/tianzhu/Desktop/girl/')
	while True:
		url = 'http://mtl.ttsqgs.com/images/img/%s/%s.jpg' % (a,b)
		headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0'}
		request = requests.get(url,headers=headers)
		if request.ok:
			b += 1
			filename = url.split('/')[-2] + url.split('/')[-1]
			if filename in os.listdir(os.getcwd()):
				continue
			else:
				with open(filename,'wb') as f:
					f.write(request.content)
			print a
			print b
		else:
			a += 1
			b = 0
if __name__=='__main__':
	opens()
