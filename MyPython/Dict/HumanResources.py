#!/usr/bin/env python

db = {}
print 'only can input ten key and value'
while True:
	key = raw_input("input you employee name:")
	value = raw_input("input you employee number:")
	db[key] = value
	length = len(db)
	if length >= 10:
		break
print 'employee name and numbers~'
for x in db.keys():
	print db[x]

