#!/usr/bin/env python

import random
while True:
	rock = random.randint(0,10)
	scissor = random.randint(0,10)
	paper = random.randint(0,10)

dirc = {'rock':rock,'scissor':scissor,'paper':paper}
def Total(one,two):
	if rock > scissor:






You_Input = raw_input("Tom input you choice!,rock,paper,scissors!:")
Other = raw_input("Anna input you choice!,rock,paer,scissor!:")

if __name__=="__main__":
	Total(dirc[You_Input],dirc[Other])
