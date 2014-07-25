import sys

list1 = []
list2 = []

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	list1, list2 = test.split('|')

	list1 = list1.split()
	list2 = list2.split()
	answer = ""
	
	for i in range(len(list1)):
		answer += str( int( list1[i] ) * int( list2[i] ) ) + " "
	print answer

test_cases.close()