import unittest
from module import Input, RoundPart2, Outcome
  
class GameRoundTest(unittest.TestCase):

    def test_loss(self):
        self.assertEqual(RoundPart2(Input.SCISSORS, Outcome.LOSS).score(), Input.PAPER.value + Outcome.LOSS.value)
        self.assertEqual(RoundPart2(Input.PAPER, Outcome.LOSS).score(), Input.ROCK.value + Outcome.LOSS.value)
        self.assertEqual(RoundPart2(Input.ROCK, Outcome.LOSS).score(), Input.SCISSORS.value + Outcome.LOSS.value)

    def test_draw(self):
        self.assertEqual(RoundPart2(Input.SCISSORS, Outcome.DRAW).score(), Input.SCISSORS.value + Outcome.DRAW.value)
        self.assertEqual(RoundPart2(Input.PAPER, Outcome.DRAW).score(), Input.PAPER.value + Outcome.DRAW.value)
        self.assertEqual(RoundPart2(Input.ROCK, Outcome.DRAW).score(), Input.ROCK.value + Outcome.DRAW.value)

    def test_win(self):
        self.assertEqual(RoundPart2(Input.SCISSORS, Outcome.WIN).score(), Input.ROCK.value + Outcome.WIN.value)
        self.assertEqual(RoundPart2(Input.PAPER, Outcome.WIN).score(), Input.SCISSORS.value + Outcome.WIN.value)
        self.assertEqual(RoundPart2(Input.ROCK, Outcome.WIN).score(), Input.PAPER.value + Outcome.WIN.value)

if __name__ == '__main__':
    unittest.main()