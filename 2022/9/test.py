import unittest

from module import Snake, Location, Move

LOCATION_P0_P0 = Location(0,0)
LOCATION_P1_P0 = Location(1,0)
LOCATION_M1_P0 = Location(-1,0)
LOCATION_P1_P2 = Location(1,2)
LOCATION_P2_P3 = Location(2,3)
LOCATION_M1_M2 = Location(-1,-2)
LOCATION_M2_M3 = Location(-2,-3)
LOCATION_M2_P4 = Location(-2,4)
LOCATION_P2_M4 = Location(2,4)
LOCATION_M2_P0 = Location(-2,0)
LOCATION_P2_P0 = Location(2,0)
LOCATION_P0_M2 = Location(0,-2)
LOCATION_P0_P2 = Location(0,2)
LOCATION_P0_P1 = Location(0,1)
LOCATION_M1_M1 = Location(-1,-1)
LOCATION_P4_P1 = Location(4,1)
LOCATION_M1_P2 = Location(-1,2)
LOCATION_P1_P1 = Location(1,1)
LOCATION_P3_P0 = Location(3,0)
LOCATION_M1_P6 = Location(-1,6)
LOCATION_M3_P6 = Location(-3,6)
LOCATION_M3_P2 = Location(-3,2)
LOCATION_P3_P2 = Location(3,2)

START = Snake([LOCATION_P0_P0] * 2, [LOCATION_P0_P0])

