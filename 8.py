"""Advent of Code - Problem 8"""

from typing import List


def read_instructions(filepath: str) -> List[str]:
    """Read instructions from file."""
    with open(filepath, 'r') as infile:
        instructions = [line.strip() for line in infile.readlines()]
    return instructions


class BootCode():
    """Store and process instructions from game console boot code."""

    def __init__(self) -> None:
        self.instructions = []
        self.accumulator = 0
        self.current_instruction_i = 0

    def load_instructions(self, instructions) -> None:
        """Parse a list of instructions."""
        for instruction in instructions:
            operation, argument = instruction.split(' ')
            argument = int(argument)
            self.instructions.append({'op': operation, 'arg': argument, 'run': False})

    def run_next_instruction(self) -> bool:
        """Run next instruction. If it has already been run, return True."""
        current_instruction = self.instructions[self.current_instruction_i]
        op = current_instruction['op']
        arg = current_instruction['arg']
        already_run = current_instruction['run']

        if already_run:
            return True
        current_instruction['run'] = True

        if op == 'acc':
            self.accumulator += arg
            self.current_instruction_i += 1
        elif op == 'jmp':
            self.current_instruction_i += arg
        elif op == 'nop':
            self.current_instruction_i += 1
        else:
            raise ValueError(f'Operation {op} not recognized.')

        will_be_on_last_line = self.current_instruction_i == len(self.instructions)

        # Wrap around if needed
        if not will_be_on_last_line:
            self.current_instruction_i = self.current_instruction_i % len(self.instructions)
        else:
            print('Part B - Program terminating - accumulator value:', self.accumulator)
            return True

        return False


if __name__ == '__main__':
    DATA_FILEPATH = '8.txt'

    instruction_list = read_instructions(DATA_FILEPATH)

    # Part A
    boot_code = BootCode()
    boot_code.load_instructions(instruction_list)
    infinite_loop = False
    while not infinite_loop:
        infinite_loop = boot_code.run_next_instruction()

    print('Part A - Accumulator Value:', boot_code.accumulator)

    # Part B
    for index, instruction in enumerate(instruction_list):
        new_instruction_list = instruction_list.copy()

        op, arg = instruction.split(' ')
        if op == 'jmp':
            new_instruction_list[index] = f'nop {arg}'
        elif op == 'nop':
            new_instruction_list[index] = f'jmp {arg}'

        boot_code = BootCode()
        boot_code.load_instructions(new_instruction_list)

        infinite_loop = False
        while not infinite_loop:
            infinite_loop = boot_code.run_next_instruction()
