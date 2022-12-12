# Advent of code Year 2022 Day 9 solution
# Author = ?
# Date = December 2021

from module import Snake,Move,Location

LOCATION_P0_P0 = Location(0,0)

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def parse_commands():
    commands = []
    for command_line in input.splitlines():
        move_string, amount_string = command_line.split(' ')

        commands.append((Move(move_string), int(amount_string)))

    return commands

def part1():
    snake = Snake([LOCATION_P0_P0] * 2, [LOCATION_P0_P0])

    for move,amount in parse_commands():
        for i in range(amount):
            snake = snake.move(move)

    return snake.number_of_locations_tail_visited()

def part2():
    snake = Snake([LOCATION_P0_P0] * 10, [LOCATION_P0_P0])

    for move,amount in parse_commands():
        for i in range(amount):
            snake = snake.move(move)

    return snake.number_of_locations_tail_visited()

print("Part One : "+ str(part1()))
print("Part Two : "+ str(part2()))