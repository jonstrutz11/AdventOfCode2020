"""Advent of Code - Problem 10"""

import math
from typing import Dict, List


def read_jolt_data(filepath: str) -> List[int]:
    """Read jolts from file and sort in ascending order."""
    with open(filepath, 'r') as infile:
        jolt_list = [0]  # initial jolt from charging outlet
        jolt_list += sorted([int(line) for line in infile.readlines()])
        jolt_list.append(jolt_list[-1] + 3)  # built-in adapter
    return jolt_list


def count_contiguous_1s(jolt_diffs: List[int]) -> Dict[int, int]:
    """Count occurence of contiguous 1 elements in list (e.g. [1, 1, 1]). Each
    contig must be flanked by non-1 values or by beginning/end of list."""
    counts = {}  # key = length of contig, val = # occurences in list
    current_contig = []
    for i, jolt_diff in enumerate(jolt_diffs):
        if jolt_diff == 1:
            current_contig.append(1)
        else:
            contig_len = len(current_contig)
            if contig_len not in counts:
                counts[contig_len] = 1
            else:
                counts[contig_len] += 1
            current_contig = []

    # don't need single 1s or instances where no 1s are present (e.g. [3, 3])
    del counts[0]
    del counts[1]

    return counts


def calculate_possible_combinations(contiguous_1_counts: Dict[int, int]) -> int:
    """Calculate all possible combinations based on list of contiguous
    1-elements."""
    all_contig_combos = []  # list of number of combinations contributed by each contig of 1s
    for contig_len in contiguous_1_counts:
        num_contigs_of_this_len = contiguous_1_counts[contig_len]
        contig_combos = [(calc_triangular_number(contig_len) + 1)] * num_contigs_of_this_len
        all_contig_combos += contig_combos
    n_combos = math.prod(all_contig_combos)
    return n_combos


def calc_triangular_number(n: int) -> int:
    """Count triangular number for triangle of side length, n."""
    return sum(range(n))


if __name__ == '__main__':
    DATA_FILEPATH = '10.txt'

    jolt_list = read_jolt_data(DATA_FILEPATH)

    jolt_diffs = [jolt - jolt_list[i - 1] for i, jolt in enumerate(jolt_list)][1:]

    # Part A
    n_1 = jolt_diffs.count(1)
    n_3 = jolt_diffs.count(3)
    part_a_answer = n_1 * n_3
    print('Part A - (1 jolt diffs) * (3 jolt diffs) =', part_a_answer)

    # Part B
    contiguous_1_counts = count_contiguous_1s(jolt_diffs)
    part_b_answer = calculate_possible_combinations(contiguous_1_counts)
    print('Part B - Number of Possible Combinations:', part_b_answer)
