#!/usr/bin/env python


import os

	
def search():
	choice = '''
	input you wannt to search wab site names or url:'''
	GET_choice = raw_input(choice)
	f = open('url','r+')
	each = [each for each in f]
	f.close()
	joineach = ''.join(each)
	if 'www' or 'com' in GET_choice:
		GET_choice = ''.join(GET_choice.split('www'))
		if 'www' or 'com' in GET_choice:
			GET_choice = ''.join(GET_choice.split('com'))
	
	find_choice = joineach.partition(GET_choice)
	count = 0
	for find in find_choice:
		if GET_choice == find:
			print 'yes the web site url or names is exists!'
			f = open('url','r+')
			for find_target in f:
				count += 1
				if GET_choice in find_target:
					print 'you search web  %s is in url file %d lines' % (GET_choice,count)
					print 
					break
			Url()
			break
			
	else:
		print 'not such web site names or url in the web site book,sory'
		print 'retry again!'
		Url()
	
def change():
	def a():
		GET_add = raw_input("input you wanna add web site names and url:")
		f = open('url','a+')
		f.write('%s%s' % (GET_add,os.linesep))
		f.close()
		print 'those is you names and url,all is here'
		print 
		f = open('url','r+')
		for each in f:
			print each,
		f.close()
		print 
		print 'is done'
		change()
	def u():
		print 'input you wanna update web site names,thank you!'
		GET_names = raw_input("which web site you wanna to change?:")
		print 
		f = open('url','r+')
		each = [each for each in f]
		f.close()
		length = range(len(each))
		for index in length:
			if GET_names in each[index]:
				print 'yes the web is exists'
				print each[index]
				target = each[index]
				break
		else:
			print 'not find in web site book,try again'
			change()
		become = '''input you want update the
web site : %snames and url to repace:''' % target
		GET_second = raw_input(become)
		lisindex = each.index(target)
		each.pop(lisindex)
		each.insert(lisindex,'%s%s'%(GET_second,os.linesep))
		f = open('url','w')
		f.writelines(each)
		f.close()
		print 'is done'
		print 'web site book lists!'
		print 
		f = open('url','r+')
		for each in f:
			print each,
		f.close()
		change()
	def d():
		print 'please input web site names to deled!'
		GET_del = raw_input("which entries you wanna to del?:")
		f = open('url','r+')
		each = [each for each in f]
		f.close()
		length = range(len(each))
		for find in length:
			if GET_del in each[find]:
				del each[find]
				break
		else:
			print 'not such web site names,try again'
		f = open('url','w')
		f.writelines(each)
		f.close()
		print 'is done'
		change()
	prompt = """
	(A) to add url and names
	(U) to update that
	(D) to del them
	(Q) to quit
	:"""
	GET_choice = raw_input(prompt).lower()
	dict1 = dict((['a',a],['u',u],['d',d],['q',optionsquit]))
	if GET_choice in "audq":
		dict1[GET_choice]()
def quit():
	list1 = []
	f = open('url','r+')
	read = [read for read in f]
	f.close()
	path = os.listdir(os.getcwd())
	if 'url.html' not in path:
		f = open('url.html','w')
		f.close()
	f = open('url.html','r+')
	for each in range(len(read)):
		string= ''.join(read[each].split())
		string = '<h4>'+string+'</h4>\n'
		list1.append(string)
	f.writelines(list1)
	f.close()
	print 'is quit'
def optionsquit():
	Url()
def files():
	list2 = []
	get_files = raw_input("input you want to create files names!:")
	paths = os.listdir(os.getcwd())
	if get_files not in paths:
		f = open(get_files,'w')
		f.close()
		print 'files is create!'

	getfiles = raw_input("which file you want to remove web link,input names:")
	if getfiles not in paths:
		print 'sory retry again,file is not exists'
		Url()
	f = open(getfiles,'r+')
	print 
	print 'select you links ,thank you'
	print 
	for each in f:
		print each,
	f.close()
	get_links = raw_input("input all you need web site links names,use { , } to separate part!:")	
	get_results = ''.join(get_links.split(','))
	f = open(getfiles,'r+')
	files_part = [x for x in f]
	f.close()
	for each in files_part:
		if get_results in each:
			list2.append(each)
			files_part.remove(each)
			break
	else:
		print 'not each links,try again'
		Url()
		
	f = open(getfiles,'w')
	f.writelines(files_part)
	f.close()
	f = open(get_files,'r+')
	f.writelines(list2)
	f.close()
	print 'is done'
	Url()
def Url():
	prompt = '''

options
(C) to add or update or del those
(S) to matching url or name as the
possible
(F) to create file
(Q) to quit the program
:'''
	print 'those is you url or names'
	print
	f = open('url','r+')
	for each in f:
		print each,
	f.close()
	GET_options = raw_input(prompt).lower()
	dict1 = dict((['s',search],['c',change],['q',quit],['f',files]))
	if GET_options in 'sqcf':
		dict1[GET_options]()
	else:
		print 'not such options,please try again'
		print 
		Url()

if __name__=="__main__":
	Url()
