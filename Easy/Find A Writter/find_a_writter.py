import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	final = []

	writter, codes = test.split("|")
	writter = list(writter)
	codes = codes.split()
	for item in codes:
		final.append(writter[int(item) - 1])

	print ''.join(final)