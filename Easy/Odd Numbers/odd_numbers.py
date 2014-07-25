def is_odd(number):
	return (number & 1) != 0

number = 1
while number <= 100:
	if (is_odd(number)):
		print number
	number += 1
