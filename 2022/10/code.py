# Advent of code Year 2022 Day 10 solution
# Author = ?
# Date = December 2021

from module import AddX, Noop, Program

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def parse_instructions():
    instructions = []

    for line in input.splitlines():
        if line == "noop":
            instructions.append(Noop())
        else:
            instructions.append(AddX(int(line.split(' ')[1])))
    return instructions

def part1():
    instructions = parse_instructions()

    program = Program(instructions)
    return program.calculate_for_cycles([20,60,100,140,180,220])

def part2():
    instructions = parse_instructions()

    program = Program(instructions)
    return '\n' + '\n'.join(program.run_to_lines())

print("Part One : "+ str(part1()))
print("Part Two : "+ str(part2()))