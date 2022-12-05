from enum import Enum
from dataclasses import dataclass
from module import Input, Outcome, RoundPart1,  RoundPart2

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

outcomes = {
    'X': Outcome.LOSS,
    'Y': Outcome.DRAW,
    'Z': Outcome.WIN
}

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def part_1():
    score = 0

    for game_line in input.split('\n'):
        split = game_line.split(' ')

        round = RoundPart1(player_mapping[split[1]], opponent_mapping[split[0]])

        score += round.score()

    return score

def part_2():
    score = 0

    for game_line in input.split('\n'):
        split = game_line.split(' ')

        round = RoundPart2(opponent_mapping[split[0]], outcomes[split[1]])

        score += round.score()

    return score

print("Part One : "+ str(part_1()))

print("Part Two : "+ str(part_2()))