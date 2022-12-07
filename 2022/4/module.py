from dataclasses import dataclass


@dataclass
class Ranges:
    first_range_edges: list
    second_range_edges: list

    def is_contained(self):
        first_range = Ranges.to_range(self.first_range_edges)
        second_range = Ranges.to_range(self.second_range_edges)

        return first_range.issubset(second_range) | second_range.issubset(first_range)

    def is_overlapping(self):
        first_range = Ranges.to_range(self.first_range_edges)
        second_range = Ranges.to_range(self.second_range_edges)

        return len(first_range.intersection(second_range)) != 0
        

    @staticmethod
    def to_range(range_edges):
        return set(range(range_edges[0], range_edges[1]+1))