import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	test = test.split()
	test = [float(x) for x in test]
	test.sort()
	print ' '.join(str(("%.3f" % x)) for x in test).strip()