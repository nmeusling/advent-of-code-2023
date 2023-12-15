from copy import copy, deepcopy
from enum import Enum


class RelativeLocations(Enum):
    RIGHT = (0, 1)
    LEFT = (0, -1)
    ABOVE = (-1, 0)
    BELOW = (1, 0)


class Coordinate:
    def __init__(self, x, y):
        self.x =x
        self.y =y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def get_input():
    with open('day10input.txt') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


def get_connected_pipes(pipe_map, location: Coordinate):
    if pipe_map[location.x][location.y] == '-':
        return [Coordinate(location.x, location.y-1), Coordinate(location.x, location.y+1)]
    elif pipe_map[location.x][location.y] == '|':
        return [Coordinate(location.x-1, location.y), Coordinate(location.x+1, location.y)]
    elif pipe_map[location.x][location.y] == 'L':
        return [Coordinate(location.x-1, location.y), Coordinate(location.x, location.y+1)]
    elif pipe_map[location.x][location.y] == 'J':
        return [Coordinate(location.x-1, location.y), Coordinate(location.x, location.y-1)]
    elif pipe_map[location.x][location.y] == '7':
        return [Coordinate(location.x, location.y - 1), Coordinate(location.x+1, location.y)]
    elif pipe_map[location.x][location.y] == 'F':
        return [Coordinate(location.x+1, location.y), Coordinate(location.x, location.y+1)]


def complete_step(pipe_map, current_location: Coordinate, previous_location: Coordinate):
    connected_pipes = get_connected_pipes(pipe_map, current_location)
    connected_pipes.remove(previous_location)
    next_location = connected_pipes[0]
    return next_location


def get_start_location(pipe_map):
    for i, row in enumerate(pipe_map):
        for j, pipe in enumerate(row):
            if pipe == 'S':
                return Coordinate(i, j)


def get_second_pipe(pipe_map, start_location: Coordinate):
    adjacent_pipes = [Coordinate(start_location.x + RelativeLocations.ABOVE.value[0],
                                 start_location.y + RelativeLocations.ABOVE.value[1]),
                      Coordinate(start_location.x + RelativeLocations.BELOW.value[0],
                                 start_location.y + RelativeLocations.BELOW.value[1]),
                      Coordinate(start_location.x + RelativeLocations.RIGHT.value[0],
                                 start_location.y + RelativeLocations.RIGHT.value[1]),
                      Coordinate(start_location.x + RelativeLocations.LEFT.value[0],
                                 start_location.y + RelativeLocations.LEFT.value[1])
                      ]
    for pipe in adjacent_pipes:
        connected_indices = get_connected_pipes(pipe_map, pipe)
        connected_pipes = [get_pipe_at_index(pipe_map, location) for location in connected_indices]
        if start_location in connected_indices and '.' not in connected_pipes:
            return pipe


def get_pipe_at_index(pipe_map, location:Coordinate):
    return pipe_map[location.x][location.y]


def get_relative_location(location1: Coordinate, location2: Coordinate):
    relative_location = (location2.x - location1.x, location2.y - location1.y)
    if relative_location == RelativeLocations.RIGHT.value:
        return RelativeLocations.RIGHT
    elif relative_location == RelativeLocations.LEFT.value:
        return RelativeLocations.LEFT
    elif relative_location == RelativeLocations.ABOVE.value:
        return RelativeLocations.ABOVE
    elif relative_location == RelativeLocations.BELOW.value:
        return RelativeLocations.BELOW


def solve_day10_part1(pipe_map):
    start_location = get_start_location(pipe_map)
    second_pipe = get_second_pipe(pipe_map, start_location)
    pipe_length = 1
    current_location = second_pipe
    previous_location = start_location
    while current_location != start_location:
        next_location = complete_step(pipe_map, current_location, previous_location)
        previous_location = current_location
        current_location = next_location
        pipe_length += 1
    return int((pipe_length + 1) / 2)

def solve_day10_part2(pipe_map):
    new_price_map = deepcopy(pipe_map)
    start_location = get_start_location(pipe_map)
    second_pipe = get_second_pipe(pipe_map, start_location)
    pipe_length = 1
    current_location = second_pipe
    previous_location = start_location
    while current_location != start_location:
        next_location = complete_step(pipe_map, current_location, previous_location)
        previous_location = current_location

        new_price_map[current_location.x] = new_price_map[current_location.x][0:current_location.y] + ' ' + new_price_map[current_location.x][current_location.y+1:]
        current_location = next_location
        pipe_length += 1
    for line in new_price_map:
        print(line)
    return int((pipe_length + 1) / 2)

if __name__ == '__main__':
    pipe_map = get_input()
    print(solve_day10_part1(pipe_map))
    pipe_map = get_input()
    print(solve_day10_part2(pipe_map))
