import sys

def SieveOfEratosthenes(N):
	# Let A be an array of Boolean values, 
	# indexed by integers 2 to n, initially all set to true.
	primes = []
	isPrime = [True] * (N + 1)
	isPrime[0] = isPrime[1] = False

	for i in range(int(N ** 0.5 + 1.5)):
		if i > 1 :
			if isPrime[i]:
				for j in range(i * i, N + 1, i):
					isPrime[j] = False
									
	for i in range(2, len(isPrime)):
	 	if isPrime[i] == True:
	 		if i < N:
	 			primes.append(i)

	print ','.join(str(i) for i in primes)

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	if len(test) == 0:
		continue

	limit = int(test)

	SieveOfEratosthenes(limit)