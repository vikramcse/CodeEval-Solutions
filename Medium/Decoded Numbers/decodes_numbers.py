import sys
import itertools

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

map = []
for i in range(1, 27):
	map.append(i)


for test in test_cases:
	test = list(test)
	#test = [int(i) for i in test]
	pairs = []
	count = 0

	for i in range(2, len(test)):
		tup = list(itertools.combinations(test, i))
		for x in tup:
			print x

	


