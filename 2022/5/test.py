import unittest

from module import Stacks

class Day5Test(unittest.TestCase):
    
    def test_part1(self):
        self.assertEqual("NDP", Stacks({
            1: ["Z", "N"],
            2: ["M", "C", "D"],
            3: ["P"]
        }).tops())
        self.assertEqual("DCP", Stacks({
            1: ["Z", "N"],
            2: ["M", "C", "D"],
            3: ["P"]
        }).move(1, 2, 1).tops())
        self.assertEqual("CMP", Stacks({
            1: ["Z", "N"],
            2: ["M", "C", "D"],
            3: ["P"]
        }).move(2, 2, 1).tops())

    def test_part2(self):
        self.assertEqual("NDP", Stacks({
            1: ["Z", "N"],
            2: ["M", "C", "D"],
            3: ["P"]
        }).tops())
        self.assertEqual("DCP", Stacks({
            1: ["Z", "N"],
            2: ["M", "C", "D"],
            3: ["P"]
        }).move_9001(1, 2, 1).tops())
        self.assertEqual("DMP", Stacks({
            1: ["Z", "N"],
            2: ["M", "C", "D"],
            3: ["P"]
        }).move_9001(2, 2, 1).tops())

if __name__ == '__main__':
    unittest.main()