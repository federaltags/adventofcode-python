from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def manhattan_distance(self, other) -> int:
        diff = self - other
        return sum((abs(diff.x), abs(diff.y)))


@dataclass
class SensorGrid:

    def __init__(self, sensor_to_beacon: dict[Point, Point]) -> None:
        self.sensor_to_beacon = sensor_to_beacon
        self.beacons = set(sensor_to_beacon.values())
        self.sensor_range = {s: b.manhattan_distance(s) for s, b in self.sensor_to_beacon.items()}
    
    def number_of_positions_that_cannot_be_a_beacon(self, y_coordinate):
        intervals = self._merge_intervals(y_coordinate)

        coverage_count = sum(interval[1]-interval[0]+1 for interval in intervals)
        beacons_to_exclude = sum(1 for beacon in self.beacons if beacon.y == y_coordinate)

        return coverage_count - beacons_to_exclude

    def _point_outside_sensor_range(self, box_range_max) -> Point:
        for sensor_point, dist_to_nearest in self.sensor_range.items():
            for dx in range(dist_to_nearest+2): # max dx is dist_to_nearest + 1
                dy = (dist_to_nearest+1) - dx   # To always be on perimeter, dx+dy must be dist_to_nearest + 1
                
                for sign_x, sign_y in [(-1, -1), (-1, 1), (1, -1), (1, 1)]: # Add our dx and dy in all directions
                    x = sensor_point.x + (dx * sign_x)
                    y = sensor_point.y + (dy * sign_y)
                    
                    # Check within the bounds defined; if not, try next dx and dy
                    if not (0 <= x <= box_range_max and 0 <= y <= box_range_max):
                        continue

                    coverage = self._merge_intervals(y) # get all disallowed intervals
                    # look for a gap between any intervals
                    if len(coverage) > 1:
                        for i in range(1, len(coverage)+1):
                            if coverage[i][0] > coverage[0][1] + 1:
                                x = coverage[i][0] - 1
                                return Point(x,y)
        
        return None
    
    def tuning_frequency(self, box_range_max) -> int:
        point = self._point_outside_sensor_range(box_range_max)
        return point.x * 4000000 + point.y

    def _get_row_coverage_intervals(self, row: int) -> list[list]:    
        close_sensors_ranges = {sensor:range for sensor, range in self.sensor_range.items() if abs(sensor.y - row) <= range}
        
        intervals: list[list] = []
        for sensor, range in close_sensors_ranges.items():
            distance_to_row = abs(sensor.y - row)
            max_x_offset = (range - distance_to_row)
            start_x = sensor.x - max_x_offset
            end_x = sensor.x + max_x_offset
            intervals.append([start_x, end_x])

        return intervals

    def _merge_intervals(self, row: int) -> list[list]:
        intervals = self._get_row_coverage_intervals(row)
        intervals.sort()
        stack = []
        stack.append(intervals[0])
        
        for interval in intervals[1:]:
            # Check for overlapping interval
            if stack[-1][0] <= interval[0] <= stack[-1][-1]:
                stack[-1][-1] = max(stack[-1][-1], interval[-1])
            else:
                stack.append(interval)
         
        return stack