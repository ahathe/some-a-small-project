#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import requests
import re
import os 

headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0'}

dict1 = {'女神':'nvshen','极品':'jipin','嫩模':'nenmo','网络红人':'wangluohongren', \
	'风俗娘':'fengsuniang','气质':'qizhi','尤物':'youwu','爆乳':'baoru','性感':'xinggan', \
	'诱惑':'youhuo','美胸':'meixiong','少妇':'shaofu','长腿':'changtui','萌妹子':'mengmeizi', \
	'萝莉':'loli','可爱':'keai','户外':'huwai','比基尼':'bijini','清纯':'qingchun','唯美':'weimei', \
	'清新':'qingxin'}	

def find_Page(key_choice,default):
	if key_choice in dict1.values():
		url = 'https://www.meitulu.com/t/%s/' % key_choice
		if default != 1:
			url = url + '%d.html' % default
		return url
	else:
		url = 'https://www.meitulu.com/search/%s' % key_choice
		count = 2
		while count:
			request = requests.get(url,headers=headers)
			request.encoding = 'utf-8'
			if count == 2:
				find_re = re.search(r'https://.+item.+\.html',request.text)
				url = find_re.group()
				count -= 1
				continue
			else:
				find_re = re.search(r'https://.+/t/.+?/',re.search(r'模特姓名.+</p>?',request.text).group())
				if find_re is not None:
					return find_re.group()
				else:
					print ('not such Name,Begin from the search!')
					return url.split('item')[0] + 'search/' + key_choice
				break
					


def Input_Num(num):
	try:
		Get = int(input('input you page num to begin \
default is <1> begin :'))
	except ValueError:
		Get = 1
		return Get
	else:
		return Get
	

def Input_Page(Path):
	for i,each in enumerate(Path):
		print (i+1,each)

	prompt = '''which you want to donwload
		input yhe names
		:'''
	key = input(prompt)
	return Path[key]

	'''if key in dict1.keys():
		try:
			Get = int(input('input you begin page,default is 1:'))
		except ValueError as e:
			print (e,'必须为整数')
		else:
			return dict1[key],Get
	else:
		print ('do not have the key,try again')'''
	
def opens(url):
	a = 2
	req = requests.get(url,headers=headers)
	m = re.compile(r'https://.+/item.+\.html')
	find_re = re.findall(m,req.text)
	sets = set(find_re)
	length = len(sets)
	if req.ok and length >= 60:
		while True:
			req = requests.get(url + '%d.html' % a,headers=headers)
			m = re.compile(r'https://.+/item.+\.html')
			find_re = re.findall(m,req.text)
			for each in iter(find_re):
				sets.add(each)
				print (each)
			a += 1
			if not req.ok:
				print ('break',len(sets))
				break
		return sets
	else:
		return sets
			
def save_img(html):
	D = 1
	length = len(html)
	rejpg = re.compile('http://.+?/img/.+?/[1-9][0-9]?\.?jpg')
	list1 = []
	for each in iter(html):
		print (each)
		request = requests.get(each,headers=headers)
		if D:
			request.encoding = 'utf-8'
			D -= 1
		find_img = re.findall(rejpg,request.text)
		for each1 in iter(find_img):
			list1.append(each1)
			print (each1)
		b = 2
		while True:
			request1 = requests.get(each.split('.html')[0] + '_%d.html' % b,headers=headers)
			find_img1 = re.findall(rejpg,request1.text)
			b += 1
			for each2 in iter(find_img1):
				list1.append(each2)
				print (each2)
			if not request1.ok:
				b = 2
				break
	return list1
			
def img(imgs):
	os.chdir('/home/tianzhu/Desktop/girl')
	c = 1
	for each in iter(imgs):
		print (each)
		request = requests.get(each,headers=headers)
		if c:
			request.encoding = 'utf-8'
			c -= 1
		filename = each.split('/')[-2] + each.split('/')[-1]
		with open(filename,'wb') as f:
			f.write(request.content)
def Choice(url):
	a = 1
	prompt = '''
	(T) to download type page
	(S) to download name page
	(K) to download kyeword page
	:'''
	prompt = input(prompt)

	if prompt == 'T':
		html = find_Page(Input_Page(dict1),Input_Num(a))
	elif prompt == 'S':
		keyword = input('input you keyword Name:')
		html = find_Page(keyword,a)
	elif prompt == 'K':
		keyword = input('input you keyword:')
		html = url + 'search/' + keyword
	else:
		print ('not such choice ,try again!')
	if prompt in 'TSK':img(save_img(opens(html)))
	
if __name__=='__main__':
	Choice('https://www.meitulu.com/')
