"""Advent of Code - Problem 4"""

import re


class Passport():
    """Class to store passport info and validate passport."""
    all_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    required_fields = all_fields[:-1]

    def __init__(self, passport_dict):
        for key, val in passport_dict.items():
            if val and key in ['byr', 'iyr', 'eyr']:
                val = int(val)
            setattr(self, key, val)

    def validate_part_a(self):
        """Validate passport (Part A). Returns a boolean value, False for an
        invalid passport, True for a valid passport"""
        for req_field in self.required_fields:
            if not getattr(self, req_field):
                return False
        return True

    def validate_part_b(self):
        """Validate passport (Part B). Returns a boolean value, False for an
        invalid passport, True for a valid passport"""
        if not self.validate_part_a():
            return False

        if (self.byr_is_valid()
            and self.iyr_is_valid()
            and self.eyr_is_valid()
            and self.hgt_is_valid()
            and self.hcl_is_valid()
            and self.ecl_is_valid()
            and self.pid_is_valid()):
            return True

        return False

    def byr_is_valid(self):
        return 1920 <= self.byr <= 2002

    def iyr_is_valid(self):
        return 2010 <= self.iyr <= 2020

    def eyr_is_valid(self):
        return 2020 <= self.eyr <= 2030

    def hgt_is_valid(self):
        if self.hgt.endswith('cm'):
            height = int(self.hgt[:-2])
            return 150 <= height <= 193
        elif self.hgt.endswith('in'):
            height = int(self.hgt[:-2])
            return 59 <= height <= 76
        return False

    def hcl_is_valid(self):
        pattern = r'^#[0-9a-f]{6}$'
        is_valid = re.match(pattern, self.hcl)
        return is_valid

    def ecl_is_valid(self):
        return self.ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def pid_is_valid(self):
        pattern = r'^[0-9]{9}$'
        is_valid = re.match(pattern, self.pid)
        return is_valid


def read_all_passport_data(filepath):
    """Parse passport data. Returns a list of passports."""
    with open(filepath, 'r') as infile:
        passport_data_chunks = infile.read().split('\n\n')

    passports = []
    for passport_data_chunk in passport_data_chunks:
        passport_dict = {field: None for field in Passport.all_fields}
        key_val_pairs = passport_data_chunk.split()
        for key_val_pair in key_val_pairs:
            key, val = key_val_pair.split(':')
            assert key in passport_dict
            passport_dict[key] = val
        passport = Passport(passport_dict)
        passports.append(passport)

    return passports


def validate_list_of_passports(passports, part_a=False):
    """Check each passport for all required fields. Returns a list of boolean
    values (in same order as input passports)."""
    is_valid_list = []
    for passport in passports:
        if part_a:
            is_valid = passport.validate_part_a()
        else:
            is_valid = passport.validate_part_b()
        is_valid_list.append(is_valid)
    return is_valid_list


if __name__ == '__main__':
    INPUT_DATA_FILEPATH = '4.txt'

    passport_data = read_all_passport_data(INPUT_DATA_FILEPATH)
    valid_list_a = validate_list_of_passports(passport_data, part_a=True)

    print("Part A:", sum(valid_list_a))

    valid_list_b = validate_list_of_passports(passport_data, part_a=False)

    print("Part B:", sum(valid_list_b))
