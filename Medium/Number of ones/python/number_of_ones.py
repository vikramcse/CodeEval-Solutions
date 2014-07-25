import sys
from collections import Counter

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    print Counter(bin(int(test)))['1']