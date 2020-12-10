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
        'min': int(min_val),
        'max': int(max_val),
        'char': letter,
        'password': password
    }

    pw_dicts.append(pw_dict)

valid = 0
invalid = 0
for pw_dict in pw_dicts:
    count = pw_dict['password'].count(pw_dict['char'])
    if pw_dict['min'] <= count <= pw_dict['max']:
        valid += 1
    else:
        invalid += 1

print(f'Valid: {valid}')
print(f'Invalid: {invalid}')