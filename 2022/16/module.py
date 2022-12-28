from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Valve:
    name: str
    flow_rate: int
    tunnels_to: list[str] = field(default_factory=list)
    
@dataclass
class Path:
    valves_visited: list[str]
    valves_opened: Dict[str,int] = field(default_factory=dict)
    
    def last_valve(self) -> str:
        return self.valves_visited[-1]
    
    def is_not_opened(self, valve: Valve) -> bool:
        return valve.name not in self.valves_opened.keys()
    
    def open_valve(self, valve: Valve, minutes: int):
        return Path(self.valves_visited, (self.valves_opened | { valve.name : valve.flow_rate * minutes}))
    
    def tunnel_to(self, tunnels: list[str]):
        paths = []
        for tunnel in tunnels:
            paths.append(Path(self.valves_visited + [tunnel], self.valves_opened))
                
        return paths
    
    def total(self):
        return sum(pressure_released for pressure_released in self.valves_opened.values())
                
class Pathing:
    
    def __init__(self, valves: Dict[str,Valve]) -> None:
        self.valves = valves
        
    def _new_paths(self, path: Path, current_valve: Valve, minutes_left):        
        new_paths = []
        if (current_valve.flow_rate != 0) & (path.is_not_opened(current_valve)):
            new_paths.append(path.open_valve(current_valve, minutes_left - 1))
            
        new_paths += path.tunnel_to(current_valve.tunnels_to)
        
        if (not new_paths):
            return [path]
        
        return new_paths
    
    def _remove_bad_paths(self, paths: list[Path]):
        if len(paths) < 100:
            return paths
        
        best_sorted_by_pressure_released = sorted(paths, key = lambda t: t.total(), reverse = True)
        half_length = len(best_sorted_by_pressure_released) // 2
        first_half = best_sorted_by_pressure_released[:half_length]
        
        return first_half
    
    def max_release_pressured(self):
        minutes_left = 30
        
        paths = [Path(['AA'])]        
        while(minutes_left > 0):
            new_paths = []
            for path in paths:
                new_paths += self._new_paths(path, self.valves[path.last_valve()], minutes_left)
            
            paths = self._remove_bad_paths(new_paths)
            
            # for path in paths:
            #     print(path)

            minutes_left -= 1
                        
        return max(path.total() for path in paths)