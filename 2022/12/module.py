from collections import deque
from dataclasses import dataclass


@dataclass
class Grid:
    squares: dict[tuple[int, int], chr]

    def shortest_from_to(self, from_squares: list[tuple[int, int]], to_square: tuple[int, int]) -> int:
        visited = deque(from_squares)

        steps = 0
        while (to_square not in visited):
            newvisited = deque()

            while visited:
                square = visited.popleft()
                newvisited += self._next_squares(square)

            for newv in newvisited:
                if newv not in visited:
                    visited.append(newv)

            steps += 1

        return steps

    def _next_squares(self, square):
        next_squares = []

        offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for offset in offsets:
            neighbour = Grid._square_offsetted_by(square, offset)
            if self._can_destination_be_reached_from(neighbour, square):
                next_squares.append(neighbour)

        return next_squares

    @staticmethod
    def _square_offsetted_by(square: tuple[int, int], offset: tuple[int, int]):
        return (square[0]+offset[0], square[1]+offset[1])

    def _can_destination_be_reached_from(self, destination: tuple[int, int], origin: tuple[int, int]) -> bool:
        if destination not in self.squares.keys():
            return False

        height_difference = ord(self.squares[destination]) - ord(self.squares[origin])
        return height_difference <= 1
