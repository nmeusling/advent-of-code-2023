from src.day14.day14 import move_rocks_in_segment, move_rocks_in_column_segments, tilt_rocks_to_north, calculate_load, \
    Directions, tilt_rocks_to_direction, complete_tilt_cycles


def test_move_rocks_in_segment():
    segment = '...O.OOO...'
    assert move_rocks_in_segment(segment) == 'OOOO.......'


def test_move_rocks_in_column_segments():
    column = '..OO..#..OO#...O...O'
    assert move_rocks_in_column_segments(column) == 'OO....#OO..#OO......'

    column = '...OO....O'
    assert move_rocks_in_column_segments(column) == 'OOO.......'


def test_tilt_rocks_to_north():
    rock_map = [
        'O....#....',
        'O.OO#....#',
        '.....##...',
        'OO.#O....O',
        '.O.....O#.',
        'O.#..O.#.#',
        '..O..#O..O',
        '.......O..',
        '#....###..',
        '#OO..#....'
    ]
    tilted_map = [
        'OOOO.#.O..',
        'OO..#....#',
        'OO..O##..O',
        'O..#.OO...',
        '........#.',
        '..#....#.#',
        '..O..#.O.O',
        '..O.......',
        '#....###..',
        '#....#....'
    ]
    assert tilt_rocks_to_north(rock_map) == tilted_map

def test_tilt_rocks_to_east():
    rock_map = [
        'O....#....',
        'O.OO#....#',
        '.....##...',
        'OO.#O....O',
        '.O.....O#.',
        'O.#..O.#.#',
        '..O..#O..O',
        '.......O..',
        '#....###..',
        '#OO..#....'
    ]
    tilted_map = [
        '....O#....',
        '.OOO#....#',
        '.....##...',
        '.OO#....OO',
        '......OO#.',
        '.O#...O#.#',
        '....O#..OO',
        '.........O',
        '#....###..',
        '#..OO#....'
    ]
    assert tilt_rocks_to_direction(rock_map, Directions.EAST) == tilted_map

def test_tilt_rocks_to_south():
    rock_map = [
        'O....#....',
        'O.OO#....#',
        '.....##...',
        'OO.#O....O',
        '.O.....O#.',
        'O.#..O.#.#',
        '..O..#O..O',
        '.......O..',
        '#....###..',
        '#OO..#....'
    ]
    tilted_map = [
        '.....#....',
        '....#....#',
        '...O.##...',
        '...#......',
        'O.O....O#O',
        'O.#..O.#.#',
        'O....#....',
        'OO....OO..',
        '#OO..###..',
        '#OO.O#...O'
    ]
    assert tilt_rocks_to_direction(rock_map, Directions.SOUTH) == tilted_map


def test_tilt_rocks_to_west():
    rock_map = [
        'O....#....',
        'O.OO#....#',
        '.....##...',
        'OO.#O....O',
        '.O.....O#.',
        'O.#..O.#.#',
        '..O..#O..O',
        '.......O..',
        '#....###..',
        '#OO..#....'
    ]
    tilted_map = [
        'O....#....',
        'OOO.#....#',
        '.....##...',
        'OO.#OO....',
        'OO......#.',
        'O.#O...#.#',
        'O....#OO..',
        'O.........',
        '#....###..',
        '#OO..#....'
    ]
    assert tilt_rocks_to_direction(rock_map, Directions.WEST) == tilted_map


def test_calculate_load():
    rock_map = [
        'OOOO.#.O..',
        'OO..#....#',
        'OO..O##..O',
        'O..#.OO...',
        '........#.',
        '..#....#.#',
        '..O..#.O.O',
        '..O.......',
        '#....###..',
        '#....#....'
    ]
    assert calculate_load(rock_map) == 136


def test_complete_tilt_cycles():
    rock_map = [
        'OOOO.#.O..',
        'OO..#....#',
        'OO..O##..O',
        'O..#.OO...',
        '........#.',
        '..#....#.#',
        '..O..#.O.O',
        '..O.......',
        '#....###..',
        '#....#....'
    ]
    after_cycles = [
        '.....#....',
        '....#...O#',
        '.....##...',
        '..O#......',
        '.....OOO#.',
        '.O#...O#.#',
        '....O#...O',
        '.......OOO',
        '#...O###.O',
        '#.OOO#...O',
    ]
    assert complete_tilt_cycles(rock_map, 3) == after_cycles
