# Advent of code Year 2022 Day 4 solution
# Author = ?
# Date = December 2021

import re
from module import Ranges

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def get_ranges():
    ranges = []
    for line in input.splitlines():
        range_edges = (list(map(int, re.search(r"(\d+)-(\d+),(\d+)-(\d+)", line).groups())))

        ranges.append(Ranges((range_edges[0], range_edges[1]), (range_edges[2], range_edges[3])))
    
    return ranges

def part1():
    ranges = get_ranges()
    return len(list(r for r in ranges if r.is_contained()))


def part2():
    ranges = get_ranges()
    return len(list(r for r in ranges if r.is_overlapping()))

print("Part One : "+ str(part1()))



print("Part Two : "+ str(part2()))