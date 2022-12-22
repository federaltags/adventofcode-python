from dataclasses import dataclass


@dataclass
class Sensor:
    sensor: tuple[int, int]
    beacon: tuple[int, int]

    def __post_init__(self):
        self.manhattan_distance = abs(self.sensor[0] - self.beacon[0]) + abs(self.sensor[1] - self.beacon[1])

    def positions_that_cannot_be_a_beacon(self, y_coordinate):
        positions = set()

        y_diff = abs(self.sensor[1] - y_coordinate)
        if y_diff > self.manhattan_distance:
            return positions

        x_diff = self.manhattan_distance - y_diff 
        for x in range((self.sensor[0] - x_diff), (self.sensor[0] + x_diff + 1)):
            positions.add((x, y_coordinate))
        
        positions.discard(self.beacon)

        return positions

@dataclass
class Sensors:
    sensors: list[Sensor]

    def number_of_positions_that_cannot_be_a_beacon(self, y_coordinate):
        positions_that_cannot_be_a_beacon = set()

        for sensor in self.sensors:
            positions_that_cannot_be_a_beacon.update(sensor.positions_that_cannot_be_a_beacon(y_coordinate))

        for sensor in self.sensors:
            positions_that_cannot_be_a_beacon.discard(sensor.beacon)
        
        return len(positions_that_cannot_be_a_beacon)


    