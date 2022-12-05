from enum import Enum
from dataclasses import dataclass
from module import Input, Round

# Advent of code Year 2022 Day 2 solution
# Author = ?
# Date = December 2021

opponent_mapping = {
    'A': Input.ROCK,
    'B': Input.PAPER,
    'C': Input.SCISSORS
}

player_mapping = {
    'X': Input.ROCK,
    'Y': Input.PAPER,
    'Z': Input.SCISSORS
}

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def part_1():
    score = 0

    for game_line in input.split('\n'):
        split = game_line.split(' ')

        print(game_line)
        round = Round(player_mapping[split[1]], opponent_mapping[split[0]])

        score += round.score()

    return score



print("Part One : "+ str(part_1()))


print("Part Two : "+ str(None))