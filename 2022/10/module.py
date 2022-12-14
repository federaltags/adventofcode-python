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
                #print(f'{cycle}:{cycle * x}')
                total += (cycle * x)

            # perform finished instruction
            x += to_perform.get(cycle, 0)

        return total

    def run_to_lines(self) -> list[str]:
        characters = ['.'] * 40 * 6
        x = 1
        cycle = 0

        to_perform = {}

        while(any(to_perform_cycle >= cycle for to_perform_cycle in to_perform.keys()) | (len(self.instructions) != 0)):
            # start instruction if non is running
            if (cycle not in to_perform.keys()) & (len(self.instructions) > 0):
                future_cycle, to_add = self.instructions.pop(0).execute(cycle)
                to_perform[future_cycle] = to_perform.get(future_cycle, 0) + to_add

            # return value
            # print(f'{cycle}:{x}')
            offset_cycle = cycle
            while offset_cycle >= 40:
                offset_cycle -= 40

            if offset_cycle in range(x-1,x+2):
                characters[cycle] = '#'

            # perform finished instruction
            x += to_perform.get(cycle, 0)
            cycle+=1

        return self.__to_lines(characters)

    def __to_lines(self, characters):
        lines = list()

        line_size = 40
        for i in range(0, len(characters), line_size):
            lines.append(''.join(characters[i:i+line_size]))
        
        return lines

@dataclass
class Noop(Instruction):
    def execute(self, cycle):
        return (cycle, 0)

@dataclass
class AddX(Instruction):
    value: int

    def execute(self, cycle):
        return (cycle+1, self.value)
