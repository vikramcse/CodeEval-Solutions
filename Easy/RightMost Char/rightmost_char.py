import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	word, find = test.split(',')

	if test == "":
		pass
		
	pos = -1
	for i in range(len(word)):
		if word[i] == find:
			pos = i
	print pos