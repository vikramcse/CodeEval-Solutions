import sys

string = []
hints = []

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    string, hints = test.split(";")

    string = string.split()
    hints = hints.split()

    final = [""] * len(string)

    i = 0
    
    for hint in hints:
        final[int(hint) - 1] = string[i] + " "
    	i = i + 1
    final[final.index('')] = string[i] + " "
    print ''.join(final)

test_cases.close()