import sys

words_list = []
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # Ignore id empty line
	if test == "\n":
		pass
	else:
		words_list = test.split()
		words_list = words_list[::-1]
		print " ".join(words_list)

test_cases.close()
