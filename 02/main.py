

def is_valid(input_line: str) -> bool:
    min_max, pass_char, password = input_line.split(' ')
    min_count, max_count = [int(i) for i in min_max.split('-')]
    pass_char = pass_char.rstrip(':')

    char_count = 0
    for char in password:
    	if char == pass_char:
    		char_count += 1

    if char_count >= min_count and char_count <= max_count:
    	return True
    return False


if __name__ == '__main__':
    lines = [i.strip() for i in open('./input_data.csv','r').readlines()]
    count = 0
    for line in lines:
        if is_valid(line):
            count += 1
    print(count)
