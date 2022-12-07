from dataclasses import dataclass


@dataclass
class Stacks:
    stacks: dict

    def move(self, number, from_stack, to_stack):
        new_stacks = self.stacks

        for i in range(0, number):
            move = new_stacks[from_stack].pop()
            new_stacks[to_stack].append(move)

        return Stacks(new_stacks)

    def tops(self):
        return ''.join(list(stack[-1] for stack in self.stacks.values()))