import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    if test:
        x, n = test.split(',')
        x, n = int(x), int(n)
        for i in xrange(1, x):
            if n * i >= x:
                num = n * i
                break
        print num