import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	N, array = test.split(";")
	N, array = int(N), array.split(',')
	array = [int(i) for i in array]

	currentSum = sum(array)
	expectedSum = ((N - 1) * (N - 2)) / 2

	print abs(expectedSum - currentSum)