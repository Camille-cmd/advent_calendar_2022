#!/usr/bin/env python3

# Day 8: Treetop Tree House -> https://adventofcode.com/2022/day/8

from functools import reduce
from operator import mul

from pathlib import Path

filepath = Path(Path(__file__).parent.absolute(), "puzzle_input.txt")
with open(filepath, 'r') as file:
    puzzle_data = file.read().splitlines()


def calculate_scenic_score(neighbour_trees_list, current_tree):
    # Start with the highest possible score, in case no tree blocking the current_tree
    score = len(neighbour_trees_list)
    for tree_position, tree in enumerate(neighbour_trees_list):
        # A tree is blocking, we stop at its position
        if tree >= current_tree:
            score = tree_position + 1
            break

    return score


def is_tree_visible(neighbour_trees_list, current_tree):
    # If our current_tree has only smaller trees around, it is visible
    return all(tree < current_tree for tree in neighbour_trees_list)


count_visible_trees = 0
up_rows = []
scenic_scores = []
for i in range(1, len(puzzle_data) - 1):
    up_row = puzzle_data[i - 1]
    up_rows.append(up_row)

    down_row = puzzle_data[i + 1]

    # On the edge all trees are visible
    if i == 1:
        # all top trees are visible
        for tree in up_row:
            count_visible_trees += 1

    if i == len(puzzle_data) - 2:
        # all down trees are visible
        for tree in down_row:
            count_visible_trees += 1

    # Check trees for the current row
    current_row = puzzle_data[i]
    for index, current_tree in enumerate(current_row):
        # All trees on the extremis are visible
        if index == 0 or index == len(current_row) - 1:
            count_visible_trees += 1
        else:
            left_trees = [tree for tree in current_row[:index]]
            right_trees = [tree for tree in current_row[index + 1:]]
            up_trees = [up_row[index] for up_row in up_rows]
            down_rows = puzzle_data[i + 1:]
            down_trees = [up_row[index] for up_row in down_rows]

            # Part 1: how many trees are visible from outside the grid?
            neighbour_trees = [up_trees, left_trees, down_trees, right_trees]
            for neighbour_trees_list in neighbour_trees:
                visible = is_tree_visible(neighbour_trees_list, current_tree)
                if visible:
                    count_visible_trees += 1
                    break

            # Part 2: What is the highest scenic score possible for any tree?
            # We need to check trees closest to our current tree first
            left_trees.reverse()
            up_trees.reverse()
            neighbour_trees = [up_trees, left_trees, down_trees, right_trees]

            scenic_score = []
            for neighbour_trees_list in neighbour_trees:
                scenic_score.append(
                    calculate_scenic_score(neighbour_trees_list, current_tree)
                )
            # end result, multiply each value of each neighbour list
            scenic_scores.append(reduce(mul, scenic_score))


print(f"Trees visible from outside: {count_visible_trees}")
print(f"Highest scenic score possible: {max(scenic_scores)}")
