import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

sum = 0
for test in test_cases:
	sum = sum + int(test)

print sum