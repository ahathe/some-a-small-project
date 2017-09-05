#!/usr/bin/env python
def Change_Str(String):
	Str = String.swapcase()
	print 'the beforer result %s' % String
	print 'the after result is %s' % Str
	


Str_Get = raw_input("input you want to change string!")
Change_Str(Str_Get)
