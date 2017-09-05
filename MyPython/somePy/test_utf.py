#!/usr/bin/env python


"An example of reading and writing Unicode string:Writes"

CODE='utf-8'
FILE='unicode.txt'

hello_out = u"Hello Wrold\n"
bytes_out = hello_out.encode(CODE)
f = open(FILE,"w")
f.write(bytes_out)
f.close()

f = open(FILE,"r")
bytes_in = f.read()
f.close()
hello_in = bytes_in.decode(CODE)
print hello_in,
