import unittest

from module import Sensor, Sensors


class Test(unittest.TestCase):

    def test_part1(self):
        sensors = Sensors([
            Sensor((2, 18), (-2, 15)),
            Sensor((9, 16), (10, 16)),
            Sensor((13, 2), (15, 3)),
            Sensor((12, 14), (10, 16)),
            Sensor((10, 20), (10, 16)),
            Sensor((14, 17), (10, 16)),
            Sensor((8, 7), (2, 10)),
            Sensor((2, 0), (2, 10)),
            Sensor((0, 11), (2, 10)),
            Sensor((20, 14), (25, 17)),
            Sensor((17, 20), (21, 22)),
            Sensor((16, 7), (15, 3)),
            Sensor((14, 3), (15, 3)),
            Sensor((20, 1), (15, 3)),
        ])
        self.assertEqual(26, sensors.number_of_positions_that_cannot_be_a_beacon(10))

if __name__ == '__main__':
    unittest.main()
