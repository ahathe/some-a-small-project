#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import requests

def find_ops(a):
	count = 1
	list1 = []
	headers = {}
	while True:
		url = 'https://3344jk.com/xiazaiqu/btyazhou/index_%s.html' % a
		headers['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0'
		req = requests.get(url,headers=headers)
		if count:
			req.encoding = 'utf-8'
			count -= 1
		m = re.search('一之',req.text)
		if m is not None:
			print (m.group())
			print (url)
			list1.append(a)
		a += 1
		print (a)
		print list1

if __name__=='__main__':
	Get = int(input('input you number:'))
	find_ops(Get)
		
