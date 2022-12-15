# Advent of code Year 2022 Day 11 solution
# Author = ?
# Date = December 2021

from module import Monkey, Multiplication, Addition, Square, Game

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()


def to_items(items_string: str) -> list[int]:
    _, list_string = items_string.strip().split("Starting items: ")
    return list(map(lambda str: int(str), list_string.split(',')))


def to_operation(operation_string: str):
    if "old * old" in operation_string:
        return Square()
    elif "*" in operation_string:
        multiplier_string = operation_string.split('* ')[1]
        return Multiplication(int(multiplier_string))
    elif "+" in operation_string:
        to_add_string = operation_string.split('+ ')[1]
        return Addition(int(to_add_string))


def to_test_divisor(test_string: str) -> int:
    divisor_string = test_string.split('  Test: divisible by ')[1]
    return int(divisor_string)


def if_true_monkey(true_monkey_string: str) -> int:
    return int(true_monkey_string.split('    If true: throw to monkey ')[1])


def if_false_monkey(false_monkey_string: str) -> int:
    return int(false_monkey_string.split('    If false: throw to monkey ')[1])


def to_monkey(monkey_string) -> Monkey:
    lines = monkey_string.splitlines()
    return Monkey(
        to_items(lines[1]),
        to_operation(lines[2]),
        to_test_divisor(lines[3]),
        if_true_monkey(lines[4]),
        if_false_monkey(lines[5])
    )

def get_game():
    monkeys = []
    for monkey_string in input.split('\n\n'):
        monkeys.append(to_monkey(monkey_string))

    game = Game(monkeys)
    return game

def part1():
    game = get_game()
    return game.total_monkey_business()

def part2():
    game = get_game()
    return game.total_monkey_business(number_of_rounds=10000,less_worry_divisor=1)

print("Part One : " + str(part1()))


print("Part Two : " + str(part2()))
