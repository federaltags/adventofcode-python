import unittest

from module import Ranges

class Day4Test(unittest.TestCase):
   
    def test_contained_ranges(self):
        self.assertFalse(Ranges((0,0),(1,1)).is_contained())
        self.assertTrue(Ranges((1,1),(1,1)).is_contained())
        self.assertTrue(Ranges((1,1),(1,2)).is_contained())
        self.assertTrue(Ranges((1,2),(1,1)).is_contained())
        self.assertTrue(Ranges((3,80),(4,80)).is_contained())
        
    def test_overlapping_ranges(self):
        self.assertFalse(Ranges((0,0),(1,1)).is_overlapping())
        self.assertTrue(Ranges((1,1),(1,1)).is_overlapping())
        self.assertTrue(Ranges((1,1),(1,2)).is_overlapping())
        self.assertTrue(Ranges((1,2),(1,1)).is_overlapping())
        self.assertTrue(Ranges((3,80),(4,80)).is_overlapping())

        self.assertTrue(Ranges((1,5),(4,8)).is_overlapping())


  
if __name__ == '__main__':
    unittest.main()