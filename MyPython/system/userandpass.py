#!/usr/bin/env python

import os
import crypt
import time
import pickle
import shelve

dictfiles = shelve.open('user.txt',writeback=True)

def quit():
	print 'is quit'
		
def In(user):
	
	times = time.strftime('%Y %x %X',time.localtime())
	if dictfiles[user][1] == '':
		dictfiles[user][1] = times
		print 'time is in'

	print 
	print '%s you last time login is %s' % (user,dictfiles[user][1])
	print 'refresh times'
	dictfiles[user][1] = times
	if user == 'admin':
		print 'you is admin view all user and password %s' % dictfiles
	else:
		print 'you is normal user'

	dictfiles.close()
	print 'in'
def Create():
	def create():
		get_user = raw_input("input you user name:")
		get_pass = raw_input("input you password:")
		dictfiles[get_user] = [get_pass,'']
		print 'is created!'
		dictfiles.close()
			
	string = raw_input('(q) to quit,(C) to create:').lower()
	dictc = dict((['c',create],['q',quit]))
	if string in 'qc':
		dictc[string]()
	else:
		print 'try again not exists options!'
	


def Login():
	prmpot = '''
	do you wanna to login in?
	input you user name to login
	:'''
	get_login = raw_input(prmpot)
	get_passi = raw_input('input you password:')
	if dictfiles.has_key(get_login):
		if dictfiles[get_login][0] == get_passi:
			In(get_login)
		else:
			print 'invain password try,again!'
			Login()
	else:
		print "sory you don't have user please to create!"
		Create()

if __name__=="__main__":
	Login()
