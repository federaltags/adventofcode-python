import unittest

from module import Grid, Move


class Test(unittest.TestCase):

    def test_part1(self):
        self.assertListEqual([0, 0, 0, 0, 0, 0, 0], Grid.get_top_row_after_drops(0))
        
        # |.......|
        # |.......|
        # |.......|
        # |..1111.|
        # +-------+
        self.assertListEqual([0, 0, 1, 1, 1, 1, 0], Grid.get_top_row_after_drops(1))
        # |...2...|
        # |..222..|
        # |...2...|
        # |..1111.|
        # +-------+
        self.assertListEqual([0, 0, 3, 4, 3, 1, 0], Grid.get_top_row_after_drops(2))
        # |....3..|
        # |....3..|
        # |..333..|
        # |...2...|
        # |..222..|
        # |...2...|
        # |..1111.|
        # +-------+
        self.assertListEqual([0, 0, 5, 5, 7, 1, 0], Grid.get_top_row_after_drops(3))
        # |..4....|
        # |..4....|
        # |..4.3..|
        # |..4.3..|
        # |..333..|
        # |...2...|
        # |..222..|
        # |...2...|
        # |..1111.|
        # +-------+
        self.assertListEqual([0, 0, 9, 5, 7, 1, 0], Grid.get_top_row_after_drops(4))
        # |..55...|
        # |..55...|
        # |..4....|
        # |..4....|
        # |..4.3..|
        # |..4.3..|
        # |..333..|
        # |...2...|
        # |..222..|
        # |...2...|
        # |..1111.|
        # +-------+
        self.assertListEqual([0, 0, 11, 11, 7, 1, 0], Grid.get_top_row_after_drops(5))
        # |..6666.|
        # |..55...|
        # |..55...|
        # |..4....|
        # |..4....|
        # |..4.3..|
        # |..4.3..|
        # |..333..|
        # |...2...|
        # |..222..|
        # |...2...|
        # |..1111.|
        # +-------+
        self.assertListEqual([0, 0, 12, 12, 12, 12, 0], Grid.get_top_row_after_drops(6))
        
        # |.......|
        # |.......|
        # |.......|
        # |1111...|
        # +-------+
        # self.assertListEqual([1, 1, 1, 1, 0, 0, 0], Grid.get_top_row_after_drops(1, [Move.LEFT]))
        

if __name__ == '__main__':
    unittest.main()
