from typing import List, Tuple


def get_instructions(filename: str) -> List[Tuple[str, int]]:
	lines = [i.strip() for i in open(filename, 'r').readlines()]
	instructions = []
	for line in lines:
		command, argument = line.split(' ')
		argument = int(argument.lstrip('+'))
		instructions.append((command, argument))
	return instructions

def patch_instructions(instructions: List[Tuple[str, str]], place: int) -> List[Tuple[str, str]]:
	output = instructions[:]
	entry = output[place]
	if entry[0] == 'jmp':
		output[place] = ('nop', output[place][1])
	else:
		output[place] = ('jmp', output[place][1])
	return output

def run_program(instructions: List[Tuple[str, str]]) -> bool:
	acc = 0
	eip = 0
	visited = set()
	previous = 0

	while True:
		if eip in visited:
			print(previous)
			print(instructions[previous])
			print(acc)
			return False
		else:
			visited.add(eip)

		previous = eip

		if eip == len(instructions):
			print('TERMINATION')
			print(acc)
			return True

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


if __name__ == '__main__':
	instructions = get_instructions('./data_input.dat')

	switches = []
	for index, i in enumerate(instructions):
		if i[0] in ('jmp', 'nop'):
			switches.append(index)

	for switch in switches:
		print(switch)
		new_instructions = patch_instructions(instructions, switch)
		if run_program(new_instructions):
			print('found it')
			print(switch)
			break
