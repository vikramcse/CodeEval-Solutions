import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	number, i, j = test.split(',')
	bin_number = bin(int(number))[2:]
	length = len(bin_number)
	
	if bin_number[length - int(i)] == bin_number[length - int(j)]:
		print "true"
	else:
		print "false"