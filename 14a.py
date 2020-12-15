"""Advent of Code - Problem 14"""

from collections import OrderedDict
import re


def read_data(filepath: str) -> OrderedDict:
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
            memory_map[int(address)] = (int(value), mask)
        else:
            raise ValueError('Line should begin with "mask" or "mem". First line must have mask.')

    return memory_map


def apply_masks_to_memory_map(memory_map: OrderedDict) -> OrderedDict:
    """Apply linked mask to each value in memory map."""
    new_memory_map = OrderedDict()
    for address, (value, mask) in memory_map.items():
        new_value = apply_mask(mask, value)
        new_memory_map[address] = (new_value, mask)

    return new_memory_map


def apply_mask(mask: str, value: int) -> int:
    """Apply a mask where it overwrites values bit-wise."""
    mask = [int(bit) for bit in mask.replace('X', '2')]
    binary_val = [int(bit) for bit in bin(value)[2:].zfill(36)]

    new_binary_val = []
    for mask_bit, value_bit in zip(mask, binary_val):
        if mask_bit != 2:  # replaced Xs in mask with 2s
            new_binary_val.append(str(mask_bit))
        else:
            new_binary_val.append(str(value_bit))

    new_binary_val = int(''.join(new_binary_val), 2)
    return new_binary_val


if __name__ == '__main__':
    DATA_FILEPATH = '14.txt'

    memory_map = read_data(DATA_FILEPATH)

    # Part A
    new_memory_map = apply_masks_to_memory_map(memory_map)
    part_a_sum = sum([new_memory_map[address][0] for address in new_memory_map])
    print(f'Part A - Sum: {part_a_sum}')
