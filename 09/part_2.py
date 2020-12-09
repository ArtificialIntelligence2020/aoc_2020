from typing import List, Tuple

TARGET = 1721308972


def _get_data_array(filename: str) -> List[int]:
	lines = open(filename, 'r').readlines()
	ints = [int(i.strip()) for i in lines]
	return ints

def get_range(data: List[int], target: int) -> Tuple[int, int]:
	for i in range(len(data)):
		s = 0
		for j in range(i, len(data)):
			s += data[j]
			if s == TARGET:
				return i, j
			if s < TARGET:
				continue
			if s > TARGET:
				break

if __name__ == '__main__':
	data = _get_data_array('./data_input.dat')
	i, j = get_range(data, TARGET)
	print(min(data[i:j+1]) + max(data[i:j+1]))
