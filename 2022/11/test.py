import unittest

from module import Game, Monkey, Multiplication, Addition, Square


class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.game = Game([
            Monkey([79, 98], Multiplication(19), 23, 2, 3),
            Monkey([54, 65, 75, 74], Addition(6), 19, 2, 0),
            Monkey([79, 60, 97], Square(), 13, 1, 3),
            Monkey([74], Addition(3), 17, 0, 1),
        ])


    def test_part1(self):
        self.assertEqual(101 * 105, self.game.total_monkey_business())

    def test_part2(self):
        self.assertEqual(52166 * 52013, self.game.total_monkey_business(number_of_rounds=10000,less_worry_divisor=1))


if __name__ == '__main__':
    unittest.main()
