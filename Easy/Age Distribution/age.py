import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	test = int(test)

	if test >= 0 and test <= 2:
		print "Home"
	elif test >= 3 and test <= 4:
		print "Preschool"
	elif test >= 5 and test <= 11:
		print "Elementary school"
	elif test >= 12 and test <= 14:
		print "Middle school"
	elif test >= 15 and test <= 18:
		print "High school"
	elif test >= 19 and test <= 22:
		print "College"
	elif test >= 23 and test <= 65:
		print "Work"
	elif test >= 66 and test <= 100:
		print "Retirement"
	elif test >= 100 or test < 0:
		print "This program is for humans"