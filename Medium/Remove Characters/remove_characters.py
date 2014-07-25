import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	if test == '':
		continue

	target, bullet = test.split(",")
	bullet = bullet.strip()

	for i in range(len(bullet)):
		target = target.replace(bullet[i], '')

	print target