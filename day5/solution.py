#!/usr/bin/env python3

# Day 5: Supply Stacks -> https://adventofcode.com/2022/day/5

import os
import sys

filepath = os.path.join(sys.path[0], "puzzle_input.txt")

with open(filepath, 'r') as file:
    puzzle_data = file.read().splitlines()

# Separate instructions from stacks
instructions = []
stacks_transposed = []
for line in puzzle_data:
    if line.startswith("move"):
        instructions.append([int(x) for x in line.split() if x.isdigit()])
    elif line.startswith(" "):
        continue
    elif not line:
        continue
    else:
        # Each stack is 4 char long (1 space and [] and the letter (or space if empty))
        stacks_transposed.append(list(line[1:][::4]))

# Create a stack dict
stacks = {}
for stack_line in stacks_transposed[::-1]:
    for index, crate in enumerate(stack_line):
        if crate == " ":
            continue
        if index + 1 not in stacks:
            stacks[index + 1] = []
        stacks[index + 1].append(crate)

for instruction in instructions:
    nb_to_move, crate_from, crate_to = instruction

    source_crate = stacks[crate_from]
    destination_crate = stacks[crate_to]
    # take out last n elements and delete them
    moving_elements = source_crate[-nb_to_move:]
    del source_crate[-nb_to_move:]

    moving_elements.reverse()

    # add elements to destinations
    destination_crate.extend(moving_elements)

# Part1: After the rearrangement procedure completes, what crate ends up on top of each stack?
end_result = []
for stack in stacks.values():
    end_result.append(stack[-1])

print("".join(end_result))

# Part 2 is the same without moving_elements.reverse()
