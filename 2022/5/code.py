# Advent of code Year 2022 Day 5 solution
# Author = ?
# Date = December 2021

import re
from module import Stacks


with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def part1():
    parts = input.split('\n\n')

    stacks = parse_stack(parts[0])
    instructions = parse_instructions(parts[1])

    for instruction in instructions:
        stacks = stacks.move(instruction[0], instruction[1], instruction[2])

    return stacks.tops()

def part2():
    parts = input.split('\n\n')

    stacks = parse_stack(parts[0])
    instructions = parse_instructions(parts[1])

    for instruction in instructions:
        stacks = stacks.move_9001(instruction[0], instruction[1], instruction[2])

    return stacks.tops()

def parse_instructions(instructions_string):
    instructions = []
    for line in instructions_string.splitlines():
        number, from_stack, to_stack = re.search(r"(\d+).*(\d).*(\d)", line).groups()
        instructions.append((int(number), int(from_stack), int(to_stack)))
    return instructions

def parse_stack(stack_string):
    stacks_lines = stack_string.splitlines();
    stacks_lines.reverse()

    all_stacks = {}
    line_length = len(stacks_lines[0])
    for i in range(1, line_length, 4):
        index = int(stacks_lines[0][i])
        all_stacks[index] = []

    for stack_line in stacks_lines[1:]:
        index = 1
        for i in range(1, line_length, 4):
            value = stack_line[i]

            if value != ' ':
                all_stacks[index].append(value)

            index += 1

    stacks = Stacks(all_stacks)
    return stacks
    
print("Part One : "+ str(part1()))
print("Part Two : "+ str(part2()))