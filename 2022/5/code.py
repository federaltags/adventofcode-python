# Advent of code Year 2022 Day 5 solution
# Author = ?
# Date = December 2021

import re
from module import Stacks


with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def part1():
    parts = input.split('\n\n')

    stacks_lines = parts[0].splitlines();
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

    #print(stacks)
    for line in parts[1].splitlines():
        number, from_stack, to_stack = re.search(r"(\d+).*(\d).*(\d)", line).groups()
        
        #print(number, from_stack, to_stack)
        stacks = stacks.move(int(number), int(from_stack), int(to_stack))

        #print(stacks)

    return stacks.tops()
    
print("Part One : "+ str(part1()))



print("Part Two : "+ str(None))