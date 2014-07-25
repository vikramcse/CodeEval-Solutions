import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:

	lower = 0.0
	upper = 0.0
	
	for i in range(len(test)):
		if test[i].islower():
			lower = lower + 1
		elif test[i].isupper():
			upper = upper + 1

	lowers = (lower / len(test)) * 100
	uppers = (upper / len(test)) * 100

	print "lowercase: " + str(("%.2f" % lowers)) + " " + "uppercase: " + str(("%.2f" % uppers))