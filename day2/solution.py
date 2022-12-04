#!/usr/bin/env python3

# Day 2: Rock Paper Scissors -> https://adventofcode.com/2022/day/2

import os
import sys


filepath = os.path.join(sys.path[0], "puzzle_input.txt")

with open(filepath, 'r') as file:
    puzzle_data = file.readlines()


# Part1: What would your total score be if everything goes exactly according
# to your strategy guide?
MOVE_POINTS = {
    "A": 1,  # rock
    "B": 2,  # paper
    "C": 3  # Scissors
}

END_RESULT_POINTS = {
    "LOSE": 0,
    "DRAW": 3,
    "WIN": 6
}

MAPPING_OF_MOVE = {
    "Y": "B",  # Y = Paper
    "X": "A",  # Y = Rock
    "Z": "C"  # Y = Scissors
}

# Key is a victory move, value is the corresponding defeat move
VICTORIES = {
    "A": "C",  # Rock beats scissors
    "B": "A",  # Paper beats rock
    "C": "B"  # Scissors beats paper
}


def determine_winner(opponent_move: str, my_move: str) -> tuple:
    """
    Determine which of the two moves wins
    """
    my_result = ""
    opponent_result = ""

    defeats = VICTORIES.get(my_move)
    if opponent_move == my_move:
        my_result = "DRAW"
        opponent_result = "DRAW"
    elif opponent_move in defeats:
        my_result = "WIN"
        opponent_result = "LOSE"
    else:
        my_result = "LOSE"
        opponent_result = "WIN"

    return my_result, opponent_result


def calculate_points(win_status: str, move: str) -> int:
    """Calculate the end results depending on the move and if the result was WIN, LOSE or DRAW"""
    result_points = END_RESULT_POINTS.get(win_status)
    move_points = MOVE_POINTS.get(move)

    return result_points + move_points


my_total_points = 0
for data in puzzle_data:
    cleaned_data = data.replace(" ", "")
    opponent_move = cleaned_data[0]
    my_move = cleaned_data[1]
    my_move = MAPPING_OF_MOVE[my_move]
    my_result, opponent_result = determine_winner(opponent_move, my_move)

    my_points = calculate_points(my_result, my_move)
    my_total_points += my_points

print(my_total_points)


# Part2: Following the Elf's instructions for the second column
# what would your total score be if everything goes exactly according to your strategy guide?
MAPPING_OF_RESULTS = {
    "Y": "DRAW",
    "X": "LOSE",
    "Z": "WIN"
}


def determine_move(expected_end_result: str) -> str:
    """Depending on what the result should be determine which move should be made"""
    if expected_end_result == "DRAW":
        # my move should be the same as the opponent
        move = opponent_move
    elif expected_end_result == "LOSE":
        # my move should be the value in VICTORIES of a victory move for my opponent
        move = VICTORIES.get(opponent_move)
    else:
        # on the contrary, my move should be the key in VICTORIES corresponding to my opponent value
        move = [k for k, v in VICTORIES.items() if v == opponent_move][0]

    return move


my_total_points = 0
for data in puzzle_data:
    cleaned_data = data.replace(" ", "")
    opponent_move = cleaned_data[0]
    expected_end_result = MAPPING_OF_RESULTS.get(cleaned_data[1])

    my_move = determine_move(expected_end_result)
    my_points = calculate_points(expected_end_result, my_move)
    my_total_points += my_points

print(my_total_points)
