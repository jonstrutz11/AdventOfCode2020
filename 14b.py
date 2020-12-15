"""Advent of Code - Problem 14"""

from collections import OrderedDict
from itertools import product
import re


def process_data(filepath: str) -> OrderedDict:
    """Read mask and operations."""
    with open(filepath, 'r') as infile:
        lines = [line.strip() for line in infile.readlines()]

    memory_map = OrderedDict()
    mask = None
    for line in lines:
        if line.startswith('mask'):
            mask = line.split(' = ')[1]
        elif mask and line.startswith('mem'):
            address, value = line.split(' = ')
            address = re.match(r"mem\[(\d+)\]", address)[1]
            new_addresses = apply_mask(mask, address)
            for address in new_addresses:
                memory_map[address] = int(value)
        else:
            raise ValueError('Line should begin with "mask" or "mem". First line must have mask.')

    return memory_map


def apply_mask(mask: str, address: int) -> int:
    """Apply a mask where it converts addresses bit-wise."""
    binary_address = bin(int(address))[2:].zfill(36)

    new_binary_address = []
    for mask_bit, address_bit in zip(mask, binary_address):
        if mask_bit == '0':  # replaced Xs in mask with 2s
            new_binary_address.append(str(address_bit))
        elif mask_bit in ['1', 'X']:
            new_binary_address.append(mask_bit)

    all_addresses = []
    n_x = new_binary_address.count('X')
    all_bit_combos = product(range(2), repeat=n_x)
    for bit_combo in all_bit_combos:
        one_binary_address = ''.join(new_binary_address)
        for bit in bit_combo:
            one_binary_address = one_binary_address.replace('X', str(bit), 1)
        one_decimal_address = int(one_binary_address, 2)
        all_addresses.append(one_decimal_address)

    return all_addresses


if __name__ == '__main__':
    DATA_FILEPATH = '14.txt'

    # Part B
    memory_map = process_data(DATA_FILEPATH)
    part_b_sum = sum([memory_map[address] for address in memory_map])
    print(f'Part B - Sum: {part_b_sum}')
