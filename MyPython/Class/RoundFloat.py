#!/usr/bin/env python

class RoundFloatManual(object):
	def __inint__(self,val):
		assert isinstance(val,float),\
			"value must be a float"
		self.value = round(val,2)
	def __str__(self):
		return str(self.valu)

rfm = RoundFloatManual()
print rfm(5.2)
