import sys
from sets import Set

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	alphas = set("abcdefghijklmnopqrstuvwxyz")

	test = test.lower()
	test.replace(" ", "")
	test = set(test)

	ans = sorted(alphas.difference(test))

	if ans:
		print ''.join(ans)
	else:
		print 'NULL'