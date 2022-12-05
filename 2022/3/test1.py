import unittest
from module import RuckSack 

class Compartments(unittest.TestCase):
   
    def test_scissors(self):
        self.assertEqual(RuckSack('b', 'c').priority(), 0)

        self.assertEqual(RuckSack('a', 'a').priority(), 1)
        self.assertEqual(RuckSack('b', 'b').priority(), 2)
        
        self.assertEqual(RuckSack('A', 'A').priority(), 27)
        self.assertEqual(RuckSack('B', 'B').priority(), 28)
  
if __name__ == '__main__':
    unittest.main()