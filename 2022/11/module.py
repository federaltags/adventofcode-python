from abc import abstractmethod
from dataclasses import dataclass

class Operation:
    @abstractmethod
    def execute(self, worry_level):
        pass

@dataclass
class Addition(Operation):
    to_add: int

    def execute(self, worry_level):
        result = worry_level + self.to_add
        # print(f'\t\tWorry level increases by {self.to_add} to {result}.')
        return result

@dataclass
class Multiplication(Operation):
    multiplier: int
    
    def execute(self, worry_level):
        result = worry_level * self.multiplier
        # print(f'\t\tWorry level is multiplied by {self.multiplier} to {result}.')
        return result

@dataclass
class Square(Operation):
    def execute(self, worry_level):
        result = worry_level * worry_level
        # print(f'\t\tWorry level is multiplied by itself to {result}.')
        return result


@dataclass
class Monkey:
    items: list[int]
    operation: Operation
    test_divisor: int
    if_true_throw_to: int
    if_false_throw_to: int
    inspected_items = 0

    def __is_applicable(self, worry_level):
        return worry_level % self.test_divisor == 0

    def inspect(self, less_worry_divisor) -> tuple[int,int]:
        worry_level = self.items.pop(0)
        # print(f'\tMonkey inspects an item with a worry level of {worry_level}.')
        self.inspected_items += 1

        worry_level = self.operation.execute(worry_level)
        worry_level = worry_level // less_worry_divisor
        # print(f'\t\tMonkey gets bored with item. Worry level is divided by 3 to {worry_level}.')

        return (worry_level, self.if_true_throw_to if self.__is_applicable(worry_level) else self.if_false_throw_to)

    def has_items(self):
        return len(self.items) != 0

    def add(self, item):
        self.items.append(item)

@dataclass
class Game:
    monkeys: list[Monkey]

    def total_monkey_business(self, number_of_rounds = 20, less_worry_divisor=3):
        lowest_common_factor = 1
        for monkey in self.monkeys:
            lowest_common_factor *= monkey.test_divisor

        for round in range(1,number_of_rounds + 1):
            for i, monkey in enumerate(self.monkeys):
                # print(f'Monkey {i}:')
                while monkey.has_items():
                    item, to_monkey = monkey.inspect(less_worry_divisor)

                    # print(f'\t\tItem with worry level {item} is thrown to monkey {to_monkey}.')
                    to_monkey = self.monkeys[to_monkey]
                    to_monkey.add(item % lowest_common_factor)

            # print(f'\nAfter round {round}, the monkeys are holding items with these worry levels:')
            # for i, monkey in enumerate(self.monkeys):
                # print(f'Monkey {i}: {monkey.items}')

        inspected_items = list(sorted(map(lambda monkey: monkey.inspected_items, self.monkeys)))
        return inspected_items[-1] * inspected_items[-2]