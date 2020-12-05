"""Advent of Code - Problem 5"""


class BoardingPass():
    """Store boarding pass code and parsed seat location information."""

    def __init__(self, seat_code):
        self.seat_code = seat_code
        self.row, self.col = self._parse_seat_code()
        self.id = self._calculate_id()

    def _parse_seat_code(self):
        """Convert binary space partitioning code to row and column number."""
        # Write in binary form
        row_bin = self.seat_code[:7].replace('F', '0').replace('B', '1')
        col_bin = self.seat_code[7:].replace('L', '0').replace('R', '1')

        # Convert from binary to decimal
        row = int(row_bin, 2)
        col = int(col_bin, 2)

        return row, col

    def _calculate_id(self):
        """Calculate seat ID."""
        return self.row * 8 + self.col


def read_and_parse_boarding_pass_data(filepath):
    """Read and parse boarding pass data."""
    with open(filepath, 'r') as infile:
        lines = infile.readlines()

    boarding_passes = []
    for line in lines:
        seat_code = line.strip()
        boarding_pass = BoardingPass(seat_code)
        boarding_passes.append(boarding_pass)

    return boarding_passes


if __name__ == '__main__':
    DATA_FILEPATH = '5.txt'

    boarding_passes = read_and_parse_boarding_pass_data(DATA_FILEPATH)

    # Part A
    highest_id = max([bp.id for bp in boarding_passes])
    print('Part A - Highest ID:', highest_id)

    # Part B
    possible_ids = list(range(128 * 8))
    for bp in boarding_passes:
        possible_ids.remove(bp.id)
    # Remove front IDs
    prev_id = -1
    for index, possible_id in enumerate(possible_ids):
        if possible_id == prev_id + 1:
            prev_id = possible_id
        else:
            possible_ids = possible_ids[index:]
            break
    # Remove back IDs
    prev_id = 1024
    for index, possible_id in enumerate(possible_ids[::-1]):
        if possible_id == prev_id - 1:
            prev_id = possible_id
        else:
            possible_ids = possible_ids[:-index]
            break
    # Should only be one ID left
    assert len(possible_ids) == 1
    print('Part B - Final Remaining ID:', possible_ids[0])
