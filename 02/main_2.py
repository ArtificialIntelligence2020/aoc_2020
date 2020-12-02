

def is_valid(input_line: str) -> bool:
    min_max, pass_char, password = input_line.split(' ')
    min_count, max_count = [int(i) for i in min_max.split('-')]
    pass_char = pass_char.rstrip(':')

    min_valid = (password[min_count-1] == pass_char)
    max_valid = (password[max_count-1] == pass_char)
    ret_val = min_valid ^ max_valid
    return ret_val


if __name__ == '__main__':
    lines = [i.strip() for i in open('./input_data.csv','r').readlines()]
    count = 0
    for line in lines:
        if is_valid(line):
            count += 1
    print(count)
