import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	test = int(test)
	if test == '' or test == 0:
		continue
		
	matrix = [[0]* test for i in range(test)]
	ans = []
	for line in range(0, test):
		for i in range(0, line + 1):
			if i == 0 or i == line:
				matrix[line][i] = 1
				ans.append(1)
			else:
				matrix[line][i] = matrix[line - 1][i - 1] + matrix[line - 1][i]
				ans.append(matrix[line][i])

	print ' '.join(str(x) for x in ans)
			