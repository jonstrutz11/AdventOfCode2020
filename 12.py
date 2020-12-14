"""Advent of Code - Problem 12"""

from typing import List, Tuple
import math


class Ferry():
    """Stores location of ferry and provides methods for executing actions."""
    turn_dict = {'L': {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'},
                 'R': {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}}

    def __init__(self) -> None:
        self.facing = 'E'
        self.x = 0
        self.y = 0
        self.waypoint = None

    def execute_action_part_a(self, action: str, value: int) -> None:
        """Perform a given action, e.g. "E10" would mean move East by 10."""
        if action == 'F':
            action = self.facing

        if action == 'N':
            self.y += value
        elif action == 'E':
            self.x += value
        elif action == 'S':
            self.y -= value
        elif action == 'W':
            self.x -= value
        elif action == 'L' or action == 'R':
            n_turns = int(value / 90)  # assuming value is multiple of 90
            for turn in range(n_turns):
                self.facing = self.turn_dict[action][self.facing]
        else:
            raise ValueError(f'Invalid Action: {action}')

    def execute_action_part_b(self, action: str, value: int) -> None:
        """Perform F actions toward waypoint."""
        if action == 'F':        
            self.x += value * self.waypoint.x
            self.y += value * self.waypoint.y
        elif action in ['N', 'E', 'S', 'W', 'R', 'L']:
            self.waypoint.execute_action(action, value)
        else:
            raise ValueError(f'Invalid Action for Ferry: {action}')


class WayPoint():
    """Store location of waypoint."""

    def __init__(self):
        self.x = 10
        self.y = 1

    def execute_action(self, action, value):
        """Perform a given action, e.g. "E10" would mean move East by 10."""
        if action == 'N':
            self.y += value
        elif action == 'E':
            self.x += value
        elif action == 'S':
            self.y -= value
        elif action == 'W':
            self.x -= value
        elif action == 'L' or action == 'R':
            if action == 'L':
                angle = math.radians(90)
            elif action == 'R':
                angle = math.radians(-90)
            n_turns = int(value / 90)  # assuming value is multiple of 90
            for turn in range(n_turns):
                self.x, self.y = rotate((0, 0), (self.x, self.y), angle)
        else:
            raise ValueError(f'Invalid Action for WayPoint: {action}')


def read_directions(filepath: str) -> List[Tuple[str, int]]:
    """Read and parse directions from file."""
    with open(filepath, 'r') as infile:
        directions = [line.strip() for line in infile.readlines()]

    direction_tuples = []
    for direction in directions:
        action = direction[0]
        value = int(direction[1:])
        direction_tuples.append((action, value))

    return direction_tuples


def rotate(origin: Tuple[int, int], point: Tuple[int, int], angle: float) -> Tuple[int, int]:
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.

    See StackOverflow Question 34372480 for original source.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)

    return qx, qy


if __name__ == '__main__':
    DATA_FILEPATH = '12.txt'

    directions = read_directions(DATA_FILEPATH)

    # Part A
    ferry = Ferry()
    for action, value in directions:
        ferry.execute_action_part_a(action, value)

    mahattan_distance = abs(ferry.x) + abs(ferry.y)
    print('Part A - Manhattan Distance:', mahattan_distance)

    # Part B
    ferry = Ferry()
    ferry.waypoint = WayPoint()
    for action, value in directions:
        ferry.execute_action_part_b(action, value)

    mahattan_distance = abs(ferry.x) + abs(ferry.y)
    print('Part B - Manhattan Distance:', mahattan_distance)
