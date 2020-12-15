"""Advent of Code - Problem 15"""

from typing import Dict, List


def read_numbers(filepath: str) -> List[int]:
    """Read file with comma-separated numbers."""
    with open(filepath, 'r') as infile:
        numbers = [int(num) for num in infile.readline().strip().split(',')]
    return numbers


def initialize_memory_dict(numbers: List[int]) -> Dict[int, int]:
    """Initialize a dict with number provided as key, turn spoken as val."""
    memory_dict = {number: turn for turn, number in enumerate(numbers[:-1])}
    return memory_dict


def say_next_number(turn: int, last_number: int, memory_dict: Dict[int, int]) -> int:
    """Figure out the next number in the sequence based on game rules."""
    if last_number not in memory_dict:
        next_number = 0
    else:
        next_number = turn - memory_dict[last_number]
    return next_number


def get_final_number(end_turn: int, numbers: List[int]):
    """Get number at turn provided based on game rules."""
    memory_dict = initialize_memory_dict(numbers)

    turn = len(numbers) - 1  # Turn is 0-indexed
    next_number = numbers[-1]
    while turn < (end_turn - 1):  # Turn is 0-indexed
        if turn % 1000000 == 0:
            print(f'Turn {turn}')
        last_number = next_number
        next_number = say_next_number(turn, last_number, memory_dict)
        memory_dict[last_number] = turn
        turn += 1

    return next_number


if __name__ == '__main__':
    DATA_FILEPATH = '15.txt'

    numbers = read_numbers(DATA_FILEPATH)

    final_number_a = get_final_number(2020, numbers)
    print('Part A - 2020th Number:', final_number_a)

    final_number_b = get_final_number(30000000, numbers)
    print('Part B - 3,000,000th Number:', final_number_b)
