import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	test = test.split(" ")
	stack = []
	output = []
	is_Even = False

	for item in test:
		stack.append(int(item))

	for i in stack[-1::-2]:
		output.append(i)

	print ' '.join(str(i) for i in output)
