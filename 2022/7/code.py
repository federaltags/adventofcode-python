# Advent of code Year 2022 Day 7 solution
# Author = ?
# Date = December 2021

from module import CommandRunner


with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def part1():
    return CommandRunner().run_for_directories(input.splitlines()).sum_of_big_directory_sizes()

def part2():
    return CommandRunner().run_for_directories(input.splitlines()).size_of_smallest_dir_to_delete()

print("Part One : "+ str(part1()))
print("Part Two : "+ str(part2()))