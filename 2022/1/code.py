from cProfile import label
from dataclasses import dataclass
from operator import countOf
from queue import Empty
from typing import List

# Advent of code Year 2022 Day 1 solution
# Author = ?
# Date = December 2021

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

@dataclass
class Elf:
    calories: List[int]

    def total_calories(self): 
        return sum(self.calories)

def parse_elfs(input): 
    elfs = []
    calories = []
    for line in input.split('\n'):
        if line == "":
            elfs.append(Elf(calories))
            calories = []
        else:
            calories.append(int(line))

    return elfs

def part1(input):
    elfs = parse_elfs(input)
    return str(max(list(map(lambda elf: elf.total_calories(), elfs))))

def part2(input):
    elfs = parse_elfs(input)
    sorted_categories = list(sorted(map(lambda elf: elf.total_calories(), elfs)))

    return sum(sorted_categories[-3:])

print("Part One : "+ part1(input))

print("Part Two : "+ str(part2(input)))