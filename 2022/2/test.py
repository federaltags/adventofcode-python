import unittest
from module import Input, Round
  
class GameRoundTest(unittest.TestCase):
   
    def test_scissors(self):
        self.assertEquals(Round(Input.SCISSORS, Input.PAPER).score(), 3 + 6)
        self.assertEquals(Round(Input.SCISSORS, Input.SCISSORS).score(), 3 + 3)
        self.assertEquals(Round(Input.SCISSORS, Input.ROCK).score(), 3 + 0)

    def test_paper(self):
        self.assertEquals(Round(Input.PAPER, Input.PAPER).score(), 2 + 3)
        self.assertEquals(Round(Input.PAPER, Input.SCISSORS).score(), 2 + 0)
        self.assertEquals(Round(Input.PAPER, Input.ROCK).score(), 2 + 6)

    def test_rock(self):
        self.assertEquals(Round(Input.ROCK, Input.PAPER).score(), 1 + 0)
        self.assertEquals(Round(Input.ROCK, Input.SCISSORS).score(), 1 + 6)
        self.assertEquals(Round(Input.ROCK, Input.ROCK).score(), 1 + 3)
  
if __name__ == '__main__':
    unittest.main()