# Advent of code Year 2022 Day 12 solution
# Author = ?
# Date = December 2021

from module import Grid

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def part1():
    from_square = None
    to_square = None
    squares = {}
    for y, line in enumerate(reversed(input.splitlines())):
        for x, height in enumerate(line):
            if height == 'S':
                from_square = (x,y)
                squares[(x,y)] = 'a'
            elif height == 'E':
                to_square = (x,y)
                squares[(x,y)] = 'z'
            else:
                squares[(x,y)] = height
    
    grid = Grid(squares)
    return grid.shortest_from_to(from_square, to_square)

print("Part One : "+ str(part1()))



print("Part Two : "+ str(None))