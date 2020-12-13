"""Advent of Code - Problem 11"""

from typing import List, Tuple
import numpy as np


IndexList = List[Tuple[int, int]]


def read_seat_layout(filepath: str) -> np.array:
    """Read seat layout from file and store in array."""
    with open(filepath, 'r') as infile:
        rows = [list(line.strip()) for line in infile.readlines()]
    seats = np.array(rows)
    return seats


def simulate_seating(starting_seats: np.array, part_b: bool) -> int:
    """Simulate seating and count final number of occupied seats."""
    old_seats = np.array(starting_seats)
    new_seats = apply_seating_rules(old_seats, part_b)
    while (new_seats != old_seats).any():
        old_seats = new_seats
        new_seats = apply_seating_rules(old_seats, part_b)

    unique, counts = np.unique(new_seats, return_counts=True)
    n_occupied = counts[list(unique).index('#')]
    return n_occupied


def apply_seating_rules(seats: np.array, part_b: bool) -> np.array:
    """Returns updated seats after applying rules to all seats once."""
    new_seats = np.array(seats)
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            current_seat = seats[i, j]

            if current_seat == '.':
                continue  # Don't do anything for floor

            if part_b:
                n_occupied = count_los_neighbors(seats, i, j)
            else:
                n_occupied = count_neighbors(seats, i, j)

            if current_seat == 'L' and n_occupied == 0:
                new_seats[i, j] = '#'
            elif current_seat == '#':
                if (part_b and n_occupied >= 5) or (not part_b and n_occupied >= 4):
                    new_seats[i, j] = 'L'

    return new_seats


def count_neighbors(seats: np.array, i: int, j: int) -> Tuple[IndexList, IndexList]:
    """Count number of occupied seats neighboring given location (i, j)."""
    n_occupied_neighbors = 0

    height = len(seats)
    width = len(seats[0])  # All rows are same length

    # Indices must be in bounds of array (e.g. no negative index values)
    directions = [(-1, -1), (0, -1), (1, -1),
                  (-1,  0),          (1,  0),
                  (-1,  1), (0,  1), (1,  1)]
    for direction in directions:
        neighbor_i = i + direction[0]
        neighbor_j = j + direction[1]

        if in_bounds(neighbor_i, neighbor_j, width, height):
            neighbor = seats[neighbor_i, neighbor_j]
            if neighbor == '#':
                n_occupied_neighbors += 1

    return n_occupied_neighbors


def count_los_neighbors(seats: np.array, i: int, j: int) -> Tuple[IndexList, IndexList]:
    """Get indices of each seat in line of sight (LOS) of location (i, j)."""
    n_occupied_los_neighbors = 0

    height = len(seats)
    width = len(seats[0])  # All rows are same length

    directions = [(-1, -1), (0, -1), (1, -1),
                  (-1,  0),          (1,  0),
                  (-1,  1), (0,  1), (1,  1)]
    for direction in directions:
        los_i, los_j = i + direction[0], j + direction[1]  # So we start in bounds
        neighbor_not_found = True
        while neighbor_not_found and in_bounds(los_i, los_j, width, height):

            possible_seat = seats[los_i, los_j]
            if possible_seat == '#':
                neighbor_not_found = False
                n_occupied_los_neighbors += 1
            elif possible_seat == 'L':
                neighbor_not_found = False

            los_i += direction[0]
            los_j += direction[1]

    return n_occupied_los_neighbors


def in_bounds(i: int, j: int, width: int, height: int) -> bool:
    """Calculate whether given i, j are within bounds of array."""
    is_in_bounds = (0 <= i < height) and (0 <= j < width)
    return is_in_bounds



if __name__ == '__main__':
    DATA_FILEPATH = '11.txt'

    starting_seats = read_seat_layout(DATA_FILEPATH)

    # Part A
    n_occupied_a = simulate_seating(starting_seats, part_b=False)
    print('Part A - Number of Occupied Seats:', n_occupied_a)

    # Part B
    n_occupied_b = simulate_seating(starting_seats, part_b=True)
    print('Part B - Number of Occupied Seats:', n_occupied_b)
