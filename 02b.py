"""Advent of Code 2020 - Problem 2"""

with open('02.txt', 'r') as infile:
    raw_data = [line for line in infile.readlines()]

pw_dicts = []
for line in raw_data:
    line_parts = line.split(' ')
    min_val, max_val = line_parts[0].split('-')
    letter = line_parts[1].replace(':', '')
    password = line_parts[2]

    pw_dict = {
        'index1': int(min_val) - 1,
        'index2': int(max_val) - 1,
        'char': letter,
        'password': password
    }

    pw_dicts.append(pw_dict)

valid = 0
invalid = 0
for pw_dict in pw_dicts:
    pw = pw_dict['password']
    char = pw_dict['char']
    i1 = pw_dict['index1']
    i2 = pw_dict['index2']

    if (pw[i1] == char and pw[i2] != char) or (pw[i1] != char and pw[i2] == char):
        valid += 1
    else:
        invalid += 1

print(f'Valid: {valid}')
print(f'Invalid: {invalid}')