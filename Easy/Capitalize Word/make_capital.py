import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	final = ""
	test = test.split()
	for word in test:
		word = list(word)
		char = word[0]
		word.remove(char)
		word.insert(0, char.upper())
		final = final + ''.join(word) + " "
	print final