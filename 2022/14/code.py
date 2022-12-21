# Advent of code Year 2022 Day 14 solution
# Author = ?
# Date = December 2021

from module import Cave

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def to_point(point_string):
    x_string,y_string = point_string.split(',')
    return (int(x_string),int(y_string))

def lines(points_string: list[str]):
    lines = []

    line_edges = list(map(to_point, points_string))

    for i in range(0, len(line_edges)-1):
        lines += points_in_line(line_edges[i], line_edges[i+1])
    
    return lines

def points_in_line(from_point, to_point):
    if from_point[0] > to_point[0]:
        x_range = range(to_point[0], from_point[0] + 1)
    else:
        x_range = range(from_point[0], to_point[0] + 1)

    if from_point[1] > to_point[1]:
        y_range = range(to_point[1], from_point[1] + 1)
    else:
        y_range = range(from_point[1], to_point[1] + 1)

    points = []
    for x in x_range:
        for y in y_range:
            points.append((x,y))

    return points


def part1():
    structure_points = set()
    for line in input.splitlines():
        structure_points.update(lines(line.split(" -> ")))
    
    cave = Cave(list(structure_points))
    cave.drop_from_until_falling_from_abyss()
    return cave.number_of_resting_grains_of_sands()

print("Part One : "+ str(part1()))



print("Part Two : "+ str(None))