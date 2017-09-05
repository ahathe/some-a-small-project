#!/usr/bin/env python

import os
import pickle



def menu():
	def quit():
		dict1 = dict((['d',displayfiles],['e',editfiles],['s',savefiles],['q',opmenu],['c',create]))
		prompt = """
		(C) to create file
                (D) to display file
                (E) to edit file
                (S) to save file
                (Q) to quit program
                 :"""
                GET_menu = raw_input(prompt).lower()

                if GET_menu in 'desq':
                	dict1[GET_menu]()
                else:
                	print 'invalid option try again!'

		def create():
			GET_Create = raw_input("input you want to create file name:")
			true = GET_Create in os.listdir(os.getcwd())
			if not true:
				New_file = open(GET_Create,'a+')
				print 'file is created ,input you string'
				while True:
					string = raw_input("input you string ,< q > to quit!:")
					if string == 'q':
						quit()
						break
					New_file.writelines('%s%s'%(string,os.linesep))
			else:
				print 'the file is exists, try again!'
				quit()



			def displayfiles():
				trues= os.path.isfile(GET_Create)
				if trues:
					New_file.seek(0,0)
					for each in New_file:
						print each,
					New_file.seek(0,0)
					print 'is working!'
					quit()
				else:
					print "not such file,please to created!"
					quit()
		
			def editfiles():
				trues = os.path.isfile(GET_Create)
				if trues:
					New_file.seek(0,0)
					for each in New_file:
						tellf = New_file.tell()
						print each
						length = len(each)
						get_choice = raw_input("do you want to edit? input y or Y to edit,else to quit:")
						if get_choice in 'yY':
							New_file.seek(tellf,1)
							New_file.truncate(length)
                					GET_edit = raw_input("input you wanna to edit string:!")
							New_file.writelines('%s%s'%(GET_edit,os.linesep))
							New_file.seek(0,0)
							print 'is done'
							quit()
							break

					else:
						print 'no contents anymore!'
						quit()
				else:
					print 'not such file,try again!'
					quit()

			def savefiles():
				trues = os.path.isfile(GET_Create)
				if trues:
					GET_Create.close()
					print 'is saved!'
					quit()
				else:
					print 'no such file,try again'
					quit()
	def opquit():
		print 'is quit'



	quit()

if __name__=="__main__":
	menu()
