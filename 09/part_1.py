from typing import List


def _get_data_array(filename: str) -> List[int]:
	lines = open(filename, 'r').readlines()
	ints = [int(i.strip()) for i in lines]
	return ints


def _validate(factors: List[int], target: int) -> bool:
	sorted_factors = sorted(factors)
	left = 0
	right = len(sorted_factors) - 1

	current = sorted_factors[left] + sorted_factors[right]
	while (left != right):
		if current == target:
			return True
		elif current > target:
			right -= 1
		elif current < target:
			left += 1
		current = sorted_factors[left] + sorted_factors[right]
	return False


if __name__ == '__main__':
	data = _get_data_array('./data_input.dat')
	for i in range(len(data) - 26):
		if not _validate(data[i:i+25], data[i+25]):
			print(f'Found a failure at index {i+25} which is {data[i+25]}')
			break
