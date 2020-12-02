if __name__ == '__main__':
    numbers = [int(i.strip()) for i in open('input_data.csv','r').readlines() if i.strip() != '']
    numbers = sorted(numbers)

    for i, i_val in enumerate(numbers):
        for j, j_val in enumerate(numbers):
            for k, k_val in enumerate(numbers):
                if i_val + j_val + k_val == 2020:
                    print(numbers[i] * numbers[j] * numbers[k])
