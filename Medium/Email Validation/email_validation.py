import sys
import re

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	if test == '':
		continue

	#regx = "[\w\.-]+@[\w\.-]+"
	regx = '^"[\w|_|-|+|.|@]+"|[\w|_|-|+|.?]*@{1}[a-z|0-9]+\.{1}[a-z|0-9|-]+\.?[a-z|0-9|-]{2,}'
	email_check = re.compile(regx)
	a = re.match(email_check, test)
	#print {None: 'false'}.get(a, 'true')
	if a == None:
		print 'false'
	else:
		print 'true'
	
