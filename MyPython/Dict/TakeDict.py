#!/usr/bin/env python

db = {}
print 'only input ten key and values~'
while True:
	key = raw_input("input you db key,key must be hash key string or number!:")
	value = raw_input("input you key value:")
	db[key] = value
	length = len(db)
	if length >= 10:
		break
a = db.keys()		
b = db.values()
db = dict(zip(b,a))
print 'you input that key and values has been overturned %s'  % db
