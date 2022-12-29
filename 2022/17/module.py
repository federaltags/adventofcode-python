from dataclasses import dataclass
from enum import Enum
from typing import Set


class Move(Enum):
    LEFT = '<'
    RIGHT = '>'


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def drop(self):
        return Point(self.x, self.y - 1)

    def move_left(self):
        return Point(self.x - 1, self.y)

    def move_right(self):
        return Point(self.x + 1, self.y)


@dataclass
class Rock:
    points: list[Point]

    def place_at(self, location: Point):
        return Rock([point + location for point in self.points])

    def drop(self):
        return Rock([point.drop() for point in self.points])

    def move_left(self):
        return Rock([point.move_left() for point in self.points])

    def move_right(self):
        return Rock([point.move_right() for point in self.points])

    def conflicts_with(self, points: list[Point]) -> bool:
        return len(set(self.points).intersection(set(points))) > 0

    def highest_point_for_x(self, x) -> Point:
        highest_point = None
        for point in self.points:
            if highest_point is None:
                highest_point = point if point.x == x else None
            else:
                highest_point = point if ((point.x == x) & (
                    point.y > highest_point.y)) else highest_point

        return highest_point


rocks = {
    # ####
    0: Rock([Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)]),
    # .#.
    # ###
    # .#.
    1: Rock([Point(0, 1), Point(1, 0), Point(1, 1), Point(1, 2), Point(2, 1)]),
    # ..#
    # ..#
    # ###
    2: Rock([Point(0, 0), Point(1, 0), Point(2, 0), Point(2, 1), Point(2, 2)]),
    # #
    # #
    # #
    # #
    3: Rock([Point(0, 0), Point(0, 1), Point(0, 2), Point(0, 3)]),
    # ##
    # ##
    4: Rock([Point(0, 0), Point(0, 1), Point(1, 0), Point(1, 1)]),
}


class Grid:

    @ staticmethod
    def _place_in_grid(rock: Rock, top_line_points: list[Point]) -> Rock:
        start_location = Point(
            2, max([point.y for point in top_line_points], default=0) + 3)

        return rock.place_at(start_location)

    @ staticmethod
    def _new_top_line_points(rock: Rock, top_line_points=list[Point]) -> list[Point]:
        new_top_line_points = []

        for top_line_point in top_line_points:
            point_in_rock = rock.highest_point_for_x(top_line_point.x)
            new_top_line_points.append(
                top_line_point if point_in_rock is None else point_in_rock)

        return new_top_line_points

    @staticmethod
    def _highest_points(occupied_points):
        highest_points = []
        for x in range(0, 7):
            highest_points.append(max(
                [(occupied_point.y + 1) for occupied_point in occupied_points if occupied_point.x == x], default=0))

        return highest_points

    @ staticmethod
    def get_top_row_after_drops(drops: int, moves: list[Move] = []) -> list[int]:
        occupied_points: Set[Point] = set()

        for rock_number in range(drops):
            rock = Grid._place_in_grid(rocks[rock_number % 5], occupied_points)

            can_drop = True
            while (can_drop):
                rock = Grid._move(moves, occupied_points, rock)

                dropped_rock = rock.drop()

                if (dropped_rock.conflicts_with(occupied_points) | (any([point.y < 0 for point in dropped_rock.points]))):
                    occupied_points.update(set(rock.points))
                    can_drop = False
                else:
                    rock = dropped_rock

        return Grid._highest_points(occupied_points)

    @staticmethod
    def _move(moves: list[Move], occupied_points: set[Point], rock: Rock):
        if moves:
            next_move = moves.pop(0)

            if next_move == Move.LEFT:
                moved_rock = rock.move_left()
                if (not moved_rock.conflicts_with(occupied_points)) & (not any(point.x < 0 for point in moved_rock.points)):
                    rock = moved_rock
            else:
                moved_rock = rock.move_right()
                if (not moved_rock.conflicts_with(occupied_points)) & (not any(point.x > 6 for point in moved_rock.points)):
                    rock = moved_rock

            moves.append(next_move)

        return rock
