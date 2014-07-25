import sys
import re

# operations allowed	
operations = "+-"
last_operation = ""


def solution():
	global last_operation

	answer = 0
	count = 0
	num_str = ""

	for item in letters:
		if item not in operations: 
			num_str += str(number_list[count])
			count = count + 1
		else:
			if item == "+":
				answer = answer + int(num_str)
			elif item == "-":
				answer = int(num_str) -answer
			last_operation = item	
			num_str = ""		
			
	if last_operation == "+":
		answer = answer + int(num_str)
	elif last_operation == "-":
		answer = answer - int(num_str)

	print answer
	return 0


test_cases = open(sys.argv[1], 'r')
for test in test_cases:

	# Ignore id empty line
	if test == "\n":
		pass
	else:
		first, second = test.split()
	
		# converted into list
		number_int = int(first)
		number_list = list(first)
		letters = list(second)

		# The number shouldn't start with 0 e.g 0148
		must_match = re.match(r'[1-9]\d*', first, re.I)

		if number_int >= 100 and must_match:
			solution()
		else:
			pass

test_cases.close()
