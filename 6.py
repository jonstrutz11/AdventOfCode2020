"""Advent of Code 2020 - Problem 6"""


def parse_customs_data(filename):
    """Read and parse customs data from file."""
    with open(filename, 'r') as infile:
        all_groups = infile.read().split('\n\n')

    all_group_answers = []
    for group in all_groups:
        group_answers = group.split('\n')
        all_group_answers.append(group_answers)

    return all_group_answers


def count_anyone_answers(group_answers):
    """Count up all answers given by anyone in a list of group's answers."""
    group_answer_sets = [set(ga) for ga in group_answers]
    anyone_answers = set.union(*group_answer_sets)
    n_letters = len(anyone_answers)
    return n_letters


def count_everyone_answers(group_answers):
    """Count up all answers given by everyone in a list of group's answers."""
    group_answer_sets = [set(ga) for ga in group_answers]
    everyone_answers = set.intersection(*group_answer_sets)
    n_letters = len(everyone_answers)
    return n_letters


if __name__ == '__main__':
    DATA_FILEPATH = '6.txt'

    all_group_answers = parse_customs_data(DATA_FILEPATH)

    # Part A
    unique_answer_total_a = 0
    for group_answers in all_group_answers:
        unique_answer_count = count_anyone_answers(group_answers)
        unique_answer_total_a += unique_answer_count

    print('Part A - Total # Unique Answers:', unique_answer_total_a)

    # Part B
    all_answer_total_b = 0
    for group_answers in all_group_answers:
        all_answer_count = count_everyone_answers(group_answers)
        all_answer_total_b += all_answer_count

    print('Part B - Total # All Answers:', all_answer_total_b)
