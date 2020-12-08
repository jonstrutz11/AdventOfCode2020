"""Advent of Code - Day 7"""

from typing import List, Optional


class Bag():
    """Stores info about bag type, count, and parents."""
    def __init__(self, style, color) -> None:
        self.style = style
        self.color = color
        self.containers = {}
        self.containees = {}

    def add_container(self, style, color, count) -> None:
        """Add bag of given style and color as a possible container of this bag."""
        if style not in self.containers:
            self.containers[style] = {}
        self.containers[style][color] = count

    def add_containee(self, style, color, count) -> None:
        """Add bag of given style and color as a containee of this bag."""
        if style not in self.containees:
            self.containees[style] = {}
        self.containees[style][color] = count

    def __repr__(self) -> str:
        return f'{self.style} {self.color} bag, contained by {self.containers}'


def parse_bag_rules(filepath: str) -> List[str]:
    """Read bag rules from file, and parse them into a list of rules."""
    with open(filepath, 'r') as infile:
        rules = [rule.rstrip('.\n') for rule in infile.readlines()]
    return rules


def parse_bag_description(description) -> (int, str, str):
    """Extract style and color strings from description of bag."""
    if description == 'no other bags':
        count, style, color = 0, None, None
    elif not description[0].isdigit():
        count = None
        style, color = description.replace(' bags', '').split(' ')
    else:
        count, style, color = description.replace(' bags', '').replace(' bag', '').split(' ')
        count = int(count)
    return (count, style, color)


def find_bag(bag_style: str, bag_color: str, bag_list: List[Bag]) -> Optional[Bag]:
    """Find a bag of given type in a list of Bags."""
    found_bag = None
    for bag in bag_list:
        if bag.style == bag_style and bag.color == bag_color:
            found_bag = bag
    return found_bag


def build_bag_hierarchy(rules: List[str]) -> List[Bag]:
    """Build mapping from containee up to container and vice versa."""
    all_bags = []
    for rule in rules:
        container, containees = rule.split(' bags contain ')

        _, container_style, container_color = parse_bag_description(container)
        container_bag = find_bag(container_style, container_color, all_bags)
        if not container_bag:
            container_bag = Bag(container_style, container_color)
            all_bags.append(container_bag)

        containees = containees.split(', ')
        for containee in containees:
            count, containee_style, containee_color = parse_bag_description(containee)

            # Add info to container bag object
            container_bag.add_containee(containee_style, containee_color, count)

            # Add info to containee bag object
            found_bag = find_bag(containee_style, containee_color, all_bags)
            if found_bag:
                found_bag.add_container(container_style, container_color, count)
            else:
                new_bag = Bag(containee_style, containee_color)
                new_bag.add_container(container_style, container_color, count)
                all_bags.append(new_bag)

    return all_bags


def list_containers(bag: Bag, bag_list: List[Bag], container_list: List[str] = []) -> List[str]:
    """List all possible containers for this bag."""
    for container_style in bag.containers:
        for container_color in bag.containers[container_style]:
            container_list.append(f'{container_style} {container_color}')
            container_bag = find_bag(container_style, container_color, bag_list)
            if container_bag:
                _ = list_containers(container_bag, bag_list, container_list)
    return container_list


def count_containees(bag: Bag, bag_list: List[Bag], total: int = 0) -> int:
    """Count number of contained bags within this bag."""
    for containee_style in bag.containees:
        for containee_color in bag.containees[containee_style]:
            count = bag.containees[containee_style][containee_color]
            if count:
                containee_bag = find_bag(containee_style, containee_color, bag_list)
                # Total = Total + N_contained_bags + N_contained_bags * N_each_of_their_bags
                total += count + count * count_containees(containee_bag, bag_list)
    return total


if __name__ == '__main__':
    DATA_FILEPATH = '7.txt'

    bag_rules = parse_bag_rules(DATA_FILEPATH)
    bag_hierarchy = build_bag_hierarchy(bag_rules)
    shiny_gold_bag = find_bag('shiny', 'gold', bag_hierarchy)

    # Part A
    all_containers = list_containers(shiny_gold_bag, bag_hierarchy)
    num_containers = len(set(all_containers))
    print('Part A - Number of Unique Containers:', num_containers)

    # Part B
    num_containees = count_containees(shiny_gold_bag, bag_hierarchy)
    print('Part B - Total Number of Containees:', num_containees)
