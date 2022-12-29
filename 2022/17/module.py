from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def drop(self):
        return Point(self.x, self.y - 1)


@dataclass
class Rock:
    points: list[Point]

    def place_at(self, location: Point):
        return Rock([point + location for point in self.points])

    def drop(self):
        return Rock([point.drop() for point in self.points])

    def conflicts_with(self, points: list[Point]) -> bool:
        return len(set(self.points).intersection(set(points))) > 0

    def highest_point_for_x(self, x) -> Point:
        highest_point = None
        for point in self.points:
            if highest_point is None:
                highest_point = point if point.x == x else None
            else:
                highest_point = point if ((point.x == x) & (point.y > highest_point.y)) else highest_point
            
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
        start_location = Point(2, max(point.y for point in top_line_points) + 3)

        return rock.place_at(start_location)

    @ staticmethod
    def _new_top_line_points(rock: Rock, top_line_points=list[Point]) -> list[Point]:
        new_top_line_points = []

        for top_line_point in top_line_points:
            point_in_rock = rock.highest_point_for_x(top_line_point.x)            
            new_top_line_points.append(top_line_point if point_in_rock is None else point_in_rock)

        return new_top_line_points

    @ staticmethod
    def get_top_row_after_drops(drops: int) -> list[int]:
        top_line_points: list[Point] = [Point(x, 0) for x in range(0,7)]

        for rock_number in range(drops):
            rock = Grid._place_in_grid(rocks[rock_number % 5], top_line_points)

            can_drop = True
            while (can_drop):
                dropped_rock = rock.drop()

                if dropped_rock.conflicts_with(top_line_points):
                    top_line_points = Grid._new_top_line_points(rock, top_line_points)
                    can_drop = False
                else:
                    rock = dropped_rock

        return [point.y for point in top_line_points]
