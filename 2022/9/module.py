from dataclasses import dataclass
from enum import Enum

class Move(Enum):
    LEFT = 'L'
    RIGHT = 'R'
    UP = 'U'
    DOWN = 'D'


@dataclass
class Location:
    x: int
    y: int

    def move(self,move):
        offsets = {
            Move.LEFT: (-1,0),
            Move.RIGHT: (1,0),
            Move.UP: (0,1),
            Move.DOWN: (0,-1),
        }

        x_offset, y_offset = offsets[move]
            
        return Location(self.x+x_offset, self.y+y_offset)

    def __diff__(self,x,y):
        if x < y:
            return -len(range(x,y))
        elif(y < x):
            return len(range(y,x))

        return 0

    def offset(self,other):
        return (
            self.__diff__(self.x, other.x), 
            self.__diff__(self.y, other.y)
        )        

    def move_with_offset(self,x,y):
        return Location(self.x + x, self.y + y)

    def __hash__(self) -> int:
        return self.x+self.y

    def __str__(self) -> str:
        return f'({self.x}:{self.y})'

@dataclass
class State:
    head_location: Location
    tail_location: Location
    visited_by_tail: list[Location]

    def number_of_locations_tail_visited(self):
        return len({*self.visited_by_tail})

    def __move_tail_if_needed__(self, new_head_location) -> Location:
        offset = new_head_location.offset(self.tail_location)

        if (offset == (-2,0)):
            return self.tail_location.move_with_offset(-1,0) #move left
        elif (offset == (2,0)):
            return self.tail_location.move_with_offset(1,0) #move right
        elif (offset == (0,-2)):
            return self.tail_location.move_with_offset(0,-1) #move down
        elif (offset == (0,2)):
            return self.tail_location.move_with_offset(0,1) #move up
        # ..H
        # T..
        # .T.
        elif (offset in [(1,2),(2,1)]): 
            return self.tail_location.move_with_offset(1,1) #move right up
        # H..
        # ..T
        # .T.
        elif (offset in [(-2,1),(-1,2)]):
            return self.tail_location.move_with_offset(-1,1) #move left up
        # .T.
        # T..
        # ..H
        elif (offset in [(2,-1),(1,-2)]):
            return self.tail_location.move_with_offset(1,-1) #move right down
        # .T.
        # ..T
        # H..
        elif (offset in [(-1,-2),(-2,-1)]):
            return self.tail_location.move_with_offset(-1,-1) #move left down

        return self.tail_location

    def move(self, move):
        new_head_location = self.head_location.move(move)
        new_tail_location = self.__move_tail_if_needed__(new_head_location)        

        new_state = State(
            head_location=new_head_location,
            tail_location=new_tail_location,
            visited_by_tail=self.visited_by_tail + [new_tail_location]
        )

        print(f'after {move}: {new_state}')

        return new_state

    def __str__(self) -> str:
        return f'{self.head_location}:{self.tail_location}'
