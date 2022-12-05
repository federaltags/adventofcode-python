from module import RuckSack, ElfGroup

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

def part_2(input):
    lines = input.split('\n')
    splits = [lines[x:x+3] for x in range(0, len(lines), 3)]

    sum = 0
    for split in splits:
        elf_group = ElfGroup(split[0], split[1], split[2])

        sum += elf_group.priority()

    return sum


print("Part One : "+ str(part_1(input)))
print("Part Two : "+ str(part_2(input)))