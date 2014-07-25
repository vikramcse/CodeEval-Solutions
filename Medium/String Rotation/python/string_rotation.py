import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	a, b = test.split(",")
	a, b = list(a), list(b)

	if a == [] or b == []:
		continue

	start_a = 0
	start_b = b.index(a[0])
	length = len(a)


	if a[start_a] == b[start_b]: 
		is_matched = True
	else:
		is_matched = False

	if len(a) != len(b):
		is_matched = False

	for i in range(length):
		if a[(start_a + i) % length] == b[(start_b + i) % length] and is_matched:
			is_matched = True
		else:
			is_matched = False
			break;

	print is_matched