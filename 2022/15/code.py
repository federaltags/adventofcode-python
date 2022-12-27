# Advent of code Year 2022 Day 15 solution
# Author = ?
# Date = December 2021

import re
from module import Point, SensorGrid

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def part1():
    return parse_sensors().number_of_positions_that_cannot_be_a_beacon(2_000_000)

def part2():
    return parse_sensors().tuning_frequency(4_000_000)

def parse_sensors():
    sensors = {}
    for line in input.splitlines():
        sensor_x_string, sensor_y_string, beacon_x_string, beacon_y_string = re.compile(r'Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)').search(line).groups()
        sensors[Point(int(sensor_x_string), int(sensor_y_string))] = Point(int(beacon_x_string), int(beacon_y_string))

    sensors = SensorGrid(sensors)
    return sensors



print("Part One : "+ str(part1()))
print("Part Two : "+ str(part2()))