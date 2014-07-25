import sys
import collections

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    a, b = test.split(',')
    c = collections.deque(b)
    rotations = set()
    for i in xrange(1, len(b) + 1):
        c.rotate(1)
        rotations.add(''.join(c))
    print a in rotations