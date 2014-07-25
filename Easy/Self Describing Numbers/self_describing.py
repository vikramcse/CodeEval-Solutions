import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	test = [int(x) for x in test]
	
	is_self_describing = False
	for i in range(len(test)):
		if test.count(i) == test[i]:
			is_self_describing = True
		else:
			is_self_describing = False
			break

	if is_self_describing:
		print 1
	else:
		print 0
