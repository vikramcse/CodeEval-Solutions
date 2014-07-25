import sys
import timeit


start = timeit.default_timer()

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # Ignore id empty line
	if test == "\n":
		pass
	else:
		print test.lower()

stop = timeit.default_timer()
print stop - start

test_cases.close()