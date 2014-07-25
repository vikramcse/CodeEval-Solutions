import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()
	
def fibo(n):
	fib = []
	if n == 0:
		return 0
	elif n == 1:
		return 1

	fib.insert(0, 1)
	fib.insert(1, 1)

	for i in range(2, n):
		fib.insert(i, fib[i - 1] + fib[i - 2])

	return fib[n - 1]

for test in test_cases:
	test = int(test)
	print fibo(test)