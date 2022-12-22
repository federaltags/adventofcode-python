# Advent of code Year 2022 Day 15 solution
# Author = ?
# Date = December 2021

import re
from module import Sensor, Sensors

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def part1():
    sensors = []
    for line in input.splitlines():
        sensor_x_string, sensor_y_string, beacon_x_string, beacon_y_string = re.compile(r'Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)').search(line).groups()
        sensors.append(Sensor(
            (int(sensor_x_string), int(sensor_y_string)),
            (int(beacon_x_string), int(beacon_y_string)),
        ))

    sensors = Sensors(sensors)
    return sensors.number_of_positions_that_cannot_be_a_beacon(2000000)

print("Part One : "+ str(part1()))



print("Part Two : "+ str(None))