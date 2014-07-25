import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	test = test.strip()
	
	for i in range(1, len(test) + 1):
		common = test[:i]

		rejoined = ''.join(test.split(common))
		if len(rejoined) == 0:
			print len(common)
			break