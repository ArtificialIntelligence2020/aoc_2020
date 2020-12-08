from typing import List, Tuple


def get_instructions(filename: str) -> List[Tuple[str, int]]:
	lines = [i.strip() for i in open(filename, 'r').readlines()]
	instructions = []
	for line in lines:
		command, argument = line.split(' ')
		argument = int(argument.lstrip('+'))
		instructions.append((command, argument))
	return instructions


if __name__ == '__main__':
	instructions = get_instructions('./data_input.dat')
	acc = 0
	eip = 0
	visited = set()

	while True:
		if eip in visited:
			print(acc)
			break
		else:
			visited.add(eip)

		current = instructions[eip]
		if current[0] == 'acc':
			acc += current[1]
			eip += 1
			continue
		elif current[0] == 'nop':
			eip += 1
			continue
		elif current[0] == 'jmp':
			eip += current[1]
			continue