class Test(unittest.TestCase):
    
    def test_offset(self):
        self.assertEqual((-2,0), LOCATION_M2_P0.offset(LOCATION_P0_P0))
        self.assertEqual((2,0), LOCATION_P2_P0.offset(LOCATION_P0_P0))
        self.assertEqual((0,-2), LOCATION_P0_M2.offset(LOCATION_P0_P0))
        self.assertEqual((0,2), LOCATION_P0_P2.offset(LOCATION_P0_P0))
        
        self.assertEqual((-1,-2), LOCATION_M1_M1.offset(LOCATION_P0_P1))
        self.assertEqual((-2,-1), LOCATION_M1_M1.offset(LOCATION_P1_P0))

        self.assertEqual((1,-2), LOCATION_P0_P0.offset(LOCATION_M1_P2))
        self.assertEqual((2,-1), LOCATION_P3_P0.offset(LOCATION_P1_P1))

        self.assertEqual((-1,2), LOCATION_M2_P4.offset(LOCATION_M1_P2))
        self.assertEqual((-2,1), LOCATION_M1_P2.offset(LOCATION_P1_P1))

        self.assertEqual((1,2), LOCATION_M2_P4.offset(LOCATION_M3_P2))
        self.assertEqual((2,1), LOCATION_P3_P2.offset(LOCATION_P1_P1))
       
    
    def test_part1(self):
        self.assertEqual(1, START.number_of_locations_tail_visited())

        self.assertEqual(1, START.move(Move.LEFT).number_of_locations_tail_visited())
        self.assertEqual(2, START.move(Move.LEFT).move(Move.LEFT).number_of_locations_tail_visited())
        self.assertEqual(3, START.move(Move.LEFT).move(Move.LEFT).move(Move.LEFT).number_of_locations_tail_visited())

        self.assertEqual(1, START.move(Move.RIGHT).number_of_locations_tail_visited())
        self.assertEqual(2, START.move(Move.RIGHT).move(Move.RIGHT).number_of_locations_tail_visited())
        self.assertEqual(3, START.move(Move.RIGHT).move(Move.RIGHT).move(Move.RIGHT).number_of_locations_tail_visited())

        self.assertEqual(1, START.move(Move.UP).number_of_locations_tail_visited())
        self.assertEqual(2, START.move(Move.UP).move(Move.UP).number_of_locations_tail_visited())
        self.assertEqual(3, START.move(Move.UP).move(Move.UP).move(Move.UP).number_of_locations_tail_visited())

        self.assertEqual(1, START.move(Move.DOWN).number_of_locations_tail_visited())
        self.assertEqual(2, START.move(Move.DOWN).move(Move.DOWN).number_of_locations_tail_visited())
        self.assertEqual(3, START.move(Move.DOWN).move(Move.DOWN).move(Move.DOWN).number_of_locations_tail_visited())

        state = START
        self.assertEqual(1, state.number_of_locations_tail_visited())

        # R 4
        state = state.move(Move.RIGHT)
        self.assertEqual(1, state.number_of_locations_tail_visited())
        state = state.move(Move.RIGHT)
        self.assertEqual(2, state.number_of_locations_tail_visited())
        state = state.move(Move.RIGHT)
        self.assertEqual(3, state.number_of_locations_tail_visited())
        state = state.move(Move.RIGHT)
        self.assertEqual(4, state.number_of_locations_tail_visited())

        # U 4
        state = state.move(Move.UP)
        self.assertEqual(4, state.number_of_locations_tail_visited())
        state = state.move(Move.UP)
        self.assertEqual(5, state.number_of_locations_tail_visited())
        state = state.move(Move.UP)
        self.assertEqual(6, state.number_of_locations_tail_visited())
        state = state.move(Move.UP) 
        self.assertEqual(7, state.number_of_locations_tail_visited())

        # L 3
        state = state.move(Move.LEFT)
        self.assertEqual(7, state.number_of_locations_tail_visited())
        state = state.move(Move.LEFT)
        self.assertEqual(8, state.number_of_locations_tail_visited())
        state = state.move(Move.LEFT)
        self.assertEqual(9, state.number_of_locations_tail_visited())

        # D 1
        state = state.move(Move.DOWN)
        self.assertEqual(9, state.number_of_locations_tail_visited())

        # R 4
        state = state.move(Move.RIGHT)
        self.assertEqual(9, state.number_of_locations_tail_visited())
        state = state.move(Move.RIGHT)
        self.assertEqual(9, state.number_of_locations_tail_visited())
        state = state.move(Move.RIGHT)
        self.assertEqual(10, state.number_of_locations_tail_visited())
        state = state.move(Move.RIGHT)
        self.assertEqual(10, state.number_of_locations_tail_visited())

        # D 1
        state = state.move(Move.DOWN)
        self.assertEqual(10, state.number_of_locations_tail_visited())

        # L 5
        state = state.move(Move.LEFT)
        self.assertEqual(10, state.number_of_locations_tail_visited())
        state = state.move(Move.LEFT)
        self.assertEqual(10, state.number_of_locations_tail_visited())
        state = state.move(Move.LEFT)
        self.assertEqual(11, state.number_of_locations_tail_visited())
        state = state.move(Move.LEFT)
        self.assertEqual(12, state.number_of_locations_tail_visited())
        state = state.move(Move.LEFT)
        self.assertEqual(13, state.number_of_locations_tail_visited())

        # R 2
        state = state.move(Move.RIGHT)
        self.assertEqual(13, state.number_of_locations_tail_visited())
        state = state.move(Move.RIGHT)
        self.assertEqual(13, state.number_of_locations_tail_visited())

    def test_part2(self):
        snake = Snake([LOCATION_P0_P0] * 10, [LOCATION_P0_P0])

        # R 5
        for _ in range(5):
            snake = snake.move(Move.RIGHT)

        # U 8
        for _ in range(8):
            snake = snake.move(Move.UP) 

        # L 8
        for _ in range(8):
            snake = snake.move(Move.LEFT)

        # D 3
        for _ in range(3):
            snake = snake.move(Move.DOWN)

        # R 17
        for _ in range(17):
            snake = snake.move(Move.RIGHT)

        # D 10
        for _ in range(10):
            snake = snake.move(Move.DOWN)
        
        # L 25
        for _ in range(25):
            snake = snake.move(Move.LEFT)

        # U 20
        for _ in range(20):
            snake = snake.move(Move.UP)

        self.assertEqual(36, snake.number_of_locations_tail_visited())

if __name__ == '__main__':
    unittest.main()