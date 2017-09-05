#!/usr/bin/env python


import shelve
import time
class User(object):
	def __init__(self):
		self.user = raw_input('input you user name:')
		self.passwd = raw_input('input you passwd :')

	def login(self):
		f = shelve.open('login',writeback=True)
		times = time.strftime('%Y %X %x',time.localtime())
		if f.has_key(self.user) and self.passwd in f[self.user]:
			if len(f[self.user]) == 1:
				f[self.user].insert(1,times)
			else:
				print 'you last time login %s' % f[self.user].pop(1)
				f[self.user].insert(1,times)
		else:
			prompt= '''not such user or passwd error
				(C) to create
				(Q) to quit
				:'''
			GetCuser = raw_input(prompt).lower()
			self.GetCuser = GetCuser

			if self.GetCuser == 'c':
				self.user = raw_input('input you want to created user name:')
				self.passwd = raw_input('input you created passwd         :')
				if not f.has_key(self.user):
					f[self.user] = [self.passwd]
					print 'is created'
				else:
					print 'the user name is exists try again'
		self.trues = f.has_key(self.user) and self.passwd in f[self.user] 
		f.close()
				

class Cart(object):
	def __init__(self):
		self.listindex = []

	def cart(self,carts=1):
		self.carts = carts
		try:
			self.carts = int(self.carts)
		except (ValueError,TypeError),e:
			print e
			print 'use default cart'
			self.listindex = [[]]
		else:
			while self.carts:
				self.carts -= 1
				self.listindex.append([])
			print 'the cart is done'
			
		

class Item(User,Cart):
	def __init__(self):
		super(Item,self).__init__()
		super(Item,self).login()
		Cart.__init__(self)
		
	def show(self):
		if self.trues:
			f = shelve.open('show')
			print 'the is all item---------'
			for each in f:
				print each,f[each]
			print '-'*23
			f.close()
			item.select()
	def select(self):
		pormpt = '''do you want buy it?
				(Y) to select
				(q) to quit
				:'''
		Gets = raw_input(pormpt).lower()
		if Gets == 'y':
			print 'how mony cart you need?'
			GetCart = raw_input(':')
			if GetCart == '' or GetCart == '0' or GetCart == '1':
				super(Item,self).cart()
			else:
				super(Item,self).cart(GetCart)
			f = shelve.open('show')
			while True:
				Getitem = raw_input('input the index select which you want to buy:').lower()
				if f.has_key(Getitem):
					try:
						self.listindex[self.carts].append(f[Getitem][0])
					except IndexError:
						break
				elif Getitem == 'c':
					if not [] in self.listindex:
						break
					print self.listindex
					self.carts -= 1
					continue
				else:
					break
			f.close()
			for each in self.listindex:
				print each
			print
			print 'the is you all item'
			item.play()
	def play(self):
		self.sumlist = []
		f = shelve.open('show')
		for each in self.listindex:
			for find in each:
				for x in f.values():
					if find in x:
						self.sumlist.append(x[1])
		f.close()
		self.sumlist = sum(self.sumlist)
		print 'the total commodity need %s money!' % self.sumlist
		Getpay = raw_input('(y) to paly and packed ?:').lower()
		if Getpay == 'y':
			f = shelve.open('login',writeback=True)
			if len(f[self.user]) >= 3 and f[self.user][2] > self.sumlist:
				f[self.user][2] -= self.sumlist
				w = shelve.open(self.user)
				w[self.user] = self.listindex
				w.close()
				print 'is play and packed'
			else:
				print 'you do not have money want to recharge?'
				s = 'input you integer money:'
				try:
					money = int(raw_input(s))
				except TypeError,e:
					print e
				else:
					f[self.user].append(money)
			f.close()


item = Item()
item.show()

