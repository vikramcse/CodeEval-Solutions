import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
	number, swap_list = test.split(":")
	swap_list = swap_list.split(",")
	number = number.split()

	for item in swap_list:
		one, two = item.split("-")
		one, two = int(one), int(two)

		number[one], number[two] = number[two], number[one]

	print ' '.join(number)