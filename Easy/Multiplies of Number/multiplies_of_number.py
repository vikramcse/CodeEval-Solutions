import sys
from collections import Counter

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	x, n = test.split(",")
	x, n = int(x), int(n)

	i = 1
	num = n
	while num < x:
		num = n * i
		i = i + 1
	print num