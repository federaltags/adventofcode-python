from enum import Enum
from dataclasses import dataclass

class Input(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

@dataclass
class Round:
    player: Input
    opponent: Input

    def score(self):
        print(self)
        score = self.player.value

        if self.player == self.opponent:
            print('draw')
            score += 3
        # wins
        elif (self.player == Input.PAPER) & (self.opponent == Input.ROCK):
            print('paper beats rock')
            score += 6
        elif (self.player == Input.SCISSORS) & (self.opponent == Input.PAPER):
            print('scissors beats paper')
            score += 6
        elif (self.player == Input.ROCK) & (self.opponent == Input.SCISSORS):
            print('rock beats scissors')
            score += 6

        print(score)

        return score