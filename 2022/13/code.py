# Advent of code Year 2022 Day 13 solution
# Author = ?
# Date = December 2021

from module import Pair

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def part1():
    pairs = []
    for pairs_string in input.split('\n\n'):
        pair1_string, pair2_string = pairs_string.splitlines()
        pairs.append((Pair(eval(pair1_string)), Pair(eval(pair2_string))))

    sum = 0
    for index, pair in enumerate(pairs):
        first_pair, second_pair = pair

        if first_pair.is_in_order_with(second_pair):
            sum = sum + (index+1)
        
    return sum

print("Part One : "+ str(part1()))



print("Part Two : "+ str(None))