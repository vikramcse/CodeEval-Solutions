import sys
from collections import Counter

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	array = test.split(";")[1]
	array = array.split(',')

	print Counter(array).most_common(1)[0][0]