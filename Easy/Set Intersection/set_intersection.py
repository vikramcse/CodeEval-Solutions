import sys
from sets import Set

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	final = ""
	first, second = test.split(";")
	first = first.split(",")
	second = second.split(",")

	first = [int(x) for x in first]
	second = [int(x) for x in second]
	
	first = Set(first)
	second = Set(second)

	first = list(first.intersection(second))
	first = sorted(first)

	print ','.join(str(x) for x in first)