# Advent of code Year 2022 Day 17 solution
# Author = ?
# Date = December 2021

from module import Move, Grid

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def part1():
    moves = [Move(move_string) for move_string in [*input]]
    return max(Grid.get_top_row_after_drops(2022, moves))

print("Part One : "+ str(part1()))



print("Part Two : "+ str(None))