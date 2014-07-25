import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	test = test.split()

	previous = test[0]
	final = ''
	count = 0

	for item in test:
		if item == previous:
			count = count + 1
		else:
			final = final + str(count)+ " " + previous + " "
			previous = item
			count = 1

	print final + str(count)+ " " + previous + " ".strip()