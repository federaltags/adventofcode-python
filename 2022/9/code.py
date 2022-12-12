# Advent of code Year 2022 Day 9 solution
# Author = ?
# Date = December 2021

from module import State,Snake,Move,Location

LOCATION_P0_P0 = Location(0,0)
START = Snake([LOCATION_P0_P0] * 2, [LOCATION_P0_P0])

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def part1():
    state = START

    for command_line in input.splitlines():
        move_string, amount_string = command_line.split(' ')

        move = Move(move_string)
        amount = int(amount_string)

        for i in range(amount):
            state = state.move(move)

    return state.number_of_locations_tail_visited()

print("Part One : "+ str(part1()))



print("Part Two : "+ str(None))