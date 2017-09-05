#!/usr/bin/env python

import shelve
import os
import time

class UserClass(object):
	def __init__(self):
		user = raw_input('input you user name!:')
		passwd = raw_input('input you passwd!:')
		self.user = user
		self.passwd = passwd

	def Check(self):
		f = shelve.open('login.txt')
		if f.has_key(self.user) and (self.passwd in f[self.user]):
			login.Login()
			f.close()
			self.choice = ''
		else:
			print 'not such user or passwd error'
			prompt = '''
			do you want to create user?
			(y) to create
			any key to quit
			:'''
			f.close()
			try:
				choice = raw_input(prompt).lower()
				self.choice = choice
				login.Create()
			except BaseException:
				print 'breaked'
		
			
	def Create(self):
		if self.choice == 'y':
			try:
				user = raw_input('input you want to create user name:')
				passwd = raw_input('input you passwd:')
			except BaseException:
				print 'breaked'
			else:
				if user and passwd:
					f = shelve.open('login.txt')
					f[user] = [passwd]
					f.close()
					print 'is done'
				else:
					print 'illegality empty user or passwd try again!'
		
		
	def Login(self):
		print 'you has login!'
		f = shelve.open('login.txt')
		list1 = f[self.user]
		t = time.strftime('%Y %X %x',time.localtime())
		if len(list1) < 2:
			list1.insert(1,t)
			print 'the is you first login in'
		else:
			print 'you last time login is',list1.pop(1)
			list1.insert(1,t)
		f[self.user] = list1
		f.close()
		count = 1
		while count:
			prompt = '''
			(A) to add options and infomation
			(U) to update infomation
			any key to quit and view!
			:'''
			info = raw_input(prompt).lower()
			if info == ('a' or 'u'):
				userinfo = shelve.open(self.user)
				print 'here is you options',userinfo.keys()
				print 'here is you values ',userinfo.values()
				while True:
					print 'both choice of one is empty or both == q,is going to break'
					getadd = raw_input('input you option add or update        :')
					getinfo = raw_input('input you infomation to add or update:')
					if (not getadd and not getinfo) or (getadd and getinfo == 'q') or (getadd and not getinfo) or (not getadd and getinfo):
						break
					userinfo[getadd] = getinfo
				userinfo.close()
				print 'done'
			else:
				userinfo = shelve.open(self.user)
				for each in userinfo:
					print '%s: %s' % (each,userinfo[each])
				print
				print 'the is you view'
				userinfo.close()
			count -= 1
			rechoice = raw_input('do you want to rechoice?:')
			if rechoice == 'y':
				count = 1
			else:
				count = False
		return count
	def __del__(self):
		print 'is saved and update!'

login = UserClass()



