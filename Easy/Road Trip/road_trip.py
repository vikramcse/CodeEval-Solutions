import sys

with open(sys.argv[1], 'r') as input:
	test_cases = input.read().strip().splitlines()

for test in test_cases:
	seprate = test.split(";")

	dist = []
	final = []
	for i in range(len(seprate)):
		item = seprate[i].split(",")
		if item[0] != "":
			dist.append(int(item[1]))

	dist = sorted(dist)
	final.append(dist[0])
	for i in range(len(dist) - 1):
		final.append(dist[i + 1] - dist[i])

	print ','.join(str(x) for x in final)