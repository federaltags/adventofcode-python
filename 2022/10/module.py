from abc import abstractmethod
from dataclasses import dataclass

class Instruction:
    @abstractmethod
    def execute(self, cycle):
        pass

@dataclass
class Program:
    instructions: list[Instruction] 

    def calculate_for_cycles(self, cycles_to_calculate):
        x = 1
        cycle = 1

        to_perform = {}

        total = 0
        for cycle in range(1, cycles_to_calculate[-1]+1):
            # start instruction if non is running
            if (cycle not in to_perform.keys()) & (len(self.instructions) > 0):
                future_cycle, to_add = self.instructions.pop(0).execute(cycle)
                to_perform[future_cycle] = to_perform.get(future_cycle, 0) + to_add

            # return value
            if (cycle in cycles_to_calculate):
                print(f'{cycle}:{cycle * x}')
                total += (cycle * x)

            # perform finished instruction
            x += to_perform.get(cycle, 0)

        return total

@dataclass
class Noop(Instruction):
    def execute(self, cycle):
        return (cycle, 0)

@dataclass
class AddX(Instruction):
    value: int

    def execute(self, cycle):
        return (cycle+1, self.value)
