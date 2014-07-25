import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

N = test_cases[0]
test_cases.remove(N)
lengths = {}

for item in test_cases:
	lengths[item] = len(item)

final = sorted(lengths.items(), key=lambda x: x[1], reverse=True)
#print sorted(lengths, key = lengths.get, reverse=True)

for i in range(int(N)):
	print final[i][0]