import unittest

from module import SensorGrid, Point


class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.sensor_grid = SensorGrid({
            Point(2, 18): Point(-2, 15),
            Point(9, 16): Point(10, 16),
            Point(13, 2): Point(15, 3),
            Point(12, 14): Point(10, 16),
            Point(10, 20): Point(10, 16),
            Point(14, 17): Point(10, 16),
            Point(8, 7): Point(2, 10),
            Point(2, 0): Point(2, 10),
            Point(0, 11): Point(2, 10),
            Point(20, 14): Point(25, 17),
            Point(17, 20): Point(21, 22),
            Point(16, 7): Point(15, 3),
            Point(14, 3): Point(15, 3),
            Point(20, 1): Point(15, 3),
        }) 

    def test_part1(self):
        self.assertEqual(26, self.sensor_grid.number_of_positions_that_cannot_be_a_beacon(10))

    def test_part2(self):
        self.assertEqual(56000011, self.sensor_grid.tuning_frequency(20))

if __name__ == '__main__':
    unittest.main()
