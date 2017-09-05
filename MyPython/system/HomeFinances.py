#!/usr/bin/env python

import os


def Usermanage(user):
	def deposits():
		GET_dep = raw_input("how much you want to deposits the money!:")
		files = os.listdir(os.getcwd())
		if user not in files:
			f = open(user,'w')
			f.write(GET_dep)
			f.close()
			print 'you money deposits is done %s' % GET_dep
			Usermanage(user)
		else:
			f = open(user,'r+')
			money = f.read()
			f.close()
			account = float(GET_dep) + float(money)
			account = str(account)
			f = open(user,'w')
			f.write(account)
			f.close()
			print 'you money deposits is done'
			print 'you account money total is %s' % account
			Usermanage(user)			
	def withdrawals():
		files = os.listdir(os.getcwd())
		if user in files:
			f = open(user,'r+')
			m = f.read()
			print 'you account money is exist ,total money is %s' % m
			f.close()
			GET_drawal = raw_input("input you number to withdrawals the money!:")
			if float(GET_drawal) > float(m):
				print "i'm sory you don't have enough money,please try again ,now you total money is %s"  %  m
				withdrawals()
			account = float(m) - float(GET_drawal)
			account = str(account)
			f = open(user,'w')
			f.write(account)
			f.close()
			print "you drawals money is %s money,now you total money is %s" % (GET_drawal,account)
			Usermanage(user)
		else:
			print "i'm sory you account is available ,but you don't have any money in that bank!"
			print "please to (D)eposits money first!"
			Usermanage(user)

	def debits():
		GET_user = raw_input("input you debits that user name:")
		files = os.listdir(os.getcwd())
		if GET_user in files:
			print 'yet the user is our bank account'
			GET_money = raw_input("how mony money you wanna from the user?:")
			f = open(GET_user,'r+')
			money = f.read()
			f.close()
			GET_debit = raw_input("input you the bank account,to turn the money for you:")
			if GET_debit in files:
				if float(GET_money) > float(money):
					print "i'm sory the user don't have enough money for you request try again,the user money total is %s" % money
					Usermanage(user)
				else:
					f = open(GET_debit,'r+')
					demoney = f.read()
					f.close()
					denowmoney = float(demoney) + float(GET_money)
					denowmoney = str(denowmoney)
					f = open(GET_debit,'w')
					f.write(demoney)
					f.close()
					f = open(GET_user,'w')
					our_bank_user = float(GET_money) - float(money)
					if our_bank_user >  0:
						our_bank_user = str(our_bank_user)
						f.write(our_bank_user)
						f.close()
					else:
						our_bank_user = str(-our_bank_user)
						f.write(our_bank_user)
						f.close()

					print "the request %s money has been turn you account" % GET_money
					print "you before total money %s" % demoney
					print "now you account and money %s %s" % (GET_debit,denowmoney)
					print "is done"
					Managesavings()
			else:
				print "you don't have our bank account,please to create!"
				Managesavings()
		else:
			print "i'm sory the account not our bank user,cannot operational things sory , try again"
			Usermanage(user)
				
	def credits():
		pass
	def quit():
		print 'is quit in public manage interface!'
		Managesavings()

	f = open(user,'r+')
	show = f.read()
	f.close()

	prompt = """
	welcome to
	enjoy it
	now you account total money is %s

	(D) to deposits
	(W) to withdrawals
	(Dr) to debits
	(Cr) to credits
	(Q) to quit
	:""" % show
	GET_choice = raw_input(prompt).lower()
	dict1 = dict((['d',deposits],['w',withdrawals],['dr',debits],['cr',credits],['q',quit]))
	if GET_choice in 'dwdrcrq':
		dict1[GET_choice]()
	else:
		print "option is not exists,try again"
		Usermanage(user)
	

def Managesavings():
	def login():
		def tocreate():
			files = os.listdir(os.getcwd())
			if 'userlogin.txt' not in files:
				f = open("userlogin.txt",'w')
				f.close()
			GET_user = raw_input("input you user name to create:")
			GET_pass = raw_input("input you password to create:")
			print '----------------------------'
			print 'The is you create username [%s] and passwrod %s' % (GET_user,GET_user)
			liststr = "%s" % [GET_user,GET_pass]
			lists = liststr
			f = open("userlogin.txt",'r+')
			for each in f:
				if each.strip() == liststr:
					f.close()
					print 'the user name is exist try again~'
					login()
					break
			else:
				f.write('%s%s' % ([GET_user,GET_pass],os.linesep))
				f.close()
				print 'is done'
				login()
		def touser():
			GET_user = raw_input("input you user name to login:")
			GET_pass = raw_input("input you password to login:")
			f = open('userlogin.txt','r')
			liststr = "%s" % [GET_user,GET_pass]
			for each in f:
				if liststr == each.strip():
					Usermanage(GET_user)
					f.close()
					break
			else:
				f.close()
				print "you don't have account,please to create,try again!"
				login()
		prompt = """
	do you have account?
	(Y)es to login
	(N)o to create
	(Q)uit to exit the progrm
	:"""
		dict1 = dict((['y',touser],['n',tocreate],['q',optionquit]))
		GET_Choice = raw_input(prompt).lower()
		if GET_Choice in 'ynq':
			dict1[GET_Choice]()
		else:
			print "option is not exists,try again"
			login()
			
			
	def checking():
		pass
	def market():
		pass
	def deposit():
		pass
	def optionquit():
		Managesavings()
	def quit():
		print 'is quit'
	dict1 = dict((['l',login],['c',checking],['m',market],['d',deposit],['q',quit]))
	prompt = """
	You choice
	(L)ogin to manage savings
	(C)hecking to change money
	(M)arket to money market
	(D) to certificate of deposit
	(Q)uit to exit the progrm
	:"""
	GET_Choice = raw_input(prompt).lower()
	if GET_Choice in 'lcmdq':
		dict1[GET_Choice]()
	else:
		print "The option is not exists,try again"
		Managesavings()
	
if __name__=="__main__":
	Managesavings()
