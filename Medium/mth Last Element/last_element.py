import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	test = test.split(" ")
	array = []
	for item in test:
		if not item.isdigit():
			array.append(item)
		else:
			N = int(item)
	if N <= len(array):
		print array[-N]
	else:
		pass
