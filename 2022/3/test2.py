import unittest
from module import ElfGroup

class ElfGroups(unittest.TestCase):
   
    def test_scissors(self):
        self.assertEqual(ElfGroup('a', 'b', 'C').priority(), 0)

        self.assertEqual(ElfGroup('a', 'a', 'a').priority(), 1)
        self.assertEqual(ElfGroup('b', 'b', 'b').priority(), 2)

        self.assertEqual(ElfGroup('A', 'A', 'A').priority(), 27)
        self.assertEqual(ElfGroup('B', 'B', 'B').priority(), 28)
        
  
if __name__ == '__main__':
    unittest.main()