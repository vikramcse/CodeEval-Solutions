import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	n = len(test)
	test = int(test)

	sum = 0
	number = test
	while(number != 0):
		sum = sum + (number % 10) ** n
		number = number // 10

	if sum == test:
		print True
	else:
		print False