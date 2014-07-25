import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	final = []
	for i in range(len(test)):
		if test[i].isupper():
			final.append(test[i].lower())
		else:
			final.append(test[i].upper())

	print ''.join(final)