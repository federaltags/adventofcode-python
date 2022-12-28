# Advent of code Year 2022 Day 16 solution
# Author = ?
# Date = December 2021

import re

from module import Pathing, Valve


with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def part1():
    valves = {}
    for line in input.splitlines():
        valve, flow_rate_string, tunnels_to_string = re.compile(r'Valve (.*) has flow rate=(.*); tunnel[s]? lead[s]? to valve[s]? (.*)').search(line).groups()

        valves[valve] = Valve(valve, int(flow_rate_string), tunnels_to_string.split(', '))
    
    pathing = Pathing(valves)
    return pathing.max_release_pressured()

print("Part One : "+ str(part1()))



print("Part Two : "+ str(None))