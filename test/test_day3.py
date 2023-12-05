from src.day3.day3 import is_part_number, get_ints_from_line, solve_day3_part1, get_adjacent_parts, \
    get_number_touching_index, solve_day3_part2


def test_is_part_number():
    schematic = ['467..114..',
                 '...*......',
                 '..35..633.',
                 '......#...',
                 '617*......',
                 '.....+.58.',
                 '..592.....',
                 '......755.',
                 '...$.*....',
                 '.664.598..',
                 '.6........',
                 '.6......#.',
                 '%6.......6'
                 ]
    assert is_part_number(3, 0, 0, schematic)
    assert is_part_number(3, 4, 0, schematic)
    assert not is_part_number(3, 0, 5, schematic)
    assert not is_part_number(2, 5, 7, schematic)
    assert not is_part_number(1, 10, 1, schematic)
    assert is_part_number(1, 11, 1, schematic)
    assert is_part_number(1, 12, 1, schematic)
    assert is_part_number(1, 12, 9, schematic)


def test_get_ints_from_line():
    assert get_ints_from_line('467..114..') == [(0, 3), (5,3)]
    assert get_ints_from_line('...*......') == []
    assert get_ints_from_line('..35..633.') == [(2,2), (6,3)]
    assert get_ints_from_line('.664.598..') == [(1,3), (5,3)]
    assert get_ints_from_line('.....+.58.') == [(7,2)]
    assert get_ints_from_line('.6........') == [(1,1)]
    assert get_ints_from_line('.........6') == [(9, 1)]
    assert get_ints_from_line('.......126') == [(7, 3)]

def test_day3_part1():
    schematic = ['467..114..',
                 '...*......',
                 '..35..633.',
                 '......#...',
                 '617*......',
                 '.....+.58.',
                 '..592.....',
                 '......755.',
                 '...$.*....',
                 '.664.598..',
                 '......-598',]
    assert solve_day3_part1(schematic) == 4361 + 598


def test_get_number_touching_index():
    assert get_number_touching_index('467..114..', 1) == ('467', 1)
    assert get_number_touching_index('467..114..', 0) == ('467', 2)
    assert get_number_touching_index('467..114..', 2) == ('467', 0)
    assert get_number_touching_index('467..114..', 5) == ('114', 2)
    assert get_number_touching_index('467..114..', 6) == ('114', 1)
    assert get_number_touching_index('467..114..', 7) == ('114', 0)
    assert get_number_touching_index('467....114', 9) == ('114', 0)
    assert get_number_touching_index('467....114', 8) == ('114', 1)
    assert get_number_touching_index('467....114', 7) == ('114', 2)


def test_get_adjacent_parts():
    schematic = ['467..114..',
                 '...*......',
                 '..35..633.',
                 '......#...',
                 '617*......',
                 '.....+.58.',
                 '..592.....',
                 '......755.',
                 '...$.*....',
                 '.664.598..',
                 '......-598',
                 ]
    assert get_adjacent_parts(1, 3, schematic) == ['467', '35']
    assert get_adjacent_parts(0, 0, schematic) == ['467']
    assert get_adjacent_parts(9, 4, schematic) == ['664', '598']
    assert get_adjacent_parts(10, 9, schematic) == ['598']
    assert get_adjacent_parts(10, 6, schematic) == ['598', '598']

def test_solve_day3_part2():
    schematic = ['467..114..',
                 '...*......',
                 '..35..633.',
                 '......#...',
                 '617*......',
                 '.....+.58.',
                 '..592.....',
                 '......755.',
                 '...$.*....',
                 '.664.598..',]
    assert solve_day3_part2(schematic) == 467835
