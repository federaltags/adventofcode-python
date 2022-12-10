# Advent of code Year 2022 Day 8 solution
# Author = ?
# Date = December 2021

from module import Grid, Row, Column

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def __add_to_list__(list, index, tree):
    if index < len(list):
        list[index].append(int(tree))
    else:
        list.append([int(tree)])

def __parse_grid__():
    trees_in_rows = []
    trees_in_columns = []

    for row_number, row in enumerate(input.splitlines()):
        for column_number, tree in enumerate(row):
            __add_to_list__(trees_in_rows, row_number, tree)
            __add_to_list__(trees_in_columns, column_number, tree)

    rows = []
    for trees_in_row in trees_in_rows:
        rows.append(Row(trees_in_row))

    columns = []
    for trees_in_column in trees_in_columns:
        columns.append(Column(trees_in_column))

    grid = Grid(rows, columns)
    return grid

grid = __parse_grid__()

def part1():    
    return grid.number_of_visible_trees()

def part2():
    return grid.highest_scenic_score()

print("Part One : "+ str(part1()))
print("Part Two : "+ str(part2()))