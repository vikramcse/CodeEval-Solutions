import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()
    
for test in test_cases:
	test = test.split()
	print test[-2]