import unittest

from module import Noop, AddX, Program

class Test(unittest.TestCase):


    def test_part1(self):
        self.assertEqual((1 * 1) , Program([Noop(),AddX(3),AddX(-5)]).calculate_for_cycles([1]))
        self.assertEqual((1 * 2), Program([Noop(),AddX(3),AddX(-5)]).calculate_for_cycles([2]))
        self.assertEqual((1 * 3), Program([Noop(),AddX(3),AddX(-5)]).calculate_for_cycles([3]))
        self.assertEqual((4 * 4), Program([Noop(),AddX(3),AddX(-5)]).calculate_for_cycles([4]))
        self.assertEqual((5 * 4), Program([Noop(),AddX(3),AddX(-5)]).calculate_for_cycles([5]))
        self.assertEqual((6 * -1), Program([Noop(),AddX(3),AddX(-5)]).calculate_for_cycles([6]))

        self.assertEqual((1 * 1) + (1 * 2), Program([Noop(),AddX(3),AddX(-5)]).calculate_for_cycles([1,2]))
        self.assertEqual((1 * 2) + (4 * 4), Program([Noop(),AddX(3),AddX(-5)]).calculate_for_cycles([2,4]))

        self.assertEqual(1 * 1, Program([AddX(2),AddX(5)]).calculate_for_cycles([1]))
        self.assertEqual(2 * 1, Program([AddX(2),AddX(5)]).calculate_for_cycles([2]))
        self.assertEqual(3 * 3, Program([AddX(2),AddX(5)]).calculate_for_cycles([3]))
        self.assertEqual(4 * 3, Program([AddX(2),AddX(5)]).calculate_for_cycles([4]))
        self.assertEqual(5 * 8, Program([AddX(2),AddX(5)]).calculate_for_cycles([5]))
    
        
    

if __name__ == '__main__':
    unittest.main()