#!/usr/bin/env python

FBString = raw_input(r'input you FBcak some string,thank you!:')

FBS1 = list(FBString)
FBS2 = list(FBString)
FBS2.reverse()
FBS3 = FBS1 + FBS2
print 'the FBS is'
for T in FBS3:
	print T,
#if FBS1 == FBS2:
#	print "is FBString"
#else:
#	print "not FBString"
