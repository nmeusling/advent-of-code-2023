from src.day11.day11 import get_galaxy_free_rows_and_columns, duplicate_galaxy_free_rows_and_columns, \
    get_shortest_path_between_two_galaxies, solve_day11_part1


def test_get_galaxy_free_rows_and_columns():
    space_map = [
        "...#......",
        ".......#..",
        "#.........",
        "..........",
        "......#...",
        ".#........",
        ".........#",
        "..........",
        ".......#..",
        "#...#....."
    ]
    assert get_galaxy_free_rows_and_columns(space_map) == ([3, 7], [2, 5, 8])


def test_duplicate_galaxy_free_rows_and_columns():
    space_map = [
        "...#......",
        ".......#..",
        "#.........",
        "..........",
        "......#...",
        ".#........",
        ".........#",
        "..........",
        ".......#..",
        "#...#....."
    ]
    expanded_space_map = [
        "....#........",
        ".........#...",
        "#............",
        ".............",
        ".............",
        "........#....",
        ".#...........",
        "............#",
        ".............",
        ".............",
        ".........#...",
        "#....#......."
    ]
    assert duplicate_galaxy_free_rows_and_columns(space_map) == expanded_space_map

def test_shortest_path():
    assert get_shortest_path_between_two_galaxies((0, 4), (10, 9)) == 15
    assert get_shortest_path_between_two_galaxies((2, 0), (7, 12)) == 17
    assert get_shortest_path_between_two_galaxies((11, 0), (11, 5)) == 5


def test_solve_day11_part1():
    space_map = [
        "...#......",
        ".......#..",
        "#.........",
        "..........",
        "......#...",
        ".#........",
        ".........#",
        "..........",
        ".......#..",
        "#...#....."
    ]
    assert solve_day11_part1(space_map) == 374