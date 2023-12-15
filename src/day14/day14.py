from copy import copy
from enum import Enum


class Directions(Enum):
    NORTH=1
    SOUTH=2
    EAST=3
    WEST=4


def get_input():
    with open('day14input.txt') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


def tilt_rocks_to_north(rock_map):
    tilted = []
    new_columns = []
    for column in range(len(rock_map[0])):
            column_map = ''.join([rock_map[row][column] for row in range(len(rock_map))])
            new_columns.append(move_rocks_in_column_segments(column_map))
    for row in range(len(rock_map)):
        new_row = ''.join([new_columns[column][row] for column in range(len(new_columns))])
        tilted.append(new_row)
    return tilted


def tilt_rocks_to_direction(rock_map, direction: Directions):
    vertical = direction in [Directions.NORTH, Directions.SOUTH]
    positive = direction in [Directions.NORTH, Directions.WEST]
    tilted = []
    if vertical:
        new_columns = []
        for column in range(len(rock_map[0])):
            column_map = ''.join([rock_map[row][column] for row in range(len(rock_map))])
            new_columns.append(move_rocks_in_column_segments(column_map, positive))
        for row in range(len(rock_map)):
            new_row = ''.join([new_columns[column][row] for column in range(len(new_columns))])
            tilted.append(new_row)
    else:
        for row in rock_map:
            new_row = move_rocks_in_column_segments(row, positive)
            tilted.append(new_row)
    return tilted


def complete_tilt_cycles(rock_map, cycles):
    current_map = copy(rock_map)
    for i in range(cycles):
        current_map = tilt_rocks_to_direction(current_map, Directions.NORTH)
        current_map = tilt_rocks_to_direction(current_map, Directions.WEST)
        current_map = tilt_rocks_to_direction(current_map, Directions.SOUTH)
        current_map = tilt_rocks_to_direction(current_map, Directions.EAST)
    return current_map


def move_rocks_in_column_segments(column: str, positive: bool = True):
    segments = column.split('#')
    new_segments = []
    for segment in segments:
        new_segments.append(move_rocks_in_segment(segment, positive))
    return '#'.join(new_segments)


def move_rocks_in_segment(segment: str, positive: bool = True):
    spaces = len(segment)
    rock_count = count_rocks_in_segment(segment)
    if positive:
        return 'O'*rock_count + '.'*(spaces-rock_count)
    return '.' * (spaces - rock_count) + 'O' * rock_count


def count_rocks_in_segment(segment: str):
    rock_count = 0
    for space in segment:
        if space == 'O':
            rock_count += 1
    return rock_count


def calculate_load(rock_map):
    rows = len(rock_map)
    load = 0
    for i, row in enumerate(rock_map):
        load_contribution = rows - i
        num_rocks = count_rocks_in_segment(row)
        load += num_rocks*load_contribution
    return load


def count_rocks_per_row(rock_map):
    rows = []
    for row in rock_map:
        num_rocks = count_rocks_in_segment(row)
        rows.append(num_rocks)
    return rows


def solve_day14_part1(rock_map):
    tilted = tilt_rocks_to_north(rock_map)
    return calculate_load(tilted)


def solve_day14_part2(rock_map):
    return analyze_rock_maps(rock_map)


def analyze_rock_maps(rock_map):
    new_map = copy(rock_map)
    rock_maps = []
    first_index = 0
    cycle = 0
    for i in range(1000):
        new_map = complete_tilt_cycles(new_map, 1)
        if new_map in rock_maps:
            first_index = rock_maps.index(new_map)
            cycle = i - first_index
            break
        rock_maps.append(new_map)
    additional_cycles = (1000000000 - i-1)%cycle
    new_map = complete_tilt_cycles(new_map, additional_cycles)
    return calculate_load(new_map)


if __name__ == '__main__':
    rock_map = get_input()
    print(solve_day14_part1(rock_map))
    print(solve_day14_part2(rock_map))
