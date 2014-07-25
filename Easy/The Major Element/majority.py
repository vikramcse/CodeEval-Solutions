import sys
from collections import Counter

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
	sequence = test.split(',')
	majority_number = Counter(sequence).most_common(1)

	if majority_number[0][1] > len(sequence) / 2:
		print majority_number[0][0]
	else:
		print "None"