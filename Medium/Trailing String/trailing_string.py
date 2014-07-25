import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	if test == '':
		continue

	first, second = test.split(",")
	
	if first[len(first) - len(second):] == second:
		print 1
	else:
		print 0