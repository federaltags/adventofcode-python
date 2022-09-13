# Advent of code Year 2015 Day 1 solution
# Author = ?
# Date = December 2021

from cgi import print_arguments

def part1(input):
    return input.count('(') - input.count(')')

def part2(input):
    floor = 0
    for i, c in enumerate(input, 1):
        floor += 1 if c == '(' else -1

        if floor < 0:
            return i

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

    

print("Part One : "+ str(part1(input)))



print("Part Two : "+ str(part2(input)))


