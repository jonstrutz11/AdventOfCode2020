"""Advent of Code 2020 - Problem 1"""

with open('1.txt', 'r') as infile:
    data = [int(num) for num in infile.readlines()]

print('Data:', data[:5])

final_numbers = ()
for number1 in data:
    left = 2020
    left = left - number1
    for number2 in data:
        if number2 == left:
            final_numbers = (number1, number2)
            break

print('Part A:', final_numbers[0] * final_numbers[1])
print('Final Numbers:', final_numbers, '\n')


final_numbers = ()
for number1 in data:
    left = 2020
    left = left - number1
    for number2 in data:
        leftfinal = left - number2
        for number3 in data:
            if number3 == leftfinal:
                final_numbers = (number1, number2, number3)
                break


print('Part A:', final_numbers[0] * final_numbers[1] * final_numbers[2])
print('Final Numbers:', final_numbers, '\n')
