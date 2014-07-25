import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:

	N, M = test.split(',')
	N, M = int(N), int(M)

	print N - ((N / M) * M)