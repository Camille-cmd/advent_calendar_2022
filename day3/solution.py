#!/usr/bin/env python3

# Day 3: Rucksack Reorganization -> https://adventofcode.com/2022/day/3

import os
import sys
from itertools import zip_longest
import string


filepath = os.path.join(sys.path[0], "puzzle_input.txt")

with open(filepath, 'r') as file:
    puzzle_data = file.readlines()

total = 0
for data in puzzle_data:
    first_half_str = slice(0, len(data)//2)
    second_half_str = slice(len(data)//2, len(data))
    compartment1 = data[first_half_str]
    compartment2 = data[second_half_str]

    common_letter_set = set(compartment1).intersection(compartment2)
    common_letter = common_letter_set.pop()

    # find the index of the letter in the alphabet
    letter_index = string.ascii_letters.index(common_letter) + 1
    total += letter_index

# Part 1: Find the item type that appears in both compartments of each rucksack.
# What is the sum of the priorities of those item types?
print(total)

# Part 2: Find the item type that corresponds to the badges of each three-Elf group.
# What is the sum of the priorities of those item types?
total = 0
# Separate the data in group of 3
args = [iter(puzzle_data)] * 3
for group in zip_longest(*args):
    # Sort the data to have the longest string first
    sorted_group_data = list(sorted(group, key=len, reverse=True))
    group_data = [r.replace("\n", "") for r in sorted_group_data]
    common_letter_set = set(group_data[0]).intersection(group_data[1], group_data[2])
    common_letter = common_letter_set.pop()

    letter_index = string.ascii_letters.index(common_letter) + 1
    total += letter_index

print(total)
