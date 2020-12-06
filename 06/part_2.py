from typing import List


def _get_groups(filename: str) -> List[List[str]]:
	data = open(filename, 'r').read()
	groups = [i.split('\n') for i in data.split('\n\n')]
	return groups

if __name__ == '__main__':
	groups = _get_groups('data_input.dat')
	count = 0
	for group in groups:
		all_yes = set(list(''.join(group)))
		for party in group:
			all_yes = all_yes.intersection(set(list(party)))
		count += len(all_yes)

	print(count)