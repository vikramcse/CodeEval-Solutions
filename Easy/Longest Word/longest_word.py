import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

lengths = []
for test in test_cases:
	test = test.split()
	lengths = [len(item) for item in test]
	print test[lengths.index(max(lengths))]