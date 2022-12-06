#!/usr/bin/env python3

# Day 6: Tuning Trouble -> https://adventofcode.com/2022/day/6

from collections import Counter
import os
import sys

filepath = os.path.join(sys.path[0], "puzzle_input.txt")

with open(filepath, 'r') as file:
    puzzle_data = file.read()

# puzzle_data = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

# How many characters need to be processed before the first start-of-message marker is detected?
PACKET_SIZE = 14


def split_data(string_data):
    # Split string into a list of PACKET_SIZE elements
    divided_letters = []
    for i in range(len(string_data) - PACKET_SIZE - 1):
        divided_letters.append(string_data[i:i+PACKET_SIZE])

    return divided_letters


for index, group in enumerate(split_data(puzzle_data)):
    # Count letter occurence in the group
    letter_counter = Counter(group)
    no_duplicated_letter = all(
        count == 1 for _, count in letter_counter.items())

    # if none is repeated, then we have our sequence
    if no_duplicated_letter:
        print(index + PACKET_SIZE)
        break
