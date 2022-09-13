# Advent of code Year 2015 Day 2 solution
# Author = ?
# Date = December 2021

from functools import partial
import math


def part1(input):
    total = 0
    for line in input.split('\n'):
        l, w, h = map(int, line.split('x'))
        total += 2*l*w + 2*w*h + 2*h*l + math.prod(sorted([l,w,h])[:2])

    return total

def part2(input):
    total = 0
    for line in input.split('\n'):
        l, w, h = map(int, line.split('x'))
        total += (l * w * h) + sum(map(lambda x:x*2, sorted([l,w,h])[:2]))
    return total

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()



print("Part One : "+ str(part1(input)))



print("Part Two : "+ str(part2(input)))