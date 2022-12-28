import unittest

from module import Valve, Pathing, Pathing


class Test(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(28 * 13, Pathing.max_pressure_released(30,{
            'AA': Valve('AA', 0, ['BB']),
            'BB': Valve('BB', 13, ['AA'])
        }))

if __name__ == '__main__':
    unittest.main()
