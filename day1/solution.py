#!/usr/bin/env python3

# Day 1: Calorie Counting -> https://adventofcode.com/2022/day/1

import os
import sys


filepath = os.path.join(sys.path[0], "puzzle_input.txt")

with open(filepath, 'r') as file:
    puzzle_data = file.readlines()

# Part 1: Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
elves_calories = []
calories_count = 0
for line in puzzle_data:
    # Each empty row is a new elf
    if line in ['\n', '\r\n']:
        print("new elf")
        print(f"calories from previous elf: {calories_count}")
        elves_calories.append(calories_count)
        calories_count = 0
    # Otherwise the line is a calories count
    else:
        calories_count += int(line)


print(f"Most calories: {max(elves_calories)}")

# Part 2: Find the top three Elves carrying the most  Calories. How many Calories are those Elves carrying in total?
sorted_elves_calories = sorted(elves_calories, reverse=True)
total_top_three = sum(sorted_elves_calories[0: 3])
print(f"Top three calories: {total_top_three}")
