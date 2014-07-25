import sys
from collections import Counter

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	test = test.split()
	c = Counter(test).most_common()
	
	collect = []
	for item in c:
		if item[1] == 1:
			collect.append(item[0])

	if collect == []:
		print 0
	else:
		print test.index(min(collect)) + 1
