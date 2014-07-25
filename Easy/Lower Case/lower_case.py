import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # Ignore if empty line
	if test == "\n":
		pass
	else:
		print test.lower()

test_cases.close()