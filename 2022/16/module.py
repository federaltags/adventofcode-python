from dataclasses import dataclass, field
import functools
from typing import Dict, Set


@dataclass(frozen=True)
class Valve:
    name: str
    flow_rate: int
    tunnels_to: list[str] = field(default_factory=list)


class Pathing:

    @staticmethod
    def max_pressure_released(minutes: int, valves: Dict[str, Valve], elephant: bool = False):

        @functools.cache
        def calculate_max_pressure_released(opened: Set[str], mins_remaining: int, curr_valve_id: str, elephant: bool = False):
            if mins_remaining <= 0:
                if elephant:
                    return calculate_max_pressure_released(opened, 26, "AA")
                else:
                    return 0

            most_pressure_released = 0
            current_valve = valves[curr_valve_id]
            for tunnel in current_valve.tunnels_to:
                most_pressure_released = max(most_pressure_released, calculate_max_pressure_released(
                    opened, mins_remaining - 1, tunnel, elephant))

            if curr_valve_id not in opened and current_valve.flow_rate > 0 and mins_remaining > 0:
                opened = set(opened)
                opened.add(curr_valve_id)
                mins_remaining -= 1
                total_released = mins_remaining * current_valve.flow_rate

                for tunnel in current_valve.tunnels_to:
                    # Try each neighbour and recurse in. Save the best one.
                    most_pressure_released = max(most_pressure_released,
                                                 total_released + calculate_max_pressure_released(frozenset(opened), mins_remaining - 1, tunnel, elephant))

            return most_pressure_released

        return calculate_max_pressure_released(frozenset(), minutes, 'AA', elephant)
