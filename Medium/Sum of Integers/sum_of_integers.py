# I have used The Dynamic programming approch

import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	if test == '':
		continue

	test = test.split(",")
	test = [int(i) for i in test]
	all_negative = False
	count_negative = 0

	# here i check if all elements are -ve 
	for i in test:
		if i < 0:
			count_negative += 1

	if count_negative == len(test):
		all_negative = True

	# if all elements are not -ve then
	# take a list Memory 
	# and if sum of current and previous element is > 0 
	# then store in Memory else store 0	
	if not all_negative:	
		Memory = [0] * len(test)
		if test[0] > 0:
			Memory[0] = test[0]
		else:
			Memory[0] = 0

		for i in range(1, len(test)):
			if (Memory[i - 1] + test[i]) > 0:
				Memory[i] = Memory[i - 1] + test[i]
			else:
				Memory[i] = 0

		print max(Memory)
	else:
		# if all -ve then return largest element from
		# the orignal list
		print max(test)

	#print max(Memory)