import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	test = test.split(",")

	jar = set([])

	for item in test:
		jar.add(int(item))

	final = sorted(jar)

	print ','.join(str(x) for x in final)