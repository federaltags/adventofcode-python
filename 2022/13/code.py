# Advent of code Year 2022 Day 13 solution
# Author = ?
# Date = December 2021

from module import Pair

PAIR_WITH_2 = Pair([[2]])
PAIR_WITH_6 = Pair([[6]])

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def part1():
    return sum(i for i, (l, r) in enumerate(parse_pairs_tuples(), 1) if l.is_in_order_with(r))

def part2():
    pairs = sorted(parse_pairs() + [PAIR_WITH_2,PAIR_WITH_6])
    return ((pairs.index(PAIR_WITH_2) + 1) * (pairs.index(PAIR_WITH_6) + 1)) 

def parse_pairs_tuples():
    pairs = []
    for pairs_string in input.split('\n\n'):
        pair1_string, pair2_string = pairs_string.splitlines()
        pairs.append((Pair(eval(pair1_string)), Pair(eval(pair2_string))))
    return pairs

def parse_pairs():
    pairs = []
    for line in input.splitlines():
        if line:
            pairs.append(Pair(eval(line)))

    return pairs

print("Part One : "+ str(part1()))
print("Part Two : "+ str(part2()))