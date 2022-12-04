#!/usr/bin/env python3

# Day 4: Camp Cleanup -> https://adventofcode.com/2022/day/4

import os
import sys


filepath = os.path.join(sys.path[0], "puzzle_input.txt")

with open(filepath, 'r') as file:
    puzzle_data = file.readlines()

double_assignment_count = 0
overlap_assignment_count = 0
for data in puzzle_data:
    # Create a range for each half of the line
    splitted_data = data.split(",")

    first_half = splitted_data[0].split("-")
    first_range = range(int(first_half[0]), int(first_half[1]))

    second_half = splitted_data[1].replace("\n", "").split("-")
    second_range = range(int(second_half[0]), int(second_half[1]))


    """
    PART 1: In how many assignment pairs does one range fully contain the other?
    If start of 1st range is greater that the start of 2nd range
    AND stop of 1st range is lower than the end 2nd range
    The first range is inside the second and vice versa
    """
    first_range_duplicated = first_range.start >= second_range.start and first_range.stop <= second_range.stop
    second_range_duplicated = second_range.start >= first_range.start and second_range.stop <= first_range.stop
    if first_range_duplicated or second_range_duplicated:
        double_assignment_count += 1

    '''
    PART 2: In how many assignment pairs do the ranges overlap?
    If we can create a new range taking the highest start value of both ranges and the lowest stop value
    It means that the ranges have common values
    ex: range(2, 6) range(4, 8) 
    -> highest start: 4, 
    -> lowest stop: 6 (+1), +1 to include the value in the range result (range() exclude last value)
    -> new range: (4, 7) exists, so it is overlapping

    range(2, 4) range(6, 8)
    -> highest start: 6, 
    -> lowest stop: 4 (+1), 
    -> new range: (6, 5) does not exists, so it is not overlapping
    '''
    highest_start = max(first_range.start, second_range.start)
    lowest_stop = min(first_range.stop, second_range.stop) + 1  
    overlapping_range = range(highest_start, lowest_stop)

    if len(overlapping_range):
        overlap_assignment_count += 1

print(f"Double assignment {double_assignment_count}")
print(f"Overlap {overlap_assignment_count}")
