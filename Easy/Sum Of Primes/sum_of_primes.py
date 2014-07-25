
def SieveOfEratosthenes(N):
	global count
	# Let A be an array of Boolean values, 
	# indexed by integers 2 to n, initially all set to true.

	isPrime = [True] * (N + 1)
	isPrime[0] = isPrime[1] = False

	for i in range(int(N ** 0.5 + 1.5)):
		if i > 1 :
			if isPrime[i]:
				for j in range(i * i, N + 1, i):
					isPrime[j] = False
					
					
	count = 0
	sums = 0				
	for i in range(2, len(isPrime)):
	 	if isPrime[i] == True:
	 		sums = sums + i
	 		count += 1
	return count, sums


N = 7900
count = 997

while count < 1000:				
	count, sums = SieveOfEratosthenes(N)
	N = N + 1
print sums

	