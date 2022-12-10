import unittest

from module import Row, Column, Grid

class Day5Test(unittest.TestCase):
    
    def test_part1(self):
        self.assertEqual([], Row([]).visible_trees())
        self.assertEqual([0], Row([1]).visible_trees())
        self.assertEqual([0,1], Row([1,1]).visible_trees())

        self.assertEqual([0,2], Row([2,1,2]).visible_trees())
        self.assertEqual([0,1,4], Row([2,4,3,4,4]).visible_trees())

        self.assertEqual([0,1,2,4], Row([2,5,5,1,2]).visible_trees())

        # 30373
        # 25512
        # 65332
        # 33549
        # 35390

        self.assertEqual(16 + 5, Grid(
            [
                Row([3,0,3,7,3]),
                Row([2,5,5,1,2]),
                Row([6,5,3,3,2]),
                Row([3,3,5,4,9]),
                Row([3,5,3,9,0]),
            ],
            [
                Column([3,2,6,3,6]),
                Column([0,5,5,3,5]),
                Column([3,5,3,5,3]),
                Column([7,1,3,4,9]),
                Column([3,2,2,9,0]),
            ]).number_of_visible_trees())

    def test_part2(self):
        self.assertEqual(2 * 2 * 1 * 2, Grid(
            [
                Row([3,0,3,7,3]),
                Row([2,5,5,1,2]),
                Row([6,5,3,3,2]),
                Row([3,3,5,4,9]),
                Row([3,5,3,9,0]),
            ],
            [
                Column([3,2,6,3,6]),
                Column([0,5,5,3,5]),
                Column([3,5,3,5,3]),
                Column([7,1,3,4,9]),
                Column([3,2,2,9,0]),
            ]).highest_scenic_score())

if __name__ == '__main__':
    unittest.main()