from collections import namedtuple
from dataclasses import dataclass, field


Point = namedtuple('Point', ['x', 'y'])


@dataclass
class Cave:
    structure_points: list[Point]
    grains_of_sand: list[Point] = field(default_factory=list)

    def drop_from_until_falling_from_abyss(self, point: Point = (500, 0)):
        highest_y_coordinate = max(structure_point[1] for structure_point in self.structure_points)

        should_continue = True
        while should_continue:
            should_continue = self._drop(point, highest_y_coordinate)

    def drop_until_blocked(self, point: Point = (500, 0)):
        highest_y_coordinate = max(structure_point[1] for structure_point in self.structure_points)

        dropped_point = None
        while (dropped_point != point):
            dropped_point = self._drop_with_bottom(point, highest_y_coordinate)
            print(dropped_point)

    def _drop(self, point, highest_y_coordinate) -> bool:
        next_point = point
        while (True):
            next_potential_drops = self._next_drops(next_point)

            occupied_points = (self.grains_of_sand + self.structure_points)
            if all(potential_drop in occupied_points for potential_drop in next_potential_drops):
                self.grains_of_sand.append(next_point)
                return True
            elif next_potential_drops[0][1] > highest_y_coordinate:
                return False
            else:
                next_point = next(filter(lambda potential_drop: potential_drop not in occupied_points, next_potential_drops), None)

    def _drop_with_bottom(self, point, highest_y_coordinate):
        next_point = point
        while (True):
            next_potential_drops = self._next_drops(next_point)

            occupied_points = (self.grains_of_sand + self.structure_points)
            if all(potential_drop in occupied_points for potential_drop in next_potential_drops):
                self.grains_of_sand.append(next_point)
                return next_point
            elif next_potential_drops[0][1] > (highest_y_coordinate+1):
                self.grains_of_sand.append(next_point)
                return next_point
            else:
                next_point = next(filter(lambda potential_drop: potential_drop not in occupied_points, next_potential_drops), None)

    def _next_drops(self, point):
        return [
            (point[0], point[1]+1),
            (point[0]-1, point[1]+1),
            (point[0]+1, point[1]+1)
        ]

    def number_of_resting_grains_of_sands(self) -> int:
        return len(self.grains_of_sand)
