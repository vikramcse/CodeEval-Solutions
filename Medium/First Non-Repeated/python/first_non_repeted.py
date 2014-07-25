import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	test = list(test)

	hashTable = {}
	exceptZero = []

	# made initially to zero
	for char in test:
		hashTable[char] = 0

	# if the number is repeated then make it -ve
	# but is it is already negative then ignore because it appeared twice
	for char in test:
		if hashTable[char] == 0:
			hashTable[char] = test.index(char) + 1
		else:
			if hashTable[char] > 0:
				hashTable[char] *= -1
			else:
				pass

	# Except the -ve extract +ve numbers			
	for char in test:
		if hashTable[char] > 0:
			exceptZero.append(hashTable[char])

	# the min index is the first non repeated		
	print test[min(exceptZero) -1]
