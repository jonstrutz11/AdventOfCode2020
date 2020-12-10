"""Advent of Code - Problem 3"""

from functools import reduce

import numpy as np


def generate_tree_array(filepath):
    """Reads data from file to generate an array where 1 is a tree (#) and 0 is
    absence of a tree (.)."""
    with open(filepath, 'r') as infile:
        data = infile.readlines()

    tree_lines_binary = []
    for line in data:
        line_binary = line.replace('.', str(0)).replace('#', str(1)).strip()
        line_binary = [int(num) for num in line_binary]
        tree_lines_binary.append(line_binary)

    tree_array = np.array(tree_lines_binary)

    return tree_array


def calc_coordinates(slope_x, slope_y, height, width):
    """Calculate all integer multiples of slope y/x constrained by height"""
    coordinates = []
    x = y = 0

    while y < height:
        coordinates.append((y, x))
        x += slope_x
        y += slope_y
        x = x % width

    return coordinates


def count_trees(slope_x, slope_y, tree_array):
    """Given integer slope, count number of trees hit in tree array."""
    coords = calc_coordinates(slope_x, slope_y,
                              height=len(tree_array),
                              width=len(tree_array[0]))

    trees = 0
    for coord in coords:
        is_tree = tree_array[coord]
        if is_tree:
            trees += 1

    return trees


if __name__ == '__main__':
    DATA_FILEPATH = '03.txt'
    SLOPE_X_LIST = [1, 3, 5, 7, 1]
    SLOPE_Y_LIST = [1, 1, 1, 1, 2]

    tree_array = generate_tree_array(DATA_FILEPATH)

    tree_counts = []
    for slope_x, slope_y in zip(SLOPE_X_LIST, SLOPE_Y_LIST):
        tree_count = count_trees(slope_x, slope_y, tree_array)
        tree_counts.append(tree_count)
    print('Tree Counts:', tree_counts)

    tree_product = reduce((lambda x, y: x * y), tree_counts)
    print('Product of Tree Counts:', tree_product)
