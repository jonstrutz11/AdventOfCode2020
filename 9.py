"""Advent of Code - Problem 9"""

from collections import deque
from itertools import permutations
from typing import List, Optional


def read_data(filepath: str) -> List[int]:
    """Read list of numbers from file."""
    with open(filepath, 'r') as infile:
        lines = infile.readlines()
    number_list = [int(line.strip()) for line in lines]
    return number_list


def initialize_data_queue(data: List[int], queue_length: int = 25) -> deque:
    """Initialize queue with preamble of given length at beginning of data."""
    data_q = deque(maxlen=queue_length)
    for number in data[:queue_length]:
        data_q.append(number)
    return data_q


def initialize_sum_queue(data_q: deque) -> deque:
    """Initialize queue with sums of preamble numbers."""
    sum_q = deque(maxlen=(data_q.maxlen * (data_q.maxlen - 1)))
    sums = [perm[0] + perm[1] for perm in permutations(data_q, 2)]
    for sum_ in sums:
        sum_q.append(sum_)
    return sum_q


def calc_new_sums(data_q: deque) -> List[int]:
    """Calculate newly possible sums after new number added to data queue."""
    new_number = data_q[-1]
    new_sums = [new_number + old_number for old_number in [data_q[i] for i in range(len(data_q))]]
    return new_sums


def process_data_until_invalid(data: List[int], data_q: deque, sum_q: deque) -> Optional[int]:
    """Process list of numbers until an invalid number is found. Returns this
    invalid number. If no invalid number is found, returns None."""
    for number in data[data_q.maxlen:]:
        number_is_valid = number in sum_q
        if not number_is_valid:
            return number

        data_q.append(number)

        new_sums = calc_new_sums(data_q)
        for new_sum in new_sums:
            sum_q.append(new_sum)

    return None


def find_continugous_summed_numbers(data: List[int], invalid_number: int) -> Optional[List[int]]:
    """Find contiguous set of numbers in data that sums to invalid number."""
    starting_index = data.index(invalid_number)
    for index in range(starting_index, 1, -1):
        for contig_length in range(2, index):
            contig = data[(index - contig_length):index]
            contig_sum = sum(contig)
            if contig_sum > invalid_number:
                break
            elif contig_sum == invalid_number:
                return contig
    return None


if __name__ == '__main__':
    DATA_FILEPATH = '9.txt'
    PREAMBLE_LENGTH = 25

    data = read_data(DATA_FILEPATH)

    data_q = initialize_data_queue(data, PREAMBLE_LENGTH)
    sum_q = initialize_sum_queue(data_q)

    # Part A
    invalid_number = process_data_until_invalid(data, data_q, sum_q)
    if invalid_number:
        print('Part A - Invalid Number Detected:', invalid_number)
    else:
        print('Part A - Invalid Number not Detected!')
        exit()

    # Part B
    contiguous_summed_numbers = find_continugous_summed_numbers(data, invalid_number)
    if contiguous_summed_numbers:
        encryption_weakness = min(contiguous_summed_numbers) + max(contiguous_summed_numbers)
        print('Part B - Encryption Weakness Found:', encryption_weakness)
    else:
        print('Part B - Encryption Waekness not Found!')
