import sys
from collections import Counter

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	sum = 0
	max_beauty = 26

	# ignored the special characters and numbers by isalnum() and isdigit() function
	# and next convert to list
	test = ''.join(item for item in test if item.isalnum() and not item.isdigit())
	test = list(test.lower())
	
	# The most common ouccurances
	count = Counter(test).most_common()

	for i in range(len(count)):
		sum = sum + (count[i][1] * max_beauty)
		max_beauty = max_beauty - 1

	print sum		