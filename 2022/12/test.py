import unittest

from module import Grid

P0_0 = (0, 0)
P0_1 = (0, 1)
P0_2 = (0, 2)
P1_0 = (1, 0)
P1_1 = (1, 1)
P1_2 = (1, 2)
P2_0 = (2, 0)
P2_1 = (2, 1)
P2_2 = (2, 2)


class Test(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(1, Grid({P0_0: 'a', P0_1: 'b'}).shortest_from_to(P0_0, P0_1))
        self.assertEqual(2, Grid({P0_0: 'a', P0_1: 'b', P0_2: 'c'}).shortest_from_to(P0_0, P0_2))
        self.assertEqual(
            8, Grid({
                P2_0: 'g', P2_1: 'f', P2_2: 'e',
                P1_0: 'h', P1_1: 'i', P1_2: 'd',
                P0_0: 'a', P0_1: 'b', P0_2: 'c'
            }).shortest_from_to(P0_0, P1_1))
        self.assertEqual(
            4, Grid({
                P2_0: 'c', P2_1: 'b', P2_2: 'c',
                P1_0: 'b', P1_1: 'e', P1_2: 'd',
                P0_0: 'a', P0_1: 'b', P0_2: 'c'
            }).shortest_from_to(P0_0, P1_1))

    def test_part2(self):
        pass
        # self.assertEqual(52166 * 52013, self.game.total_monkey_business(number_of_rounds=10000,less_worry_divisor=1))


if __name__ == '__main__':
    unittest.main()
