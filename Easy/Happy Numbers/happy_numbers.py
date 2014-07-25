import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    all_nums, happy, num = [], 1, test
    while num != 1:
        num = sum(int(i) ** 2 for i in str(num))
        if num in all_nums:
            happy = 0
            break
        else:
            all_nums.append(num)
    print happy