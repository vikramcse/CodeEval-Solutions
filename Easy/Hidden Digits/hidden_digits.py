import sys

numbers = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()


for test in test_cases:
	final = []
	for i in range(len(test)):
		final.append(str(numbers.get(test[i], '')))

	final = ''.join(final)

	if final :
		print ''.join(final)
	else:
		print "NONE"	