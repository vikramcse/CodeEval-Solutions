def is_palindrome(N):
	rev_num = 0
	orig = N

	while N > 0:
		rev_num = (rev_num * 10) + (N % 10)
		N = N / 10

	return rev_num == orig


def SieveOfEratosthenes(N):
	# Let A be an array of Boolean values, 
	# indexed by integers 2 to n, initially all set to true.

	isPrime = [True] * (N + 1)
	isPrime[0] = isPrime[1] = False

	for i in range(int(N ** 0.5 + 1.5)):
		if i > 1 :
			if isPrime[i]:
				for j in range(i * i, N + 1, i):
					isPrime[j] = False
	
	large = 0							
	for i in range(2, len(isPrime)):
	 	if isPrime[i] == True:
	 		if is_palindrome(i):
	 			if large < i:
	 				large = i
	print large

SieveOfEratosthenes(1000)