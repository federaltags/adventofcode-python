# Advent of code Year 2022 Day 6 solution
# Author = ?
# Date = December 2021

from module import Datastream


with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def part1():
    return Datastream(input).start_of_packet_marker()

def part2():
    return Datastream(input).start_of_message_marker()

print("Part One : "+ str(part1()))
print("Part Two : "+ str(part2()))