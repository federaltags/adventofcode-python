import unittest

from module import Cave


class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.cave = Cave(
            structure_points=[
                (498, 4), (498, 5), (498, 6), (497, 6), (496, 6),
                (494, 9), (495, 9), (496, 9), (497, 9), (498, 9),
                (499, 9), (500, 9), (501, 9), (502, 9), (502, 8),
                (502, 7), (502, 6), (502, 5), (502, 4), (503, 4)
            ]
        )

    def test_part1(self):
        self.cave.drop_from_until_falling_from_abyss()
        self.assertEqual(24, self.cave.number_of_resting_grains_of_sands())

    def test_part2(self): #25434
        self.cave.drop_until_blocked()
        self.assertEqual(93, self.cave.number_of_resting_grains_of_sands())
        


if __name__ == '__main__':
    unittest.main()
