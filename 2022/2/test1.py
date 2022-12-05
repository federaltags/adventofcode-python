import unittest
from module import Input, RoundPart1
  
class GameRoundTest(unittest.TestCase):
   
    def test_scissors(self):
        self.assertEqual(RoundPart1(Input.SCISSORS, Input.PAPER).score(), 3 + 6)
        self.assertEqual(RoundPart1(Input.SCISSORS, Input.SCISSORS).score(), 3 + 3)
        self.assertEqual(RoundPart1(Input.SCISSORS, Input.ROCK).score(), 3 + 0)

    def test_paper(self):
        self.assertEqual(RoundPart1(Input.PAPER, Input.PAPER).score(), 2 + 3)
        self.assertEqual(RoundPart1(Input.PAPER, Input.SCISSORS).score(), 2 + 0)
        self.assertEqual(RoundPart1(Input.PAPER, Input.ROCK).score(), 2 + 6)

    def test_rock(self):
        self.assertEqual(RoundPart1(Input.ROCK, Input.PAPER).score(), 1 + 0)
        self.assertEqual(RoundPart1(Input.ROCK, Input.SCISSORS).score(), 1 + 6)
        self.assertEqual(RoundPart1(Input.ROCK, Input.ROCK).score(), 1 + 3)
  
if __name__ == '__main__':
    unittest.main()