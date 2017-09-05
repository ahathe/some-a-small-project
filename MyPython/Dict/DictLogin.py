#!/usr/bin/env python

import time
import crypt
import Tkinter
import string
string = string.punctuation + string.whitespace + ' '

db = {}
log = {}
				

def showuser():
	print 'All User And Passwd Is Here! '
	for x in db.items():
		print x

def deluser():
	prompt = 'Input You Want To Del That User: '
	name = raw_input(prompt).lower()
	if name in db.keys():
		del db[name]
		print '(%s) user has been dele ' % name
	else:
		print 'Not Find The User (%s) ,Try Again~ Thank You ' % name
def login():
	prompt = 'login desired: '
	while True:
		name = raw_input(prompt).lower()
		if name not in db.keys():
			prompt =  'are you new user? do you want to setup?yes or no:'	
			choce = raw_input(prompt).lower
			if choce == 'yes' or 'y':
				pwd = raw_input('passwd: ')
				encrypt = crypt.crypt(pwd,'iloveyou')
				db[name] = encrypt
				print 'the user has been setup~'
				break
			else:
				break

		if name in db.keys():
			passwd = raw_input('input you passwd: ')
			encrypt = crypt.crypt(passwd,'iloveyou')
			if encrypt == db[name]:
				log[time.strftime('%H%S',time.localtime())] = time.asctime(time.localtime(time.time()))
				print 'welcome bakc',name
				break
				while  len(log) >= 2:
					first = log.keys()[0]
					last = log.keys()[1]
					firstnum1 = log[first][11] + log[first][12]
					lastnum1 = log[last][11] + log[last][12]
					num1 = int(firstnum1)
					num2 = int(lastnum1)
					num2 = num2 + 4
					if num1 <= num2:
						print "You already logged in at: %s" % log[last]
						break
		else:
			print 'login incorrect'
			break

				
def newuser():
	prompt = 'login desired: '
	while True:
		name = raw_input(prompt).lower()
		if db.has_key(name):
			prompt = 'name taken,try another: '
			continue

		else:
			break

	pwd = raw_input('passwd: ')
	encrypt = crypt.crypt(pwd,'iloveyou')
	db[name] = encrypt
	for x in name:
		if x in string:
			del db[name]
			print 'The Create User Name Is Illegality,has been deled, please Try Again~ \
   Must Be Alphanumeric ,Thank You'
			break
	
def olduser():
	print 'plaese input you user name and passwd! '
	name = raw_input('login: ').lower()
	pwd = raw_input('passwd: ')
	encrypt = crypt.crypt(pwd,'iloveyou')
	passwd = db.get(name)
	if passwd == encrypt:
		log[time.strftime('%H%S',time.localtime())] = time.asctime(time.localtime(time.time()))
		print 'welcome back',name
		if len(log) >= 2:
			first = log.keys()[0]
			last = log.keys()[1]
			firstnum1 = log[first][11] + log[first][12]
			lastnum1 = log[last][11] + log[last][12]
			num1 = int(firstnum1)
			num2 = int(lastnum1)
			num2 = num2 + 4
			if num1 <= num2:
				print "You already logged in at: %s" % log[last]
	else:
		print 'login incorrect'

def showmenu():
	prompt = """
(N)ew User Login
(E)xisting User Login
(Q)uit
(S)how User and Passwd
(D)el Exists User
(L)ogin User
Enter choice: """

	done = False
	while not done:
		chosen = False
		while not chosen:
			try:
				choice = raw_input(prompt).strip()[0].lower()
			except (EOFError,KeyboardInterrupt):
				choice = 'q'
			print '\nYou picked: [%s]' % choice
			if choice not in 'neqsdl':
				print 'invalid option,try again'
			else:
				chosen = True

		if choice == 'q':done = True
		if choice == 'n':newuser()
		if choice == 'e':olduser()
		if choice == 's':showuser()
		if choice == 'd':deluser()
		if choice == 'l':login()

if __name__=="__main__":
	showmenu()
