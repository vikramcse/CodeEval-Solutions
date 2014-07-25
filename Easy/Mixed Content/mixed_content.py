import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	numbers = []
	words = []

	test = test.split(',')
	for item in test:
		if item.isalpha():
			words.append(item)
		else:
			numbers.append(item)

	if words == []:
		print ','.join(numbers).strip()
	elif numbers == []:
		print ','.join(words).strip()
	else:
		print ','.join(words) + "|" +','.join(numbers).strip()