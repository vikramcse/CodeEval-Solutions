import sys

def add_digits(N):
	sum = 0
	while N:
		sum = sum + N % 10
		N = N // 10
	print sum

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test == "\n":
    	pass
    else:
    	add_digits(int(test))

test_cases.close()
