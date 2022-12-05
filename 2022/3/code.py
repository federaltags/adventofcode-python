from module import RuckSack

# Advent of code Year 2022 Day 3 solution
# Author = ?
# Date = December 2021

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def part_1(input):
    sum = 0

    for line in input.split('\n'):
        n = len(line)
        rucksack = RuckSack(line[0:n//2], line[n//2:])

        sum += rucksack.priority()

    return sum

print("Part One : "+ str(part_1(input)))



print("Part Two : "+ str(None))