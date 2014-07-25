for i in range(12):
	table = []
	for j in range(12):
		table.append((i + 1) * (j + 1))
	print '{:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3}'.format(*table).strip()
	print '\n'