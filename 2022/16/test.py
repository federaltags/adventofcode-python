import unittest

from module import Valve, Pathing


class Test(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(10 * 29, Pathing({
            'AA': Valve('AA', 10)
        }).max_release_pressured())
        self.assertEqual(28 * 13, Pathing({
            'AA': Valve('AA', 0, ['BB']),
            'BB': Valve('BB', 13, [])
        }).max_release_pressured())
        self.assertEqual(28 * 13, Pathing({
            'AA': Valve('AA', 0, ['BB']),
            'BB': Valve('BB', 13, ['AA'])
        }).max_release_pressured())


if __name__ == '__main__':
    unittest.main()
