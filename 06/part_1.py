from typing import List


def _get_groups(filename: str) -> List[str]:
	data = open(filename, 'r').read()
	groups = [i.replace('\n', '') for i in data.split('\n\n')]
	return groups

if __name__ == '__main__':
	groups = _get_groups('data_input.dat')
	count = 0
	for group in groups:
		letters = set(list(group))
		count += len(letters)
	print(count)