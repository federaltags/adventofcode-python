from enum import Enum
from dataclasses import dataclass

class Input(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Outcome(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6

@dataclass
class RoundPart2:
    opponent: Input
    outcome: Outcome

    def score(self):
        if self.outcome == Outcome.DRAW:
            player = self.opponent 
        elif self.outcome == Outcome.WIN:
            if self.opponent == Input.ROCK:
                player = Input.PAPER
            elif self.opponent == Input.PAPER:
                player = Input.SCISSORS
            else:
                player = Input.ROCK
        else:
            if self.opponent == Input.ROCK:
                player = Input.SCISSORS
            elif self.opponent == Input.PAPER:
                player = Input.ROCK
            else:
                player = Input.PAPER

        return self.outcome.value + player.value


@dataclass
class RoundPart1:
    player: Input
    opponent: Input

    def score(self):
        score = self.player.value

        if self.player == self.opponent:
            score += Outcome.DRAW.value
        # wins
        elif (self.player == Input.PAPER) & (self.opponent == Input.ROCK):
            score += Outcome.WIN.value
        elif (self.player == Input.SCISSORS) & (self.opponent == Input.PAPER):
            score += Outcome.WIN.value
        elif (self.player == Input.ROCK) & (self.opponent == Input.SCISSORS):
            score += Outcome.WIN.value

        return score