#!/usr/bin/env python

import os
def FT(TF):
	truet = os.path.isfile(TF)
	if '/' in TF:
		os.chdir(os.path.split(TF)[0])
		TF = TF.split('/')[-1]
	return TF

def FG(GF):
	trueg = os.path.isfile(GF)
	if '/' in GF:
		os.chdir(os.path.split(GF)[0])
		GF = GF.split('/')[-1]
	return GF

def FileComparison(TaF,GeF):
	tf = open(TaF,'r')
	tg = open(GeF,'r')
	list1 = [x for x in tf]
	list2 = [i for i in tg]
	for x in range(len(list1)):		
		s = [[list1[x][i],list2[x][i]] for i in range(len(list1[x])) if list1[x][i] != list2[x][i]]
		if s != []:
			print 'not matching first file line %s column %s,second is line %s column %s' % (x+1,i+1,x+1,i+1)
			break
	else:
		print 'is match ~ first file %s' % list1
		print 'to'
		print 'is match ~ second file %s' % list2
	tf.close()
	tg.close()
		
TAKE_F = raw_input("input you file name or full file path name to comparison~:")
GET_F = raw_input("input you file name or full file path name to comparison~:")

FileComparison(FT(TAKE_F),FG(GET_F))
