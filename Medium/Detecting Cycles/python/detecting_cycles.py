import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	test = test.split()
	test = [int(x) for x in test]

	length = len(test)
	x = 0
	y = 1

	# Detection of loop
	while test[x] != test[y]:
		x = (x + 1) % length
		y = (y + 2) % length

	y = abs(x - y) 
	x = 0
	final = []
	
	while test[x] != test[y]:
		x = (x + 1) % length
		y = (y + 1) % length

	
	# find the cycle length
	length, y = 1, x + 1
	while test[x] != test[y]:
		y += 1
		length += 1

        
	for i in range(x, x + length):
		final.append(test[i])

	print ' '.join(str(x) for x in final)